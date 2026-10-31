// Proves verify and the build have teeth: each rule is broken on purpose in a
// throwaway copy of the repo, and the check must fail on exactly that rule. A
// check that has never been seen to fail proves nothing.
//
//   node tools/verify-selftest.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { verify } from './verify.mjs';
import { build, BuildError } from './build.mjs';

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const tracked = execFileSync('git', ['ls-files', '-z', '--cached', '--others', '--exclude-standard'], { cwd: REPO, encoding: 'utf8' }).split('\0').filter(Boolean);

function copy() {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'portal-selftest-'));
  for (const f of tracked) {
    if (f.startsWith('tools/node_modules/')) continue;
    if (!fs.existsSync(path.join(REPO, f))) continue;
    fs.mkdirSync(path.dirname(path.join(dir, f)), { recursive: true });
    fs.copyFileSync(path.join(REPO, f), path.join(dir, f));
  }
  return dir;
}
const rd = (d, f) => fs.readFileSync(path.join(d, f), 'utf8');
const wr = (d, f, t) => fs.writeFileSync(path.join(d, f), t);
function rebuild(d) {
  wr(d, 'index.html', build({ template: rd(d, 'source/index.template.html'), read: f => rd(d, 'content/' + f) }));
}
function editTemplate(d, from, to) {
  const t = rd(d, 'source/index.template.html');
  if (!t.includes(from)) throw new Error('selftest fixture missing: ' + from);
  wr(d, 'source/index.template.html', t.replace(from, to));
  rebuild(d);
}

let caught = 0, total = 0;
function expectRule(name, rules, d, opts) {
  total++;
  const { failures } = verify(d, opts);
  const hit = failures.filter(f => rules.some(r => f.startsWith(`[${r}]`)));
  if (!hit.length) { console.log(`NOT CAUGHT: ${name}\n  failures were: ${failures.join(' | ') || '(none - verify passed)'}`); return; }
  caught++; console.log(`caught: ${name} -> ${hit[0].slice(0, 140)}`);
}
function expectBuildError(name, d) {
  total++;
  try { build({ template: rd(d, 'source/index.template.html'), read: f => rd(d, 'content/' + f) }); console.log('NOT CAUGHT: ' + name); }
  catch (e) { if (e instanceof BuildError) { caught++; console.log(`caught: ${name} -> ${e.message.slice(0, 140)}`); } else throw e; }
}

// The clean tree must pass, or every "caught" below means nothing.
const clean = copy();
const base = verify(clean);
if (base.failures.length) { console.log('clean copy fails verify: ' + base.failures.join(' | ')); process.exit(1); }
console.log('clean copy passes verify');

{ const d = copy(); wr(d, 'index.html', rd(d, 'index.html').replace('<title>', '<title>x')); expectRule('index.html edited directly, not via source/', ['reproduce'], d); }
{ const d = copy(); editTemplate(d, "function acadKey(id){return 'acad_'+id;}", "function acadKey(id){return 'acad_'+id;"); expectRule('a missing } in a script', ['syntax'], d); }
{ const d = copy(); editTemplate(d, '<script src="ask-optimum.js?v=2" defer></script>', ''); expectRule('the Ask Optimum line removed', ['ask-optimum'], d); }
{ const d = copy(); fs.rmSync(path.join(d, 'assets/img/pop.jpg')); expectRule('a referenced image missing', ['assets'], d); }
{ const d = copy(); fs.rmSync(path.join(d, 'posters/2-6-1.jpg')); expectRule('a lesson poster missing', ['assets'], d); }
{ const d = copy(); fs.renameSync(path.join(d, 'assets/img/pop.jpg'), path.join(d, 'assets/img/tmp.jpg')); fs.renameSync(path.join(d, 'assets/img/tmp.jpg'), path.join(d, 'assets/img/Pop.jpg'));
  expectRule('an image whose name differs only in case (works on a Mac, 404s on GitHub Pages)', ['assets'], d); }
{ const d = copy();
  execFileSync('/bin/sh', ['-c', 'git init -q && git add -A && git rm -q --cached assets/img/huddle.jpg'], { cwd: d });
  expectRule('an image on disk but never committed (the 29 Oct upload bug)', ['assets'], d); }
{ const d = copy();
  fs.copyFileSync(path.join(d, 'assets/img/pop.jpg'), path.join(d, 'promo-new.jpg'));
  const a = JSON.parse(rd(d, 'content/academy.json'));
  a[0].lessons[0].keyTakeaways[0] += ' <img src="promo-new.jpg">';
  wr(d, 'content/academy.json', JSON.stringify(a, null, 1) + '\n');
  rebuild(d);
  execFileSync('/bin/sh', ['-c', 'git init -q && git add -A && git rm -q --cached promo-new.jpg'], { cwd: d });
  expectRule('an uncommitted image referenced from lesson text (escaped quotes inside JSON)', ['assets'], d); }
{ const d = copy();
  const a = JSON.parse(rd(d, 'content/academy.json'));
  a[0].lessons[0].keyTakeaways[0] += ' </script><script>alert(1)</script> <!-- x';
  wr(d, 'content/academy.json', JSON.stringify(a, null, 1) + '\n');
  rebuild(d);
  const ok = verify(d);
  total++;
  if (ok.failures.length) console.log('NOT CAUGHT: lesson text containing </script> was not made safe: ' + ok.failures.join(' | '));
  else { caught++; console.log('caught: lesson text containing </script> and <!-- is escaped by the build and the page still parses'); }
  wr(d, 'index.html', rd(d, 'index.html').replace('<\\/script><script>alert(1)<\\/script> <\\!-- x', '</script><script>alert(1)</script> <!-- x'));
  expectRule('the same text pasted into index.html unescaped', ['script-escape', 'syntax'], d); }
{ const d = copy(); const uri = 'data:image/jpeg;base64,' + fs.readFileSync(path.join(d, 'assets/img/pop.jpg')).toString('base64');
  editTemplate(d, 'assets/img/pop.jpg', uri); expectRule('an image pasted back in inline', ['inline-images'], d); }
{ const d = copy(); expectRule('index.html over a size ceiling', ['max-bytes'], d, { maxBytes: 1000 }); }
{ const d = copy(); wr(d, 'content/fast-start.js', rd(d, 'content/fast-start.js').replace("{id:'plug'", "{id:'plug',,")); expectBuildError('a syntax error in content/fast-start.js', d); }
{ const d = copy(); wr(d, 'content/states.json', rd(d, 'content/states.json').replace('{', '{,')); expectBuildError('invalid JSON in content/states.json', d); }
{ const d = copy(); fs.rmSync(path.join(d, 'content/carriers.js')); try { expectBuildError('a content file deleted', d); } catch (e) { if (e.code === 'ENOENT') { caught++; console.log('caught: a content file deleted -> ENOENT'); } else throw e; } }

if (caught !== total) { console.log(`FAIL: ${total - caught} of ${total} deliberate breaks were not caught`); process.exit(1); }
console.log(`SELFTEST OK: ${caught}/${total} deliberate breaks caught; clean tree passes`);
