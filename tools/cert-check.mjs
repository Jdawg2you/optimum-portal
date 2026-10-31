// Certificate check (handoff step 1's one real trap).
//
// m5DrawCert paints the certificate base image onto a canvas and calls toDataURL.
// Inline, that image was ready the instant it was assigned; as a file it arrives
// over the network, so this test makes it arrive late on a cold cache and then
// does what an impatient agent does: opens the Academy and presses Download before
// the image is in. It passes only when:
//   - the on-page certificate fills in,
//   - the download is a real 1426x1103 PNG,
//   - the download and the on-page image are byte-identical,
//   - both are byte-identical to the certificate the --old build draws for the same
//     agent on the same date (so the name and date are on it exactly as before),
//   - a different name draws a different certificate (the name really is painted).
//
//   node tools/cert-check.mjs --old origin/main --new . [--save cert.png]
import fs from 'node:fs';
import path from 'node:path';
import { materialize, startServer, launch, makeBackend, preparePage, login, seedProgress, tmpDir, fail } from './lib/harness.mjs';

const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
const OLD = materialize(arg('--old', 'origin/main'));
const NEW = materialize(arg('--new', '.'));
const CERT_PATH = /certificate-base\.jpg$/;
const LATE_MS = 9000;

function pngInfo(buf) {
  const sig = buf.subarray(0, 8).toString('hex');
  if (sig !== '89504e470d0a1a0a') return null;
  return { w: buf.readUInt32BE(16), h: buf.readUInt32BE(20) };
}
const fromDataURL = u => Buffer.from(u.split(',')[1], 'base64');

async function drawFor(root, { late }) {
  const server = await startServer(root);
  const browser = await launch(); // fresh profile every time: a cold cache
  try {
    const page = await browser.newPage();
    const backend = makeBackend();
    const rec = await preparePage(page, { origin: server.origin, backend, cache: false });
    const dl = tmpDir('download');
    const cdp = await page.createCDPSession();
    await cdp.send('Browser.setDownloadBehavior', { behavior: 'allow', downloadPath: dl });

    await page.goto(server.origin + '/', { waitUntil: 'load' });
    await seedProgress(page, 'all');
    if (late) server.setDelays([{ re: CERT_PATH, ms: LATE_MS }]);
    await page.reload({ waitUntil: 'domcontentloaded' });
    await login(page);
    const startedLate = late ? await page.evaluate(() => !(m5CertBase.complete && m5CertBase.naturalWidth)) : null;
    if (late && !startedLate) fail('the certificate image was already loaded, so the slow path was not exercised');

    await page.evaluate(() => { m5acad.view = 'home'; go('academy'); });
    await page.waitForSelector('#m5certimg', { timeout: 10000 });
    await page.click('.m5-certcard .m5-goldbtn'); // press Download straight away

    const target = path.join(dl, 'Optimum-Academy-Certificate.png');
    const deadline = Date.now() + LATE_MS + 15000;
    let onPage = '';
    while (Date.now() < deadline) {
      onPage = await page.$eval('#m5certimg', i => i.getAttribute('src') || '');
      if (onPage.startsWith('data:image/png') && fs.existsSync(target) && fs.statSync(target).size > 0) break;
      await new Promise(r => setTimeout(r, 250));
    }
    if (!onPage.startsWith('data:image/png')) fail(`${late ? 'cold/late' : 'warm'} build: the on-page certificate never filled in`);
    if (!fs.existsSync(target)) fail(`${late ? 'cold/late' : 'warm'} build: pressing Download produced no file`);
    await new Promise(r => setTimeout(r, 300));
    const file = fs.readFileSync(target);

    const other = await page.evaluate(() => new Promise(res => {
      store.data.first = 'Zed'; store.data.last = 'Other'; m5DrawCert(res);
    }));
    if (rec.errors.length) fail('page errors: ' + rec.errors.join(' | '));
    if (rec.leaked.length) fail('outside requests leaked: ' + rec.leaked.join(', '));
    return { onPage: fromDataURL(onPage), file, other: fromDataURL(other), certRequests: server.log.filter(x => CERT_PATH.test(x.path)) };
  } finally {
    await browser.close(); await server.close();
  }
}

const before = await drawFor(OLD, { late: false });
const after = await drawFor(NEW, { late: true });

const info = pngInfo(after.file);
if (!info) fail('the download is not a PNG');
if (info.w !== 1426 || info.h !== 1103) fail(`the download is ${info.w}x${info.h}, expected 1426x1103`);
if (!after.file.equals(after.onPage)) fail('the download differs from the certificate shown on the page');
if (!after.file.equals(before.file)) fail('the certificate differs from the one the old build draws for the same agent and date');
if (after.file.equals(after.other)) fail('a different name drew the same certificate - the name is not being painted');
if (after.certRequests.length === 0) fail('the new build never requested assets/img/certificate-base.jpg (is the image still inline?)');
console.log(`old build certificate: ${before.file.length} bytes; new build (cold cache, image ${LATE_MS} ms late, Download pressed first): ${after.file.length} bytes, ${info.w}x${info.h}, identical`);
if (arg('--save')) fs.writeFileSync(arg('--save'), after.file);
console.log('CERT OK');
