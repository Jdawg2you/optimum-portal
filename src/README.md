# Source for portal.ffloptimum.com

`index.html` at the repo root is a **build artifact**, not something to edit by hand.
It is ~9 MB because the Academy content and three standalone tools are embedded in it.
These files are what produce it.

## Build

```
python3 merge.py      # writes index.html
```

No dependencies, no build server, no package.json. Python 3 only.

## What each file is

| File | What it holds |
|---|---|
| `merge.py` | The build. Injects CSS/JS into the base HTML at comment tokens. |
| `uploaded_v2.html` | Base page: shell, nav, login, Fast Start + Get Licensed content, carriers, Tools of the Trade. |
| `m5_assets.py` | `M5_CSS` + `M5_SCRIPT` — dashboard, pre-licensing, academy. |
| `reskin_assets.py` | `RESKIN_STYLE` + `RESKIN_JS` — visual layer, Agency Dashboard, new-recruit cards. |
| `acad_manifest.json` | 5.3 MB of Academy lesson content. |
| `register.html` | The registration page. Standalone — **not** part of the merge. |

## Two things that will bite you

**1. `merge.py` escapes `</` to `<\/` when injecting the manifest.** Without that, lesson
HTML closes the surrounding `<script>` tag and the whole page dies. Any change to how
content gets inlined into a script tag needs the same escaping.

**2. The list that is displayed and the list that is scored must be the same object.**
A percentage was once computed against `GYL` while the page rendered `PRE_STEPS`. The two
shared no step IDs, so every unlicensed agent read 0% no matter what they did. It was
invisible for weeks because 0% looks like "hasn't started yet".

## Backend

The backend is a Google Apps Script web app bound to the "FFL Optimum New Agent Intake
Form (Responses)" spreadsheet. It is **not** in this repo — it lives in the Apps Script
editor attached to that sheet. The sheet is the database.

## Deploying

Upload the rebuilt `index.html` to the repo root. GitHub Pages serves it at
portal.ffloptimum.com, usually within a minute.
