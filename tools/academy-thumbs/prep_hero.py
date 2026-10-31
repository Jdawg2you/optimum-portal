#!/usr/bin/env python3
"""Turn a generated hero into a transparent cutout.

The art comes back as gold line-work on its own near-black field. Dropped onto
a card that has its own glow, that field shows -- as a hard square, or, once
masked, as a dark halo. Both were visible on the first two attempts.

Luminance IS the artwork here: everything bright is line, everything dark is
background. So alpha = the brightest channel. No edge detection, no keying
tolerance to tune, and it works whatever background the generator chose.

Usage: prep_hero.py hero/A.1.png [...]
"""
import subprocess
import sys
from pathlib import Path

for arg in sys.argv[1:]:
    src = Path(arg)
    out = src.with_name(src.stem + "-cut.png")
    subprocess.run([
        "ffmpeg", "-v", "error", "-i", str(src),
        # Upscale first: the generator returns 200x200 and these sit ~760px wide.
        # lanczos on smooth glow art holds up far better than the browser's scaler.
        "-vf", ("scale=1024:1024:flags=lanczos,format=rgba,"
                "geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':"
                # A floor, because the generator's "black" is not black -- it
                # came back around 10-20, which survived as a faint visible
                # square across the whole frame. Anything under 28 goes to
                # zero and the rest is restretched, so the glow keeps its
                # falloff and the field disappears.
                "a='clip((max(max(r(X,Y),g(X,Y)),b(X,Y))-28)*1.123,0,255)'"),
        str(out), "-y"], check=True)

    # Trim the transparent border. The generator is asked for "generous margin"
    # and obliges, so the square that comes back is mostly empty -- and because
    # the card scales the art with object-fit:contain, that empty margin became
    # dead space ON the card: a gap half again as wide as any in the set Jesse
    # sent. Cropping to the ink (plus a little air) lets the art actually fill
    # the space the layout gives it.
    from PIL import Image
    art = Image.open(out).convert("RGBA")
    box = art.split()[3].getbbox()
    if box:
        pad = round(max(art.size) * 0.02)
        box = (max(0, box[0] - pad), max(0, box[1] - pad),
               min(art.width, box[2] + pad), min(art.height, box[3] + pad))
        art.crop(box).save(out)
    art.close()

    out.replace(src)
    print("cut", src.name)
