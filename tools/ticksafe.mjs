// ticksafe: proves no agent progress is lost across an upgrade. Run before every deploy.
//
// Agent progress cannot be restored by a git revert, so this test plays the upgrade
// the way an agent lives it. On ONE origin (localStorage is per origin; two ports
// would pass on an empty store) it:
//   1. serves the --old build, seeds an agent's progress, logs in through the real
//      form, and lets the page save to the (mocked) sheet;
//   2. swaps the server to the --new build, reloads, logs in again;
//   3. opens the new build on a second, empty device, where progress can only come
//      back from the sheet copy.
// Twice: an agent who finished the Academy (certificate earned) and one halfway.
//
// It fails when, in the new build, on either device:
//   - a lesson the agent completed shows as not complete, or no longer exists,
//   - a do-next tick is gone from a lesson whose dnRev did not change,
//   - a Fast Start step the agent ticked shows unticked,
//   - an earned certificate is not on the Academy page,
//   - any stored tick changed value or was cleared, locally or in the sheet copy.
// Lessons legitimately removed can be named with --allow-removed id,id.
//
//   node tools/ticksafe.mjs --old origin/main --new .
//   node tools/ticksafe.mjs --selftest     # proves it fails on two broken builds
import fs from 'node:fs';
import path from 'node:path';
import { materialize, startServer, launch, makeBackend, preparePage, login, seedProgress, settle, tmpDir, fail, AGENT } from './lib/harness.mjs';

const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };

function readProgress(page) {
  return page.evaluate(() => {
    const lessons = [];
    ACAD_LMS.forEach(m => m.lessons.forEach(l => lessons.push({
      id: l.id, cs: acadIsCS(l), done: acadDone(l.id), rev: l.dnRev || 1,
      dn: (l.doNext || []).map((_, i) => !!store.data.checks[acadDoKey(l, i)]),
    })));
    const fast = [];
    FAST.forEach(g => (g.items || []).forEach(it => { if (it.id) fast.push({ id: it.id, done: isDone(it.id) }); }));
    m5acad.view = 'home'; go('academy');
    return {
      lessons, fast, course: acadCourseProgress(),
      cert: !!document.getElementById('m5certimg'),
      store: JSON.parse(localStorage.getItem('optimumPortalV2') || 'null'),
    };
  });
}

function compare(label, before, after, sheetAfter, allowRemoved, problems) {
  const p = msg => problems.push(`${label}: ${msg}`);
  const nl = new Map(after.lessons.map(l => [l.id, l]));
  for (const l of before.lessons) {
    const n = nl.get(l.id);
    if (!n) { if (l.done && !allowRemoved.includes(l.id)) p(`completed lesson ${l.id} no longer exists`); continue; }
    if (l.done && !n.done) p(`lesson ${l.id} was complete and now is not`);
    if (l.rev === n.rev) l.dn.forEach((t, i) => { if (t && !n.dn[i]) p(`do-next ${l.id}[${i}] was ticked and now is not`); });
  }
  const nf = new Map(after.fast.map(f => [f.id, f]));
  for (const f of before.fast) if (f.done && nf.has(f.id) && !nf.get(f.id).done) p(`Fast Start ${f.id} was ticked and now is not`);
  if (before.cert && !after.cert) p('the certificate was earned and is no longer shown');
  const was = (before.store && before.store.checks) || {};
  for (const [where, s] of [['local', after.store], ['sheet', sheetAfter]]) {
    const now = (s && s.checks) || {};
    for (const [k, v] of Object.entries(was)) if (v && now[k] !== v) p(`${where} tick ${k} was ${JSON.stringify(v)}, now ${JSON.stringify(now[k])}`);
    if (before.store && before.store.t_acadDone && (!s || s.t_acadDone !== before.store.t_acadDone)) p(`${where} t_acadDone was lost`);
  }
}

export async function ticksafe(oldDir, newDir, { allowRemoved = [], quiet = false } = {}) {
  const problems = [];
  const server = await startServer(oldDir);
  try {
    for (const mode of ['all', 'partial']) {
      const backend = makeBackend();
      const browser = await launch();
      try {
        const page = await browser.newPage();
        const rec = await preparePage(page, { origin: server.origin, backend });
        server.setRoot(oldDir);
        await page.goto(server.origin + '/', { waitUntil: 'load' });
        await seedProgress(page, mode);
        await login(page);
        const before = await readProgress(page);
        if (mode === 'all' && !before.cert) problems.push('setup: the old build did not show the certificate for a finished agent');
        if (!before.course.done) problems.push(`setup (${mode}): the old build shows no completed lessons, so nothing was tested`);
        if (!backend.sheet[AGENT.email]) problems.push(`setup (${mode}): the old build never saved to the sheet`);

        server.setRoot(newDir);
        await page.reload({ waitUntil: 'load' });
        await login(page);
        await settle(page);
        const after = await readProgress(page);
        compare(`${mode}/same device`, before, after, backend.sheet[AGENT.email], allowRemoved, problems);

        const ctx = await browser.createBrowserContext(); // a second device: empty localStorage
        const other = await ctx.newPage();
        const rec2 = await preparePage(other, { origin: server.origin, backend });
        await other.goto(server.origin + '/', { waitUntil: 'load' });
        await other.evaluate(() => localStorage.setItem('m5.lang', 'en'));
        await other.reload({ waitUntil: 'load' });
        await login(other);
        await settle(other);
        const second = await readProgress(other);
        compare(`${mode}/new device`, before, second, backend.sheet[AGENT.email], allowRemoved, problems);

        for (const r of [rec, rec2]) {
          if (r.leaked.length) problems.push('outside requests leaked: ' + r.leaked.join(', '));
          for (const e of r.errors) if (/^local (4|5)\d\d/.test(e)) problems.push(`${mode}: ${e}`);
        }
        if (!quiet) console.log(`${mode}: old ${before.course.done}/${before.course.total} lessons, cert ${before.cert} -> new ${after.course.done}/${after.course.total}, cert ${after.cert}; second device ${second.course.done}/${second.course.total}; sheet saves ${backend.saves.length}`);
      } finally { await browser.close(); }
    }
  } finally { await server.close(); }
  return problems;
}

function brokenCopy(srcDir, transform) {
  const dir = tmpDir('broken');
  fs.cpSync(srcDir, dir, { recursive: true, filter: s => !s.includes(`${path.sep}node_modules`) && !s.includes(`${path.sep}.git`) });
  const f = path.join(dir, 'index.html');
  const before = fs.readFileSync(f, 'utf8');
  const after = transform(before);
  if (after === before) throw new Error('control transform changed nothing');
  fs.writeFileSync(f, after);
  return dir;
}

if (process.argv.includes('--selftest')) {
  const base = materialize(arg('--new', '.'));
  const controls = [
    ['a lesson id renamed (its completion key no longer matches)', s => s.replace('"id": "s-1",', '"id": "s-1-renamed",')],
    ['the completion key prefix changed', s => s.replace("function acadKey(id){return 'acad_'+id;}", "function acadKey(id){return 'acad2_'+id;}")],
  ];
  for (const [name, t] of controls) {
    const problems = await ticksafe(base, brokenCopy(base, t), { quiet: true });
    if (!problems.length) fail(`control not caught: ${name}`);
    console.log(`caught: ${name} (${problems.length} problems, e.g. ${problems[0]})`);
  }
  console.log('TICKSAFE CONTROL CAUGHT');
} else {
  const problems = await ticksafe(materialize(arg('--old', 'origin/main')), materialize(arg('--new', '.')),
    { allowRemoved: (arg('--allow-removed', '') || '').split(',').filter(Boolean) });
  if (problems.length) { console.log(problems.slice(0, 40).join('\n')); fail(`${problems.length} progress problem(s)`); }
  console.log('TICKSAFE PASS');
}
