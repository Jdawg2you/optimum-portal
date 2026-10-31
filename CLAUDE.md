# Working in optimum-portal

portal.ffloptimum.com. Read `README.md` for the build and the checks. These are the
standing rules; the reasons and the backlog are in `docs/decisions.md`.

## This repo is public

GitHub Pages serves it, and every file here is readable at github.com and at
portal.ffloptimum.com/<path>. Never commit:

- agent PII: names tied to status, emails, phones, NPNs, addresses, survey answers, coaching notes;
- anything from the intake-form responses sheet (it holds IDs, signatures and SSNs);
- the Apps Script backend source or notes on how it can be broken. They are kept privately, not here.

## How changes ship

- Edit `source/index.template.html` and `content/*`. Never edit or web-upload `index.html`;
  it is built. If someone did, `node tools/build.mjs --extract` adopts the edit.
- Ship only with `./deploy.sh "what changed"`. It refuses when `main` is behind, verify
  fails or ticksafe finds lost progress, and it checks the live site by sha256 afterwards.
- Never force-push. A rejected push means someone else shipped; fetch and rebuild on top.

## Jesse's rules

- **Change control (30 Jul 2026).** The portal's structure is locked: left nav, page
  layouts, how pages work. Do not add, remove, reorder, rename, condense or "streamline"
  anything unless Jesse asks for that specific change. Scoped content edits are fine. If a
  scoped edit would change structure as a side effect, stop and ask.
- **Edit the real embedded tools; never rebuild them.** The Activity Planner, Agency Builder,
  Income Calculator and the others are base64 inside the template (`mountFrame`). Decode,
  edit, re-encode, and assert the round trip.
- **No edits of any kind to the intake form responses sheet.** Read only.
- **Never clear a tick.** Never rename a lesson id. Do-next ticks are keyed by position:
  append steps, or bump the lesson's `dnRev`. Migrations copy keys forward, never remove.
- **Data scoping is server-side only.** No full roster ever goes to the browser; the
  hierarchy lives in the sheet, never in code.
- **GOAT order in Fast Start:** leads first (`f_goat_promo`), join second (`f_goat`); the ids
  read backwards on purpose. The leads link is "where you go to buy your leads", not an
  affiliate link.
- **Optimum does not give free leads.** Pull any content that says it does.
- **Approved copy is verbatim:** the Agency Builder prompt and the four New-Recruit card
  states. Do not rewrite either.

## Testing

Browser tests (`tools/lib/harness.mjs`) answer the Apps Script backend with a local mock and
refuse every other outside request, so they never write to the sheet. Testing by hand as
another agent: use a private window. `m5BackendLoad` merges this browser's ticks into the
record it loads, so a normal window can write your ticks onto someone else's record.

## Lesson posters

1080x1920 portrait (`posters/`), made by `tools/academy-thumbs/make_covers.py`. By default it
reproduces the posters as they shipped, in Chrome's fallback bold font, because the original
font link never resolved. `--fonts` renders the intended Anton/Inter, which changes how every
poster looks; that is Jesse's call.
