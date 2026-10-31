#!/bin/sh
# Ship portal.ffloptimum.com in one command:
#   build -> verify (+ ticksafe against what is live) -> commit -> push -> wait for
#   GitHub Pages -> fetch every file from the live site and compare sha256 -> require
#   origin/main == HEAD.
#
#   ./deploy.sh "What changed, in a sentence"     build, commit and ship
#   ./deploy.sh --dry-run                         everything up to the push, nothing shipped
#
# Edit source/index.template.html and content/*, never index.html. If index.html was
# edited directly, run `node tools/build.mjs --extract` first to adopt the edit.
# First run on a new machine: (cd tools && npm ci).
set -eu
cd "$(dirname "$0")"

DRY=0; MSG=""
for a in "$@"; do
  case "$a" in
    --dry-run) DRY=1 ;;
    *) MSG="$a" ;;
  esac
done
say() { printf '\n== %s\n' "$*"; }
die() { printf '\nDEPLOY STOPPED: %s\n' "$*" >&2; exit 1; }

[ -d tools/node_modules ] || die "test tools not installed: run (cd tools && npm ci)"
[ "$(git rev-parse --abbrev-ref HEAD)" = "main" ] || [ "$DRY" = 1 ] || die "not on main"

say "1/7 Fetch: never build on an old copy"
git fetch -q origin main
git merge-base --is-ancestor origin/main HEAD || die "origin/main has commits this checkout does not. Pull (or rebase) first; never force."

say "2/7 Build index.html from source/ + content/ (refuses a page that fails verify)"
node tools/build.mjs

say "3/7 Stage the page and what it serves"
PRE_INDEX=$(git write-tree)   # a dry run puts the index back exactly as it was, even when it stops early
trap '[ "$DRY" = 1 ] && git read-tree "$PRE_INDEX"' EXIT
git add -- index.html source content assets posters
OTHER=$(git status --porcelain --untracked-files=no | grep -v '^[MADR] ' || true)
[ -z "$OTHER" ] || die "uncommitted changes outside what deploy stages:
$OTHER"

say "4/7 Verify against git (referenced files must be committed) + ticksafe against origin/main"
node tools/verify.mjs --ticksafe origin/main

if git diff --cached --quiet; then
  say "5/7 Nothing new to commit; shipping HEAD as it is"
else
  [ -n "$MSG" ] || { [ "$DRY" = 1 ] && MSG="dry run"; } || die "give a commit message: ./deploy.sh \"what changed\""
  if [ "$DRY" = 1 ]; then
    say "5/7 Dry run: would commit"; git diff --cached --stat
  else
    say "5/7 Commit"; git commit -q -m "$MSG"
  fi
fi

if [ "$DRY" = 1 ]; then
  git log -1 --oneline
  say "Dry run complete: build, verify and ticksafe passed; nothing pushed"
  exit 0
fi

say "6/7 Push (fast-forward only)"
git push origin HEAD:main

say "7/7 Wait for GitHub Pages, then compare every live file with HEAD by sha256"
node tools/live-check.mjs https://portal.ffloptimum.com --wait 900 --require-origin-equal
say "Shipped $(git rev-parse --short HEAD) and verified live"
