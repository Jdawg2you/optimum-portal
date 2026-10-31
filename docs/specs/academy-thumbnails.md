> **Note (31 Oct 2026):** this brief measures the **older 600x1066** lesson posters. The v3 posters are **1080x1920** portrait, made by `tools/academy-thumbs/make_covers.py`. The Academy image box is 9:16.

# Optimum Academy Thumbnail — Design Brief

A spec for recreating the lesson thumbnails used in the FFL Optimum agent portal.
All measurements below were taken from the existing files, not estimated.

---

## 1. Canvas

| | |
|---|---|
| **Dimensions** | 600 × 1066 px |
| **Aspect ratio** | 9:16 portrait (0.5629 measured — exactly 9:16) |
| **Format** | JPEG, ~100–125 KB each |
| **Orientation** | Portrait. This matters — they render in a portrait grid, so a 16:9 version will crop badly. |

---

## 2. Palette

| Role | Hex | Notes |
|---|---|---|
| Background | `#010D1D` → `#000C1C` | Near-black navy. Essentially flat, with a barely-there vignette darkening the corners. Not a strong gradient. |
| Gold — bright | `#F5B516` | Highlights, glow cores, the brightest edges of the hero object |
| Gold — mid | `#D3971D` | Divider line, icon rings, mid-tones on the hero object |
| Gold — deep | `#69440F` | Shadow side of gold elements, the outer falloff of the divider |
| Title text | `#EEEEEE` | Off-white. Not pure white. |
| Bullet text | `#FEFFFF` | Pure white — slightly brighter than the title, which reads as crisper at small size. |

**The whole design is two colours: gold on near-black navy.** No third accent colour anywhere. Resist adding one.

---

## 3. Layout — five stacked zones

Positions are given as a percentage of the 1066 px height so they scale cleanly.

### Zone 1 — Wordmark · 4.3% → 8.3% (y ≈ 46–88 px)
The word **OPTIMUM** in off-white, centred, all caps, light weight, very wide letter-spacing (roughly 0.35em). Clean geometric sans. Height of the cap ≈ 42 px.

### Zone 2 — Sub-lockup · 10.2% → 11.5% (y ≈ 109–123 px)
**HEALTH | LIFE | RETIREMENT** centred beneath it. Same off-white, all caps, much smaller (cap height ≈ 14 px), wide letter-spacing, separated by thin vertical pipes. The pipes are the same weight as the letterforms.

### Zone 3 — Divider · 14.4% → 15.8% (y ≈ 153–168 px)
A single hairline horizontal gold rule, roughly 60% of the canvas width, centred. It is **not** a flat line: it has a bright four-point star glint at the exact centre (`#F5B516`) that falls off symmetrically to `#69440F` at both ends before fading out entirely. Think of a thin lens flare lying on its side.

### Zone 4 — Title · 18.1% → 43.9% (y ≈ 193–468 px)
The lesson title, centred, **all caps**, in a heavy condensed sans — very tall, very tight, almost no letter-spacing, lines packed close together with minimal leading. Cap height per line ≈ 81 px with ~15 px between lines.

- Two to four lines. Three is the norm.
- Text is broken across lines **for rhythm and to fill the width**, not by grammar. Lines are sized to run nearly edge to edge with a small side margin.
- A parenthetical qualifier — e.g. `(VET SCRIPT §1)` — is set noticeably smaller than the main lines and sits on its own final line.
- Colour `#EEEEEE`, no outline, no drop shadow, no gradient on the type.

### Zone 5 — Hero object · 44.7% → 71.3% (y ≈ 476–760 px)
One single object, centred, occupying roughly a quarter of the canvas height.

- **Rendered as polished gold** — 3D, glossy, with specular highlights and visible metallic depth. Not flat, not an icon, not line art.
- It sits on the dark ground and **emits a soft radial glow** behind itself, warm gold, fading to nothing well before the edges of the canvas.
- Usually one object, occasionally an object plus a supporting element (a location pin beside a winding road; a lightbulb glowing inside a brain).
- No background scene, no environment, no text inside the object — except where a number is integral to it (the stopwatch face reads `90 / SEC`).

Examples in use: a location pin on a curving road, a brain with a glowing filament bulb at its centre, a stopwatch.

### Zone 6 — Bullet rows · 73.5% → 96.5% (y ≈ 783–1029 px)
**Exactly three rows.** Each row is 76–77 px tall with a 9 px gap between rows.

Each row is built the same way, left to right:

1. **Icon badge** — a circular gold ring, ~48 px across, starting at x ≈ 102. Thin gold outline, dark fill, with a simple flat gold pictogram inside (graduation cap, gears, stopwatch, open book, checkmark, clipboard, arrows, a small `YES` bubble). The pictogram matches the bullet's meaning.
2. **Vertical divider** — a short thin gold bar separating the badge from the text.
3. **Text** — two lines, all caps, pure white, in a condensed sans; noticeably smaller than the title but still bold and tight. The text block runs from x ≈ 197 to x ≈ 432.

Bullets are short imperative statements, usually 4–8 words, wrapping to exactly two lines. Em dashes are used freely. Quotation marks appear when quoting the script.

---

## 4. Tone

Premium, high-contrast, cinematic. It should feel like a film poster or a sports-network title card — not a webinar slide. The gold is the only warmth; everything else recedes into the dark.

---

## 5. Prompt scaffold for an image model

Generate the **hero object only** and composite the text yourself — see the note at the end of this brief.

> A single polished gold [OBJECT], photographed in 3D with glossy metallic highlights and deep shadows, centred on a near-black navy background (#010D1D). A soft warm gold radial glow emanates from behind the object and fades to black. No text, no background scene, no environment, no people. Premium cinematic product-render lighting. Square composition, object centred with generous margin.

Fill `[OBJECT]` from the lesson's subject: a stopwatch, a brain with a glowing bulb inside, a location pin on a winding road, a key, a ladder, a compass, a phone handset, a shield.

---

## 6. Recommended approach — read this before you start

**Do not ask an image model to produce the whole thumbnail.** Image models render text unreliably: letters drop, words garble, and the tight condensed type and precise letter-spacing here will not survive. Three bullet rows of small all-caps text is close to a worst case for them.

The reliable split is:

- **Image model** → the gold hero object only, one per thumbnail, on a plain dark background. That is what image models are genuinely good at.
- **Code** → the wordmark, divider, title, bullet rows and badges, rendered as HTML and exported to PNG at exactly 600 × 1066.

That second half produces pixel-identical, perfectly legible type every time, and makes every thumbnail after the first one nearly free — new title, new bullets, new hero object, done.

---

## 7. What is needed per thumbnail

- **Lesson title** — will be set in all caps and broken across 2–4 lines
- **Three bullets** — 4–8 words each, all caps, written to wrap to two lines
- **Icon for each bullet** — a simple concrete object matching the point
- **Hero object** — one noun that captures the lesson

Given a script, all four can be derived from it: the title from the lesson's subject, the three bullets from its key takeaways, and the hero object from its central metaphor.

---
---

# PART 2 — The four thumbnails to build

Four separate images. Same template, same palette, same zone positions as Part 1.
Only the title, the three bullets, the three bullet icons and the hero object change.

**Work one image at a time.** Ask for image 1, check it, then ask for image 2. Requesting
all four in one go reliably produces four inconsistent designs.

---

## IMAGE 1 — Social Media: Your Modern Résumé

**Title** (3 lines, all caps, centred, heavy condensed sans):

```
SOCIAL MEDIA:
YOUR MODERN
RESUME
```

> Use **RESUME** with no accents. The accented É is a common failure point — it drops or
> corrupts. The design is all-caps anyway, so nothing is lost.

**Hero object:** a polished gold smartphone standing upright, with a glowing gold document
— ruled like a résumé — rising out of its screen. Warm gold glow behind.

**Bullet rows:**

| # | Icon | Line 1 | Line 2 |
|---|---|---|---|
| 1 | Magnifying glass | THEY LOOK YOU UP | BEFORE THEY TRUST YOU |
| 2 | Calendar | ONE VALUE POST A DAY — | NO DANCES, NO MEMES |
| 3 | Rising bar chart | IT COMPOUNDS IN MONTHS, | NOT WEEKS |

---

## IMAGE 2 — Recruit From Day One (as a Referral)

**Title** (3 lines; the parenthetical on its own final line, set noticeably smaller):

```
RECRUIT FROM
DAY ONE
(AS A REFERRAL)
```

**Hero object:** a polished gold relay baton mid-handoff, tilted, with a glowing gold light
trail streaking behind it. One baton only — no runners, no track.

**Bullet rows:**

| # | Icon | Line 1 | Line 2 |
|---|---|---|---|
| 1 | Two arrows passing | REFER THEM — | DON'T BUILD OR TRAIN |
| 2 | Phone with a message | FIVE MINUTES AND A TEXT. | THAT'S THE WHOLE COST |
| 3 | Checkmark | CLIENT CALLS | ALWAYS COME FIRST |

---

## IMAGE 3 — The Five-Minute Recruiting Conversation

**Title** (3 lines):

```
THE FIVE-MINUTE
RECRUITING
CONVERSATION
```

**Hero object:** two overlapping polished gold speech bubbles, the smaller one in front
carrying a glowing `5 MIN` on its face. Warm gold glow behind.

> A number on the hero object is on-brand — an existing thumbnail uses a stopwatch reading
> `90 / SEC`. Do **not** use a stopwatch here; that one is already taken and the set should
> not repeat hero objects.

**Bullet rows:**

| # | Icon | Line 1 | Line 2 |
|---|---|---|---|
| 1 | Eye | LOOK FOR TIRED, | NOT IMPRESSIVE |
| 2 | Two speech bubbles | TWO QUESTIONS, THEN | HAND THEM YOUR NUMBER |
| 3 | Hourglass | FIVE MINUTES BREEDS CURIOSITY — | FORTY-SEVEN BREEDS CONTEMPT |

> Row 3 runs long. If it will not fit two lines cleanly, shorten to
> `LESS IS MORE —` / `FIVE MINUTES, NOT FORTY-SEVEN`.

---

## IMAGE 4 — Identity & Longevity

**Title** (2 lines — larger than the others, since there are only two):

```
IDENTITY
& LONGEVITY
```

**Hero object:** a polished gold ladder rising upward and disappearing into a warm gold
glow at the top. Viewed straight on, slightly below eye level so it reads as climbing.

**Bullet rows:**

| # | Icon | Line 1 | Line 2 |
|---|---|---|---|
| 1 | Crown | WORK FROM WHO YOU ARE, | NOT TOWARD THINGS |
| 2 | Hourglass | TWO TO FIVE YEARS — | NOT NINETY DAYS |
| 3 | Two people | TAKE PROBLEMS TO PRODUCERS, | NOT COMPLAINERS |

---

## Attach the reference images

**Yes — attach them.** This is the single biggest thing you can do for consistency. A written
description of "polished gold on near-black navy" leaves an enormous amount of room; three
real examples close almost all of it.

Attach `REFERENCE-1.jpg`, `REFERENCE-2.jpg` and `REFERENCE-3.jpg` to your first message,
with wording like:

> These three images are the existing set. Match them exactly — same 600×1066 portrait canvas,
> same near-black navy background, same gold, same OPTIMUM header lockup, same divider, same
> heavy condensed all-caps title, same single glowing gold hero object, same three bullet rows
> with circular gold icon badges. Only the title, the bullets and the hero object change.
> Build **image 1** from the spec below.

Keep all four in the **same chat**. Each finished image becomes another reference for the next,
and consistency improves as you go.

---

## If the text comes out wrong

It probably will — three rows of small condensed all-caps is close to the worst case for an
image model. Two ways out:

1. Ask for the thumbnail **without any bullet text** — just background, header, title and hero
   object — and have the bullet rows added afterwards in code or a design tool.
2. Ask for the **hero object alone** on a plain near-black navy background, and have the whole
   frame built around it. This is the reliable route, and it is what Part 1 §6 recommends.

---

## Source material these were drawn from

| Image | Lesson | Video |
|---|---|---|
| 1 | 5.1 — Social Media: Your Modern Résumé | https://youtube.com/shorts/CRSADN81wiA |
| 2 | 5.2 — Recruit From Day One (as a Referral) | https://youtube.com/shorts/txcPfzVu9ao |
| 3 | The Five-Minute Recruiting Conversation (new) | https://youtube.com/shorts/8y65W93OYL0 |
| 4 | 5.3 — Identity & Longevity | https://youtube.com/shorts/pmMw3_Ve5uM |

Every bullet above is lifted from that lesson's own notes, compressed to fit two lines of
all-caps without losing the point.
