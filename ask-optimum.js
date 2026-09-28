/* =====================================================================
   Ask Optimum inside the Agent Portal
   ---------------------------------------------------------------------
   - Floating "Ask Optimum" button, bottom right, on every portal screen
     once an agent is signed in (licensed app AND the pre-licensing page).
   - Licensed dashboard: an ask bar under the welcome line.
   - Pre-licensing page: a "Questions while you get licensed?" card under
     the Get Licensed hero.
   - All of them open one side panel that loads brain.html?embed=1.
   The chat page asks window.m5AskContext() who is asking and where they
   are, so answers fit licensed vs not-licensed-yet and "what's next".
   ===================================================================== */
(function () {
  'use strict';
  if (window.__askOptimum) return;
  window.__askOptimum = true;

  var PAGE = 'brain.html?embed=1';
  var CHIPS = {
    licensed: ['What should I do next?', 'What leads should I start with?', 'Help me with an objection'],
    unlicensed: ['What should I do next?', 'How do I schedule my exam?', 'Can I join the team calls?']
  };

  /* ---------- styles ---------- */
  var css = [
    '.ao-fab{position:fixed;right:22px;bottom:22px;z-index:9990;display:flex;align-items:center;gap:9px;height:52px;padding:0 20px 0 15px;',
    '  background:#0e2244;color:#fff;border:2px solid #e0a83d;border-radius:999px;font:700 15px/1 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;',
    '  cursor:pointer;box-shadow:0 10px 26px rgba(12,28,60,.28);transition:transform .12s}',
    '.ao-fab:hover{transform:translateY(-2px)} .ao-fab:focus-visible{outline:3px solid #e0a83d;outline-offset:3px}',
    '.ao-fab svg{flex:0 0 auto}',
    'body.ao-open .ao-fab{display:none}',
    '.ao-panel{position:fixed;top:0;right:0;bottom:0;width:430px;max-width:100vw;z-index:9995;background:#f4f7fc;',
    '  border-left:1px solid #e6eaf1;box-shadow:-12px 0 36px rgba(12,28,60,.18);transform:translateX(104%);transition:transform .22s ease;display:flex}',
    'body.ao-open .ao-panel{transform:none}',
    '.ao-panel iframe{border:0;width:100%;height:100%;display:block;background:#f4f7fc}',
    '.ao-scrim{display:none}',
    '@media (max-width:700px){.ao-panel{width:100vw;border-left:0} .ao-fab{right:14px;bottom:14px;height:50px;padding:0 17px 0 13px}',
    '  body.ao-open{overflow:hidden}}',
    '@media (min-width:701px){body.ao-open .ao-scrim{display:block;position:fixed;inset:0;z-index:9994;background:rgba(12,28,60,.18)}}',
    '@media (prefers-reduced-motion:reduce){.ao-panel,.ao-fab{transition:none}}',
    /* ask bar (dashboard + pre-licensing card) */
    '.ao-bar{display:flex;align-items:center;gap:12px;width:100%;max-width:760px;min-height:56px;padding:0 10px 0 18px;margin:4px 0 12px;',
    '  background:#fff;border:1px solid #d9e0ec;border-radius:14px;cursor:text;text-align:left;font:inherit;color:#5a6678;',
    '  box-shadow:0 1px 2px rgba(12,28,60,.06),0 8px 22px rgba(12,28,60,.05)}',
    '.ao-bar:hover{border-color:#e0a83d} .ao-bar:focus-visible{outline:3px solid #e0a83d;outline-offset:2px}',
    '.ao-bar .ao-bt{flex:1;font-size:15.5px;line-height:1.3;padding:14px 0}',
    '.ao-bar .ao-go{flex:0 0 auto;background:#0e2244;color:#fff;border-radius:10px;padding:9px 14px;font-weight:800;font-size:13.5px}',
    '.ao-chips{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 22px}',
    '.ao-chip{appearance:none;border:1px solid #d9e0ec;background:#fff;color:#0e2244;font:inherit;font-weight:600;font-size:13px;',
    '  padding:8px 12px;border-radius:999px;cursor:pointer}',
    '.ao-chip:hover{border-color:#e0a83d;background:#fffaf0} .ao-chip:focus-visible{outline:3px solid #e0a83d;outline-offset:2px}',
    '.ao-pre{background:#fff;border:1px solid #e6eaf1;border-radius:16px;padding:18px 18px 4px;margin:18px 0 22px;box-shadow:0 1px 2px rgba(12,28,60,.06)}',
    '.ao-pre h3{margin:0 0 4px;font-size:17px;color:#0e2244} .ao-pre p{margin:0 0 12px;color:#5a6678;font-size:14px;line-height:1.5}',
    '.ao-pre .ao-bar{margin-bottom:10px;box-shadow:none;background:#f7f9fc} .ao-pre .ao-chips{margin-bottom:14px}'
  ].join('\n');
  var st = document.createElement('style'); st.id = 'ao-style'; st.textContent = css;
  document.head.appendChild(st);

  var ICON = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#e0a83d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"></path><path d="M9 11h6"></path><path d="M9 14h4"></path></svg>';
  var SEARCH = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#b9821f" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M20 20l-3.5-3.5"></path></svg>';

  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function plain(h) { return String(h || '').replace(/<[^>]*>/g, ' ').replace(/&[a-z#0-9]+;/gi, ' ').replace(/\s+/g, ' ').trim(); }
  function data() { try { return (typeof store !== 'undefined' && store.data) || {}; } catch (e) { return {}; } }
  function real() { try { return (typeof store !== 'undefined' && store.__realData) || data(); } catch (e) { return data(); } }
  function isOn(id) { var el = document.getElementById(id); return !!(el && !el.classList.contains('hidden')); }
  function checked(id) { var c = data().checks || {}; return !!c[id]; }

  /* ---------- who's asking, and where they are (read by brain.html) ---------- */
  window.m5AskContext = function () {
    var d = data(), r = real();
    var status = d.status === 'licensed' || d.status === 'unlicensed' ? d.status : '';
    if (isOn('m5-prelic')) status = 'unlicensed';
    var lines = [];
    try {
      if (status === 'unlicensed' && typeof PRE_STEPS !== 'undefined') {
        var done = PRE_STEPS.filter(function (s) { return checked(s.id); });
        lines.push('Get Licensed page: ' + done.length + ' of ' + PRE_STEPS.length + ' steps checked off.');
        var next = PRE_STEPS.filter(function (s) { return !checked(s.id); })[0];
        lines.push(next ? 'Next licensing step: ' + plain(next.t) + '.' : 'All licensing steps checked off; next is starting the licensed-agent onboarding.');
        if (d.examDate) lines.push('Exam date they entered: ' + plain(d.examDate) + '.');
        if (d.stateAb) lines.push('State: ' + plain(d.stateAb) + '.');
      } else if (status === 'licensed') {
        if (typeof progress === 'function') { var p = progress(); lines.push('Fast Start: ' + p.done + ' of ' + p.total + ' steps done (' + p.pct + '%).'); }
        if (typeof acadCourseProgress === 'function') { var a = acadCourseProgress(); if (a && a.total) lines.push('Academy: ' + a.pct + '% done.'); }
        if (typeof FAST !== 'undefined') {
          var todo = [];
          FAST.forEach(function (m) { (m.items || []).forEach(function (i) { if (!i.info && !checked(i.id) && todo.length < 3) todo.push(plain(m.t) + ' → ' + plain(i.l)); }); });
          if (todo.length) lines.push('Next unchecked Fast Start steps: ' + todo.join('; ') + '.');
          else lines.push('Fast Start is complete.');
        }
      }
    } catch (e) {}
    var lang = ''; try { lang = typeof M5_LANG !== 'undefined' ? M5_LANG : ''; } catch (e) {}
    return {
      status: status,
      email: String(r.email || d.email || '').trim().toLowerCase(),
      name: [d.first, d.last].filter(Boolean).join(' ') || r.first || '',
      phone: String(r.phone || d.phone || ''),
      lang: lang === 'es' ? 'es' : 'en',
      progress: lines.join('\n')
    };
  };

  /* ---------- the panel ---------- */
  var fab, panel, scrim, frame, lastFocus = null;
  function build() {
    fab = document.createElement('button');
    fab.type = 'button'; fab.className = 'ao-fab'; fab.setAttribute('aria-label', 'Ask Optimum');
    fab.innerHTML = ICON + '<span>Ask Optimum</span>';
    fab.onclick = function () { open(''); };
    scrim = document.createElement('div'); scrim.className = 'ao-scrim'; scrim.onclick = close;
    panel = document.createElement('div');
    panel.className = 'ao-panel'; panel.setAttribute('role', 'dialog'); panel.setAttribute('aria-label', 'Ask Optimum');
    panel.setAttribute('aria-hidden', 'true');
    document.body.appendChild(fab); document.body.appendChild(scrim); document.body.appendChild(panel);
    sync();
  }
  function open(q) {
    lastFocus = document.activeElement;
    if (!frame) {
      frame = document.createElement('iframe');
      frame.title = 'Ask Optimum';
      frame.src = PAGE + (q ? '&q=' + encodeURIComponent(q) : '');
      panel.appendChild(frame);
    } else {
      try { frame.contentWindow.postMessage({ type: 'ao-ask', q: q || '' }, location.origin); } catch (e) {}
    }
    document.body.classList.add('ao-open');
    panel.setAttribute('aria-hidden', 'false');
    setTimeout(function () { try { frame.focus(); } catch (e) {} }, 60);
  }
  function close() {
    document.body.classList.remove('ao-open');
    if (panel) panel.setAttribute('aria-hidden', 'true');
    if (lastFocus && lastFocus.focus) { try { lastFocus.focus(); } catch (e) {} }
  }
  window.m5AskOptimum = open;
  window.addEventListener('message', function (e) {
    if (e.origin === location.origin && e.data && e.data.type === 'ao-close') close();
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && document.body.classList.contains('ao-open')) close(); });

  /* Only for signed-in agents: the licensed app or the pre-licensing page. */
  function sync() {
    if (!fab) return;
    var on = isOn('app') || isOn('m5-prelic');
    fab.style.display = on ? '' : 'none';
    if (!on) close();
    placePre();
  }

  /* ---------- ask bars ---------- */
  function barHtml(placeholder, chips) {
    return '<button type="button" class="ao-bar" data-ao="">' + SEARCH + '<span class="ao-bt">' + esc(placeholder) + '</span><span class="ao-go">Ask</span></button>' +
      '<div class="ao-chips">' + chips.map(function (c) { return '<button type="button" class="ao-chip" data-ao="' + esc(c) + '">' + esc(c) + '</button>'; }).join('') + '</div>';
  }
  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('[data-ao]');
    if (t) { e.preventDefault(); open(t.getAttribute('data-ao')); }
  });

  function placeDash() {
    var c = document.getElementById('content');
    if (!c || c.querySelector('.ao-bar') || data().status !== 'licensed') return;
    var sub = c.querySelector('p.sub') || c.querySelector('h1.page');
    if (!sub) return;
    var w = document.createElement('div'); w.className = 'ao-dash';
    w.innerHTML = barHtml('Ask Optimum anything: scripts, leads, contracting, mindset…', CHIPS.licensed);
    sub.parentNode.insertBefore(w, sub.nextSibling);
  }
  function placePre() {
    var hero = document.getElementById('m5-prehero');
    if (!hero || document.getElementById('ao-pre')) return;
    var w = document.createElement('div'); w.id = 'ao-pre'; w.className = 'ao-pre';
    w.innerHTML = '<h3>Questions while you get licensed?</h3>' +
      '<p>Ask Optimum about your state’s steps, the course, the exam, or joining the team calls while you study.</p>' +
      barHtml('Ask about getting licensed…', CHIPS.unlicensed);
    hero.parentNode.insertBefore(w, hero.nextSibling);
  }

  /* Re-add the dashboard bar after every render of the dashboard. */
  if (typeof render === 'function') {
    var _render = render;
    window.render = function (v) {
      _render.apply(this, arguments);
      if (v === 'dashboard') { try { placeDash(); } catch (e) {} }
    };
  }

  function boot() {
    build();
    try { if (typeof currentView === 'function' && currentView() === 'dashboard') placeDash(); } catch (e) {}
    ['app', 'm5-prelic', 'login'].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) new MutationObserver(sync).observe(el, { attributes: true, attributeFilter: ['class'] });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
