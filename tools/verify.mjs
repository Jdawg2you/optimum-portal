// verify: refuses a portal build that would break for agents. Run by deploy.sh before
// anything is pushed, and by build.mjs before it writes index.html.
//
//   node tools/verify.mjs                     static rules on the repo
//   node tools/verify.mjs --ticksafe origin/main   ...plus ticksafe against that build
//   node tools/verify.mjs --root DIR          check another tree (used by the self-test)
//   node tools/verify.mjs --disk              accept files that exist on disk but are not committed yet
//
// Rules (each failure names its rule):
//   reproduce      index.html is exactly what source/ + content/ build
//   syntax         every inline <script> passes `node --check`
//   ask-optimum    the Ask Optimum <script> line is present, once
//   assets         every assets/ and posters/ path, and every relative src/href/url(),
//                  names a file that exists in exact case AND is committed to git
//                  (an uncommitted file is not deployed: the 29 Oct bug)
//   script-escape  no inline <script> carries <!--, and no content literal carries </script
//   inline-images  no data:image over 4 KB in index.html (images belong in assets/)
//   max-bytes      optional --max-bytes N ceiling on index.html
//   ticksafe       optional, see tools/ticksafe.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync, spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { build, locate, escapeForScript, BuildError } from './build.mjs';

const ASK_LINE = '<script src="ask-optimum.js?v=2" defer></script>';
const INLINE_IMAGE_LIMIT = 4096;

/** Every local file the page refers to, as repo-relative paths. */
export function referencedFiles(html) {
  const refs = new Set();
  for (const m of html.matchAll(/(?<![\w/.%-])((?:assets|posters)\/[\w./%-]+?\.(?:jpe?g|png|gif|webp|svg|pdf|mp4|ico|js|css))(?![\w-])/gi)) refs.add(m[1]);
  for (const m of html.matchAll(/(?:\b(?:src|href|poster)=["']|url\(['"]?)(\/?[^"')#?:${}<>\s]+\.(?:html|pdf|png|jpe?g|ico|js|css|webp|svg|gif|mp4))(?:\?[^"')]*)?["')]/gi)) {
    if (m[1].startsWith('//')) continue;
    refs.add(m[1].replace(/^\//, ''));
  }
  return [...refs].sort();
}

function listFiles(root, disk) {
  if (!disk && fs.existsSync(path.join(root, '.git'))) {
    const out = execFileSync('git', ['ls-files', '-z', '--cached'], { cwd: root, encoding: 'utf8' });
    return { files: new Set(out.split('\0').filter(Boolean)), source: 'committed or staged in git' };
  }
  const files = new Set();
  const walk = (d, rel) => { for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    if (e.name === 'node_modules' || e.name === '.git') continue;
    const r = rel ? rel + '/' + e.name : e.name;
    if (e.isDirectory()) walk(path.join(d, e.name), r); else files.add(r);
  } };
  walk(root, '');
  return { files, source: 'on disk (exact case)' };
}

export function verify(root, { maxBytes, disk = false } = {}) {
  const failures = [];
  const bad = (rule, msg) => failures.push(`[${rule}] ${msg}`);
  const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');

  // reproduce
  try {
    const built = build({
      template: fs.readFileSync(path.join(root, 'source', 'index.template.html'), 'utf8'),
      read: f => fs.readFileSync(path.join(root, 'content', f), 'utf8'),
    });
    if (built !== html) bad('reproduce', 'index.html is not what source/ + content/ build. Edited directly? Run: node tools/build.mjs --extract');
  } catch (e) { bad('reproduce', e instanceof BuildError ? e.message : String(e)); }

  // syntax
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'portal-verify-'));
  let n = 0;
  for (const m of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)) {
    if (/\bsrc=/.test(m[1])) continue;
    const type = (m[1].match(/type=["']?([^"'\s>]+)/) || [])[1];
    if (type && !/^(text\/javascript|module)$/i.test(type)) continue;
    n++;
    const f = path.join(tmp, `block-${n}.${type === 'module' ? 'mjs' : 'js'}`);
    fs.writeFileSync(f, m[2]);
    const r = spawnSync(process.execPath, ['--check', f], { encoding: 'utf8' });
    if (r.status !== 0) bad('syntax', `inline <script> #${n} (line ${html.slice(0, m.index).split('\n').length}): ${(r.stderr || '').split('\n').find(l => /Error/.test(l)) || r.stderr}`);
    // Inside a script, <!-- followed later by <script switches the HTML parser into a state
    // where </script> no longer closes the block. None of the page's scripts need it.
    if (m[2].includes('<!--')) bad('script-escape', `inline <script> #${n} contains <!-- (write it as <\\!--)`);
  }
  if (n === 0) bad('syntax', 'found no inline <script> blocks at all');

  // ask-optimum
  const asks = html.split(ASK_LINE).length - 1;
  if (asks !== 1) bad('ask-optimum', `expected the line ${ASK_LINE} once, found ${asks}`);

  // assets
  const { files, source } = listFiles(root, disk);
  const refs = referencedFiles(html);
  for (const r of refs) {
    const p = decodeURIComponent(r);
    if (!files.has(p)) bad('assets', `index.html refers to ${r}, which is not ${source}`);
  }

  // script-escape: every mapped literal must be inside a script and carry neither sequence
  try {
    for (const s of locate(html)) {
      const text = html.slice(s.start, s.end);
      if (/<\/script/i.test(text) || text.includes('<!--')) bad('script-escape', `${s.name} carries an unescaped </script or <!-- inside its <script>`);
      if (escapeForScript(text) !== text) bad('script-escape', `${s.name} is not escaped`);
    }
  } catch (e) { bad('script-escape', 'could not locate the content literals: ' + e.message); }

  // inline-images
  for (const m of html.matchAll(/data:image\/[a-z+]+;base64,[A-Za-z0-9+/=]+/g)) {
    if (m[0].length > INLINE_IMAGE_LIMIT) bad('inline-images', `a ${m[0].length}-char inline image at char ${m.index}; put it in assets/img/`);
  }

  const bytes = Buffer.byteLength(html);
  if (maxBytes && bytes > maxBytes) bad('max-bytes', `index.html is ${bytes} bytes, over ${maxBytes}`);
  return { failures, bytes, scripts: n, refs: refs.length };
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
  const root = path.resolve(arg('--root', path.join(path.dirname(fileURLToPath(import.meta.url)), '..')));
  const res = verify(root, { maxBytes: arg('--max-bytes') ? Number(arg('--max-bytes')) : undefined, disk: process.argv.includes('--disk') });
  console.log(`index.html ${res.bytes} bytes, ${res.scripts} inline scripts checked, ${res.refs} referenced files`);
  const ref = arg('--ticksafe');
  if (ref && !res.failures.length) {
    const r = spawnSync(process.execPath, [path.join(path.dirname(fileURLToPath(import.meta.url)), 'ticksafe.mjs'), '--old', ref, '--new', root], { encoding: 'utf8' });
    process.stdout.write(r.stdout);
    if (r.status !== 0 || !/TICKSAFE PASS/.test(r.stdout)) res.failures.push('[ticksafe] ' + ((r.stderr || '').trim().split('\n').slice(-1)[0] || 'failed'));
  }
  if (res.failures.length) { for (const f of res.failures) console.log('VERIFY FAIL ' + f); process.exit(1); }
  console.log('VERIFY OK');
}
