// Render comparison: does the new build show agents exactly what the old one does?
//
// Logs the same agent into both builds (same origin, same clock, same seeded
// randomness, same mocked sheet) and walks every view, every Academy module and
// every lesson, plus the pre-licensing page. For each it records:
//   - the view's HTML, with every image URL replaced by the sha256 of its bytes
//     (so a data URI and the file it became compare equal, and nothing else does),
//   - the view's visible text,
//   - every image on the page - <img> and CSS background - fetched and hashed in
//     the page, and whether each <img> actually decoded.
// It also presses every Share-image Download button and hashes the file.
// Passes only when all of that is identical, every image loaded, and the new
// build raised no page error the old one did not.
//
//   node tools/compare-render.mjs --old origin/main --new .
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { materialize, startServer, launch, makeBackend, preparePage, login, seedProgress, settle, tmpDir, fail } from './lib/harness.mjs';

const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
const OLD = materialize(arg('--old', 'origin/main'));
const NEW = materialize(arg('--new', '.'));
const sha = b => crypto.createHash('sha256').update(b).digest('hex');

function normaliser(root) {
  const cache = new Map();
  const fileHash = rel => {
    if (!cache.has(rel)) { const f = path.join(root, rel); cache.set(rel, fs.existsSync(f) ? sha(fs.readFileSync(f)).slice(0, 16) : 'MISSING:' + rel); }
    return cache.get(rel);
  };
  return html => html
    .replace(/data:image\/[a-z+]+;base64,[A-Za-z0-9+/=]+/g, m => 'IMG:' + sha(Buffer.from(m.split(',')[1], 'base64')).slice(0, 16))
    .replace(/assets\/img\/[\w.-]+/g, m => 'IMG:' + fileHash(m));
}

async function snapshot(page, sel = '#content') {
  await page.waitForFunction(() => { const c = document.getElementById('m5certimg'); return !c || (c.getAttribute('src') || '').startsWith('data:'); }, { timeout: 15000 });
  return page.evaluate(async sel => {
    const urls = [];
    for (const el of document.querySelectorAll('*')) {
      if (el.closest('.hidden')) continue;
      const bg = getComputedStyle(el).backgroundImage;
      if (bg && bg !== 'none') for (const m of bg.matchAll(/url\("?(.*?)"?\)/g)) urls.push({ kind: 'bg', url: m[1] });
      if (el.tagName === 'IMG' && el.getAttribute('src')) urls.push({ kind: 'img', url: el.currentSrc || el.src, ok: el.naturalWidth > 0 });
    }
    const hashes = new Map();
    for (const u of urls) {
      if (hashes.has(u.url) || !/^(data:|http:\/\/127\.0\.0\.1)/.test(u.url)) continue;
      try {
        const r = await fetch(u.url);
        hashes.set(u.url, r.ok ? [...new Uint8Array(await crypto.subtle.digest('SHA-256', await r.arrayBuffer()))].map(b => b.toString(16).padStart(2, '0')).join('').slice(0, 16) : 'HTTP' + r.status);
      } catch (e) { hashes.set(u.url, 'FETCHFAIL'); }
    }
    const c = document.querySelector(sel);
    return {
      html: c ? c.innerHTML : '',
      text: c ? c.innerText : '',
      images: urls.map(u => ({ kind: u.kind, h: hashes.get(u.url) || ('EXTERNAL:' + u.url.slice(0, 60)), ok: u.ok })),
    };
  }, sel);
}

async function walk(root) {
  const server = await startServer(root);
  const browser = await launch();
  const out = { views: {}, errors: [], downloads: {}, local404: [] };
  try {
    // A licensed admin sees every view, including the Agency Dashboard.
    const page = await browser.newPage();
    const rec = await preparePage(page, { origin: server.origin, backend: makeBackend({ admin: true }) });
    const dl = tmpDir('dl');
    const cdp = await page.createCDPSession();
    await cdp.send('Browser.setDownloadBehavior', { behavior: 'allow', downloadPath: dl });
    await page.goto(server.origin + '/', { waitUntil: 'load' });
    await seedProgress(page, 'all');
    await login(page);
    const norm = normaliser(root);
    const views = await page.evaluate(() => {
      const names = new Set(NAV.filter(n => n.v && !n.url).map(n => n.v));
      ['income', 'activity', 'agencybuild', 'calc', 'shareffl', 'inperson', 'gethelp', 'kpi', 'profile', 'agency'].forEach(v => names.add(v));
      return [...names];
    });
    const take = async key => { const s = await snapshot(page); s.html = norm(s.html); out.views[key] = s; };
    for (const v of views) { await page.evaluate(v => go(v), v); await settle(page, 400); await take('view:' + v); }
    const lessons = await page.evaluate(() => ACAD_LMS.map(m => [m.id, m.lessons.map(l => l.id)]));
    for (const [mod, les] of lessons) {
      await page.evaluate(m => { go('academy'); acadGoMod(m); }, mod); await settle(page, 200); await take('module:' + mod);
      for (const l of les) { await page.evaluate((m, l) => acadGoLes(m, l), mod, l); await settle(page, 200); await take(`lesson:${mod}/${l}`); }
    }
    // Every share image's Download button.
    const keys = await page.evaluate(() => ['schedule', 'prelic', 'licensed', 'reading', 'vbo', 'shawn', 'ignyte', 'convention', 'huddle', 'pop', 'manhattan', 'mmaker']);
    for (const k of keys) {
      const name = 'share-' + k + '.img';
      await page.evaluate((k, n) => dlImg(k, n), k, name);
      const f = path.join(dl, name); const t0 = Date.now();
      while (!fs.existsSync(f) && Date.now() - t0 < 10000) await new Promise(r => setTimeout(r, 100));
      await new Promise(r => setTimeout(r, 200));
      out.downloads[k] = fs.existsSync(f) ? sha(fs.readFileSync(f)).slice(0, 16) : 'NO FILE';
    }
    out.errors.push(...rec.errors);
    if (rec.leaked.length) fail('outside requests leaked: ' + rec.leaked.join(', '));
    await page.close();

    // A brand-new licensed agent with no progress sees the welcome and strategy-call videos.
    const fresh = await browser.newPage();
    const recF = await preparePage(fresh, { origin: server.origin, backend: makeBackend() });
    await fresh.goto(server.origin + '/', { waitUntil: 'load' });
    await fresh.evaluate(() => { localStorage.clear(); localStorage.setItem('m5.lang', 'en'); });
    await fresh.reload({ waitUntil: 'load' });
    await login(fresh);
    for (const v of ['dashboard', 'faststart', 'academy']) {
      await fresh.evaluate(v => go(v), v); await settle(fresh, 400);
      const s = await snapshot(fresh); s.html = norm(s.html); out.views['fresh:' + v] = s;
    }
    out.errors.push(...recF.errors);
    await fresh.close();

    // An unlicensed agent lands on the pre-licensing page instead.
    const pre = await browser.newPage();
    const rec2 = await preparePage(pre, { origin: server.origin, backend: makeBackend({ licensed: false }) });
    await pre.goto(server.origin + '/', { waitUntil: 'load' });
    await pre.evaluate(() => { localStorage.clear(); localStorage.setItem('m5.lang', 'en'); });
    await pre.reload({ waitUntil: 'load' });
    await pre.waitForSelector('#li-first', { visible: true });
    for (const [id, v] of [['li-first', 'Tess'], ['li-last', 'Ticksafe'], ['li-email', 'ticksafe@example.invalid'], ['li-phone', '5555550100']]) await pre.$eval('#' + id, (el, v) => { el.value = v; }, v);
    await pre.click('#li-btn');
    await pre.waitForFunction(() => { const p = document.getElementById('m5-prelic'); return p && !p.classList.contains('hidden'); }, { timeout: 20000 });
    await settle(pre);
    const prelic = await snapshot(pre, '#m5-prelic');
    prelic.html = norm(prelic.html);
    out.views['prelicensing'] = prelic;
    out.errors.push(...rec2.errors);
    out.local404 = server.log.filter(x => x.status !== 200).map(x => x.path);
  } finally { await browser.close(); await server.close(); }
  return out;
}

const a = await walk(OLD);
console.log(`old build: ${Object.keys(a.views).length} snapshots`);
const b = await walk(NEW);
const problems = [];
const keys = new Set([...Object.keys(a.views), ...Object.keys(b.views)]);
let imgCount = 0;
for (const k of keys) {
  const x = a.views[k], y = b.views[k];
  if (!x || !y) { problems.push(`${k}: present in only one build`); continue; }
  if (x.text !== y.text) problems.push(`${k}: visible text differs`);
  if (x.html !== y.html) {
    let i = 0; while (i < x.html.length && x.html[i] === y.html[i]) i++;
    problems.push(`${k}: HTML differs at ${i}: old ${JSON.stringify(x.html.slice(i - 40, i + 60))} new ${JSON.stringify(y.html.slice(i - 40, i + 60))}`);
  }
  if (JSON.stringify(x.images) !== JSON.stringify(y.images)) problems.push(`${k}: images differ: old ${JSON.stringify(x.images)} new ${JSON.stringify(y.images)}`);
  for (const im of y.images) { imgCount++; if (im.kind === 'img' && !im.ok && !im.h.startsWith('EXTERNAL')) problems.push(`${k}: an <img> did not decode (${im.h})`); if (/^(HTTP|FETCHFAIL|MISSING)/.test(im.h)) problems.push(`${k}: image failed to load (${im.h})`); }
}
for (const k of Object.keys(a.downloads)) {
  if (a.downloads[k] !== b.downloads[k]) problems.push(`share download ${k}: old ${a.downloads[k]} new ${b.downloads[k]}`);
}
const newErrors = b.errors.filter(e => !a.errors.includes(e));
for (const e of newErrors) problems.push('new page error: ' + e);
if (b.local404.length) problems.push('missing local files in new build: ' + [...new Set(b.local404)].join(', '));

if (process.env.RENDER_DUMP) fs.writeFileSync(process.env.RENDER_DUMP, JSON.stringify({ a, b }, null, 1));
console.log(`compared ${keys.size} views/modules/lessons, ${imgCount} image placements, ${Object.keys(b.downloads).length} share downloads`);
if (a.errors.length) console.log(`page errors present in BOTH builds (pre-existing, not caused by this change): ${[...new Set(a.errors)].join(' | ')}`);
if (problems.length) { console.log(problems.slice(0, 40).join('\n')); fail(`${problems.length} difference(s)`); }
console.log('RENDER IDENTICAL');
