# optimum-portal

portal.ffloptimum.com, served by GitHub Pages from `main`.

## Do not edit or upload `index.html`

`index.html` is **built**. Since 31 Oct 2026 it is the output of:

| Edit this | What it holds |
|---|---|
| `source/index.template.html` | the page: markup, styles, code |
| `content/academy.json` | Optimum Academy (`ACAD_LMS`) |
| `content/states.json` | state licensing steps (`M5_STATES`) |
| `content/fast-start.js` | Fast Start (`FAST`) |
| `content/get-licensed.js` | Get Licensed (`GYL`) |
| `content/carriers.js` | carriers (`CARRIERS`) |
| `content/events-daily.js`, `events-huddle.js`, `events-week.js` | the call schedule (`DAILY`, `HUDDLE`, `WEEK`) |
| `assets/img/` | page images (no more inline base64) |
| `posters/` | Academy lesson thumbnails, 1080x1920 for v3 lessons |

`tools/content-map.json` says which data structure lives in which file.
Uploading an `index.html` through the GitHub web page replaces the built file
and will be overwritten by the next build. If it happens anyway, adopt the edit
instead of losing it:

```
node tools/build.mjs --extract    # index.html -> source/ + content/, only if the round trip is exact
```

## Ship

```
(cd tools && npm ci)              # once per machine
./deploy.sh --dry-run             # build + every check, nothing pushed
./deploy.sh "What changed"        # build, check, commit, push, then verify the live site
```

`deploy.sh` refuses to ship when `main` is behind `origin/main`, when the page
fails `tools/verify.mjs`, or when `tools/ticksafe.mjs` finds agent progress lost
against what is live. After the push it waits for GitHub Pages and compares
every file the page uses, by sha256, with the commit: a 200 status does not
prove the right file is there (29 Oct: eleven missing thumbnails, then three
stale ones that all returned 200).

## Agent progress is sacred

Progress lives in `store.data.checks` and syncs to the intake Google Sheet
through Apps Script (not in this repo; never edit that sheet from here).

- `acad_<lessonId>` is a completed lesson. **Never rename a lesson id.**
- `acaddo_<lessonId>_<i>` is a do-next tick, keyed by **position**. Append new
  steps; to rewrite steps, bump the lesson's `dnRev`.
- Migrations in `m5MigrateChecks` copy keys forward and never remove one.
- An earned certificate stays earned (`t_acadDone`).

`node tools/ticksafe.mjs --old origin/main --new .` proves it for a change.
Every browser test answers the Apps Script backend with a local mock and refuses
every other outside request, so tests never write to the sheet.

## Ask Optimum

Loaded by one line near the bottom of the page:

```html
<script src="ask-optimum.js?v=2" defer></script>
```

Keep it: without it the Ask Optimum button, the dashboard ask bar and the
pre-licensing help card disappear for every agent. `verify` fails without it.
The chat itself lives in `brain.html` and `ask-optimum.js`.

## Checks

| Command | Proves |
|---|---|
| `node tools/build.mjs --check` | `index.html` is exactly what source/ + content/ build |
| `node tools/verify.mjs` | scripts parse, Ask Optimum line, every referenced file committed in exact case, script escaping, no inline images |
| `node tools/verify-selftest.mjs` | each verify rule fails when deliberately broken |
| `node tools/ticksafe.mjs --old origin/main --new .` | completions, ticks and certificate survive the upgrade (`--selftest` for its controls) |
| `node tools/compare-render.mjs --old origin/main --new .` | every view and lesson renders identically (for refactors, not content changes) |
| `node tools/cert-check.mjs --old origin/main --new .` | the certificate on a cold cache |
| `node tools/live-check.mjs https://portal.ffloptimum.com` | the live site serves HEAD byte for byte |
