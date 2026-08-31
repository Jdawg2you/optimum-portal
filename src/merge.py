#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Optimum Agent Portal — build script.

Reconstructed 2026-08-18 from the deployed index.html
(github.com/jdawg2you/optimum-portal, commit d328691) after the original
build thread became unusable. Verified to reproduce that deployed file
byte-for-byte.

SOURCES
  uploaded_v2.html   BASE page. Login, nav shell, page views, RES_TILES,
                     vSales / salesPanel, BOOKS, embedded tool iframes.
                     Contains two injection tokens:
                       <!--__M5_CSS__-->   (in <head>)
                       <!--__M5_BODY__-->  (just before </body>)
  m5_assets.py       M5_CSS    -> injected at <!--__M5_CSS__-->
                     M5_SCRIPT -> first half of <!--__M5_BODY__-->.
                     Academy LMS engine, Fast Start, m5SysTools, m5RowList,
                     backend sync. Holds the __ACAD_LMS__ placeholder.
  acad_manifest.json Academy course source of truth (13 modules / 44 lessons).
                     Substituted into M5_SCRIPT at __ACAD_LMS__.
  reskin_assets.py   RESKIN_STYLE + RESKIN_JS -> rest of <!--__M5_BODY__-->.
                     Goal Card, Agency roster, Income Calculator, search bars,
                     vRecruiting, vSelfDev.

BUILD
  python3 merge.py            # -> optimum-portal-merged.html + index.html
  python3 merge.py --check    # build in memory and diff vs reference/index.html

AFTER BUILDING
  node --check each <script> block, screenshot, then deploy by uploading
  index.html to github.com/jdawg2you/optimum-portal/upload/main
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

BASE_FILE     = os.path.join(HERE, 'uploaded_v2.html')
MANIFEST_FILE = os.path.join(HERE, 'acad_manifest.json')
OUT_FILE      = os.path.join(HERE, 'optimum-portal-merged.html')
INDEX_FILE    = os.path.join(HERE, 'index.html')
REFERENCE     = os.path.join(HERE, 'reference', 'index.html')

TOKEN_CSS  = '<!--__M5_CSS__-->'
TOKEN_BODY = '<!--__M5_BODY__-->'
TOKEN_ACAD = '__ACAD_LMS__'

sys.path.insert(0, HERE)
from m5_assets import M5_CSS, M5_SCRIPT          # noqa: E402
from reskin_assets import RESKIN_STYLE, RESKIN_JS  # noqa: E402


def manifest_js():
    """acad_manifest.json -> the exact JS array literal the page expects.

    indent=1 / ensure_ascii=False matches the deployed formatting, and '</' is
    escaped to '<\\/' so lesson HTML can't terminate the <script> tag early.
    """
    with open(MANIFEST_FILE, encoding='utf-8') as f:
        manifest = json.load(f)
    return json.dumps(manifest, indent=1, ensure_ascii=False).replace('</', '<\\/')


def build():
    with open(BASE_FILE, encoding='utf-8') as f:
        html = f.read()

    for token in (TOKEN_CSS, TOKEN_BODY):
        if html.count(token) != 1:
            raise SystemExit('ERROR: %s appears %d times in %s (expected 1)'
                             % (token, html.count(token), os.path.basename(BASE_FILE)))
    if M5_SCRIPT.count(TOKEN_ACAD) != 1:
        raise SystemExit('ERROR: %s appears %d times in M5_SCRIPT (expected 1)'
                         % (TOKEN_ACAD, M5_SCRIPT.count(TOKEN_ACAD)))

    script = M5_SCRIPT.replace(TOKEN_ACAD, manifest_js())
    body = script + '\n\n' + RESKIN_STYLE + '\n\n' + RESKIN_JS

    html = html.replace(TOKEN_CSS, M5_CSS, 1)
    html = html.replace(TOKEN_BODY, body, 1)
    return html


def main():
    html = build()

    if '--check' in sys.argv:
        if not os.path.exists(REFERENCE):
            raise SystemExit('ERROR: no reference build at %s' % REFERENCE)
        with open(REFERENCE, encoding='utf-8') as f:
            ref = f.read()
        if html == ref:
            print('OK  build is byte-identical to reference/index.html (%d bytes)' % len(html))
            return 0
        print('DIFF  built %d bytes vs reference %d bytes' % (len(html), len(ref)))
        n = min(len(html), len(ref))
        i = 0
        while i < n and html[i] == ref[i]:
            i += 1
        print('first difference at byte %d (line %d)' % (i, html.count('\n', 0, i) + 1))
        print('built    : %r' % html[max(0, i - 80):i + 80])
        print('reference: %r' % ref[max(0, i - 80):i + 80])
        return 1

    for path in (OUT_FILE, INDEX_FILE):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print('wrote %s (%d bytes)' % (os.path.basename(path), len(html)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
