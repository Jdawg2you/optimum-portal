// One-time migration (handoff step 1): move the 21 inline base64 images out of
// index.html into assets/img/ and point index.html at the files.
//
// Each image is identified by the sha256 of its decoded bytes, so this refuses to
// run on a file whose images differ from the ones named here, and running it a
// second time is a no-op. The bytes written are exactly the decoded data URI, and
// the only change to index.html is each data URI's text becoming a path.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { REPO } from '../lib/harness.mjs';

const NAMES = {
  ca2b082b9e32: 'optimum-logo.png',          // .m5-logoimg
  '1b9c9e07dc4d': 'prelicensing-video.jpg',  // .m5-prevideo
  b7fccf6b7f29: 'licensed-video.jpg',        // .m5-licvideo
  c289b5861a92: 'fast-start-video.jpg',      // .m5-fsvideo
  '01915ebc592d': 'strategy-video.jpg',      // .m5-stratvideo
  da3255571c32: 'prelicensing-snapshot.jpg', // IMG_PRELIC
  '41d6f3045935': 'licensed-snapshot.jpg',   // IMG_LICENSED
  '0c6e93401ee0': 'morning-kickoff.jpg',     // IMG_READING
  df14539c8e28: 'vbo-everyday.jpg',          // IMG_VBO
  '6e32e323a874': 'shawn-coaching.jpg',      // IMG_SHAWN
  e695e0f846fe: 'ignyte-fall-2026.jpg',      // IMG_IGNYTE
  '282b467dae25': 'convention-2027.jpg',     // IMG_CONVENTION
  '0a0605707e5c': 'weekly-schedule.jpg',     // IMG_SCHEDULE
  ff7dfdf1fb85: 'huddle.jpg',                // IMG_HUDDLE
  '7a447525bd0b': 'pop.jpg',                 // IMG_POP
  '9437ff1b81f0': 'manhattan-life.jpg',      // IMG_MANHATTAN
  d1d9319e70f8: 'mmaker.jpg',                // IMG_MMAKER
  '2bb78f34ba1b': 'dashboard-snapshot.jpg',  // <img class="m5-snapshot">
  '3eaad80b6d29': 'firstvbo-flyer.jpg',      // <img class="m5-flyer">
  '0e68c5fb4064': 'certificate-base.jpg',    // IMG_CERT, painted onto a canvas
  f73c54f8a84c: 'agency-overview-thumb.jpg', // M5_OVERVIEW_THUMB
};
const MAGIC = { png: '89504e47', jpeg: 'ffd8ff' };

const file = path.join(REPO, 'index.html');
const outDir = path.join(REPO, 'assets', 'img');
let html = fs.readFileSync(file, 'utf8');
const re = /data:image\/(png|jpeg);base64,([A-Za-z0-9+/=]+)/g;
const found = [];
for (const m of html.matchAll(re)) {
  const bytes = Buffer.from(m[2], 'base64');
  if (bytes.toString('base64') !== m[2]) throw new Error('base64 does not round-trip at offset ' + m.index);
  if (!bytes.toString('hex').startsWith(MAGIC[m[1]])) throw new Error(`declared ${m[1]} but bytes say otherwise at ${m.index}`);
  const id = crypto.createHash('sha256').update(bytes).digest('hex').slice(0, 12);
  const name = NAMES[id];
  if (!name) throw new Error(`unknown inline image ${id} (${bytes.length} bytes) at offset ${m.index}`);
  found.push({ uri: m[0], bytes, name, id });
}
if (found.length === 0) { console.log('no inline images left; nothing to do'); process.exit(0); }
if (found.length !== Object.keys(NAMES).length) throw new Error(`expected ${Object.keys(NAMES).length} images, found ${found.length}`);

fs.mkdirSync(outDir, { recursive: true });
for (const f of found) {
  const dest = path.join(outDir, f.name);
  if (fs.existsSync(dest) && !fs.readFileSync(dest).equals(f.bytes)) throw new Error(dest + ' exists with different bytes');
  fs.writeFileSync(dest, f.bytes);
  const before = html.length;
  html = html.split(f.uri).join('assets/img/' + f.name);
  if (before - html.length !== f.uri.length - ('assets/img/' + f.name).length) throw new Error(f.name + ' was not replaced exactly once');
}
fs.writeFileSync(file, html);
console.log(`moved ${found.length} images to assets/img/; index.html is now ${Buffer.byteLength(html)} bytes`);
