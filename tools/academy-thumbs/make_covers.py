#!/usr/bin/env python3
"""Optimum Academy lesson covers (9:16) and YouTube thumbnails (16:9).

Two different assets, because they land in different places:
  covers/  1080x1920  the portal lesson card, matching the set Jesse showed me
                      on 28 Oct -- wordmark lockup, big condensed caps, a gold
                      hero illustration, a play button, three takeaway rows
  youtube/ 1280x720   the YouTube thumbnail. Same language, no play button
                      (YouTube draws its own) and no takeaway rows, which are
                      unreadable at the size a thumbnail is actually seen.

Hero art is generated separately and lives in hero/<code>.png. A lesson with no
hero renders with the space closed up rather than a hole.

Usage: make_covers.py [--yt] [--fonts] [lesson code ...]

In the portal repo since 31 Oct 2026. Fonts, the icon set and the wordmark it
borrowed from the tools workspace are vendored in vendor/, so it runs from here.
hero/ is source art and is committed; covers/ and youtube/ are regenerated and
are not. Covers then go into ../../posters/ as the lesson thumbnails.
"""
import html
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ICONS = json.load(open(os.path.join(HERE, "vendor", "icons.json")))
ITEMS = {i["code"]: i for i in json.load(open(os.path.join(HERE, "academy.json")))}
COPY = json.load(open(os.path.join(HERE, "cover-copy.json")))

GOLD, DARK = "#C9A24E", "#070B16"

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:%(w)spx;height:%(h)spx;overflow:hidden;background:%(dark)s}
.c{width:%(w)spx;height:%(h)spx;position:relative;background:%(dark)s;color:#fff;
   font-family:Inter,-apple-system,sans-serif;display:flex;flex-direction:column;
   align-items:center;text-align:center;padding:%(pad)s;overflow:hidden}
/* the glow behind everything, warmest at the top where the lockup sits */
.c:before{content:'';position:absolute;left:50%%;top:-18%%;width:150%%;height:85%%;
  transform:translateX(-50%%);pointer-events:none;
  background:radial-gradient(ellipse at 50%% 45%%,rgba(201,162,78,.20) 0%%,rgba(201,162,78,.07) 38%%,transparent 68%%)}
.c>*{position:relative;z-index:1}
.main{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;width:100%%}
.lock{font-weight:600;letter-spacing:.42em;text-indent:.42em;font-size:%(lock)spx;color:#fff}
.sub{font-size:%(subf)spx;letter-spacing:.30em;text-indent:.30em;color:%(gold)s;margin-top:%(subm)spx;font-weight:600}
.rule{width:%(rule)spx;height:1px;margin:%(rulem)spx 0 0;
  background:linear-gradient(90deg,transparent,%(gold)s 35%%,#fff 50%%,%(gold)s 65%%,transparent)}
h1{font-family:Anton,Impact,sans-serif;text-transform:uppercase;line-height:.98;
   letter-spacing:.005em;margin-top:%(h1m)spx;font-size:%(h1)spx;font-weight:400;
   color:#EEEEEE}
/* No gold line. An earlier version put the last line in a gold gradient and the
   comment claimed his set did that -- it does not. Sampling the bright type
   pixels across all four examples he sent gives rgb(176,176,174) every time,
   and the written brief says the same: "no outline, no drop shadow, no
   gradient on the type". The class stays so the copy data need not change. */
h1 .g{color:#EEEEEE;-webkit-text-fill-color:#EEEEEE;background:none}
.hero{position:relative;margin-top:%(herom)spx;width:%(hero)spx;flex:1 1 auto;
      min-height:0;display:flex;align-items:center;justify-content:center}
/* The generated art is gold on its own near-black field, which shows as a
   visible square against the card. Screen blending drops the black entirely
   and leaves only the glow, so the artwork sits on the card rather than in a
   box -- and it means the hero never needs a transparent PNG. */
/* prep_hero.py has already turned the art's black field into transparency,
   so no blend mode and no mask are needed -- both of those left a visible
   square or a dark halo. The glow is a real drop-shadow on a real cutout. */
.hero img{width:100%%;height:100%%;object-fit:contain;
  filter:drop-shadow(0 0 60px rgba(201,162,78,.38))}
.play{position:absolute;width:%(play)spx;height:%(play)spx;border-radius:50%%;
  background:%(gold)s;display:flex;align-items:center;justify-content:center;
  box-shadow:0 10px 40px rgba(0,0,0,.45)}
.play i{display:block;width:0;height:0;margin-left:%(tri)spx;
  border-left:%(tri)spx solid %(dark)s;border-top:%(trih)spx solid transparent;
  border-bottom:%(trih)spx solid transparent}
.rows{margin-top:%(rowsm)s;width:100%%;display:flex;flex-direction:column;gap:%(rowg)spx}
.r{display:flex;align-items:center;gap:%(icg)spx;text-align:left}
.ic{flex:none;width:%(ic)spx;height:%(ic)spx;border-radius:50%%;border:2px solid rgba(201,162,78,.55);
    display:flex;align-items:center;justify-content:center;color:%(gold)s;
    background:rgba(201,162,78,.08)}
.ic svg{width:%(ics)spx;height:%(ics)spx;fill:none;stroke:currentColor;stroke-width:1.7;
        stroke-linecap:round;stroke-linejoin:round}
.bar{flex:none;width:2px;align-self:stretch;background:rgba(201,162,78,.45)}
.r p{font-size:%(rowf)spx;font-weight:600;line-height:1.25;text-transform:uppercase;
     letter-spacing:.02em;color:#E8E4DA}

/* 16:9 only. A thumbnail is seen at about 360px wide in a YouTube grid, so it
   gets fewer elements and bigger type, ranged left with the art beside it
   rather than stacked under it. Two columns, not a grid: the stacked layout
   overflowed its row when the headline ran to three lines. */
.c.yt{flex-direction:row;align-items:center;text-align:left;gap:34px}
.c.yt .main{flex:1;display:flex;flex-direction:column;align-items:flex-start;min-width:0}
.c.yt .rule{margin-left:0}
.c.yt h1{margin-top:22px}
.c.yt .hero{flex:none;width:420px;height:420px;margin-top:0}
.c.yt h1{color:#EEEEEE}
"""

TPL = ("<!doctype html><meta charset=utf-8>"
       "%(fontlink)s"
       "<style>%(css)s</style><div class='c %(kind)s'>"
       "<div class=main><div class=lock>OPTIMUM</div>"
       "<div class=sub>HEALTH | LIFE | RETIREMENT</div>"
       "<div class=rule></div><h1>%(title)s</h1></div>%(hero)s%(rows)s</div>")

# 9:16 portal cover and 16:9 YouTube thumbnail differ by more than scale, so
# each carries its own numbers rather than one set multiplied by a factor.
COVER = dict(w=1080, h=1920, pad="86px 76px 84px", lock=46, subf=19, subm=16, rule=360,
             rulem=26, h1=102, h1m=40, hero=928, herom=6, play=148, tri=26, trih=30,
             rowsm='22px', rowg=30, ic=74, ics=36, icg=26, rowf=25, gold=GOLD, dark=DARK)
YT = dict(w=1280, h=720, pad="44px 70px 46px", lock=30, subf=14, subm=11, rule=250,
          rulem=18, h1=86, h1m=0, hero=430, herom=0, play=0, tri=0, trih=0,
          rowsm='0', rowg=0, ic=0, ics=0, icg=0, rowf=0, gold=GOLD, dark=DARK)


def headline(code, kind):
    """Caps headline, with the final line in gold like the set Jesse showed."""
    lines = COPY[code]["title"]
    if kind == "yt" and len(lines) > 3:        # a thumbnail is seen small
        lines = lines[:3]
    out = []
    for i, line in enumerate(lines):
        text = html.escape(line)
        out.append(f"<span class=g>{text}</span>" if i == len(lines) - 1 else text)
    return "<br>".join(out)


def rows_html(code):
    out = []
    for icon, lines in COPY[code]["rows"]:
        glyph = ICONS.get(icon, ICONS["star"])
        out.append(
            f"<div class=r><span class=ic><svg viewBox='0 0 24 24'>{glyph}</svg></span>"
            f"<span class=bar></span><p>{'<br>'.join(html.escape(x) for x in lines)}</p></div>")
    return "<div class=rows>" + "".join(out) + "</div>"


def render(code, kind):
    item, spec = ITEMS[code], (YT if kind == "yt" else COVER)
    key = item["file"].rsplit(".", 1)[0]
    outdir = os.path.join(HERE, "youtube" if kind == "yt" else "covers")
    os.makedirs(outdir, exist_ok=True)
    src, png = os.path.join(outdir, key + ".html"), os.path.join(outdir, key + ".png")

    heroimg = os.path.join(HERE, "hero", code + ".png")
    hero = ""
    if os.path.exists(heroimg):
        play = "" if kind == "yt" else "<div class=play><i></i></div>"
        hero = f"<div class=hero><img src='../hero/{code}.png' alt=''>{play}</div>"

    open(src, "w").write(TPL % {
        "fontlink": FONT_LINK, "css": CSS % spec, "title": headline(code, kind),
        "kind": "yt" if kind == "yt" else "",
        "hero": hero, "rows": "" if kind == "yt" else rows_html(code)})

    if os.path.exists(png):
        os.remove(png)
    # Chrome writes the PNG then never exits on this Mac, so wait for the file,
    # give it a beat to finish writing, and kill it. Same as make_posts.py.
    proc = subprocess.Popen(
        [CHROME, "--headless", "--no-first-run", "--no-default-browser-check", "--disable-gpu",
         "--hide-scrollbars", "--force-device-scale-factor=1",
         f"--window-size={spec['w']},{spec['h']}",
         f"--user-data-dir={os.path.join(HERE, '.chrome')}", f"--screenshot={png}",
         "file://" + src], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(60):
        if os.path.exists(png) and os.path.getsize(png) > 0:
            time.sleep(1)
            break
        time.sleep(0.5)
    proc.kill()
    if not os.path.exists(png):
        sys.exit("could not render " + key)
    print("made", os.path.relpath(png, HERE))


# The covers on the live site were rendered WITHOUT these fonts: the original link
# (../social-cards/fonts/local.css, written next to covers/) never resolved, so Chrome
# fell back to its default bold sans. Reproducing the shipped look is the default;
# --fonts loads the intended Anton/Inter and changes how every cover looks.
FONT_LINK = "<link href=../vendor/fonts/local.css rel=stylesheet>" if "--fonts" in sys.argv[1:] else ""
args = [a for a in sys.argv[1:] if a not in ("--yt", "--fonts")]
kind = "yt" if "--yt" in sys.argv[1:] else "cover"
for code in (args or [c for c in COPY]):
    render(code, kind)
