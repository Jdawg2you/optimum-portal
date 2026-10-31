// Local preview of a portal build, safe to click through by hand.
//
//   node tools/preview.mjs [ref|dir] [port]   e.g. node tools/preview.mjs academy-path 8781
//
// Serves the build at `ref` (a branch or commit, frozen at start, so the preview
// cannot change under the person looking at it) on 127.0.0.1. The page's Apps
// Script backend is pointed at this server instead of Google: any name and email
// logs in as a licensed agent, progress is kept in memory for this run, and
// nothing reaches the intake sheet.
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { materialize, REPO } from './lib/harness.mjs';

const ref = process.argv[2] || 'HEAD';
const port = Number(process.argv[3] || 8781);
// A directory is served as it is (extract a commit there once with `git archive`); a ref is extracted now.
const isDir = fs.existsSync(ref) && fs.statSync(ref).isDirectory();
const sha = isDir ? path.basename(ref) : execFileSync('git', ['rev-parse', '--short', ref], { cwd: REPO, encoding: 'utf8' }).trim();
const root = isDir ? path.resolve(ref) : materialize(sha);
const LIVE_BACKEND = /var BACKEND_URL='https:\/\/script\.google\.com\/[^']+';/;
const indexHtml = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
if (!LIVE_BACKEND.test(indexHtml)) throw new Error('could not find BACKEND_URL to point at the local mock; refusing to serve a page that would reach the real sheet');
const page = indexHtml.replace(LIVE_BACKEND, "var BACKEND_URL='/__preview_backend';");

const sheet = {};
function answer(body) {
  const email = String(body.email || '').trim().toLowerCase();
  switch (body.action) {
    case 'lookup': return { ok: true, match: { found: true, licensed: true, hasNPN: true, admin: false, email, state: 'FL', lang: 'en', code: 'PREVIEW' } };
    case 'load': return sheet[email] ? { ok: true, data: sheet[email] } : { ok: true };
    case 'save': sheet[email] = body.data || {}; return { ok: true };
    case 'roster': return { ok: true, agents: [] };
    default: return { ok: true };
  }
}
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.svg': 'image/svg+xml', '.ico': 'image/x-icon', '.pdf': 'application/pdf' };

http.createServer((req, res) => {
  const url = new URL(req.url, 'http://x');
  if (url.pathname === '/__preview_backend') {
    let raw = ''; req.on('data', c => { raw += c; });
    req.on('end', () => { let body = {}; try { body = JSON.parse(raw || '{}'); } catch {}
      res.writeHead(200, { 'content-type': 'application/json', 'cache-control': 'no-store' }); res.end(JSON.stringify(answer(body))); });
    return;
  }
  let rel = decodeURIComponent(url.pathname); if (rel.endsWith('/')) rel += 'index.html';
  if (rel === '/index.html') { res.writeHead(200, { 'content-type': TYPES['.html'], 'cache-control': 'no-store' }); res.end(page); return; }
  const file = path.join(root, rel);
  if (!file.startsWith(root) || !fs.existsSync(file) || !fs.statSync(file).isFile()) { res.writeHead(404); res.end('not found'); return; }
  res.writeHead(200, { 'content-type': TYPES[path.extname(file).toLowerCase()] || 'application/octet-stream', 'cache-control': 'no-store' });
  fs.createReadStream(file).pipe(res);
}).listen(port, '127.0.0.1', () => console.log(`preview of ${ref} (${sha}) at http://127.0.0.1:${port}/ - backend mocked, nothing reaches the sheet`));
