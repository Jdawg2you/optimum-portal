# Portal cheat sheets — standard Optimum header, banner, pop-ups, share card and print rules

Paste this into the **portal thread** (repo `Jdawg2you/optimum-portal`). It is self-contained: the
code below was copied out of the page that is live right now at **https://tools.ffloptimum.com/**
(15 Sep 2026), so the cheat sheets will match it exactly.

## Which pages

- `opening-objections.html`
- `closing-objections.html`
- `policy-benefits.html`
- `state-requirements.html` ← has **no** brand row at all today; it needs the whole header

None of the four currently has any of these pieces (checked 15 Sep 2026: no orbit mark, no GOAT
button, no `goatleads` link, no banner, no recruiting modal).

## Why

These four pages are linked from the free-tools landing page at `tools.ffloptimum.com`, and they're
reached by agents from outside Optimum. Every free tool now carries the same top bar. It has two
jobs: the **GOAT sign-up** (Optimum earns a commission on each one) and the opt-in **"Not a Family
First Life agent?"** recruiting pop-up. Without them, these pages are the one place in the suite
where neither offer appears.

---

## What each page gets — top to bottom

1. **Navy header bar**: gold orbit mark, the page's own title, *"Tools built for agents, by agents ·
   Brought to you by Optimum"* (Optimum links to `https://www.ffloptimum.com/`), and the gold
   **★ FREE Agent Website, Digital Business Card & Booking Calendar** button on the right.
2. **Cream strip** directly under it: *"Free for every agent, period.  Not a Family First Life agent?"*
3. **Two pop-ups**, hidden until clicked: the GOAT pop-up (opened by the gold button) and the
   recruiting pop-up (opened by the strip's link).
4. **A share card at the bottom** — *"Know an agent who'd use these?"* with a **Share with an agent**
   button. It shares the **whole free-tools suite** (`https://tools.ffloptimum.com/`), not the cheat
   sheet, using exactly the same message as the tools site.
5. **Clean printing.** These are printable resources. When printed, the header, the cream strip and the
   share card must **not** appear — the printout is just the cheat sheet.

Use each page's **own title** in the header (e.g. "Opening Objections"), in place of "Free Tools for Agents".

**No tab row, and no "More free tools" menu** — this is the same single-page version the tools
landing page uses. If you *want* the menu on these pages, it's a separate follow-up; the wizard and
navigator repos show how it's wired.

---

## Step 1 — the logo

The orbit mark is an inline base64 PNG (~21 KB). Don't retype it: open the live page's source at
`https://tools.ffloptimum.com/`, find `<img class="bmark"`, and copy that whole tag.

## Step 2 — fonts (in `<head>`, if the page doesn't already load them)

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap" rel="stylesheet">
```

## Step 3 — CSS (inside the page's `<style>`)

These rules reference CSS variables. Make sure the page's `:root` defines `--navy:#16203C`,
`--gold:#C9A24E`, `--golddk:#A8853A`, `--cream:#F5F1E8`, `--rule:#E3DFD4`, `--slate:#4A4A44`,
`--serif:'Source Serif 4',Georgia,serif` and `--sans:'Inter',-apple-system,'Segoe UI',Roboto,sans-serif`,
plus any other `var(--…)` used below. Add whichever are missing. **Don't change values the page
already defines.**

```css
  :root{--blue:#2C4A7C;--golddk:#A8853A;--muted:#8B8A82;--rule:#E3DFD4;--rule-soft:#EDE9DF;--sans:'Inter',-apple-system,'Segoe UI',Roboto,sans-serif;--serif:'Source Serif 4',Georgia,serif;--slate:#4A4A44}
  header{background:var(--navy);color:#fff;flex:0 0 auto;padding:12px 20px 0;position:relative;z-index:2}
  .brandrow{display:flex;align-items:center;gap:14px;margin-bottom:12px}
  .bmark{flex:0 0 auto;width:40px;height:40px;display:block}
  .bwrap{flex:0 0 auto;line-height:1.1}
  .bt{font-family:var(--serif);font-weight:700;font-size:20px;color:#fff;letter-spacing:-.01em;white-space:nowrap}
  .bs{font-size:12px;font-weight:500;color:rgba(255,255,255,.62);margin-top:3px}
  .bs .sep{color:rgba(255,255,255,.35);margin:0 4px}
  .bs a{color:var(--gold);font-family:var(--serif);font-weight:700;font-size:13.5px;text-decoration:none}
  .bs a:hover{color:#fff}
  .goat{margin-left:auto;appearance:none;cursor:pointer;background:var(--gold);color:var(--navy);
        border:1px solid var(--gold);font-family:inherit;font-size:12.5px;font-weight:700;
        padding:8px 16px;border-radius:999px;display:inline-flex;align-items:center;gap:7px;
        transition:background .12s,color .12s,border-color .12s}
  .goat:hover{background:var(--blue);border-color:var(--blue);color:#fff}
  .gstar{font-size:11px;line-height:1}
  .gshort{display:none}
  .modal[hidden]{display:none}
  .modal{position:fixed;inset:0;z-index:50;display:flex;align-items:center;justify-content:center;padding:20px}
  .backdrop{position:absolute;inset:0;background:rgba(22,32,60,.55)}
  .sheet{position:relative;background:var(--card);border-radius:14px;max-width:520px;width:100%;
         max-height:88vh;overflow-y:auto;padding:28px 28px 24px;box-shadow:0 24px 60px rgba(22,32,60,.35);color:var(--ink)}
  .sheet .x{position:absolute;top:14px;right:14px;appearance:none;border:0;background:transparent;
            font-size:16px;color:var(--muted);cursor:pointer;padding:6px;line-height:1}
  .sheet .x:hover{color:var(--navy)}
  .sheet h2{font-family:var(--serif);font-size:24px;font-weight:700;line-height:1.2;letter-spacing:-.015em;margin:0 0 6px;color:var(--navy);padding-right:24px}
  .kick{font-size:13px;color:var(--golddk);font-weight:500;margin:0 0 8px}
  .gitem{border-top:1px solid var(--rule-soft);padding:14px 0 2px;margin-top:8px}
  .gitem h3{font-family:var(--serif);font-size:16px;font-weight:700;margin:0 0 4px;color:var(--navy)}
  .gitem p{margin:0;font-size:13.5px;line-height:1.6;color:var(--slate)}
  .gclose{font-size:13px;line-height:1.6;color:var(--slate);margin:18px 0 16px}
  .gcta{display:block;text-align:center;text-decoration:none;background:var(--navy);color:#fff;
        font-size:15px;font-weight:600;padding:14px;border-radius:8px}
  .gcta:hover{background:var(--blue)}
@media(max-width:860px){
  .glong{display:none}
  .gshort{display:inline}
  }
@media(max-width:640px){
  header{padding:10px 14px 0}
  .brandrow{flex-wrap:wrap}
  .bt{font-size:17px}
  .bs{font-size:11px}
  .bmark{width:32px;height:32px}
  .goat{margin:6px 0 2px;flex:1 1 auto;justify-content:center}
  .brandrow>.goat{flex:1 0 100%}
  .bwrap{flex:1 1 0;min-width:0}
  .sheet{padding:22px 20px 20px}
  .sheet h2{font-size:21px}
  }
  .recopen{appearance:none;cursor:pointer;font-family:'Inter',-apple-system,'Segoe UI',Roboto,sans-serif}
  .recstrip{background:#EFEADD;border-bottom:1px solid #E3DFD4;padding:9px 20px;text-align:center;
    font-size:13px;color:#4A4A44;font-family:'Inter',-apple-system,'Segoe UI',Roboto,sans-serif}
  .recstrip .recopen{background:transparent;border:0;color:#A8853A;font-size:13px;font-weight:800;
    text-decoration:underline;padding:0 0 0 5px}
@media(max-width:640px){
  .recstrip{font-size:12px;padding:8px 14px;line-height:1.5}
  .recstrip .recopen{font-size:12px}
  }
  #recModal .sheet{max-width:580px}
  #recModal .recnote{background:#F5F1E8;border-left:3px solid #C9A24E;border-radius:0 10px 10px 0;
    padding:11px 15px;margin:14px 0 16px;font-size:13px;line-height:1.55;color:#4A4A44}
  #recModal .recnote b{color:#16203C}
  #recModal .recask{font-size:14.5px;line-height:1.6;color:#4A4A44;margin:0 0 4px}
  #recModal .recask b{color:#16203C}
  #recModal .recturn{font-size:13px;font-weight:700;color:#4A4A44;margin:16px 0 10px}
  #recModal .gcta{margin-top:20px}
  #recModal .rec2{margin:12px 0 0;text-align:center;font-size:13.5px}
  #recModal .rec2 a{color:#A8853A;font-weight:700;text-decoration:none}
  #recModal .rec2 a:hover{text-decoration:underline}
  .share{margin:26px 0 0;background:var(--card);border:1px solid var(--rule);border-radius:14px;padding:20px 22px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
  .share-t{flex:1 1 260px;font-family:var(--sans);font-size:14px;color:#55503f;line-height:1.55}
  .share-t b{display:block;font-family:var(--serif);font-size:18px;color:var(--navy);margin-bottom:2px}
  .share-btn{appearance:none;cursor:pointer;display:inline-flex;align-items:center;gap:9px;background:var(--navy);color:#fff;border:0;border-radius:10px;padding:12px 20px;font:700 14px var(--sans)}
  .share-btn:hover{background:#22305a}
  .share-btn svg{width:17px;height:17px;flex:none}
  .share-ok{flex-basis:100%;font-family:var(--sans);font-size:13px;font-weight:600;color:#3F7A56}
@media(max-width:720px){
  .share{padding:18px}
  .share-btn{width:100%;justify-content:center}
  }

  /* landing only: no tab row under the brand row, so the header must hold its own bottom
     spacing — otherwise the brand row's margin collapses out of the navy band */
  header{padding-bottom:12px}
  header .brandrow{margin-bottom:0}
  @media(max-width:640px){ header{padding-bottom:10px} }
```

The last block matters. Without a tab row under the header, the logo sits flush on the bottom edge of
the navy bar. Those three lines give it 12px above and below.

## Step 4 — markup (first thing inside `<body>`)

After pasting, add a `data-noprint` attribute to the two top-level elements — `<header data-noprint>`
and `<div class="recstrip" data-noprint>`. Step 8 hides everything carrying it when printing.

```html
<header>
  <div class="brandrow">
    <img class="bmark" src="data:image/png;base64,…(see step 1 — copy from the live page)…" alt="" width="40" height="40">
    <div class="bwrap">
      <div class="bt">Free Tools for Agents</div>
      <div class="bs">Tools built for agents, by agents <span class="sep">&middot;</span> Brought to you by <a href="https://www.ffloptimum.com/" target="_blank" rel="noopener">Optimum</a></div>
    </div>
    <button type="button" class="goat" id="goatBtn" aria-haspopup="dialog">
        <span class="gstar">&#9733;</span>
        <span class="glong">FREE Agent Website, Digital Business Card &amp; Booking Calendar</span>
        <span class="gshort">FREE Website, Card &amp; Calendar</span>
      </button>
  </div>
</header>
<div class="recstrip">Free for every agent, period.<button type="button" class="recopen" aria-haspopup="dialog">Not a Family First Life agent?</button></div>
```

## Step 5 — the two pop-ups (just before `</body>`)

```html
<div class="modal" id="goatModal" hidden>
  <div class="backdrop" data-close></div>
  <div class="sheet" role="dialog" aria-modal="true" aria-labelledby="goatTitle">
    <button type="button" class="x" id="goatClose" aria-label="Close">&#10005;</button>
        <h2 id="goatTitle">Three things every agent should have on day one</h2>
    <p class="kick">Free when you sign up with GOAT through Optimum</p>

    <div class="gitem">
      <h3>A verified agent website</h3>
      <p>Your own page with your photo, bio, carriers and state licenses pulled from NIPR &mdash; so a
      client can check you out before they buy.</p>
    </div>
    <div class="gitem">
      <h3>A digital business card</h3>
      <p>One tap saves your name, direct line and NPN to the client's phone, links to your website,
      and shows you're a verified, licensed agent.</p>
    </div>
    <div class="gitem">
      <h3>A booking calendar</h3>
      <p>A booking link clients use to grab a time with you &mdash; no back-and-forth texting.</p>
    </div>

    <p class="gclose">All three are free when you sign up with GOAT through Optimum. Set-up takes
    about fifteen minutes.</p>
    <a class="gcta" id="goatCta"
       href="https://goatleads.com/registration/new?affiliate_id=66c4aa379e0123651ad2f0e6"
       target="_blank" rel="noopener">Sign up free with GOAT</a>
  </div>
</div>

<div class="modal" id="recModal" hidden>
  <div class="backdrop" data-close></div>
  <div class="sheet" role="dialog" aria-modal="true" aria-labelledby="recTitle">
    <button type="button" class="x" id="recClose" aria-label="Close">&#10005;</button>
    <h2 id="recTitle">Not with Family First Life? You can still use these tools.</h2>

    <p class="recask">They're free, and they stay free. But while you're running your numbers, it's
    worth asking what you're actually being paid for that production &mdash; <b>a lower contract can
    cost you six figures over a few years without ever showing up on a single statement.</b>
    If they're not paying you what you're worth, that's worth a hard look.</p>

    <div class="recnote"><b>Already with FFL?</b> You're in the best position there is &mdash;
    congratulations.</div>

    <p class="recturn">If you're outside Family First Life, here's the honest take:</p>

    <div class="gitem"><h3>100% independent, never captive</h3>
      <p>Forty-plus carriers. You write what's best for your client &mdash; not whatever a captive
      shelf allows.</p></div>
    <div class="gitem"><h3>Real leads, priced honestly</h3>
      <p>High-intent leads from vetted independent partners. Not one overpriced in-house lead type
      you're required to buy, and not &ldquo;free&rdquo; cold leads you quietly pay for in low comp.</p></div>
    <div class="gitem"><h3>A plug-and-play system from day one</h3>
      <p>You're handed something that already works. FFL writes over $110 million a month &mdash; more
      than some brokerages do in a year &mdash; as the fastest-growing brokerage in the country.
      The system is figured out. You just run it.</p></div>
    <div class="gitem"><h3>Vested from day one</h3>
      <p>Your business is yours &mdash; including all renewals.</p></div>
    <div class="gitem"><h3>The highest compensation in the business</h3>
      <p>Up to 145% on your own production, plus producer bonuses, manager bonuses, carrier
      bonuses and company trips.</p></div>

    <a class="gcta" href="https://www.ffloptimum.com/#apply" target="_blank" rel="noopener">Start the conversation &rarr;</a>
    <p class="rec2"><a href="https://www.ffloptimum.com/#why" target="_blank" rel="noopener">Or read more about the agency first &rarr;</a></p>
  </div>
</div>
```

## Step 6 — scripts (after the pop-ups)

```html
<script>
(function(){var rm=document.getElementById('recModal');if(!rm)return;
 function op(){rm.hidden=false;document.getElementById('recClose').focus();}
 function sh(){rm.hidden=true;}
 document.getElementById('recClose').addEventListener('click',sh);
 rm.querySelector('.backdrop').addEventListener('click',sh);
 document.addEventListener('keydown',function(e){if(e.key==='Escape')sh();});
 document.querySelectorAll('.recopen').forEach(function(b){b.addEventListener('click',op);});})();
</script>
<script>
/* GOAT call-out */
var gm = document.getElementById('goatModal');
function goatOpen(){ gm.hidden = false; document.getElementById('goatClose').focus(); }
function goatShut(){ gm.hidden = true; document.getElementById('goatBtn').focus(); }
document.getElementById('goatBtn').addEventListener('click', goatOpen);
document.getElementById('goatClose').addEventListener('click', goatShut);
gm.addEventListener('click', function(e){ if(e.target.hasAttribute('data-close')) goatShut(); });
document.addEventListener('keydown', function(e){ if(e.key === 'Escape' && !gm.hidden) goatShut(); });
document.getElementById('goatCta').addEventListener('click', goatShut);
</script>
```

## Step 7 — the share card (at the end of the page content, just above any page footer)

CSS, inside `<style>` — it also uses `--card` (`#FFFFFF`) and `--rule`, so add those to `:root` if missing:

```css
  /* share with an agent — defined once here; build_shell.py lifts it into the landing page */
  .share{margin:26px 0 0;background:var(--card);border:1px solid var(--rule);border-radius:14px;padding:20px 22px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
  .share-t{flex:1 1 260px;font-family:var(--sans);font-size:14px;color:#55503f;line-height:1.55}
  .share-t b{display:block;font-family:var(--serif);font-size:18px;color:var(--navy);margin-bottom:2px}
  .share-btn{appearance:none;cursor:pointer;display:inline-flex;align-items:center;gap:9px;background:var(--navy);color:#fff;border:0;border-radius:10px;padding:12px 20px;font:700 14px var(--sans)}
  .share-btn:hover{background:#22305a}
  .share-btn svg{width:17px;height:17px;flex:none}
  .share-ok{flex-basis:100%;font-family:var(--sans);font-size:13px;font-weight:600;color:#3F7A56}
  @media(max-width:720px){.share{padding:18px}.share-btn{width:100%;justify-content:center}}
```

Markup — note the `data-noprint` attribute is already on it:

```html
<div class="share" data-noprint>
        <div class="share-t"><b>Know an agent who'd use these?</b>Send them the link &mdash; it takes about ten seconds.</div>
        <button type="button" class="share-btn" id="shareBtn">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12"/><path d="M7 8l5-5 5 5"/><path d="M5 13v6a2 2 0 002 2h10a2 2 0 002-2v-6"/></svg>
          Share with an agent
        </button>
        <span class="share-ok" id="shareOk" hidden>Link copied &mdash; paste it into a text to another agent.</span>
      </div>
```

Script, just before `</body>`:

```html
<script>
/* Share with an agent: opens the phone's share sheet with the message pre-written.
   Where the browser has no share sheet, it copies the message + link instead.
   The link goes INSIDE the text: many share targets (Copy, AirDrop, Notes, sometimes
   Messages) drop the text entirely when a separate url is passed alongside it. */
(function(){
  var btn=document.getElementById('shareBtn'), ok=document.getElementById('shareOk');
  if(!btn) return;
  var LINK='https://tools.ffloptimum.com/';
  var TEXT='Found some amazing free tools for insurance agents. An insurance product wizard, interactive call scripts, an income planner with activity planner, as well as tools to help build your agency. And the best part is there\'s no catch, it really is all free.';
  function done(){ ok.hidden=false; clearTimeout(done.t); done.t=setTimeout(function(){ ok.hidden=true; }, 5000); }
  function legacyCopy(){
    var t=document.createElement('textarea'); t.value=TEXT+' '+LINK; t.setAttribute('readonly','');
    t.style.cssText='position:fixed;top:0;left:0;opacity:0'; document.body.appendChild(t); t.select();
    try{ document.execCommand('copy'); }catch(e){} document.body.removeChild(t); done();
  }
  btn.addEventListener('click', function(){
    if(navigator.share){ navigator.share({text:TEXT+' '+LINK}).catch(function(){}); return; }
    if(navigator.clipboard && window.isSecureContext){ navigator.clipboard.writeText(TEXT+' '+LINK).then(done, legacyCopy); return; }
    legacyCopy();
  });
})();
</script>
```

The link is deliberately **inside** the message text rather than passed as a separate `url`: many
share targets (Copy, AirDrop, Notes, sometimes Messages) throw the text away when both are given,
and the recipient gets a bare link with no words. Don't "fix" that. To change the wording later,
change it on the tools site first (`shell-template.html` in `optimum-tools`) and copy it here, so
every page says the same thing.

## Step 8 — print rules (inside `<style>`)

```css
@media print{
  [data-noprint], .modal{ display:none !important; }
}
```

Only elements you tagged are hidden — **do not** write `header{display:none}` in print; if a cheat
sheet uses a `<header>` for its own title it would vanish from the printout. If a page already has an
`@media print` block, add this rule inside it rather than starting a second one.

---

## Watch for collisions — these are shared-sounding names

Before pasting, search each page for these classes and ids. If any already exist and mean something
else, rename the **page's** version rather than these:

`header` (element) · `.brandrow` `.bmark` `.bwrap` `.bt` `.bs` `.sep` · **`.goat`** `.gstar` `.glong`
`.gshort` · `.modal` `.backdrop` `.sheet` `.x` `.kick` `.gitem` `.gclose` `.gcta` · `.recstrip`
`.recopen` `.recnote` `.recask` `.recturn` `.rec2` · `#goatBtn` `#goatModal` `#goatClose` `#goatCta`
`#goatTitle` `#recModal` `#recClose` `#recTitle` · `.share` `.share-t` `.share-btn` `.share-ok` `#shareBtn` `#shareOk`

This bit us once already: on the tools landing page, a big GOAT *block* and the header's GOAT
*button* both used `.goat` and restyled each other.

## Don't change the copy

The recruiting pop-up's wording was written line by line by Jesse. That includes the "Already with
FFL? You're in the best position there is — congratulations." note, which is there so FFL agents
from other teams never feel recruited. Reproduce it exactly. The GOAT link must keep
`?affiliate_id=66c4aa379e0123651ad2f0e6`; a bare goatleads.com link earns nothing.

## Check it worked — on each of the four pages

1. The navy header shows the orbit mark, **that page's** title, and the gold GOAT button.
2. "Optimum" in the header goes to `https://www.ffloptimum.com/`.
3. The gold button opens the GOAT pop-up; its sign-up link carries the affiliate ID.
4. "Not a Family First Life agent?" opens the recruiting pop-up; X, clicking outside, and Escape all close it.
5. The pop-up buttons go to `https://www.ffloptimum.com/#apply` and `#why`.
6. The logo has equal navy space above and below.
7. At a 430px phone width, nothing scrolls sideways and the logo sits beside the title.
8. **"Share with an agent"** on a phone opens the share sheet with the full message ending in
   `https://tools.ffloptimum.com/`; on a computer it copies it and says "Link copied".
9. **Print preview** (Cmd/Ctrl-P): no navy header, no cream strip, no share card — only the cheat
   sheet, laid out exactly as it printed before this change.
10. At 430px the share button goes full width and nothing scrolls sideways.
