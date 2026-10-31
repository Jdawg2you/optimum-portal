// Measure each Academy lesson video's real length on YouTube and store it as videoSeconds.
//
//   node tools/video-lengths.mjs          writes content/academy.json, then rebuild
//   node tools/video-lengths.mjs --check  exits 1 if any stored length is missing or out of date
//
// The portal adds these up for "about N min of video left" on the way to Clear to Dial.
// videoTargetSeconds is the length a lesson was planned at; videoSeconds is what was published.
import fs from 'node:fs';
import { REPO } from './lib/harness.mjs';

const FILE = REPO + '/content/academy.json';
const raw = fs.readFileSync(FILE, 'utf8');
const A = JSON.parse(raw);
const check = process.argv.includes('--check');
const ytId = u => ((u || '').match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|shorts\/|embed\/))([\w-]+)/) || [])[1];

async function length(id) {
  const res = await fetch('https://www.youtube.com/watch?v=' + id, { headers: { 'user-agent': 'Mozilla/5.0', 'accept-language': 'en' } });
  const m = (await res.text()).match(/"lengthSeconds":"(\d+)"/);
  if (!m) throw new Error(`no length found for video ${id} (HTTP ${res.status}) - is it private or deleted?`);
  return Number(m[1]);
}

const problems = []; let changed = 0;
for (const m of A) for (const l of m.lessons) {
  const id = ytId(l.videoEmbedUrl);
  if (l.status === 'coming_soon' || !id) continue;
  const s = await length(id);
  if (l.videoSeconds !== s) {
    problems.push(`${l.id}: stored ${l.videoSeconds ?? 'nothing'}, YouTube says ${s}s`);
    // keep the field next to the video it measures
    const out = {};
    for (const [k, v] of Object.entries(l)) { if (k === 'videoSeconds') continue; out[k] = v; if (k === 'videoEmbedUrl') out.videoSeconds = s; }
    Object.keys(l).forEach(k => delete l[k]); Object.assign(l, out); changed++;
  }
}
if (check) { if (problems.length) { console.log('VIDEO LENGTHS OUT OF DATE:\n' + problems.join('\n')); process.exit(1); } console.log('VIDEO LENGTHS CURRENT'); }
else { if (changed) fs.writeFileSync(FILE, JSON.stringify(A, null, 1) + (raw.endsWith('\n') ? '\n' : '')); console.log(problems.join('\n') || 'no changes'); console.log(`${changed} lesson(s) updated`); }
