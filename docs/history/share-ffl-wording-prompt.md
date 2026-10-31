# Portal — update the two Share FFL messages: new wording + new video link

Paste this into the **portal thread** (repo `Jdawg2you/optimum-portal`).

## What changed and why

The public Share Family First Life page (`https://tools.ffloptimum.com/share/`, moved there 17 Sep
2026 from `jdawg2you.github.io/Share-FFL/shareffl.html`, which now redirects) was
rebranded on 15 Sep 2026, and Jesse approved cleaned-up wording for its two messages. The meaning and
voice are the same. The capitalisation is normal now ("family", "company", "new reps"), the "!!" and
"..." are gone, and "Pass this Info Along for me!" became "would you pass it along for me?".

**The video link changed too (16 Sep 2026).** Both messages now end with
`https://youtu.be/PFufqDZLhYU` (*Family First Life: Company Overview*) instead of `JoinUS.FFLALL.com`.
In a real browser, `JoinUS.FFLALL.com` redirects to a **different, older** video — *The Rogue IMO
Overview (2022)* from FFL National — which is not the one Jesse wants people to watch.

The portal's Share FFL sub-page (`vShareFFL` in `index.html`) sends the **same two messages**, and they
must stay identical to the public page, character for character.

## The edit

In `index.html`, in the list of share messages used by `vShareFFL`, replace the two `body` strings.

**`k:'new'` — "If you're new to the business"**

```
Hey! Hope all is well with your family. Quick heads-up — I just started with a new company and they're looking to bring on new reps. If you know anyone, they pay really well, part-time or full-time. Here's a short overview video — would you pass it along for me? https://youtu.be/PFufqDZLhYU
```

**`k:'vet'` — "If you've been with FFL for a while"**

```
Hey! Hope all is well with your family. You may have seen that I help people with insurance and retirement. Our company is looking to bring on new reps — if you know anyone, they pay really well, part-time or full-time. Here's a short overview video — would you pass it along for me? https://youtu.be/PFufqDZLhYU
```

Notes:

- The dashes are real em dashes (—), and the apostrophes are plain `'`. In a JS string delimited
  with `"`, the apostrophes need no escaping; with `'`, escape them.
- **`m5ShareLinkify`** currently turns `JoinUS.FFLALL.com` into a link. Change it to match
  `https://youtu.be/PFufqDZLhYU` instead, so the video link in each card is still clickable.
- **The video preview** under the cards (`m5-shvthumb`) links to `https://JoinUS.FFLALL.com`. Point it at
  `https://youtu.be/PFufqDZLhYU`. If its thumbnail image (`M5_OVERVIEW_THUMB`) is a still from the old
  2022 video, swap it for this video's thumbnail: `https://i.ytimg.com/vi/PFufqDZLhYU/hqdefault.jpg`.
- Any other on-page text saying the messages point to JoinUS.FFLALL.com should say they point to the
  Family First Life company overview video.
- **Leave everything else alone:** the card titles and descriptions, and the first-name sign-off from
  `m5ShareSignoff`. The sign-off is added after the body, so it keeps working unchanged.
- The old code comment says the messages are "the agency's own wording, character for character".
  Update it to say they match the public Share-FFL page, as approved by Jesse on 15 Sep 2026.

## Check it worked

1. On the portal's Share FFL page, each card shows the new text above.
2. **Copy** puts exactly that text on the clipboard, plus the agent's first-name sign-off when known.
3. The video link `https://youtu.be/PFufqDZLhYU` is a clickable link in both cards, and the video
   preview opens the same video. No `JoinUS.FFLALL.com` remains on the Share FFL page.
4. Compare with `https://tools.ffloptimum.com/share/`: the two messages match word
   for word.
