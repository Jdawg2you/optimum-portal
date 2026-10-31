// Shared test harness for the portal's browser checks.
//
// Three rules every check inherits from here:
//  1. One origin. The server's root can be switched between builds, so an
//     "old build -> new build" test keeps the same localStorage. Different
//     ports are different origins and an upgrade test on two ports passes on
//     an empty store.
//  2. Nothing leaves this machine. The Apps Script backend is answered by an
//     in-process mock (the real one writes to the intake sheet), and every
//     other outside request is refused. A check fails if any outside request
//     was let through.
//  3. One clock. Date is frozen (it creeps at 1/1000 speed so debounces and
//     "elapsed" logic still move), so two builds render the same day.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import http from 'node:http';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import puppeteer from 'puppeteer-core';

export const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
export const CHROME = process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
export const BACKEND_HOST = 'script.google.com';
export const FROZEN_NOW = Date.parse('2026-10-28T15:00:00Z'); // a Wednesday, 11:00 ET

export const AGENT = {
  first: 'Tess', last: 'Ticksafe', email: 'ticksafe@example.invalid', phone: '5555550100',
};

export function fail(msg) { console.error('FAIL: ' + msg); process.exit(1); }

export function tmpDir(tag) { return fs.mkdtempSync(path.join(os.tmpdir(), 'portal-' + tag + '-')); }

/** A directory holding the tree for `ref`: '.' is the working tree, anything else is a git ref. */
export function materialize(ref) {
  if (ref === '.' || ref === REPO) return REPO;
  if (fs.existsSync(ref) && fs.statSync(ref).isDirectory()) return path.resolve(ref);
  const sha = execFileSync('git', ['rev-parse', '--verify', ref + '^{commit}'], { cwd: REPO, encoding: 'utf8' }).trim();
  const dir = tmpDir('tree-' + sha.slice(0, 7));
  execFileSync('/bin/sh', ['-c', `git archive ${sha} | tar -x -C "${dir}"`], { cwd: REPO });
  return dir;
}

const TYPES = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.mjs': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8', '.json': 'application/json; charset=utf-8', '.png': 'image/png',
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.svg': 'image/svg+xml', '.webp': 'image/webp',
  '.ico': 'image/x-icon', '.pdf': 'application/pdf', '.txt': 'text/plain; charset=utf-8',
};

/** Static server on 127.0.0.1 whose root can be swapped. `delays` maps a path regex to milliseconds. */
export async function startServer(root, { delays = [] } = {}) {
  const state = { root, delays, log: [] };
  const server = http.createServer((req, res) => {
    const url = new URL(req.url, 'http://x');
    let rel = decodeURIComponent(url.pathname);
    if (rel.endsWith('/')) rel += 'index.html';
    const file = path.join(state.root, rel);
    const send = () => {
      if (!file.startsWith(state.root) || !fs.existsSync(file) || !fs.statSync(file).isFile()) {
        state.log.push({ path: rel, status: 404 });
        res.writeHead(404, { 'content-type': 'text/plain' }); res.end('not found'); return;
      }
      state.log.push({ path: rel, status: 200 });
      res.writeHead(200, {
        'content-type': TYPES[path.extname(file).toLowerCase()] || 'application/octet-stream',
        'cache-control': 'no-store',
      });
      fs.createReadStream(file).pipe(res);
    };
    const d = state.delays.find(x => x.re.test(rel));
    if (d) setTimeout(send, d.ms); else send();
  });
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const { port } = server.address();
  return {
    origin: `http://127.0.0.1:${port}`,
    setRoot(dir) { state.root = dir; },
    setDelays(list) { state.delays = list; },
    log: state.log,
    close: () => new Promise(r => server.close(r)),
  };
}

export async function launch() {
  const userDataDir = tmpDir('profile');
  const browser = await puppeteer.launch({
    executablePath: CHROME, headless: true, userDataDir,
    args: ['--no-proxy-server', '--no-first-run', '--no-default-browser-check', '--disable-extensions'],
    defaultViewport: { width: 1280, height: 900 },
    protocolTimeout: 60000,
  });
  return browser;
}

/** In-memory stand-in for the Apps Script web app. `sheet` is keyed by email. */
export function makeBackend({ admin = false, licensed = true } = {}) {
  const b = { sheet: {}, calls: [], saves: [] };
  b.answer = (bodyText) => {
    let body = {}; try { body = JSON.parse(bodyText || '{}'); } catch {}
    b.calls.push(body.action || '?');
    const email = String(body.email || '').toLowerCase();
    switch (body.action) {
      case 'lookup':
        return { ok: true, match: { found: true, licensed, hasNPN: licensed, admin, first: AGENT.first, last: AGENT.last,
          email: AGENT.email, state: 'FL', lang: 'en', code: 'TST1' } };
      case 'load':
        return b.sheet[email] ? { ok: true, data: JSON.parse(JSON.stringify(b.sheet[email])) } : { ok: true };
      case 'save':
        b.sheet[email] = JSON.parse(JSON.stringify(body.data || {}));
        b.saves.push(b.sheet[email]);
        return { ok: true };
      case 'roster': return { ok: true, agents: [] };
      default: return { ok: true };
    }
  };
  return b;
}

/**
 * Wires a page to the harness: request policy, backend mock, frozen clock, error capture.
 * Returns a record the caller asserts on.
 */
export async function preparePage(page, { origin, backend, cache = true }) {
  const rec = { errors: [], leaked: [], refused: [], local: [] };
  await page.setCacheEnabled(cache);
  await page.setRequestInterception(true);
  page.on('request', req => {
    const u = new URL(req.url());
    if (u.protocol === 'data:' || u.protocol === 'blob:') return req.continue();
    if (u.origin === origin) { rec.local.push(u.pathname); return req.continue(); }
    if (u.hostname === BACKEND_HOST || u.hostname.endsWith('.googleusercontent.com')) {
      if (req.method() === 'OPTIONS') return req.respond({ status: 204, headers: { 'access-control-allow-origin': '*' } });
      const out = backend ? backend.answer(req.postData()) : { ok: false };
      return req.respond({ status: 200, contentType: 'application/json', headers: { 'access-control-allow-origin': '*' }, body: JSON.stringify(out) });
    }
    rec.refused.push(u.hostname);
    return req.abort('blockedbyclient');
  });
  page.on('pageerror', e => rec.errors.push(String(e && e.message || e)));
  page.on('console', m => { if (m.type() === 'error' && !/net::ERR_BLOCKED_BY_CLIENT|Failed to load resource/.test(m.text())) rec.errors.push('console: ' + m.text()); });
  page.on('requestfailed', r => {
    const u = new URL(r.url());
    if (u.origin === origin) rec.errors.push('local request failed: ' + u.pathname + ' ' + (r.failure() || {}).errorText);
  });
  page.on('response', r => {
    const u = new URL(r.url());
    if (u.origin === origin && r.status() >= 400) rec.errors.push(`local ${r.status()}: ${u.pathname}`);
  });
  await page.evaluateOnNewDocument((NOW) => {
    const RealDate = Date; const t0 = performance.now();
    const now = () => NOW + (performance.now() - t0) / 1000;
    class FrozenDate extends RealDate {
      constructor(...a) { if (a.length === 0) super(now()); else super(...a); }
      static now() { return Math.floor(now()); }
    }
    FrozenDate.UTC = RealDate.UTC; FrozenDate.parse = RealDate.parse;
    // eslint-disable-next-line no-global-assign
    Date = FrozenDate;
    // Seeded so anything the page picks at random picks the same thing in both builds.
    let seed = 0x9e3779b9;
    Math.random = () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
      t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
  }, FROZEN_NOW);
  return rec;
}

/** Logs in through the real form, the way an agent does. */
export async function login(page) {
  await page.waitForSelector('#li-first', { visible: true, timeout: 20000 });
  for (const [id, v] of [['li-first', AGENT.first], ['li-last', AGENT.last], ['li-email', AGENT.email], ['li-phone', AGENT.phone]]) {
    await page.$eval('#' + id, (el, v) => { el.value = v; el.dispatchEvent(new Event('input', { bubbles: true })); }, v);
  }
  await page.click('#li-btn');
  await page.waitForFunction(() => { const a = document.getElementById('app'); return a && !a.classList.contains('hidden'); }, { timeout: 20000 });
  await settle(page);
}

/** Waits for the backend round trip, the 1.2 s save debounce, and every image on the page. */
export async function settle(page, ms = 1800) {
  await new Promise(r => setTimeout(r, ms));
  // Lazy images below the fold would never load in a headless check, so make them eager,
  // then wait for each image (capped, so one that never settles fails the check instead
  // of hanging it).
  await page.evaluate(() => Promise.all([...document.images].map(i => {
    if (i.loading === 'lazy') i.loading = 'eager';
    return i.complete ? 0 : new Promise(r => { i.addEventListener('load', r, { once: true }); i.addEventListener('error', r, { once: true }); setTimeout(r, 8000); });
  })));
}

/**
 * Writes an agent's progress into this origin's localStorage from the build that is
 * loaded, then reloads. 'all' completes every published lesson and earns the
 * certificate; 'partial' completes every other one. Both tick the first and last
 * do-next step of every lesson, every Fast Start step, and two legacy keys the
 * migrations carry forward (f_goat, acaddo_4-3_1).
 */
export async function seedProgress(page, mode = 'all') {
  await page.evaluate((mode, AGENT) => {
    const T = '2026-10-20T14:00:00.000Z';
    const checks = { f_goat: T, 'acaddo_4-3_1': T };
    let i = 0;
    ACAD_LMS.forEach(m => m.lessons.forEach(l => {
      if (l.status === 'coming_soon') return;
      if (mode === 'all' || (i++ % 2 === 0)) checks['acad_' + l.id] = T;
      const n = (l.doNext || []).length;
      if (n) { checks[acadDoKey(l, 0)] = T; checks[acadDoKey(l, n - 1)] = T; }
    }));
    FAST.forEach(g => (g.items || []).forEach(it => { if (it.id) checks[it.id] = T; }));
    const data = { status: 'licensed', first: AGENT.first, last: AGENT.last, email: AGENT.email, phone: AGENT.phone, checks };
    if (mode === 'all') data.t_acadDone = T;
    localStorage.setItem('optimumPortalV2', JSON.stringify(data));
    localStorage.setItem('m5.lang', 'en');
  }, mode, AGENT);
  await page.reload({ waitUntil: 'load' });
}

export async function readStore(page) {
  return page.evaluate(() => { try { return JSON.parse(localStorage.getItem('optimumPortalV2') || 'null'); } catch { return null; } });
}

export function assertNoLeaks(rec, label) {
  if (rec.leaked.length) fail(`${label}: outside requests were let through: ${rec.leaked.join(', ')}`);
}

export function sha256(buf) {
  return import('node:crypto').then(c => c.createHash('sha256').update(buf).digest('hex'));
}
