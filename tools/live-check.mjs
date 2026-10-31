// live-check: is the live site serving exactly what HEAD says it should?
//
// A status code proves a file is there, not that it is the right file: on 29 Oct
// three lessons kept old thumbnails while every request returned 200. So this
// fetches index.html and every file it refers to from the site and compares the
// sha256 of each with the committed bytes at HEAD. Requests carry a unique query
// string so the CDN answers from GitHub, not from its 10-minute cache.
//
//   node tools/live-check.mjs https://portal.ffloptimum.com
//        [--wait SECONDS]           keep retrying while GitHub Pages deploys
//        [--require-origin-equal]   also require `git diff origin/main HEAD` to be empty
//   node tools/live-check.mjs --selftest   proves it catches an omitted file and a stale one
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { referencedFiles } from './verify.mjs';

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const git = (...a) => execFileSync('git', a, { cwd: REPO, maxBuffer: 64 << 20 });
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };

/** What the site should serve: every path with the sha256 of its committed bytes at `ref`. */
export function expected(ref = 'HEAD') {
  const html = git('show', `${ref}:index.html`).toString('utf8');
  const out = [{ path: 'index.html', sha: sha(Buffer.from(html, 'utf8')) }];
  for (const p of referencedFiles(html)) {
    let bytes;
    try { bytes = git('show', `${ref}:${decodeURIComponent(p)}`); } catch { out.push({ path: p, sha: 'NOT IN GIT' }); continue; }
    out.push({ path: p, sha: sha(bytes) });
  }
  return out;
}

export async function check(base, want, { bust = Date.now().toString(36) } = {}) {
  const problems = [];
  await Promise.all(want.map(async (w, i) => {
    await new Promise(r => setTimeout(r, i * 15)); // be gentle with the CDN
    const url = `${base.replace(/\/$/, '')}/${w.path === 'index.html' ? '' : w.path}?livecheck=${bust}`;
    try {
      const r = await fetch(url, { redirect: 'follow', cache: 'no-store' });
      if (!r.ok) { problems.push(`${w.path}: HTTP ${r.status}`); return; }
      const got = sha(Buffer.from(await r.arrayBuffer()));
      if (got !== w.sha) problems.push(`${w.path}: served bytes differ from HEAD (status ${r.status}, so a status check would have passed)`);
    } catch (e) { problems.push(`${w.path}: ${e.message}`); }
  }));
  return problems;
}

const isMain = process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1]);
if (isMain && process.argv.includes('--selftest')) {
  const { startServer, materialize, tmpDir } = await import('./lib/harness.mjs');
  const want = expected('HEAD');
  const dir = tmpDir('live');
  fs.cpSync(materialize('HEAD'), dir, { recursive: true });
  const server = await startServer(dir);
  const results = [];
  const run = async (name, mutate, shouldPass) => {
    const undo = mutate();
    const problems = await check(server.origin, want);
    undo();
    const ok = shouldPass ? problems.length === 0 : problems.length > 0;
    results.push(ok);
    console.log(`${ok ? 'ok' : 'WRONG'}: ${name} -> ${problems.length ? problems[0] : 'matches'}`);
  };
  const f = p => path.join(dir, p);
  try {
    await run('a correct deploy', () => () => {}, true);
    await run('an omitted asset (29 Oct bug 1)', () => { const b = fs.readFileSync(f('assets/img/pop.jpg')); fs.rmSync(f('assets/img/pop.jpg')); return () => fs.writeFileSync(f('assets/img/pop.jpg'), b); }, false);
    await run('a stale poster under the same name, served 200 (29 Oct bug 2)', () => { const b = fs.readFileSync(f('posters/2-6-1.jpg')); fs.writeFileSync(f('posters/2-6-1.jpg'), fs.readFileSync(f('posters/a-1.jpg'))); return () => fs.writeFileSync(f('posters/2-6-1.jpg'), b); }, false);
    await run('a stale index.html', () => { const b = fs.readFileSync(f('index.html')); fs.writeFileSync(f('index.html'), Buffer.concat([b, Buffer.from('\n')])); return () => fs.writeFileSync(f('index.html'), b); }, false);
  } finally { await server.close(); }
  if (results.every(Boolean)) console.log(`checked ${want.length} files per run`), console.log('LIVECHECK SELFTEST OK');
  else { console.log('FAIL: the live check did not behave'); process.exit(1); }
} else if (isMain) {
  const base = process.argv.slice(2).find(a => /^https?:\/\//.test(a));
  if (!base) { console.error('usage: node tools/live-check.mjs https://portal.ffloptimum.com [--wait S] [--require-origin-equal]'); process.exit(2); }
  const want = expected('HEAD');
  const deadline = Date.now() + Number(arg('--wait', 0)) * 1000;
  let problems;
  for (;;) {
    problems = await check(base, want);
    if (!problems.length || Date.now() >= deadline) break;
    console.log(`not live yet (${problems.length} files differ, e.g. ${problems[0]}); retrying in 20 s`);
    await new Promise(r => setTimeout(r, 20000));
  }
  if (process.argv.includes('--require-origin-equal')) {
    git('fetch', '-q', 'origin', 'main');
    const diff = git('diff', '--name-status', 'origin/main', 'HEAD').toString().trim();
    if (diff) problems.push('git diff origin/main HEAD is not empty:\n' + diff);
  }
  if (problems.length) { console.log(problems.join('\n')); console.log(`FAIL: ${problems.length} of ${want.length} files do not match HEAD`); process.exit(1); }
  console.log(`${want.length} files at ${base} match HEAD ${git('rev-parse', '--short', 'HEAD').toString().trim()} by sha256`);
  console.log('LIVE MATCHES HEAD');
}
