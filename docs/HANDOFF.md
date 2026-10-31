> **Status (31 Oct 2026):** steps 0-4 are done. `git push` works from the Mac; the tools in section 5 were lost with the cloud workspace and are rebuilt in `tools/` (`ticksafe.mjs`, `compare-render.mjs`, `cert-check.mjs`, `verify.mjs`, `live-check.mjs`). `index.html` is now **built** from `source/` + `content/`, so "index.html is the source of truth" below no longer holds. See the README.

# Handoff — moving the Optimum Agent Portal onto a code workflow

**For:** a fresh Claude Code thread working in `Jdawg2you/optimum-portal`
**From:** the thread that shipped Academy v3.6 on 29 Oct 2026
**Owner:** Jesse Stamm

Read this whole file before touching anything. The short version: this is
doable cleanly, every step can be proven byte-for-byte, and the dangerous part
is not the code — it is the deploy channel. Fix that first.

---

## 1. What this is

`portal.ffloptimum.com` is a single hand-edited `index.html` served by GitHub
Pages from the repo root. It is the daily tool for Jesse's agents. It holds the
Optimum Academy (55 lessons), Fast Start, Get Licensed, the Goal Card, Agency
Dashboard, Income Calculator, events, carriers and a dozen tools.

Live right now: `main` at `0974a61`. Academy v3.6 — 55 lessons, 50 published,
5 Coming Soon, 50 videos embedded, 50 thumbnails.

**`index.html` is the source of truth. Nothing else is.**

### The numbers that matter

| | |
|---|---|
| `index.html` | 4,861,993 bytes |
| of which 21 inline base64 images | **3.88 MB (84%)** |
| actual code + content | ~760 KB |
| `<script>` blocks | 10 |
| `<style>` blocks | 5 |
| top-level data structures (`GYL`, `FAST`, `WEEK`, `CARRIERS`, `M5_STATES`, `ACAD_LMS`, …) | 62 |
| sibling pages in the repo | 18 more `.html` files |

That 84% is the headline. This file is not 4.8 MB of tangled code. It is
~760 KB of code wearing 3.9 MB of images.

---

## 2. Hard constraints — break any of these and agents lose work

### 2.1 Completion data is sacred

Agent progress lives in `store.data.checks`, keyed by string, synced to a
Google Sheet through an Apps Script backend **that is not in this repo**.

- `acad_<lessonId>` — lesson complete. Value is an ISO timestamp. **Never
  cleared, ever.** `acadDone()` only checks truthiness.
- `acaddo_<lessonId>_<index>` — a "Do This Next" checkbox. **Keyed by array
  position.** Reordering or inserting a step silently re-points every later
  tick at a different instruction.
- `acaddo_<lessonId>v<rev>_<index>` — the same thing for a lesson whose steps
  were rewritten. The `dnRev` field on the lesson selects the key space. 2.6.1,
  3.1 and 4.3 are at `dnRev:2`. See `acadDoKey()`.
- Certificate: `cp.pct>=100 || store.data.t_acadDone`. **Once earned, always
  earned** — the Academy can grow and push the percentage below 100; the
  certificate does not come back off the wall.
- `coming_soon` lessons count in no numerator and no denominator, and
  `acadMarkComplete` refuses to tick them.

**The rule when content changes:** adding a do-next step must append; replacing
one must keep its index; anything else must move the lesson to a new `dnRev`
rather than deleting a key. Migrations in `m5MigrateChecks` are **additive
only** — they copy an old key to a new one and never remove the old.

There is a working test for this: `ticksafe.mjs` (see §5). It seeds a browser
profile with pre-release progress on the live build, serves the new build from
the same origin, and asserts completions and the certificate survive. **Run it
before every deploy.** It must be the same origin — different ports mean
different `localStorage` and the test silently passes on an empty store.

### 2.2 The Ask Optimum line

```html
<script src="ask-optimum.js?v=2" defer></script>
```

Remove it and the Ask Optimum button, the dashboard ask bar and the
pre-licensing help card vanish for every agent. The repo README calls this out.
Any build must assert this line survives.

### 2.3 The backend is not in this repo

A Google Apps Script web app bound to the "FFL Optimum New Agent Intake Form
(Responses)" spreadsheet. The sheet is the database. Do not try to change it
from the portal repo. Jesse has a standing instruction: **no edits to the
intake form responses sheet.**

### 2.4 `src/` is a trap

`src/` holds a disabled build (`merge.py` raises `SystemExit` on import) whose
sources were last touched **31 August**. Its own header lists what building
from it would silently revert. `src/acad_manifest.json` describes 44 lessons;
live has 55.

**Do not build from `src/`. Do not trust `src/acad_manifest.json`.** Treat the
whole folder as an archive. Deleting it is a reasonable early step, once the
new build exists.

---

## 3. The deploy channel — this is the real risk

`git push` **does not work**:

```
remote: access denied by the git proxy: Jdawg2you/optimum-portal is not in
this session's authorized repository set, so the proxy will not inject a
credential for it. To fix, add the repository to the session's sources.
```

`git fetch` works fine. So the only way to ship is the **GitHub web upload
form**, driven through a browser, which replaces whole files.

### What went wrong on 29 Oct, twice

Both bugs shipped despite the build being correct locally and every test
passing. Both were invisible to local testing:

1. Uploaded `index.html` alone. Eleven `posters/*.jpg` the new lessons
   reference were never uploaded → **404** → eleven lessons showed an empty
   player. The page does not error on a missing image.
2. Fixed it by uploading only the files that were *missing*. Three more
   (2.6.1, 3.1, 4.3) already existed under the same names and were left at
   their old 600×1066 versions, so three lessons with brand-new videos kept
   their old thumbnails. **All three returned HTTP 200.** Status proves a file
   is there, not that it is the right file.

### The check that catches both

After any deploy, fetch and re-diff:

```bash
git fetch origin main
git diff --name-status origin/main HEAD    # empty, or the deploy is incomplete
```

An empty diff is the only proof. Add to it: load every referenced asset from
the live site and check its **dimensions or byte length**, not its status code.

### Therefore: step 0 is to fix the deploy

Getting `push` working — adding the repo to the session's authorized sources —
removes the manual upload step that caused both bugs. Everything else in this
plan is safer afterwards and more dangerous before. **Ask Jesse to do this
first.**

---

## 4. What is already proven

Don't re-derive these; they were tested on the live file today.

**The Academy data extracts and reassembles byte-for-byte.** Split
`index.html` at `const ACAD_LMS=` … `];`, write the literal to JSON with
`json.dumps(data, indent=1, ensure_ascii=False)`, put `__ACAD_LMS__` in its
place, then substitute back:

```
index.html  4861993 chars  md5 8b1a3f3f723f
rebuilt     4861993 chars  md5 8b1a3f3f723f
ROUND TRIP BYTE-IDENTICAL: True
```

The literal is *already* JSON — a previous step rewrote it that way — so it
round-trips exactly. `acadlib.py` (§5) does this and asserts the prefix and
suffix come back untouched on every save. It was used for four separate edits
today without incident.

**The `</` escape matters.** When a JSON blob is injected inside a `<script>`
tag, `</` must become `<\/` or lesson HTML can terminate the script tag and
kill the page. The old `merge.py` did this; any new build must too.

---

## 5. Tools that already exist — in `/mnt/user-data/uploads/academy-v3/`

| File | What it does |
|---|---|
| `acadlib.py` | Load / mutate / save `ACAD_LMS` with prefix+suffix byte assertions, plus `snapshot()` and `diff()` for before/after field comparison |
| `ticksafe.mjs` | **The important one.** Proves no agent progress is lost across an upgrade |
| `gate.mjs` | Per-lesson render gate: takeaways, do-next, poster loads, facade sized, embed and watch link match the lesson's own video. Takes `--expect-fail` for a positive control |
| `final.mjs` | Walks all 19 nav views, 13 modules and a lesson in each, collecting JS errors |
| `step7.py`, `step4b.py`, `part4.py` | Doc-parsing and applying, with word-for-word match assertions |
| `patches/` | The 9 commits of the v3.6 build as replayable patches |
| `part10-inventory.{md,csv}` | 76-row inventory: every Academy lesson and Fast Start step |

All of these launch headless Chromium via
`/home/claude/.npm-global/lib/node_modules/playwright/index.js` with
`executablePath:'/opt/pw-browsers/chromium', args:['--no-proxy-server']`.
They serve the repo over a local HTTP server — **`file://` will not work**,
several things in the page need a real origin.

---

## 6. The sequence

Each step is independently provable and independently revertible. Do not start
the next one until the current one is proven. **No step requires a rewrite.**

### Step 0 — Fix the deploy channel *(blocks everything; Jesse's action)*
Get `git push` working. Until then every step below ships through a browser
form and carries the §3 risks.
**Proven when:** `git push` succeeds and `git diff origin/main HEAD` is empty.

### Step 1 — Extract the images *(biggest win, lowest risk)*
21 inline base64 images are 84% of the file. Write each to `assets/` and
replace the data URI with a path.
**Careful — `IMG_CERT` is the one to test.** `m5DrawCert` paints it onto a
canvas and calls `c.toDataURL('image/png')` to build the downloadable
certificate. Two things to know, both verified in the live file:

- Serving it from `assets/` keeps it same-origin, so canvas tainting should
  *not* occur. But the whole function body is wrapped in `try{…}catch(e){}`
  **with an empty catch** — if it ever did throw, the download button would
  silently do nothing. You would not see an error.
- The real behaviour change is timing. A data URI is complete the instant it
  is assigned; a network image is not. `m5DrawCert` already handles this
  (`if(m5CertBase.complete&&m5CertBase.naturalWidth)draw(); else
  m5CertBase.onload=draw;`), but that `else` branch has probably never run in
  production. Test it with a cold cache.

The large images are `IMG_CERT`, `IMG_SCHEDULE`, `IMG_MANHATTAN`, `IMG_HUDDLE`
and `IMG_LICENSED`. Convert the safe ones; leave any that must stay inline, and
say which and why.
**Proven when:** the page renders identically, the certificate **downloads a
real PNG with the agent's name on it on a cold cache**, and `index.html` drops
from 4.86 MB to roughly 1 MB.

### Step 2 — Extract the content data
Start with `ACAD_LMS` → `content/academy.json` (already proven, §4). Then the
other 61 structures, a few at a time: `WEEK`, `CARRIERS`, `M5_STATES`, `FAST`,
`GYL` are the ones that change most.
**Proven when:** `build.py` reproduces the committed `index.html` byte-for-byte
from template + data, every time, as a test.

### Step 3 — A build with teeth
`build.py` plus a `verify` step that refuses to emit a file unless:
- every `<script>` block passes `node --check`
- the Ask Optimum line is present
- every asset path referenced in the HTML exists on disk
- `</` is escaped inside injected JSON
- `ticksafe.mjs` passes against the previous committed build
**Proven when:** deliberately breaking each check makes the build fail. Test
the failure, not just the success.

### Step 4 — Deploy as one command
`deploy.sh`: build → verify → commit → push → wait for Pages → fetch every
referenced asset from the live site and compare byte length → `git diff
origin/main HEAD` must be empty.
**Proven when:** it catches a deliberately omitted asset.

### Step 5 — Only now, consider structure
Splitting the 10 script blocks into modules, a dev server, etc. This is
optional and lowest value. Do not start it until 0–4 are done.

---

## 7. What not to do

- **Do not rewrite the portal.** The accumulated behaviour is the asset: the
  completion rules, the sheet sync, the Spanish layer (`M5_ES`), the
  pre-licensed fork, the certificate. A rewrite puts all of it at risk to gain
  tidiness.
- **Do not build from `src/`.** §2.4.
- **Do not touch the Apps Script backend or the intake-form sheet.**
- **Do not reformat `index.html`** (prettier, a formatter, "cleanup"). It
  destroys the byte-level diffs that make every step above provable, and buries
  real changes in noise.
- **Do not trust a green local test as proof a deploy worked.** Both 29 Oct
  bugs passed locally. Check the live site.
- **Do not clear a tick**, in a migration or anywhere else.

---

## 8. Open items inherited from v3.6

1. **0.0 and 1.3 are held.** Part 6 of the production doc pairs their new text
   with a new video; Jesse has not cleared either video, so neither the text
   nor the video went in. They keep their current content.
2. **T.1** is Coming Soon pending Jesse's review of its video.
3. **Part 8's Daily Focus `e1`/`sd1`** name ids the widget no longer has.
4. **2.5.3's Script Navigator URL** is the doc's bare `script.ffloptimum.com`;
   2.4.1 uses the working deep link `?script=veteran`. Worth reconciling.
5. **Part 3 of the production doc says 1280×720 thumbnails and is wrong.** The
   Academy image box is 9:16. The 14 v3 lessons are 1080×1920; the 37 older
   ones are 600×1066.
6. **Part 10 inventory is partial** — Academy and Fast Start are exported; New
   Agent Orientation, the weekly-call recording libraries, the tool pages and
   the Recruiter Playbook still need a pass.

---

## 9. Answering the question honestly

**Can this be done without breaking anything? Yes — under three conditions.**

1. **Step 0 happens first.** While deploys are a human dragging files into a
   web form, every change carries a risk that has nothing to do with the
   change itself. Both 29 Oct bugs were deploy bugs, not code bugs.
2. **Every step proves itself byte-for-byte before the next begins.** The
   round-trip test in §4 is the model: not "it looks right" but "the rebuilt
   file is identical to the committed one". A step that cannot be proven that
   way should be split until it can.
3. **`ticksafe.mjs` runs before every deploy.** Agent progress is the one thing
   that cannot be restored from a git revert.

The thing that makes this tractable is that the file is 84% images. Step 1
alone removes most of the bulk without touching a line of logic, and after
Step 2 the content that actually changes week to week lives in JSON files you
can read in a diff. Neither step requires understanding all 760 KB of code at
once.

**The honest risk:** Step 1 has one real trap (canvas tainting on the
certificate image) and Step 2 has 62 structures, some of which may have
subtleties the way `ACAD_LMS` had the `</` escape. Both are discoverable by
testing, not by reading. Budget for finding a few.
