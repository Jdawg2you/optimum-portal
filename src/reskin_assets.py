# -*- coding: utf-8 -*-
"""Visual reskin + app logic injected before </body> by merge.py.

RESKIN_STYLE = the M5 VISUAL RESKIN <style> block.
RESKIN_JS    = the reskin/app <script> block (Goal Card, roster, income calc,
               search bars, vRecruiting, vSelfDev, etc).
"""

RESKIN_STYLE = r"""<style>
/* ============================= M5 VISUAL RESKIN ============================= */
:root{--m5gold:#e8b73a;--m5navy:#0b1a34;}

/* ===== Agency Dashboard ===== */
.ag-wrap{max-width:1180px}
.ag-head{display:flex;justify-content:space-between;align-items:flex-start;gap:14px;flex-wrap:wrap;margin:0 0 14px}
.ag-headr{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.ag-refresh{display:inline-flex;align-items:center;gap:7px;border:1px solid #16233f;background:#16233f;color:#fff;border-radius:999px;padding:9px 17px;font-weight:800;font-size:13.5px;cursor:pointer;font-family:inherit;transition:opacity .15s}
.ag-refresh:hover{opacity:.9}
.ag-refresh:disabled{opacity:.65;cursor:default}
.ag-synced{color:#8a93a9;font-size:12.5px;font-weight:600}
.ag-spin{display:inline-block;width:13px;height:13px;border:2px solid rgba(255,255,255,.45);border-top-color:#fff;border-radius:50%;animation:agspin .6s linear infinite}
@keyframes agspin{to{transform:rotate(360deg)}}
.ag-load{background:#fff;border:1px solid #e5e9f2;border-radius:14px;padding:40px;text-align:center;color:#55617d;font-size:15px}
.ag-filters{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 16px}
.ag-fbtn{border:1px solid #d9e0ee;background:#fff;color:#16233f;border-radius:999px;padding:7px 15px;font-weight:700;font-size:13px;cursor:pointer}
.ag-fbtn.on{background:#16233f;color:#fff;border-color:#16233f}
.ag-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:0 0 18px}
.ag-stat{background:#fff;border:1px solid #e5e9f2;border-radius:14px;padding:15px 16px;box-shadow:0 4px 14px rgba(20,35,63,.04)}
.ag-stat .k{font-size:11px;font-weight:800;color:#8a93a9;text-transform:uppercase;letter-spacing:.05em}
.ag-stat .v{font-size:30px;font-weight:800;color:#16233f;line-height:1.1;margin-top:3px}
.ag-stat .s{font-size:12px;color:#55617d;margin-top:2px}
.ag-grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:18px}
.ag-grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-bottom:18px}
.ag-card{background:#fff;border:1px solid #e5e9f2;border-radius:16px;padding:18px 20px;box-shadow:0 6px 18px rgba(20,35,63,.05)}
.ag-card h3{margin:0 0 3px;font-size:15px;color:#16233f}
.ag-card .sub{margin:0 0 14px;font-size:12.5px;color:#8a93a9}
/* --- Agency Dashboard empty state: shown to anyone who hasn't recruited yet --- */
.agz{background:linear-gradient(150deg,var(--navy),var(--navy-2));color:#eaf0fb;border-radius:18px;padding:30px 24px 28px;text-align:center;box-shadow:0 10px 30px rgba(14,34,68,.22)}
.agz-kick{display:inline-block;font-size:11px;font-weight:800;letter-spacing:1.1px;text-transform:uppercase;color:var(--gold);background:rgba(224,168,61,.15);border:1px solid rgba(224,168,61,.35);border-radius:999px;padding:5px 13px;margin-bottom:16px}
.agz h2{margin:0 0 12px;font-size:26px;line-height:1.22;font-weight:800;letter-spacing:-.3px;color:#fff}
.agz p{margin:0 auto;font-size:15px;line-height:1.6;color:#c4d2ec;max-width:440px}
.agz-ctas{max-width:440px;margin:22px auto 0;text-align:left}
.agz-cta{display:block;text-decoration:none;border-radius:13px;padding:15px 18px;margin-top:14px;transition:.14s;border:1px solid transparent;cursor:pointer}
.agz-cta .t{display:block;font-weight:800;font-size:15.5px;line-height:1.25}
.agz-cta .d{display:block;font-size:13px;margin-top:3px;line-height:1.45;opacity:.9}
.agz-cta .a{float:right;font-size:19px;line-height:1;margin-top:2px;opacity:.85}
.agz-cta.gold{background:var(--gold);color:#2b1d02}
.agz-cta.gold .d{color:#5c4409}
.agz-cta.gold:hover{background:#eeb84a;transform:translateY(-1px)}
.agz-cta.ghost{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.22);color:#eaf0fb}
.agz-cta.ghost .d{color:#a9bcdd}
.agz-cta.ghost:hover{background:rgba(255,255,255,.13);transform:translateY(-1px)}
.agz-prev{margin-top:26px}
.agz-prevh{font-size:12px;font-weight:800;letter-spacing:.5px;text-transform:uppercase;color:#98a2b6;margin:0 0 10px;text-align:center}
.agz-ghost{position:relative;overflow:hidden;filter:grayscale(.35);opacity:.62}
.agz-ghost::after{content:"";position:absolute;left:0;right:0;top:0;bottom:0;background:linear-gradient(180deg,rgba(244,247,252,0) 30%,rgba(244,247,252,.92) 100%);pointer-events:none}
.agz-stats{display:flex;gap:10px;margin-bottom:14px}
.agz-stat{flex:1;background:#f7fafe;border:1px solid var(--line);border-radius:11px;padding:10px 8px;text-align:center}
.agz-stat b{display:block;font-size:19px;color:var(--navy);line-height:1.1}
.agz-stat span{font-size:10.5px;color:#8a93a9;font-weight:700;text-transform:uppercase;letter-spacing:.3px}
.agz-tbl{width:100%;border-collapse:collapse;font-size:12.5px}
.agz-tbl th{text-align:left;font-size:10.5px;text-transform:uppercase;letter-spacing:.4px;color:#8a93a9;padding:7px 6px;border-bottom:1px solid var(--line)}
.agz-tbl td{padding:9px 6px;border-bottom:1px solid #f1f4f9;color:#48536a}
.agz-tbl td.nm{font-weight:700;color:var(--ink)}
.agz-bar{height:6px;background:#eaeff7;border-radius:99px;overflow:hidden;min-width:54px}
.agz-bar i{display:block;height:100%;background:var(--brand);border-radius:99px}
.agz-bar i.g{background:#1faa5f}
.agz-pill{display:inline-block;font-size:10px;font-weight:800;border-radius:999px;padding:2px 8px}
.agz-pill.lic{background:rgba(31,170,95,.13);color:#12793f}
.agz-pill.pre{background:rgba(224,168,61,.16);color:var(--gold-deep)}
@media(max-width:640px){ .agz{padding:26px 18px 24px} .agz h2{font-size:23px} .agz p{font-size:14.5px} }
.ag-funnel-row{display:flex;align-items:center;gap:10px;margin:7px 0}
.ag-funnel-lab{width:118px;font-size:12.5px;color:#55617d;text-align:right;font-weight:600}
.ag-funnel-bar{flex:1;background:#eef2f8;border-radius:7px;height:26px;position:relative;overflow:hidden}
.ag-funnel-fill{position:absolute;left:0;top:0;bottom:0;border-radius:7px;display:flex;align-items:center;padding-left:10px;color:#fff;font-weight:800;font-size:12.5px}
.ag-funnel-pct{width:44px;text-align:right;font-weight:800;font-size:13px;color:#16233f}
.ag-mixbar{display:flex;height:34px;border-radius:9px;overflow:hidden;margin-bottom:8px}
.ag-mixseg{display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:12.5px;min-width:0}
.ag-legend{display:flex;gap:16px;font-size:12px;color:#55617d;margin-top:2px}
.ag-dot{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:5px;vertical-align:middle}
.ag-bars{display:flex;align-items:flex-end;gap:6px;height:120px;margin-top:12px}
.ag-bar{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%}
.ag-bar .bv{font-size:12px;font-weight:800;color:#16233f;margin-bottom:3px}
.ag-bar .bfill{width:100%;border-radius:6px 6px 0 0;min-height:3px}
.ag-bar .bl{font-size:10.5px;color:#8a93a9;margin-top:5px;text-align:center}
.ag-big{font-size:34px;font-weight:800;color:#16233f;line-height:1;margin-top:2px}
.ag-soon{background:repeating-linear-gradient(45deg,#f7f9fc,#f7f9fc 10px,#f2f5fb 10px,#f2f5fb 20px);border:1px dashed #cfd8ea;border-radius:14px;padding:20px;text-align:center;color:#8a93a9;font-size:12.5px;line-height:1.5}
.ag-soon .t{font-weight:800;color:#55617d;font-size:14px;margin-bottom:4px}
.ag-tablewrap{overflow-x:auto}
.ag-table{width:100%;border-collapse:collapse;font-size:13px}
.ag-table th{text-align:left;background:#16233f;color:#fff;padding:10px 10px;font-size:11.5px;font-weight:700;cursor:pointer;white-space:nowrap}
.ag-table th:hover{background:#1f2c4e}
.ag-table td{padding:9px 10px;border-bottom:1px solid #eef2f8;color:#16233f;white-space:nowrap}
.ag-table tr:hover td{background:#f9fbfe}
.ag-pill{display:inline-block;padding:3px 9px;border-radius:999px;font-size:11px;font-weight:800}
.ag-pill.lic{background:#e6f2ea;color:#1f7a44}
.ag-pill.unl{background:#fdeee7;color:#b5561f}
.ag-mini{display:inline-block;width:56px;height:7px;background:#eef2f8;border-radius:5px;overflow:hidden;vertical-align:middle;margin-right:6px}
.ag-mini > span{display:block;height:100%;border-radius:5px}
.ag-eng{display:flex;align-items:center;gap:11px;margin:11px 0}
.ag-engn{width:22px;height:22px;border-radius:50%;background:#eef2f8;color:#55617d;font-weight:800;font-size:12px;display:flex;align-items:center;justify-content:center;flex:0 0 auto}
.ag-eng:first-child .ag-engn{background:#c9a227;color:#fff}
.ag-engname{font-weight:700;font-size:13.5px;color:#16233f;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ag-engmeta{font-size:11.5px;color:#8a93a9;margin:1px 0 4px}
.ag-engbarwrap{background:#eef2f8;border-radius:5px;height:7px;overflow:hidden}
.ag-engbarwrap>span{display:block;height:100%;background:linear-gradient(90deg,#c9a227,#e8b73a);border-radius:5px}
.ag-engscore{font-weight:800;font-size:14px;color:#16233f;flex:0 0 auto}
.ag-poprow{display:flex;align-items:center;gap:12px;margin:9px 0}
.ag-poplab{width:150px;font-size:12.5px;color:#16233f;font-weight:600;text-align:right;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ag-popbar{flex:1;background:#eef2f8;border-radius:6px;height:16px;overflow:hidden}
.ag-popbar>span{display:block;height:100%;background:#2f6df0;border-radius:6px}
.ag-popval{width:44px;text-align:right;font-weight:800;font-size:13px;color:#16233f}
@media(max-width:900px){ .ag-grid2,.ag-grid3{grid-template-columns:1fr} .ag-poplab{width:110px} }
aside{background:linear-gradient(180deg,#0c1c3a 0%,#0a1730 100%)!important}

/* ---- Sidebar OPTIMUM wordmark header ---- */
.side-brand.m5-brandhdr{flex-direction:column;align-items:center;gap:0;padding:20px 14px 15px;border-bottom:1px solid rgba(255,255,255,.06)}
.m5-bh-name{color:#fff;font-weight:700;font-size:21px;letter-spacing:.28em;padding-left:.28em;line-height:1}
.m5-bh-sub{display:flex;align-items:center;gap:7px;margin-top:8px}
.m5-bh-sub span{color:#e4eaf6;font-size:9px;letter-spacing:.14em;font-weight:600}
.m5-bh-sub i{width:1px;height:9px;background:var(--m5gold);display:inline-block}
.m5-bh-div{margin-top:11px;width:82%;height:3px;background:radial-gradient(ellipse at center,var(--m5gold) 0%,rgba(232,183,58,0) 70%)}

/* ---- Nav items + icons ---- */
nav.side{padding:9px 10px}
.navitem{gap:12px;padding:7.5px 12px;border-radius:10px;margin-bottom:1px}
.navitem .ic{width:20px;height:20px;display:flex;align-items:center;justify-content:center;font-size:0;color:var(--m5gold)}
.navitem .ic svg{width:19px;height:19px;display:block}
.navitem:hover .ic{color:#f4cf68}
.navitem.active{background:rgba(232,183,58,.13)!important;color:#fff!important;box-shadow:none!important;position:relative}
.navitem.active .ic{color:#fff!important}
.navitem.active::before{content:"";position:absolute;left:0;top:7px;bottom:7px;width:3px;border-radius:0 3px 3px 0;background:var(--m5gold)}

/* ---- Sidebar user card ---- */
.side-foot .m5-sideuser{display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.09);border-radius:12px;padding:8px 10px;margin-bottom:8px}
.m5-suav{width:34px;height:34px;border-radius:50%;background:linear-gradient(135deg,#f2c64f,#d29627);color:#1b2a49;font-weight:800;font-size:12.5px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.m5-sumeta{flex:1;min-width:0}
.side-foot .m5-suname{font-size:13px;font-weight:700;color:#fff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.side-foot .m5-supill{background:none;color:#9fb0cf;padding:0;margin:1px 0 0;border-radius:0;display:block;font-size:10.5px;font-weight:600}
.m5-suchev{color:#7f92b4;font-size:11px;flex-shrink:0}
.navitem.m5-logout{color:#9fb0cf}
.navitem.m5-logout .ic{color:#9fb0cf}
.navitem.m5-logout .ic svg{transform:scaleX(-1)}

/* ---- Launchpad tiles (Sales Tools, Resources) ---- */
.tool-grid{gap:16px}
.tool{padding:22px 18px 46px!important;border-radius:16px!important;position:relative}
.tool:hover{border-color:var(--line)!important;box-shadow:0 10px 24px rgba(20,35,63,.10);transform:translateY(-2px)}
.tool.sel{border-color:var(--m5gold)!important;box-shadow:0 0 0 1px var(--m5gold)}
.tic.m5-chip{width:54px!important;height:54px!important;border-radius:15px!important;background:linear-gradient(150deg,#17294c,#101f3c)!important;color:var(--m5gold)!important;display:flex;align-items:center;justify-content:center;margin:0 auto 13px!important;font-size:0!important;box-shadow:inset 0 0 0 1px rgba(232,183,58,.20)}
.tic.m5-chip svg{width:26px;height:26px;color:var(--m5gold)}
.tool .tt{font-size:15px}
.tool::after{content:"\2192";position:absolute;right:14px;bottom:12px;width:27px;height:27px;border-radius:50%;background:#f5f8fc;border:1px solid var(--line);color:#c19a24;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700}

/* ---- Launchpad rows (Systems/Tools, Get Help, Training Library) ---- */
.m5-row{padding:14px 16px!important;border-radius:14px!important;gap:14px;align-items:center}
.m5-row .ri{width:46px;height:46px;flex-shrink:0}
.m5-row .ri.m5-chip{border-radius:12px;background:linear-gradient(150deg,#17294c,#101f3c);color:var(--m5gold);display:flex;align-items:center;justify-content:center;font-size:0;box-shadow:inset 0 0 0 1px rgba(232,183,58,.20)}
.m5-row .ri.m5-chip svg{width:22px;height:22px;color:var(--m5gold)}
.m5-rtext{display:flex;flex-direction:column;flex:1;min-width:0}
.m5-row .rl{font-size:14.5px;font-weight:700;color:#16233f}
.m5-row .rd{font-size:12px;color:#8a93a5;font-weight:500;margin-top:2px}
.m5-row .ra{color:#b6c0d1;font-size:16px;flex-shrink:0}

/* ---- Inline gold header icons (wave, dashboard) ---- */
.m5-hi{display:inline-flex;vertical-align:-5px;margin-right:8px;color:var(--m5gold)}
.m5-hi svg{width:28px;height:28px}
.m5-dashi{display:inline-flex;vertical-align:-4px;margin-right:9px;color:var(--m5gold)}
.m5-dashi svg{width:19px;height:19px}

/* ---- Dashboard call cards: icon + name ---- */
.m5-chead{display:flex;align-items:center;gap:8px;margin-bottom:2px}
.m5-cicon{width:24px;height:24px;flex-shrink:0;color:var(--m5gold);display:flex;align-items:center;justify-content:center}
.m5-cicon svg{width:22px;height:22px}
.m5-call .m5-ct{margin:0}

/* ---- Dashboard progress modules (Fast Start / Academy trackers) ---- */
.m5-modrow{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:14px 0}
@media(max-width:820px){.m5-modrow{grid-template-columns:1fr}}
.m5-pmod{background:#fff;border:1px solid var(--line);border-radius:16px;box-shadow:0 2px 10px rgba(20,35,63,.06);padding:18px 20px;display:flex;gap:18px;align-items:center}
.m5-pmod.hl{border-top:3px solid var(--m5gold)}
.m5-pmring{flex-shrink:0}
.m5-ring{width:104px;height:104px;display:block}
.m5-ring-bg{fill:none;stroke:#eef2f9;stroke-width:11}
.m5-ring-fg{fill:none;stroke:url(#m5gg);stroke-width:11;stroke-linecap:round;transform:rotate(-90deg);transform-origin:center;transition:stroke-dashoffset .6s ease}
.m5-ring-t{fill:#16233f;font-size:25px;font-weight:800}
.m5-ring-s{fill:#8a93a5;font-size:8px;font-weight:700;letter-spacing:.09em}
.m5-pmbody{flex:1;min-width:0}
.m5-pmhead{display:flex;align-items:center;gap:9px;font-size:15px;font-weight:800;color:#16233f}
.m5-pmchip{width:30px;height:30px;flex-shrink:0;border-radius:8px;background:linear-gradient(150deg,#17294c,#101f3c);display:flex;align-items:center;justify-content:center;box-shadow:inset 0 0 0 1px rgba(232,183,58,.20)}
.m5-pmchip svg{width:17px;height:17px;color:var(--m5gold)}
.m5-pmmeta{font-size:12.5px;color:#8a93a5;margin:2px 0 10px}
.m5-pmwin{font-size:12px;color:#1a9e63;font-weight:700;margin-bottom:9px}
.m5-pmnext{background:#f7fafe;border:1px solid var(--line);border-left:3px solid var(--m5gold);border-radius:10px;padding:9px 12px;margin-bottom:12px}
.m5-pmnext.done{border-left-color:#1a9e63}
.m5-pmnl{font-size:10px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:#c9971f;margin-bottom:2px}
.m5-pmnext.done .m5-pmnl{color:#1a9e63}
.m5-pmnt{font-size:13.5px;font-weight:800;color:#16233f}
.m5-pmnm{font-size:12px;color:#8a93a5;margin-top:2px;line-height:1.45}
.m5-pmbtn{display:inline-flex;align-items:center;gap:7px;background:linear-gradient(135deg,var(--m5gold),#c9971f);color:#2a2205;font-weight:800;font-size:13px;padding:10px 18px;border-radius:9px;cursor:pointer;text-decoration:none}
.m5-pmod.acad .m5-pmbtn{background:#0e2244;color:#fff}
.m5-pmbtn:hover{filter:brightness(1.05)}

/* ---- Virtual Calls refresh ---- */
.m5-callsec{background:#fff;border:1px solid var(--line);border-radius:16px;padding:8px;margin-bottom:14px;box-shadow:0 2px 8px rgba(20,35,63,.05)}
.m5-callsec-h{font-size:12px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:#8a93a5;padding:8px 10px 6px}
.m5-callrow{display:flex;align-items:center;gap:13px;padding:11px 12px;border-radius:12px;text-decoration:none;transition:.12s}
.m5-callrow:hover{background:#f6f9fe}
.m5-crchip{width:42px;height:42px;flex-shrink:0;border-radius:11px;background:linear-gradient(150deg,#17294c,#101f3c);display:flex;align-items:center;justify-content:center;box-shadow:inset 0 0 0 1px rgba(232,183,58,.20)}
.m5-crchip svg{width:21px;height:21px;color:var(--m5gold)}
.m5-crtext{flex:1;min-width:0;display:flex;flex-direction:column}
.m5-crname{font-size:14px;font-weight:700;color:#16233f;line-height:1.25}
.m5-crtime{font-size:12px;color:#8a93a5;margin-top:2px}
.m5-crjoin{flex-shrink:0;background:var(--m5gold);color:#1b2a49;font-weight:800;font-size:12px;padding:8px 17px;border-radius:8px}
.m5-callrow:hover .m5-crjoin{filter:brightness(1.06)}
.m5-daygrid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
@media(max-width:820px){.m5-daygrid{grid-template-columns:1fr 1fr}}
.m5-daycard{background:#fff;border:1px solid var(--line);border-radius:16px;padding:8px;box-shadow:0 2px 8px rgba(20,35,63,.05)}
.m5-daycard.today{border-color:var(--m5gold);box-shadow:0 0 0 1px var(--m5gold)}
.m5-daycard-h{font-size:13.5px;font-weight:800;color:#16233f;padding:8px 10px 6px;display:flex;align-items:center;gap:8px}
.m5-todaypill{background:var(--m5gold);color:#1b2a49;font-size:10px;font-weight:800;padding:2px 8px;border-radius:20px;text-transform:uppercase;letter-spacing:.03em}
.m5-dayempty{font-size:12.5px;color:#9aa3b2;padding:6px 10px 10px}
/* ---- Today section (top of Virtual Calls) ---- */
.m5-todaysec{border-color:var(--m5gold);box-shadow:0 0 0 1px var(--m5gold),0 4px 16px rgba(232,183,58,.18)}
.m5-todayhd{color:#16233f !important;display:flex;align-items:center;gap:9px}
.m5-etpill{background:#0e2244;color:#fff;font-size:9.5px;font-weight:800;padding:2px 8px;border-radius:20px;letter-spacing:.05em}
.m5-todaynote{font-size:13px;color:#4a5568;padding:2px 10px 8px;line-height:1.5}
.m5-todaynote.m5-restday{color:#5a6678}
.m5-todaynote b{color:#16233f}

/* ---- Gold buttons for FB/WhatsApp/Discord + button icons + optional note ---- */
.m5-lnk.fb,.m5-lnk.wa,.m5-lnk.dc{background:#c9a227!important;color:#2a2205!important}
.m5-lnk .m5-bico{display:inline-flex;align-items:center;color:#16233f}
.m5-lnk .m5-bico svg{width:16px;height:16px;display:block}
.m5-note{background:#f3f5f9;border:1px solid #e2e7f0;border-radius:10px;padding:11px 13px;margin:10px 0 2px;font-size:13px;color:#4a5568;line-height:1.55}
.m5-note b{color:#2a3550}

/* ---- Inline text icons (calendar / dashboard inside copy) ---- */
.m5-inico{display:inline-flex;vertical-align:-3px}
.m5-inico svg{width:15px;height:15px;display:block}

/* ---- Checkmark bullet lists (Strategy / Cleared-to-Dial) ---- */
.m5-ckbul{list-style:none;padding-left:2px;margin:7px 0 0}
.m5-ckbul li{position:relative;padding-left:24px;margin:5px 0;line-height:1.5}
.m5-ckbul li::before{content:"";position:absolute;left:0;top:2px;width:16px;height:16px;border-radius:5px;background:#e6f6ee;border:1px solid #bfe6d1}
.m5-ckbul li::after{content:"\2713";position:absolute;left:3.5px;top:2px;font-size:11px;font-weight:800;color:#1a9e63;line-height:16px}
.m5-paren{display:block;color:#8a93a5;font-size:12.5px;font-style:italic;margin-bottom:2px}

/* ---- Recruiting: expandable "How to enroll your new hire" ---- */
.m5-expand{background:#fff;border:1px solid var(--line);border-radius:14px;margin:10px 0;overflow:hidden;box-shadow:0 2px 8px rgba(20,35,63,.05)}
.m5-exhead{display:flex;align-items:center;gap:14px;padding:14px 16px;cursor:pointer;user-select:none}
.m5-exhead:hover{background:#f6f9fe}
.m5-exchip{width:46px;height:46px;flex-shrink:0;border-radius:12px;background:linear-gradient(150deg,#17294c,#101f3c);display:flex;align-items:center;justify-content:center;box-shadow:inset 0 0 0 1px rgba(232,183,58,.20)}
.m5-exchip svg{width:22px;height:22px;color:var(--m5gold)}
.m5-extext{flex:1;min-width:0}
.m5-exname{font-size:14.5px;font-weight:700;color:#16233f}
.m5-exsub{font-size:12px;color:#8a93a5;margin-top:2px}
.m5-exchev{color:#b6c0d1;font-size:20px;flex-shrink:0;transition:transform .18s}
.m5-expand.open .m5-exchev{transform:rotate(90deg)}
.m5-exbody{display:none;padding:4px 18px 18px;border-top:1px solid var(--line)}
.m5-expand.open .m5-exbody{display:block}
.m5-estep{display:block;margin:18px 0 0}
.m5-estep-h{font-size:14px;font-weight:800;color:#16233f;margin:0 0 6px;display:flex;align-items:center;gap:8px}
.m5-estep-n{width:22px;height:22px;flex-shrink:0;border-radius:7px;background:var(--m5gold);color:#1b2a49;font-weight:800;font-size:12px;display:flex;align-items:center;justify-content:center}
.m5-estep p{margin:5px 0;font-size:13.5px;color:#3d4657;line-height:1.55}
.m5-estep ul,.m5-estep ol{margin:6px 0;padding-left:20px;font-size:13.5px;color:#3d4657;line-height:1.6}
.m5-estep li{margin:4px 0}
.m5-msgcard{background:#f7fafe;border:1px solid var(--line);border-radius:12px;padding:13px 15px;margin:10px 0}
.m5-msgcard-h{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:8px}
.m5-msgcard-t{font-size:12.5px;font-weight:800;color:#16233f;text-transform:uppercase;letter-spacing:.03em}
.m5-copybtn{flex-shrink:0;background:#16233f;color:#fff;border:none;border-radius:8px;padding:7px 14px;font-size:12px;font-weight:700;cursor:pointer;display:inline-flex;align-items:center;gap:6px}
.m5-copybtn:hover{filter:brightness(1.12)}
.m5-copybtn.copied{background:#1a9e63}
.m5-msgbody{font-size:13px;color:#3d4657;line-height:1.6;white-space:pre-wrap}
.m5-msgbody a{color:#2563ff;word-break:break-all}
.m5-enrollbtn-wrap{margin-top:18px;text-align:center}
.m5-enrollbtn{display:inline-flex;align-items:center;gap:9px;background:linear-gradient(135deg,#e8b73a,#c9971f);color:#2a2205;font-weight:800;font-size:14.5px;padding:13px 26px;border-radius:11px;text-decoration:none;box-shadow:0 6px 16px rgba(201,151,31,.28)}
.m5-enrollbtn:hover{filter:brightness(1.05)}
.m5-enrollbtn svg{width:18px;height:18px}

/* ---- Fast Start: navy module number badges, heading rocket, bigger progress ---- */
.mod .mn{background:#0e2244!important;color:#fff!important;font-size:20px!important;font-weight:800;width:38px!important;height:38px!important;flex:0 0 38px!important}
.m5-fsrocket{display:inline-flex;vertical-align:-4px;margin-left:8px;color:#0e2244}
.m5-fsrocket svg{width:27px;height:27px}
.m5-fsprog{margin:16px 0 20px}
.m5-fsprog .lab{font-size:15.5px!important}
.m5-fsprog .bar{height:12px!important}

/* ---- Book covers (real cover via ISBN, branded fallback) ---- */
.bookcover{position:relative;background:linear-gradient(150deg,#17294c,#0c1c38)!important}
.bookcov-fb{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#e8b73a}
.bookcov-fb svg{width:22px;height:22px}
.bookcov-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}

/* ---- Recruiting compensation link list (inside expandable) ---- */
.m5-complist{display:flex;flex-direction:column;gap:8px;margin-top:4px}
.m5-comprow{display:flex;align-items:center;gap:11px;padding:11px 13px;border:1px solid var(--line);border-radius:11px;text-decoration:none;background:#fff;transition:.12s}
.m5-comprow:hover{background:#f6f9fe;border-color:#c9d0dd}
.m5-comprow .m5-cdot{width:30px;height:30px;flex-shrink:0;border-radius:8px;background:linear-gradient(150deg,#17294c,#101f3c);display:flex;align-items:center;justify-content:center}
.m5-comprow .m5-cdot svg{width:15px;height:15px;color:var(--m5gold)}
.m5-comprow .m5-clbl{flex:1;font-size:13.5px;font-weight:700;color:#16233f}
.m5-comprow .m5-carr{color:#b6c0d1;font-size:15px}

/* ---- Health page ---- */
.m5-hhead{display:inline-flex;vertical-align:-4px;margin-right:9px;color:#e0576f}
.m5-hhead svg{width:26px;height:26px}
.m5-hcard{background:#fff;border:1px solid var(--line);border-radius:15px;box-shadow:0 2px 8px rgba(20,35,63,.05);padding:18px 20px;margin:14px 0}
.m5-hcard-h{display:flex;align-items:center;gap:11px;font-size:16px;font-weight:800;color:#16233f;margin-bottom:6px}
.m5-hico{width:34px;height:34px;flex-shrink:0;border-radius:9px;background:linear-gradient(150deg,#17294c,#101f3c);display:flex;align-items:center;justify-content:center;box-shadow:inset 0 0 0 1px rgba(232,183,58,.20)}
.m5-hico svg{width:19px;height:19px;color:var(--m5gold)}
.m5-hblurb{font-size:13.5px;color:#4a5568;line-height:1.55;margin:6px 0 12px}
.m5-flyerph{border:2px dashed #ccd6e6;border-radius:12px;background:#f7fafe;padding:22px;text-align:center;color:#5a6678;font-size:13.5px;line-height:1.55;margin-top:8px}
.m5-biglnk{font-size:14.5px!important;padding:13px 22px!important;border-radius:11px!important}
.m5-poplogo{display:block;margin-top:6px;text-align:center;border:1px solid var(--line);border-radius:12px;padding:18px;background:#fff;transition:.15s}
.m5-poplogo:hover{box-shadow:0 8px 20px rgba(20,35,63,.12);border-color:#c9d0dd}
.m5-poplogo img{max-width:340px;width:100%;height:auto;display:inline-block}
.m5-flyer{display:block;width:100%;max-width:340px;height:auto;border-radius:12px;border:1px solid var(--line);box-shadow:0 4px 14px rgba(20,35,63,.10);margin-top:4px}
.m5-hbullets{margin:6px 0 14px;padding-left:0;list-style:none}
.m5-hbullets li{position:relative;padding-left:22px;margin:9px 0;font-size:13.5px;color:#4a5568;line-height:1.55}
.m5-hbullets li::before{content:"";position:absolute;left:2px;top:7px;width:8px;height:8px;border-radius:50%;background:var(--m5gold)}
.m5-popfb{display:none;font-size:16px;color:#16233f;font-weight:700}
.m5-popfb b{color:#c9971f}
.m5-poperr img{display:none}
.m5-poperr .m5-popfb{display:inline-block}

/* ---- Preview-experience: recruiting entry card + floating exit pill ---- */
.m5-previewcard{background:linear-gradient(135deg,#132a52,#0e2244);border-radius:16px;padding:20px 22px;margin-top:14px;box-shadow:0 8px 24px rgba(20,35,63,.14)}
.m5-pvtitle{display:flex;align-items:center;gap:9px;color:#fff;font-size:16px;font-weight:800}
.m5-pvtitle .m5-pvi{width:22px;height:22px;display:inline-flex;align-items:center;justify-content:center;color:var(--m5gold)}
.m5-pvtitle .m5-pvi svg{width:20px;height:20px}
.m5-pvsub{color:#cdd6e6;font-size:13.5px;line-height:1.55;margin:8px 0 14px}
.m5-pvbtn{background:var(--m5gold);color:#2a2205;border:none;border-radius:11px;padding:12px 20px;font-size:14px;font-weight:800;cursor:pointer}
.m5-pvbtn:hover{filter:brightness(1.05)}
#m5-previewbar{position:fixed;top:14px;left:50%;transform:translateX(-50%);z-index:4000;display:flex;align-items:center;gap:12px;background:#0e2244;color:#fff;border-radius:999px;padding:9px 9px 9px 16px;box-shadow:0 10px 30px rgba(0,0,0,.35);max-width:calc(100vw - 20px)}
#m5-previewbar .m5-pbdot{color:var(--m5gold);display:inline-flex;flex-shrink:0}
#m5-previewbar .m5-pbdot svg{width:17px;height:17px}
#m5-previewbar .m5-pbtxt{font-size:12.5px;line-height:1.3}
#m5-previewbar .m5-pbtxt b{color:var(--m5gold)}
.m5-pbexit{background:var(--m5gold);color:#2a2205;border:none;border-radius:999px;padding:7px 14px;font-size:12.5px;font-weight:800;cursor:pointer;white-space:nowrap;flex-shrink:0}
.m5-pbexit:hover{filter:brightness(1.05)}
body.m5-previewing #m5-prelic .m5-signout{visibility:hidden}
@media(max-width:600px){#m5-previewbar{top:8px;padding:8px 8px 8px 13px;gap:9px}#m5-previewbar .m5-pbtxt{font-size:11px}}

/* ===================================================================== */
/* ==================  MOBILE LAYER  (phones ≤ 768px)  ================== */
/* Desktop (>768px) is completely unaffected — every rule below is gated  */
/* behind the media query or the hidden-by-default hamburger.             */
/* ===================================================================== */
.m5-hamb{display:none;align-items:center;justify-content:center;width:40px;height:40px;flex-shrink:0;border:none;border-radius:11px;background:linear-gradient(150deg,#17294c,#0e2244);color:#fff;cursor:pointer;padding:0}
.m5-hamb svg{width:22px;height:22px;stroke:#fff;stroke-width:2.2;fill:none;stroke-linecap:round}
.m5-hamb:active{transform:scale(.93)}
.m5-backdrop{position:fixed;inset:0;background:rgba(7,15,30,.55);z-index:900;opacity:0;pointer-events:none;transition:opacity .25s}

@media(max-width:768px){
  html,body{overflow-x:hidden;max-width:100%}
  /* --- sidebar becomes an off-canvas drawer --- */
  #app>aside{position:fixed;top:0;left:0;height:100vh;height:100dvh;width:min(85vw,310px);z-index:1000;
             transform:translateX(-100%);transition:transform .27s cubic-bezier(.4,0,.2,1);
             box-shadow:0 0 44px rgba(0,0,0,.5);overflow-y:auto}
  body.m5-navopen #app>aside{transform:translateX(0)}
  body.m5-navopen .m5-backdrop{opacity:1;pointer-events:auto}
  /* --- main takes the full width --- */
  #app>main{width:100%;min-width:0}
  /* --- top bar + hamburger --- */
  .topbar{padding:9px 13px;gap:11px}
  .m5-hamb{display:inline-flex}
  .crumb{font-size:16px;font-weight:800}
  .topright{gap:9px}
  .statuschip{font-size:10.5px;padding:4px 9px;white-space:nowrap}
  .protobanner{padding:7px 14px;font-size:11.5px;line-height:1.45}
  /* --- content spacing --- */
  .content{padding:16px 14px 40px}
  h1.page{font-size:22px;line-height:1.2}
  .sub{font-size:13.5px}
  /* --- collapse every multi-column layout to a single column --- */
  .grid2,.tiles,.course-grid,.tool-grid,.m5-daygrid,.m5-modrow,.m5-comprow,
  .m5-poprow,.m5-hrow,.m5-tgrid,.m5-splitrow,.m5-tworow{grid-template-columns:1fr !important}
  /* --- keep wide media inside the screen --- */
  .content img,.content table,.content pre,.content iframe,.toolframe{max-width:100% !important}
  .toolframe{height:1500px}
  /* --- roomier tap targets for call/list rows --- */
  .m5-callrow,.navitem{min-height:44px}
  /* --- dashboard "Today's calls": stack cards instead of clipping the row --- */
  .m5-calls{flex-direction:column;overflow-x:visible;gap:8px}
  .m5-call{min-width:0;width:100%;flex:none}
  .m5-dashpanel.open .m5-dashinner{max-height:1200px}
}
/* ===== Goal Card + Activity Dashboard ===== */
#m5gc-app{--gcn:#16233f;--gcg:#c9a227;--gcl:#e5e9f0;--gci:#1f2a44;--gcs:#6b7688;--gcgood:#1a8f5a;--gcbad:#c0392b;color:var(--gci)}
#m5gc-app .m5gc-card{background:#fff;border:1px solid var(--gcl);border-radius:16px;padding:20px;margin-top:16px;box-shadow:0 8px 26px rgba(20,35,63,.06)}
#m5gc-app .m5gc-stitle{text-align:center;font-family:Georgia,'Times New Roman',serif;font-size:22px;color:var(--gcn);letter-spacing:.06em;font-weight:700}
#m5gc-app .m5gc-stars{text-align:center;color:var(--gcg);font-size:15px;letter-spacing:3px;margin:4px 0 8px}
#m5gc-app .m5gc-ssub{text-align:center;font-size:13px;color:var(--gcs);margin:0 0 14px}
#m5gc-app .m5gc-row2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
#m5gc-app .m5gc-fld{font-size:11px;font-weight:800;color:var(--gcs);text-transform:uppercase;letter-spacing:.03em;display:flex;flex-direction:column;gap:6px}
#m5gc-app .m5gc-fld input{font-size:15px;padding:9px 11px;border:1px solid var(--gcl);border-radius:9px;font-family:inherit;color:var(--gci);background:#fff}
#m5gc-app .m5gc-fld input:focus{outline:none;border-color:var(--gcg)}
#m5gc-app .m5gc-track{display:grid;grid-template-columns:repeat(6,1fr);gap:8px;margin:14px 0 4px}
#m5gc-app .m5gc-stat{background:#f7fafe;border:1px solid var(--gcl);border-radius:11px;padding:10px 6px;text-align:center}
#m5gc-app .m5gc-stat .l{font-size:9px;font-weight:800;color:var(--gcs);text-transform:uppercase}
#m5gc-app .m5gc-stat .v{font-size:20px;font-weight:800;color:var(--gcn);margin-top:2px}
#m5gc-app .m5gc-stat.hl{background:#fbf7e9;border-color:#efe3b8}
#m5gc-app .m5gc-stat.hl .v{color:#a9861d}
#m5gc-app .m5gc-planbar{background:#f4f7fc;border:1px solid #dde6f2;border-radius:12px;padding:12px 14px;margin:14px 0 2px}
#m5gc-app .m5gc-planbar .pintro{font-size:12.5px;color:var(--gcs);margin-bottom:10px}
#m5gc-app .m5gc-planbar .pintro b{color:var(--gcn)}
#m5gc-app .m5gc-planbar .plangrid{display:grid;grid-template-columns:repeat(4,1fr);gap:9px}
#m5gc-app .m5gc-planbar .plan{background:#fff;border:1px solid var(--gcl);border-radius:10px;padding:8px;text-align:center}
#m5gc-app .m5gc-planbar .plan .l{font-size:9px;font-weight:800;color:var(--gcs);text-transform:uppercase}
#m5gc-app .m5gc-planbar .plan .v{font-size:17px;font-weight:800;color:var(--gcn);margin-top:2px}
#m5gc-app .m5gc-planbar .plan.acc .v{color:#a9861d}
#m5gc-app .m5gc-prog{background:#f4f6fa;border:1px solid var(--gcl);border-radius:12px;padding:12px 14px;margin:12px 0 4px}
#m5gc-app .m5gc-prog .pt{font-size:14px;font-weight:700;color:var(--gcn)}
#m5gc-app .m5gc-barp{height:9px;background:#e3e8f0;border-radius:6px;overflow:hidden;margin-top:8px}
#m5gc-app .m5gc-barp>i{display:block;height:100%;background:linear-gradient(90deg,#e8b73a,#c9971f);border-radius:6px}
#m5gc-app table.m5gc-act{width:100%;border-collapse:collapse;margin-top:14px;font-size:13.5px}
#m5gc-app table.m5gc-act th{background:var(--gcn);color:#fff;padding:9px 5px;font-size:10.5px;font-weight:700;text-align:center}
#m5gc-app table.m5gc-act th small{display:block;font-weight:500;color:#b9c6e0;font-size:9px;margin-top:2px}
#m5gc-app table.m5gc-act td{border:1px solid var(--gcl);padding:5px;text-align:center}
#m5gc-app table.m5gc-act td.time{background:#f4f6fa;font-weight:700;color:var(--gcn);font-size:12px;white-space:nowrap}
#m5gc-app table.m5gc-act tr.planned td.time{box-shadow:inset 4px 0 0 var(--gcg)}
#m5gc-app table.m5gc-act tr.planned td{background:#fcfaf1}
#m5gc-app table.m5gc-act input[type=number]{width:52px;text-align:center;font-size:14px;padding:6px 4px;border:1px solid var(--gcl);border-radius:7px;font-family:inherit;background:#fff}
#m5gc-app table.m5gc-act input[type=number]:focus{outline:none;border-color:var(--gcg)}
#m5gc-app table.m5gc-act input[type=checkbox]{width:19px;height:19px;accent-color:var(--gcg);cursor:pointer}
#m5gc-app table.m5gc-act td.rp{font-weight:800;color:var(--gcn);background:#f7fafe}
#m5gc-app table.m5gc-act tr.tot td{background:var(--gcn);color:#fff;font-weight:800;font-size:13px;padding:9px 5px}
#m5gc-app .m5gc-btns{text-align:center;margin-top:18px;display:flex;gap:10px;justify-content:center;flex-wrap:wrap}
#m5gc-app .m5gc-btn{border:0;border-radius:9px;padding:11px 20px;font-size:13.5px;font-weight:800;cursor:pointer;font-family:inherit}
#m5gc-app .m5gc-btn.p{background:var(--gcg);color:#16233f}
#m5gc-app .m5gc-btn.s{background:var(--gcn);color:#fff}
#m5gc-app .m5gc-btn.g{background:#eef1f6;color:var(--gcn)}
#m5gc-app .m5gc-dashh{font-family:Georgia,serif;font-size:20px;color:var(--gcn);font-weight:700}
#m5gc-app .m5gc-hint{background:#f4f7fc;border:1px dashed #cdd8ee;border-radius:10px;padding:10px 12px;font-size:12.5px;color:var(--gcs);margin:10px 0}
#m5gc-app .m5gc-cmp3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:12px}
#m5gc-app .m5gc-cmp{background:#f7fafe;border:1px solid var(--gcl);border-radius:14px;padding:14px}
#m5gc-app .m5gc-cmp .ct{font-size:11px;font-weight:800;color:var(--gcs);text-transform:uppercase}
#m5gc-app .m5gc-cmp .cbig{font-size:28px;font-weight:800;color:var(--gcn);margin:6px 0 2px;line-height:1}
#m5gc-app .m5gc-cmp .cunit{font-size:12px;color:var(--gcs);font-weight:600}
#m5gc-app .m5gc-delta{display:inline-flex;align-items:center;gap:5px;font-size:12.5px;font-weight:800;padding:3px 9px;border-radius:20px;margin-top:8px}
#m5gc-app .m5gc-delta.up{background:#e6f5ee;color:var(--gcgood)}
#m5gc-app .m5gc-delta.down{background:#fbeae7;color:var(--gcbad)}
#m5gc-app .m5gc-delta.flat{background:#eef1f6;color:var(--gcs)}
#m5gc-app .m5gc-cmp .cprev{font-size:11.5px;color:var(--gcs);margin-top:8px}
#m5gc-app .m5gc-avgstrip{display:grid;grid-template-columns:repeat(5,1fr);gap:9px;margin-top:14px}
#m5gc-app .m5gc-avg{background:#fff;border:1px solid var(--gcl);border-radius:11px;padding:10px 6px;text-align:center}
#m5gc-app .m5gc-avg .l{font-size:9px;font-weight:800;color:var(--gcs);text-transform:uppercase}
#m5gc-app .m5gc-avg .v{font-size:18px;font-weight:800;color:var(--gcn);margin-top:2px}
#m5gc-app .m5gc-hlgrid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:11px;margin-top:14px}
#m5gc-app .m5gc-hlc{display:flex;gap:11px;align-items:flex-start;background:linear-gradient(135deg,#fbfcfe,#f4f7fc);border:1px solid var(--gcl);border-radius:13px;padding:13px}
#m5gc-app .m5gc-hlc .ic{font-size:21px}
#m5gc-app .m5gc-hlc .ht{font-size:10.5px;font-weight:800;color:var(--gcs);text-transform:uppercase}
#m5gc-app .m5gc-hlc .hv{font-size:15px;font-weight:800;color:var(--gcn);margin-top:2px}
#m5gc-app .m5gc-hlc .hd{font-size:11.5px;color:var(--gcs);margin-top:2px}
#m5gc-app .m5gc-chart{margin-top:18px}
#m5gc-app .m5gc-chart h4{font-size:12px;font-weight:800;color:var(--gcs);text-transform:uppercase;margin:0 0 12px}
#m5gc-app .m5gc-bars{display:flex;align-items:flex-end;gap:8px;height:150px;padding:0 4px;border-bottom:2px solid var(--gcl)}
#m5gc-app .m5gc-b{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%}
#m5gc-app .m5gc-b .col{width:70%;max-width:44px;background:linear-gradient(180deg,#2c4a86,#16233f);border-radius:6px 6px 0 0;position:relative}
#m5gc-app .m5gc-b .col.goal{background:linear-gradient(180deg,#38b06f,#1a8f5a)}
#m5gc-app .m5gc-b .col .n{position:absolute;top:-18px;left:50%;transform:translateX(-50%);font-size:11px;font-weight:800;color:var(--gcn)}
#m5gc-app .m5gc-b .lab{font-size:10.5px;color:var(--gcs);margin-top:7px;font-weight:600}
#m5gc-app .m5gc-b .dow{font-size:9.5px;color:#9aa4b5}
#m5gc-app .m5gc-legend{font-size:11.5px;color:var(--gcs);margin-top:12px;text-align:center}
@media(max-width:720px){#m5gc-app .m5gc-row2,#m5gc-app .m5gc-cmp3,#m5gc-app .m5gc-hlgrid{grid-template-columns:1fr}#m5gc-app .m5gc-track,#m5gc-app .m5gc-avgstrip,#m5gc-app .m5gc-planbar .plangrid{grid-template-columns:repeat(2,1fr)}#m5gc-app table.m5gc-act input[type=number]{width:40px}}
@media print{body *{visibility:hidden!important}#m5gc-printarea,#m5gc-printarea *{visibility:visible!important}#m5gc-printarea{position:absolute;left:0;top:0;width:100%;box-shadow:none;border:none;margin:0}#m5gc-app .m5gc-noprint,.m5gc-noprint{display:none!important}}
/* ===== Calls / Events — hero + calendar ===== */
.m5-evseclabel{font-size:12px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:#8a93a5;margin:22px 2px 2px}
.m5-evhero{position:relative;border-radius:16px;overflow:hidden;margin:10px 0 6px;color:#fff;background:#16233f;background-size:cover;background-position:center;box-shadow:0 10px 28px rgba(20,35,63,.18)}
.m5-evhero::before{content:"";position:absolute;inset:0;background:linear-gradient(115deg,rgba(11,20,40,.88),rgba(11,20,40,.56))}
.m5-evhero.conv::before{background:linear-gradient(115deg,rgba(26,15,42,.88),rgba(20,12,42,.58))}
.m5-evhero-in{position:relative;padding:24px 24px 22px}
.m5-evbadge{display:inline-block;background:#b23a2e;color:#fff;font-size:11px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;padding:5px 11px;border-radius:6px}
.m5-evbadge.gold{background:var(--m5gold);color:#1b2a49}
.m5-evtitle{font-family:Georgia,'Times New Roman',serif;font-size:30px;line-height:1.06;font-weight:800;margin:12px 0 4px}
.m5-evmeta{font-size:14px;color:#cdd8ee;margin-bottom:14px}
.m5-cd{display:flex;gap:9px;margin:6px 0 16px;flex-wrap:wrap}
.m5-cd .u{background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.22);border-radius:10px;padding:8px 0;width:62px;text-align:center}
.m5-cd .u .n{font-size:22px;font-weight:800;line-height:1}
.m5-cd .u .l{font-size:9px;letter-spacing:.06em;text-transform:uppercase;color:#c4d0e6;margin-top:4px}
.m5-evbtns{display:flex;gap:10px;flex-wrap:wrap}
.m5-evbtn{border:0;border-radius:9px;padding:11px 18px;font-size:13.5px;font-weight:800;cursor:pointer;font-family:inherit;display:inline-flex;align-items:center;gap:7px}
.m5-evbtn.reg{background:#b23a2e;color:#fff}
.m5-evbtn.cal{background:#fff;color:#16233f}
.m5-evbtn.gold{background:var(--m5gold);color:#1b2a49}
.m5-evbtn:hover{filter:brightness(1.05)}
.m5-crbtns{flex-shrink:0;display:flex;gap:7px;align-items:center}
.m5-crjoin{border:0;cursor:pointer;font-family:inherit}
.m5-crcal{flex-shrink:0;background:#f4efe0;color:#8a6d16;border:1px solid #e7dab4;font-weight:800;font-size:12px;padding:8px 13px;border-radius:8px;cursor:pointer;font-family:inherit;white-space:nowrap}
.m5-crcal:hover{filter:brightness(1.03)}
.m5-trio{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:8px 0 4px}
@media(max-width:820px){.m5-trio{grid-template-columns:1fr}}
.m5-tcard{background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:0 2px 8px rgba(20,35,63,.05);display:flex;flex-direction:column}
.m5-tcard img{width:100%;display:block;border-bottom:1px solid var(--line)}
.m5-tcard-b{padding:13px 15px 15px;flex:1;display:flex;flex-direction:column;gap:8px}
.m5-tcard-t{font-weight:800;font-size:14.5px;color:#16233f}
.m5-tcard-d{font-size:12.5px;color:#6b7688;flex:1}
.m5-tcard .btn,.m5-tcard .openbtn{width:100%;justify-content:center;text-align:center}
/* ===== Resources / Sales Tools search ===== */
.m5s-wrap{position:relative;margin:2px 0 16px}
.m5s-wrap .m5s-mag{position:absolute;left:15px;top:50%;transform:translateY(-50%);font-size:16px;opacity:.5;pointer-events:none}
.m5s-wrap input{width:100%;padding:13px 44px 13px 42px;border:1.5px solid var(--line);border-radius:12px;font-size:15px;font-family:inherit;outline:none;background:#fff;color:var(--ink);transition:border-color .15s,box-shadow .15s}
.m5s-wrap input:focus{border-color:var(--gold);box-shadow:0 0 0 4px rgba(224,168,61,.15)}
.m5s-wrap input::placeholder{color:#9aa3b4}
.m5s-clr{position:absolute;right:11px;top:50%;transform:translateY(-50%);border:0;background:#eef1f7;color:#66708a;width:25px;height:25px;border-radius:50%;cursor:pointer;font-size:13px;line-height:1;display:none}
.m5s-clr.show{display:block}
.m5s-results .listcard{margin-top:6px}
.m5s-rescount{font-size:12.5px;color:var(--ink-soft);font-weight:700;margin:2px 0 4px}
.m5s-hit{cursor:pointer;border-radius:9px;transition:background .12s;padding-left:8px;padding-right:8px;margin:0 -8px}
.m5s-hit:hover{background:#f7f9fd}
.m5s-grp{display:inline-block;font-size:10.5px;font-weight:800;color:var(--gold-deep);background:rgba(224,168,61,.14);border-radius:999px;padding:2px 8px;margin-left:8px;letter-spacing:.2px;vertical-align:middle}
.m5s-hit mark{background:rgba(224,168,61,.42);color:inherit;border-radius:3px;padding:0 1px}
.m5s-empty{background:#fff;border:1px dashed var(--line);border-radius:13px;padding:30px 20px;text-align:center;color:var(--ink-soft);font-size:14px}
.m5s-empty .big{font-size:26px;margin-bottom:6px}
.m5-row-soon{opacity:.72;cursor:default}
.m5-expand-soon{opacity:.82}
.m5-expand-soon .m5-exhead{cursor:default}
.m5-soonpill{margin-left:auto;flex:0 0 auto;font-size:10.5px;font-weight:800;letter-spacing:.03em;text-transform:uppercase;color:#a9861d;background:rgba(224,168,61,.15);border:1px solid rgba(224,168,61,.4);border-radius:999px;padding:3px 9px;white-space:nowrap}
/* ================== NEW-RECRUIT ACTION CARDS ================== */
.nr-wrap{margin:0 0 18px}
.nr{--nrg:#1a9e63;--nrgb:#e6f6ee;--nra:#c58a1a;--nrab:#fbf3e0;--nrr:#c0392b;--nru:#c2560f;--nrub:#fdefe6;
  position:relative;background:#fff;border:1px solid var(--line);border-radius:14px;
  box-shadow:0 1px 2px rgba(12,28,60,.06),0 10px 30px rgba(12,28,60,.07);
  padding:18px 20px 16px;margin:0 0 12px;overflow:hidden;border-left:4px solid var(--gold)}
.nr.t-warn{border-left-color:var(--nru)}
.nr.t-promo{border-left-color:var(--nrg)}
.nr-top{display:flex;align-items:flex-start;justify-content:space-between;gap:14px}
.nr-chip{display:inline-block;background:#fbf3e0;color:var(--gold-deep);border:1px solid #f0e0bd;
  font-size:10.5px;font-weight:900;letter-spacing:.9px;text-transform:uppercase;padding:4px 9px;border-radius:999px;margin:0 0 9px}
.t-warn .nr-chip{background:var(--nrub);color:var(--nru);border-color:#f7d6c2}
.t-promo .nr-chip{background:var(--nrgb);color:var(--nrg);border-color:#c9e9d8}
.nr-h{font-size:18.5px;font-weight:800;margin:0 0 5px;line-height:1.32}
.nr-state.lic{color:var(--nrg)} .nr-state.unl{color:var(--nru)}
.nr-meta{color:var(--ink-soft);font-size:13px}
.nr-x{flex:none;border:1px solid var(--line);background:#fff;color:var(--ink-soft);width:30px;height:30px;
  border-radius:8px;font-size:15px;line-height:1;cursor:pointer;font-family:inherit;transition:.15s}
.nr-x:hover{background:#f6f8fc;color:var(--ink);border-color:#d6deea}
.nr-prog{display:flex;align-items:center;gap:10px;margin:14px 0 12px}
.nr-bar{flex:1;height:7px;background:#eef2f8;border-radius:999px;overflow:hidden}
.nr-bar i{display:block;height:100%;background:var(--gold);border-radius:999px;transition:width .3s}
.t-promo .nr-bar i{background:var(--nrg)}
.nr-pct{font-size:12.5px;font-weight:800;color:var(--ink-soft);white-space:nowrap}
.nr-steps{list-style:none;margin:0;padding:0}
.nr-step{display:flex;gap:12px;align-items:flex-start;padding:12px 0;border-top:1px solid var(--line)}
.nr-step:first-child{border-top:0}
.nr-box{flex:none;width:23px;height:23px;border-radius:7px;border:2px solid #cbd5e4;background:#fff;
  cursor:pointer;margin-top:1px;position:relative;transition:.15s;padding:0}
.nr-box:hover{border-color:var(--gold)}
.nr-box.on{background:var(--nrg);border-color:var(--nrg)}
.nr-box.on:after{content:"";position:absolute;left:6.5px;top:2.5px;width:5px;height:10px;
  border:solid #fff;border-width:0 2.5px 2.5px 0;transform:rotate(45deg)}
.nr-box.auto{cursor:default;border-style:dashed}
.nr-box.auto.on{border-style:solid}
.nr-body{flex:1;min-width:0}
.nr-t{font-size:14.5px;font-weight:700;line-height:1.4}
.nr-step.done .nr-t{color:var(--ink-soft);text-decoration:line-through;text-decoration-color:#c3ccdb}
.nr-d{font-size:13px;color:var(--ink-soft);margin-top:3px;line-height:1.5}
.nr-tag{display:inline-block;font-size:10.5px;font-weight:900;letter-spacing:.5px;text-transform:uppercase;
  padding:3px 7px;border-radius:5px;margin-left:7px;vertical-align:2px}
.nr-tag.ok{background:var(--nrgb);color:var(--nrg);border:1px solid #c9e9d8}
.nr-tag.wait{background:var(--nrab);color:var(--nra);border:1px solid #f0e0bd}
.nr-msgbtn{display:inline-flex;align-items:center;gap:7px;margin-top:9px;background:#f2f6fd;border:1px solid #dde6f6;
  color:var(--brand-deep);font-size:12.5px;font-weight:800;padding:7px 12px;border-radius:8px;cursor:pointer;font-family:inherit}
.nr-msgbtn:hover{background:#e8effc}
.nr-msg{margin-top:10px;border:1px solid #dde6f6;background:#f8faff;border-radius:11px;padding:14px 15px 12px}
.nr-msg p{margin:0 0 10px;font-size:13.5px;line-height:1.55;white-space:pre-line}
.nr-msgfoot{display:flex;align-items:center;gap:10px;border-top:1px solid #e3ebfa;padding-top:11px}
.nr-copy{background:var(--brand-deep);border:1px solid var(--brand-deep);color:#fff;font-size:12.5px;font-weight:800;
  padding:7px 14px;border-radius:8px;cursor:pointer;font-family:inherit}
.nr-copy:hover{opacity:.92}
.nr-msgnote{font-size:12px;color:var(--ink-soft)}
.nr-alert{margin:12px 0 0;background:var(--nrub);border:1px solid #f7d6c2;color:#8a3c0a;
  border-radius:10px;padding:11px 13px;font-size:13.2px;font-weight:700;line-height:1.5}
.nr-alert .nr-msgbtn{background:#fff;border-color:#f0cdb2;color:#8a3c0a;margin-top:9px}
.nr-alert .nr-msg{background:#fff;border-color:#f0cdb2}
.nr-alert .nr-msg p{font-weight:500;color:var(--ink)}
.nr-foot{margin-top:15px;padding-top:13px;border-top:1px solid var(--line);
  display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.nr-dash{margin-left:auto;background:#16233f;border:1px solid #16233f;color:#fff;font-size:13px;font-weight:800;
  padding:9px 16px;border-radius:9px;cursor:pointer;font-family:inherit;text-decoration:none}
.nr-dash:hover{opacity:.9}
.nr-more{background:#fff;border:1px dashed #cbd5e4;border-radius:12px;padding:13px 16px;
  font-size:13.5px;font-weight:700;color:var(--ink-soft);cursor:pointer;text-align:center;font-family:inherit;width:100%}
.nr-more:hover{border-color:var(--gold);color:var(--ink)}
.nr-confirm{position:absolute;left:0;right:0;top:0;bottom:0;background:rgba(255,255,255,.97);display:flex;flex-direction:column;
  align-items:center;justify-content:center;text-align:center;padding:20px;gap:13px;z-index:5}
.nr-confirm p{margin:0;font-size:14.5px;font-weight:700;max-width:440px;line-height:1.5}
.nr-confirm .nr-row{display:flex;gap:9px}
.nr-btn{border:1px solid var(--line);background:#fff;color:var(--ink);font-size:13.5px;font-weight:800;
  padding:9px 16px;border-radius:9px;cursor:pointer;font-family:inherit}
.nr-btn.warn{background:var(--nrr);border-color:var(--nrr);color:#fff}
@media(max-width:640px){ .nr{padding:16px 15px 14px} .nr-h{font-size:17px} .nr-dash{margin-left:0;width:100%;text-align:center} }


.nr-ctl{flex:none;display:flex;align-items:center;gap:7px}
.nr-collapse{border:1px solid var(--line);background:#fff;color:var(--ink-soft);font-size:12.5px;font-weight:800;
  padding:7px 12px;border-radius:8px;cursor:pointer;font-family:inherit;white-space:nowrap;transition:.15s}
.nr-collapse:hover{background:#f6f8fc;color:var(--ink);border-color:#d6deea}
.nr-collapse .car{font-size:10px;vertical-align:1px;margin-right:2px}
.nr .nr-x{opacity:.45;font-weight:700}
.nr .nr-x:hover{opacity:1}
.nr-under{color:var(--gold-deep);font-weight:700}
.nr-fnote{font-size:12.5px;color:var(--ink-soft)}
.nr-reopen{margin:12px 0 0;background:#eef4ff;border:1px solid #d5e2fb;color:#123a99;
  border-radius:10px;padding:9px 12px;font-size:12.8px;font-weight:700}
.nr-shut{margin-top:14px}
.nr-shuth{font-size:11px;font-weight:900;letter-spacing:.7px;text-transform:uppercase;color:#98a2b6;margin:0 0 8px 2px}
.nr-row{display:flex;align-items:center;gap:11px;background:#fff;border:1px solid var(--line);
  border-left:4px solid #cbd5e4;border-radius:11px;padding:9px 12px;margin-bottom:8px}
.nr-row.warn{border-left-color:#c2560f}
.nr-expand{border:1px solid var(--line);background:#f7fafe;color:var(--ink-soft);font-size:12px;font-weight:800;
  padding:5px 10px;border-radius:7px;cursor:pointer;font-family:inherit;white-space:nowrap}
.nr-expand:hover{background:#eef3fa;color:var(--ink)}
.nr-expand .car{font-size:9px;vertical-align:1px;margin-right:2px}
.nr-rname{font-weight:800;font-size:14px;flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.nr-rmeta{font-size:12.5px;color:var(--ink-soft);white-space:nowrap}
.nr-row .nr-x{width:26px;height:26px;font-size:13px;opacity:.4}
@media(max-width:640px){
  .nr-collapse{padding:7px 10px;font-size:12px}
  .nr-runder{display:none}
  .nr-rmeta{font-size:12px}
  .nr-fnote{width:100%}
}

.nr-chips{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 9px}
.nr-chips .nr-chip{margin:0}
.nr-chip.lic{background:var(--nrgb);color:var(--nrg);border-color:#c9e9d8}
.nr-chip.unl{background:var(--nrub);color:var(--nru);border-color:#f7d6c2}
.nr-chip.lic.new{background:var(--nrg);color:#fff;border-color:var(--nrg)}

.nr-contact{display:flex;align-items:center;gap:8px;margin-top:10px}
.nr-tel{display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:800;color:var(--brand-deep);
  text-decoration:none;background:#f2f6fd;border:1px solid #dde6f6;border-radius:9px;padding:7px 12px;
  white-space:nowrap;min-width:0}
.nr-tel:hover{background:#e8effc}
.nr-tel .ico{font-size:13px}
.nr-text{background:#fff;border:1px solid #dde6f6;color:var(--brand-deep);font-size:13px;font-weight:800;
  padding:7px 15px;border-radius:9px;cursor:pointer;font-family:inherit;white-space:nowrap;transition:.15s;flex:none}
@media(max-width:430px){ .nr-tel{font-size:13.5px;padding:7px 10px} .nr-text{padding:7px 12px} }
.nr-text:hover{background:#f2f6fd}
.nr-text.ok{background:var(--nrg,#1a9e63);border-color:var(--nrg,#1a9e63);color:#fff}
</style>"""

RESKIN_JS = r"""<script>
(function(){
var ICO={
 dash:'<rect x="3" y="3" width="7" height="9" rx="1.5"/><rect x="14" y="3" width="7" height="5" rx="1.5"/><rect x="14" y="12" width="7" height="9" rx="1.5"/><rect x="3" y="16" width="7" height="5" rx="1.5"/>',
 rocket:'<path d="M12 3c3 2 4.5 6 4.5 9L14 14.5h-4L7.5 12C7.5 9 9 5 12 3z"/><path d="M9.6 14.6C7 15 6 17.5 6 20c2.5 0 5-1 5.4-3.4"/><circle cx="12" cy="9" r="1.4"/>',
 cap:'<path d="M12 4 2.5 8.5 12 13l9.5-4.5L12 4z"/><path d="M6.5 11v4.2c0 1.4 2.7 2.8 5.5 2.8s5.5-1.4 5.5-2.8V11"/><path d="M21.5 8.5v5"/>',
 briefcase:'<rect x="3" y="7.5" width="18" height="12.5" rx="2"/><path d="M8 7.5V6a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v1.5"/><path d="M3 12.5h18"/>',
 sliders:'<path d="M4 6h16"/><path d="M4 12h16"/><path d="M4 18h16"/><circle cx="9" cy="6" r="2.3"/><circle cx="15" cy="12" r="2.3"/><circle cx="8" cy="18" r="2.3"/>',
 calc:'<rect x="5" y="2.5" width="14" height="19" rx="2"/><rect x="8" y="5.5" width="8" height="3" rx="0.6"/><path d="M8.5 12.5h.01M12 12.5h.01M15.5 12.5h.01M8.5 16.5h.01M12 16.5h.01M15.5 16.5h.01"/>',
 users:'<circle cx="9" cy="8" r="3.3"/><path d="M3.5 19.5c0-3 2.5-5 5.5-5s5.5 2 5.5 5"/><path d="M16 5a3.3 3.3 0 0 1 0 6.4"/><path d="M18.5 19.5c0-2-.9-3.6-2.3-4.5"/>',
 book:'<path d="M12 6.5C10 4.8 6.5 4.5 3.5 5.3v13c3-.8 6.5-.5 8.5 1.2 2-1.7 5.5-2 8.5-1.2v-13C17.5 4.5 14 4.8 12 6.5z"/><path d="M12 6.5v13"/>',
 folder:'<path d="M3 7.5a2 2 0 0 1 2-2h3.8l2 2H19a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
 calendar:'<rect x="3.5" y="5" width="17" height="15.5" rx="2"/><path d="M3.5 9.5h17"/><path d="M8 3v4M16 3v4"/>',
 pin:'<path d="M12 21.5s6.5-5.7 6.5-11A6.5 6.5 0 0 0 5.5 10.5c0 5.3 6.5 11 6.5 11z"/><circle cx="12" cy="10.3" r="2.4"/>',
 chat:'<path d="M20.5 11.5a8 7.5 0 0 1-11 7L4 20.5l1.6-4.3A7.5 7.5 0 1 1 20.5 11.5z"/>',
 buoy:'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3.4"/><path d="M5.6 5.6 9.6 9.6M14.4 14.4l4 4M18.4 5.6 14.4 9.6M9.6 14.4l-4 4"/>',
 target:'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.4" fill="currentColor" stroke="none"/>',
 user:'<circle cx="12" cy="8" r="4"/><path d="M4.5 20.5c0-4 3.5-6 7.5-6s7.5 2 7.5 6"/>',
 pen:'<path d="M4 13.5V19a1 1 0 0 0 1 1h5.5"/><path d="M4 10V5a1 1 0 0 1 1-1h9"/><path d="M17.5 3.5 20.5 6.5 11 16l-4 1 1-4z"/>',
 laptop:'<rect x="4" y="5" width="16" height="10.5" rx="1.5"/><path d="M2 19.5h20"/>',
 shield:'<path d="M12 3.2 19 6v5c0 5-3.5 8.2-7 10-3.5-1.8-7-5-7-10V6z"/>',
 shieldc:'<path d="M12 3.2 19 6v5c0 5-3.5 8.2-7 10-3.5-1.8-7-5-7-10V6z"/><path d="M9 12l2 2 4-4"/>',
 bars:'<path d="M4 20h16"/><rect x="6" y="11" width="3" height="7" rx="0.6"/><rect x="10.5" y="7" width="3" height="11" rx="0.6"/><rect x="15" y="4" width="3" height="14" rx="0.6"/>',
 present:'<rect x="3" y="4" width="18" height="11" rx="1.5"/><path d="M12 15v4M9 21l3-2 3 2"/><path d="M7.5 11l2.5-2.5L13 11l3.5-4"/>',
 play:'<circle cx="12" cy="12" r="9"/><path d="M10 8.4 16 12l-6 3.6z" fill="currentColor" stroke="none"/>',
 file:'<path d="M6.5 2.5h7l4.5 4.5v14.5H6.5z"/><path d="M13.5 2.5V7h4.5"/><path d="M9 12.5h6M9 16.5h6"/>',
 award:'<circle cx="12" cy="9" r="5"/><path d="M9 13 8 22l4-2.2L16 22l-1-9"/>',
 dollar:'<path d="M12 2.5v19"/><path d="M16 6.5c0-2-2-2.7-4-2.7S8 4.5 8 7s2 3 4 3.5 4 1 4 3-2 2.7-4 2.7-4-.7-4-2.7"/>',
 login:'<path d="M14 3.5h4.5a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H14"/><path d="M10 16.5l4.5-4.5L10 7.5"/><path d="M14.5 12H3.5"/>',
 globe:'<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.6 2.6 2.6 15.4 0 18M12 3c-2.6 2.6-2.6 15.4 0 18"/>',
 monitor:'<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M9 20h6M12 16v4"/>',
 news:'<path d="M4 5.5h13v14H5.5a1.5 1.5 0 0 1-1.5-1.5z"/><path d="M17 8.5h3v9a2 2 0 0 1-2 2"/><path d="M7 9h7M7 12.5h7M7 16h4"/>',
 card:'<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8.5" cy="11" r="2.2"/><path d="M13.5 10h4.5M13.5 14h4.5"/>',
 clap:'<path d="M3.5 8.5h17v11a1 1 0 0 1-1 1H4.5a1 1 0 0 1-1-1z"/><path d="M3.8 8.5 5 4.6l3.8 1-1.2 3.9M8.8 5.6l3.9 1-1.2 3.9M12.8 6.6l3.9 1-1.2 3.9"/>',
 msg:'<path d="M4 5.5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H9.5l-4 4z"/>',
 phone:'<path d="M6.5 3.5 9 4l1 3.8L8.2 9.6a12 12 0 0 0 6.2 6.2l1.8-1.8 3.8 1 .5 2.5c0 1-1 2-2 2A16.5 16.5 0 0 1 4 5.5c0-1 1-2 2.5-2z"/>',
 clip:'<rect x="5" y="4" width="14" height="17" rx="2"/><rect x="9" y="2.5" width="6" height="4" rx="1.2"/><path d="M8.5 10.5h7M8.5 14h7M8.5 17.5h4"/>',
 mega:'<path d="M3.5 11v2a1 1 0 0 0 1 1h2l7.5 4V6L6.5 10h-2a1 1 0 0 0-1 1z"/><path d="M17 8.5a5 5 0 0 1 0 7"/>',
 ticket:'<path d="M3 8.5a1 1 0 0 1 1-1h16a1 1 0 0 1 1 1v2a2 2 0 0 0 0 3.8v2a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-2a2 2 0 0 0 0-3.8z"/>',
 headset:'<path d="M4.5 13v-1a7.5 7.5 0 0 1 15 0v1"/><rect x="3.5" y="12.5" width="4" height="6" rx="1.6"/><rect x="16.5" y="12.5" width="4" height="6" rx="1.6"/><path d="M19.5 18.5a4 4 0 0 1-4 3h-2"/>',
 wave:'<path d="M7 13.5V7a1.25 1.25 0 0 1 2.5 0v4.5"/><path d="M9.5 11V5.5a1.25 1.25 0 0 1 2.5 0V11"/><path d="M12 11V6a1.25 1.25 0 0 1 2.5 0v5.5"/><path d="M14.5 12V8a1.25 1.25 0 0 1 2.5 0v5.5c0 3.3-2.2 6-5.6 6-2.2 0-3.8-1-4.8-2.8l-1.7-3a1.25 1.25 0 0 1 2.2-1.2l1 1.6"/><path d="M17.8 4.2a4 4 0 0 1 1.2 2.6M19.8 2.6a6 6 0 0 1 1.7 3.9"/>',
 funnel:'<path d="M3 5h18l-7 8v5.5l-4 2.5V13z"/>',
 heart:'<path d="M12 20.3 4.2 12.5a4.6 4.6 0 0 1 6.5-6.5l1.3 1.3 1.3-1.3a4.6 4.6 0 0 1 6.5 6.5z"/>'
};
function m5CallIcon(n){n=(n||'').toLowerCase();
 if(n.indexOf('reading')>=0)return 'book';
 if(n.indexOf('dial')>=0)return 'phone';
 if(n.indexOf('vbo')>=0||n.indexOf('business overview')>=0)return 'present';
 if(n.indexOf('huddle')>=0)return 'users';
 if(n.indexOf('builders')>=0)return 'target';
 if(n.indexOf('winning')>=0)return 'award';
 if(n.indexOf('training')>=0)return 'cap';
 if(n.indexOf('srs')>=0||n.indexOf('annuity')>=0||n.indexOf('iul')>=0)return 'dollar';
 if(n.indexOf('coaching')>=0||n.indexOf('shawn')>=0)return 'award';
 if(n.indexOf('orientation')>=0)return 'rocket';
 if(n.indexOf('call')>=0)return 'phone';
 return 'calendar';
}
function m5icon(n){var i=ICO[n]||ICO.folder;return '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+i+'</svg>';}
var NAVICO={dashboard:'dash',faststart:'rocket',academy:'cap',sales:'briefcase',systools:'sliders',goalcard:'bars',leads:'funnel',calc:'calc',recruiting:'users',selfdev:'book',resources:'folder',income:'dollar',activity:'phone',agencybuild:'users',health:'heart',virtual:'calendar',inperson:'pin',support:'chat',gethelp:'buoy',kpi:'target',profile:'user'};
var NAVGOLD={dashboard:1,faststart:1,academy:1,sales:1,calc:1,resources:1,kpi:1};
var TITLEICO=[['sales scripts','pen'],['electronic app','laptop'],['carrier portal','shield'],['continuing education','cap'],['presentation material','bars'],['sales presentation','present'],['training video','play'],['guides & pdf','file'],['guides and pdf','file'],['va benefit','award'],['agent compensation','dollar'],['gateway','login'],['the hub','globe'],['crm center','monitor'],['crm login','monitor'],['integrityconnect','shieldc'],['integrity connect','shieldc'],['newsletter','news'],['business card','card'],['fast start playbook','clap'],['objection handling','msg'],['product & carrier','file'],['product and carrier','file'],['presentation walk','present'],['power dialer','phone'],['quoting engine','calc'],['lead order','clip'],['share ffl','mega'],['vbo','present'],['webinar','present'],['enroll a new hire','users'],['recruiting resource','file'],['recruiter playbook','clap'],['talk track','msg'],['why recruit','users'],['recruit','users'],['compensation','dollar'],['register your number','phone'],['more pickups','phone'],['adding other state','award'],['state license','award'],['leaderboard','bars'],['contact for help','headset'],['recordings','clap'],['weekly schedule','calendar'],['agency in goat','users'],['where you buy leads','clip'],['lead strategy','target'],['the winning system','award'],['message your upline','msg'],['ask the optimum','chat'],['message jesse','chat'],['whatsapp','chat'],['reduce spam','phone'],['more pickups','phone'],['other state license','award'],['contact support','headset'],['faq','book'],['submit a ticket','ticket'],['scripts','pen']];
function icoForTitle(t){t=(t||'').toLowerCase();for(var i=0;i<TITLEICO.length;i++){if(t.indexOf(TITLEICO[i][0])>=0)return TITLEICO[i][1];}return 'folder';}
var _mo=null;
function m5Reskin(){
  if(_mo)_mo.disconnect();
  try{ if(typeof m5CertMount==='function') m5CertMount(); }catch(e){}
  try{
    document.querySelectorAll('.navitem[data-view]').forEach(function(n){
      if(n.getAttribute('data-m5ico'))return;
      var v=n.getAttribute('data-view');var ic=n.querySelector('.ic');if(!ic)return;
      ic.innerHTML=m5icon(NAVICO[v]||'folder');
      n.classList.add(NAVGOLD[v]?'m5-ig':'m5-iw');
      n.setAttribute('data-m5ico','1');
    });
    document.querySelectorAll('.navitem.m5-logout').forEach(function(n){
      if(n.getAttribute('data-m5ico'))return;var ic=n.querySelector('.ic');if(ic)ic.innerHTML=m5icon('login');n.setAttribute('data-m5ico','1');
    });
    var av=document.getElementById('m5-suav');
    if(av){var f=((store&&store.data&&store.data.first)||'A');var l=((store&&store.data&&store.data.last)||'');av.textContent=((f.charAt(0)||'A')+(l.charAt(0)||'')).toUpperCase();}
    document.querySelectorAll('.tool').forEach(function(t){
      if(t.getAttribute('data-m5ico'))return;
      var tic=t.querySelector('.tic');var tt=t.querySelector('.tt');
      if(tic&&tt){tic.innerHTML=m5icon(icoForTitle(tt.textContent));tic.classList.add('m5-chip');}
      t.setAttribute('data-m5ico','1');
    });
    document.querySelectorAll('.m5-row').forEach(function(r){
      if(r.getAttribute('data-m5ico'))return;
      var ri=r.querySelector('.ri');var rl=r.querySelector('.rl');
      if(ri&&rl){ri.innerHTML=m5icon(icoForTitle(rl.textContent));ri.classList.add('m5-chip');}
      r.setAttribute('data-m5ico','1');
    });
    document.querySelectorAll('[data-ico]').forEach(function(el){
      if(el.getAttribute('data-m5ico'))return;
      el.innerHTML=m5icon(el.getAttribute('data-ico'));el.setAttribute('data-m5ico','1');
    });
  }catch(e){}
  if(_mo)_mo.observe(document.body,{childList:true,subtree:true});
}
/* ---- Recruiting + General Support -> same row style as Systems/Tools ---- */
function m5PairRows(rows){return rows.map(function(r){
  var l=(r[0]||'').replace(/^[^A-Za-z0-9(]+/,'');
  var s=r[1]||'';var o={l:l};
  if(/^https?:/i.test(s)){o.url=s;}
  else if(/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(s)){o.url='mailto:'+s;o.d=s;}
  else if(s){o.d=s;}
  return o;
});}
/* ---- Personal recruiting link (ref code comes from login lookup) ---- */
window.m5MyRefCode=function(){ return (typeof store!=='undefined'&&store.data&&store.data.refCode)||''; }
window.m5MyRegLink=function(){ var c=m5MyRefCode(); return 'https://portal.ffloptimum.com/register.html'+(c?('?ref='+c):''); }
window.m5CopyMyLink=function(btn){ var i=document.getElementById('m5-reglink'); if(!i)return; try{ i.select(); }catch(e){} try{ navigator.clipboard.writeText(i.value); }catch(e){} if(btn){ var o=btn.textContent; btn.textContent='Copied ✓'; setTimeout(function(){ btn.textContent=o; }, 1500); } }
window.m5RecruitLinkCard=function(){
  var link=m5MyRegLink(), code=m5MyRefCode();
  var body = code
    ? '<div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap"><input id="m5-reglink" readonly value="'+link+'" onclick="this.select()" style="flex:1;min-width:210px;font-size:13px;padding:10px 12px;border:1px solid #dbe3f0;border-radius:9px;background:#f7f9fc;color:#16233f;font-family:inherit"><button onclick="m5CopyMyLink(this)" style="background:#16233f;color:#fff;border:0;border-radius:9px;padding:10px 18px;font-weight:700;font-size:13px;cursor:pointer;white-space:nowrap">Copy link</button></div>'
    : '<div style="font-size:12.5px;color:#8a93a9">Your link will appear here once your account syncs — log out and back in if you do not see it.</div>';
  return '<div style="background:#fff;border:1px solid #e3e8f2;border-left:4px solid #c9a227;border-radius:14px;padding:16px 18px;margin-top:14px;box-shadow:0 6px 20px rgba(20,35,63,.05)">'+
    '<div style="font-size:12px;font-weight:800;color:#a9861d;text-transform:uppercase;letter-spacing:.05em">Your personal recruiting link</div>'+
    '<p style="font-size:12.5px;color:#55617d;margin:6px 0 12px;line-height:1.5">Send this to anyone you bring onto your team. When they register through your link, they are automatically placed on your team in the Optimum Portal. You still need to follow the rest of the FFL enrollment steps on the recruiting page.</p>'+
    body+'</div>';
}
/* ---- NPN capture: persistent banner for licensed agents missing an NPN ---- */
window.m5PostPromote=function(){
  try{
    if(typeof BACKEND_URL==='undefined'||!BACKEND_URL) return;
    var email=((store.data&&store.data.email)||'').trim().toLowerCase();
    var phone=(store.data&&store.data.phone)||'';
    if(!email&&!phone) return;
    fetch(BACKEND_URL,{method:'POST',body:JSON.stringify({action:'promote',email:email,phone:phone})}).catch(function(){});
  }catch(e){}
}
window.m5NeedsNpn=function(){ return (typeof store!=='undefined'&&store.data&&store.data.status==='licensed'&&store.data.hasNPN===false); }
window.m5NpnBanner=function(){
  if(!m5NeedsNpn()) return '';
  return '<div id="m5-npnbanner" style="background:#fff;border:1px solid #e7d9a8;border-left:5px solid #c9a227;border-radius:14px;padding:18px 20px;margin:0 0 20px;box-shadow:0 8px 24px rgba(201,162,39,.12)">'+
    '<div style="display:flex;align-items:center;gap:9px;margin-bottom:4px"><span style="font-size:20px">📋</span>'+
      '<span style="font-size:15px;font-weight:800;color:#16233f">Complete your NPN</span>'+
      '<span style="font-size:11px;font-weight:800;color:#a9861d;background:#fbf4dd;padding:3px 9px;border-radius:999px;text-transform:uppercase;letter-spacing:.04em">Required</span></div>'+
    '<p style="font-size:13px;color:#55617d;margin:2px 0 13px;line-height:1.55">Enter your <b>NPN</b> (National Producer Number) — this is <b>not</b> your state license number. It is the number FFL and your carriers use to appoint you. Once you save it, this box goes away.</p>'+
    '<div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap">'+
      '<input id="m5-npn-in" inputmode="numeric" autocomplete="off" placeholder="Your NPN (numbers only)" onkeydown="if(event.key===\'Enter\')m5SaveNpn(document.getElementById(\'m5-npn-save\'))" style="flex:1;min-width:190px;font-size:14px;padding:11px 13px;border:1px solid #dbe3f0;border-radius:9px;background:#f7f9fc;color:#16233f;font-family:inherit">'+
      '<button id="m5-npn-save" onclick="m5SaveNpn(this)" style="background:#c9a227;color:#16233f;border:0;border-radius:9px;padding:11px 22px;font-weight:800;font-size:14px;cursor:pointer;white-space:nowrap">Save NPN</button></div>'+
    '<div id="m5-npn-msg" style="font-size:12.5px;margin-top:9px;display:none"></div>'+
    '</div>';
}
window.m5SaveNpn=function(btn){
  var inp=document.getElementById('m5-npn-in'); if(!inp) return;
  var v=(inp.value||'').replace(/\D/g,'');
  var msg=document.getElementById('m5-npn-msg');
  function showMsg(t,c){ if(msg){ msg.textContent=t; msg.style.color=c||'#c0392b'; msg.style.display='block'; } }
  if(v.length<4||v.length>12){ showMsg('Please enter a valid NPN — numbers only, no dashes or letters.'); return; }
  if(typeof BACKEND_URL==='undefined'||!BACKEND_URL){ showMsg('Cannot reach the server right now — please try again shortly.'); return; }
  if(btn){ btn.disabled=true; btn._o=btn.textContent; btn.textContent='Saving…'; }
  var email=((store.data&&store.data.email)||'').trim().toLowerCase();
  var phone=(store.data&&store.data.phone)||'';
  fetch(BACKEND_URL,{method:'POST',body:JSON.stringify({action:'npn',email:email,phone:phone,npn:v})})
    .then(function(r){return r.json();})
    .then(function(j){
      if(j&&j.ok){
        store.data.npn=v; store.data.hasNPN=true; if(store.save)store.save();
        m5NpnSavedFlow(v,(j.recruiter)||null);
      } else { showMsg('Could not save your NPN — please try again.'); if(btn){btn.disabled=false;btn.textContent=btn._o||'Save NPN';} }
    })
    .catch(function(){ showMsg('Network issue — please try again.'); if(btn){btn.disabled=false;btn.textContent=btn._o||'Save NPN';} });
}
var m5_npnMsg='';
window.m5NpnSavedFlow=function(npn,rec){
  var b=document.getElementById('m5-npnbanner'); if(!b) return;
  var recFirst=(rec&&rec.first)?(''+rec.first).trim():'';
  var recPhone=((rec&&rec.phone)?(''+rec.phone):'').replace(/\D/g,'');
  var name=((store.data.first||'')+' '+(store.data.last||'')).trim();
  m5_npnMsg='Hi'+(recFirst?(' '+recFirst):'')+', I just got my NPN — it\'s '+npn+'. This is '+(name||'your new agent')+'. Can you add it to my file? Thank you!';
  var smsBtn = recPhone ? '<a href="sms:'+recPhone+'&body='+encodeURIComponent(m5_npnMsg)+'" style="display:inline-flex;align-items:center;gap:6px;background:#16233f;color:#fff;text-decoration:none;border-radius:9px;padding:11px 18px;font-weight:800;font-size:13.5px;white-space:nowrap">💬 Text my recruiter</a>' : '';
  var copyBtn='<button onclick="m5CopyNpnMsg(this)" style="background:#eef2fa;color:#16233f;border:0;border-radius:9px;padding:11px 18px;font-weight:800;font-size:13.5px;cursor:pointer;white-space:nowrap">Copy message</button>';
  b.style.borderLeftColor='#1f9d55'; b.style.borderColor='#bfe3cd';
  b.innerHTML='<div style="display:flex;align-items:center;gap:9px;margin-bottom:4px"><span style="font-size:20px">✅</span>'+
      '<span style="font-size:15px;font-weight:800;color:#16233f">NPN saved — nice work!</span></div>'+
    '<p style="font-size:13px;color:#55617d;margin:2px 0 13px;line-height:1.55">Your NPN <b>'+npn+'</b> is on file. One last thing: let your recruiter'+(recFirst?(' ('+recFirst+')'):'')+' know so they can update your records. Tap below to send it.</p>'+
    '<div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap">'+smsBtn+copyBtn+
      '<button onclick="m5DismissNpn()" style="background:transparent;color:#8a93a9;border:0;padding:11px 8px;font-weight:700;font-size:13px;cursor:pointer">Done</button></div>';
}
window.m5CopyNpnMsg=function(btn){ try{ navigator.clipboard.writeText(m5_npnMsg); }catch(e){} if(btn){ var o=btn.textContent; btn.textContent='Copied ✓'; setTimeout(function(){ btn.textContent=o; },1500); } }
window.m5DismissNpn=function(){ if(typeof render==='function'&&typeof currentView==='function') render(currentView()); }
try{
  if(typeof m5RowList==='function'){
    window.vRecruiting=function(){
      var topItems=[
        {l:'Share FFL — Invite App',d:'Send the opportunity to a prospect in seconds.',url:'https://jdawg2you.github.io/Share-FFL/shareffl.html'},
        {l:'Why recruit from day one',d:'The mindset and philosophy — straight from the Academy.',onclick:"acadGoLes('build-your-future','5-2')"},
        {l:'Recruiting Playbook',d:'Your go-to recruiting resource.',soon:true},
        {l:'Your VBO recruiting webinar',d:'The automated business-overview webinar system.',url:'https://www.fflvbo.com/join.html'}
      ];
      var COMP=[
        ['General Compensation','https://drive.google.com/file/d/1w4ZNu10uKH44yC1GrD1FdjguYJLCA7Mx/view'],
        ['Compensation by Product','https://drive.google.com/file/d/1rOQUezUVaQjtXhfHZTxtYbyJPvaytOhK/view'],
        ['Annuity & IUL Compensation','https://drive.google.com/file/d/1xVpb9OhZfa5RskUW1ib6iNiH5LGFHwPF/view'],
        ['Producer Bonus','https://drive.google.com/file/d/1QMbjz2HpePURBVBD432q9m49zG0coSGW/view'],
        ['VP Bonus','https://docs.google.com/document/d/1A7sNIR98B9WGF6sUNwAStIbYBAvj2yFckOmq0ZToPcw/edit']
      ];
      var compRows=COMP.map(function(c){return '<a class="m5-comprow" href="'+c[1]+'" target="_blank" rel="noopener"><span class="m5-cdot" data-ico="dollar"></span><span class="m5-clbl">'+c[0]+'</span><span class="m5-carr">↗</span></a>';}).join('');
      var comp='<div class="m5-expand" id="m5-comp">'+
        '<div class="m5-exhead" onclick="m5ToggleExpand(this)"><span class="m5-exchip" data-ico="dollar"></span>'+
          '<span class="m5-extext"><span class="m5-exname">Compensation documents</span><span class="m5-exsub">General, by product, IUL/annuity, producer &amp; VP bonus — tap to open.</span></span>'+
          '<span class="m5-exchev">›</span></div>'+
        '<div class="m5-exbody"><div class="m5-complist">'+compRows+'</div></div></div>';
      var PORTAL=m5MyRegLink();
      var link='<a href="'+PORTAL+'" target="_blank" rel="noopener">'+PORTAL+'</a>';
      var _sfirst=(store.data.first||'').trim(), _slast=(store.data.last||'').trim();
      var _sname=(_sfirst+' '+_slast).trim();
      var _sphone=(((store.data.phone)||(typeof m5CurrentUser!=='undefined'&&m5CurrentUser.phone)||'')+'').trim();
      var _semail=(((store.data.email)||(typeof m5CurrentUser!=='undefined'&&m5CurrentUser.email)||'')+'').trim();
      var sig=(_sname||'[Your name]');
      if(_sphone) sig+='<br>'+_sphone;
      if(_semail) sig+='<br>'+_semail;
      var msgUnlic='Welcome to the team! First, save my contact info so you can always reach me.<br><br>'+
        'Click your personal registration link below to get registered and into our team portal — your home base for everything. Right now your focus is getting <b>licensed within 2 weeks</b>!<br><br>'+link+'<br><br>'+
        'Please let me know if you have any questions along the way. Again, congratulations — I\'m excited to have you on the team. Let\'s go!!!!<br>'+sig;
      var msgLic='Welcome to the team! First, save my contact info so you can always reach me.<br><br>'+
        'Click your personal registration link below to get registered and into our team portal — your home base for everything. Right now your focus is getting <b>contracted and appointed with our carriers as quickly as possible</b>, and beginning your initial training.<br><br>'+link+'<br><br>'+
        'Please let me know if you have any questions along the way. Again, congratulations — I\'m excited to have you on the team. Let\'s go!!!!<br>'+sig;
      var ex='<div class="m5-expand" id="m5-enroll">'+
        '<div class="m5-exhead" onclick="m5ToggleExpand(this)"><span class="m5-exchip" data-ico="users"></span>'+
          '<span class="m5-extext"><span class="m5-exname">How to enroll your new hire</span><span class="m5-exsub">Welcome them, set expectations, then add them to the system — tap to open.</span></span>'+
          '<span class="m5-exchev">›</span></div>'+
        '<div class="m5-exbody">'+
          '<div class="m5-estep"><div class="m5-estep-h"><span class="m5-estep-n">1</span>Welcome your new hire &amp; set expectations</div>'+
            '<p>The moment someone joins, reach out and welcome them. Copy the message that matches your new hire — it\'s already signed with your name, phone, and email — paste it into a text or email and send it. Each message points them to the onboarding portal — their home base.</p>'+
            '<div class="m5-msgcard"><div class="m5-msgcard-h"><span class="m5-msgcard-t">New Unlicensed Agent</span><button class="m5-copybtn" onclick="m5CopyMsg(\'m5-msg-unlic\',this)"><span data-ico="clip"></span> Copy</button></div>'+
              '<div class="m5-msgbody" id="m5-msg-unlic">'+msgUnlic+'</div></div>'+
            '<p class="m5-fine"><b>Then set expectations:</b> get their state exam scheduled ASAP, the course done and passed within 1–2 weeks, and have them connect with you every few days.</p>'+
            '<div class="m5-msgcard"><div class="m5-msgcard-h"><span class="m5-msgcard-t">New Licensed Agent</span><button class="m5-copybtn" onclick="m5CopyMsg(\'m5-msg-lic\',this)"><span data-ico="clip"></span> Copy</button></div>'+
              '<div class="m5-msgbody" id="m5-msg-lic">'+msgLic+'</div></div>'+
            '<p class="m5-fine"><b>Then set expectations:</b> get their onboarding Zoom scheduled within 24 hours (with you or an upline mentor), introduce their mentor ASAP, and on the Zoom walk through the onboarding-Zoom drop-down from the Licensed Agents page.</p>'+
          '</div>'+
          '<div class="m5-estep"><div class="m5-estep-h"><span class="m5-estep-n">2</span>Enroll them on the Family First Life system</div>'+
            '<p>Head to the <b>Family First Life (National) Join</b> page and follow these steps:</p>'+
            '<ol><li><b>Add New Hire</b></li>'+
              '<li>Password: <b>4321</b></li>'+
              '<li>Select the right path — if <b>unlicensed</b>, enroll them in the course; if <b>licensed</b>, select that option.</li>'+
              '<li>Agency: <b>FFL Optimum Financial Solutions</b></li>'+
              '<li>Compensation rate for all starting agents: <b>80%</b></li>'+
              '<li>Upline: <b>you</b></li>'+
              '<li>Recruiter: <b>"Agent"</b></li>'+
              '<li>Lead Source: usually <b>"Warm Market"</b></li></ol>'+
            '<p class="m5-fine"><b>Have their info ready before you start.</b> You\'ll need your new agent\'s proper name, phone number, email address, and mailing address. If they\'re a <b>licensed agent</b>, you\'ll also need their <b>National Producer Number (NPN)</b>.</p>'+
          '</div>'+
          '<div class="m5-enrollbtn-wrap"><p class="m5-fine" style="margin:0 0 9px;text-align:center">Click the link below to enroll your new hire:</p><a class="m5-enrollbtn" href="https://www.joinfflnational.com/" target="_blank" rel="noopener"><span data-ico="rocket"></span> Enroll your new hire</a></div>'+
        '</div></div>';
      var qrCard='<div style="background:#fff;border:1px solid #e3e8f2;border-radius:14px;padding:14px 16px;margin-top:10px;box-shadow:0 6px 20px rgba(20,35,63,.05);display:flex;align-items:center;gap:15px;flex-wrap:wrap">'+
        '<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKCAIAAAD0S4FSAAAFs0lEQVR4nO3dwY0bORBAUY/hHJyAA3HoG8gm4Ci01z0RhmlOsb/eu6vV4swHLwXy4/V6fQGKvk6/AHCKvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWd+mvvj7j59TX33Ir3//+ePPPnE1dn7v2hNXY+3cWq3ZvSFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IWtsam1taspnbWeaauezd67GlDtX485JO7s3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkXTq1tnZuQmhqImr9vevfO/XZtamV7P1v7LB7Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlD1iOn1vh9UzNtO0/mb7F7Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlDlqm1T7Izp3VuxuvOc9r4W+zekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96Q9ciptXc7qevdbvnc8cR3PsfuDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWZdOrfVO6rrzxsxzZ62d0/vfOMfuDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWR+v12v6Hd7C1KzVudmyO2fa+D+7N2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZI2dtfbEmadz79w7t+zck3fW6s63OsfuDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWZeetbYzXdSbADtn54bQnSfvuHOdTa0Bn0rekCVvyJI3ZMkbsuQNWfKGLHlDlrwh69KptbVz01RTZ3FN/aI7V2PHnf8bUzNtdm/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8gam1qbOjFral5q6l7LO+/T3HHuF9355B12b8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyHrkWWtr7zZrtePOGb4nnmpmag34VPKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z36a+eGoy6YlTTVPvvHZuLm3q3tK1O+fS1uzekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QdekNoXfOLZ1z50ls76Z3ApzdG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbssbOWjvn3ClfU6bmpZ54mtrOk3uTlHZvyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/ICk6tnTM1xXXOnbdtnnty7zS1Nbs3ZMkbsuQNWfKGLHlDlrwhS96QJW/Ikjdkjd0Q+m6mptbOfe+dM153TgdOsXtDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUPW2Flrd96ouGM9ETV1v+S5Oa1zv+iJk2d3vrPdG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsi69IfSJk0nnnDsRbeqstbUn/vXvfGe7N2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZF06tbb2bvNS50zN4d150l7vfDi7N2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZD1yau3d7ExEnbvHc+fJ5z67Y+oW13Ps3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekGVq7QHunDw759xcWm+t1uzekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96Q9cipNfd4/r6dtZqaHpua0uuxe0OWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q9alU2t3nly1Y2rW6txKTk2AnVuN3kyb3Ruy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7I+Xq/X9DsAR9i9IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oas/wAiGW64W9+4JQAAAABJRU5ErkJggg==" alt="Scan to open the Share FFL app" width="112" height="112" style="width:112px;height:112px;border:1px solid #e3e8f2;border-radius:10px;padding:6px;background:#fff;flex:0 0 auto">'+
        '<div style="font-size:13px;color:#55617d;line-height:1.55;flex:1;min-width:190px"><b style="color:#16233f">On your computer?</b> Scan this QR code with your phone to open the Share FFL app — or type the link below onto your phone:<br><a href="https://bit.ly/shareffl" target="_blank" rel="noopener" style="color:#2a56d6;font-weight:700">bit.ly/shareffl</a></div>'+
      '</div>';
      return '<h1 class="page">Recruiting</h1><p class="sub">Build your team — resources, webinar system, and comp.</p>'+
        m5RowList([topItems[0]])+qrCard+m5RowList(topItems.slice(1))+
        '<div class="m5-seclabel" style="margin-top:26px">Bringing on a new agent</div>'+m5RecruitLinkCard()+ex+
        '<div class="m5-previewcard"><div class="m5-pvtitle"><span class="m5-pvi" data-ico="user"></span>See it from their side</div>'+
          '<p class="m5-pvsub">Preview exactly what your new agent sees before they\'re licensed — the full pre-licensing experience. Nothing you do here is saved or tracked.</p>'+
          '<button class="m5-pvbtn" onclick="m5EnterPreview()">Preview the unlicensed agent experience &rarr;</button></div>'+
        '<div class="m5-seclabel" style="margin-top:26px">Compensation</div>'+comp;
    };
  }
  if(typeof m5RowList==='function'){
    window.vSelfDev=function(){
      var bookCards=(typeof BOOKS!=='undefined'?BOOKS:[]).map(function(b){
        return '<div class="bookcard"><div class="bookcover">'+(typeof m5BookCover==='function'?m5BookCover(b.t):'')+'</div><div class="bookinfo"><div class="booktitle">'+b.t+(b.by?' <span style="font-weight:500;color:var(--ink-soft)">· '+b.by+'</span>':'')+'</div><div class="bookblurb">'+(b.blurb||'')+'</div><div class="bookbtns">'+(b.pdf?'<button class="openbtn" onclick="window.open(\''+b.pdf+'\',\'_blank\')">PDF &amp; ePub</button>':'')+(b.wb?'<button class="openbtn" onclick="window.open(\''+b.wb+'\',\'_blank\')">PDF Workbook</button>':'')+'<button class="openbtn" onclick="toast(\'Opening Amazon…\')">Amazon</button></div></div></div>';
      }).join('');
      var listenItems=[
        {l:'Jim Rohn — Building Your Network Marketing Business',d:'Classic audio on building the business.'},
        {l:'Charisma on Command (YouTube)',d:'Presence, connection &amp; communication.',url:'https://www.youtube.com/@Charismaoncommand'}
      ];
      function acc(ico,name,sub,body){
        return '<div class="m5-expand"><div class="m5-exhead" onclick="m5ToggleExpand(this)"><span class="m5-exchip" data-ico="'+ico+'"></span><span class="m5-extext"><span class="m5-exname">'+name+'</span><span class="m5-exsub">'+sub+'</span></span><span class="m5-exchev">›</span></div><div class="m5-exbody">'+body+'</div></div>';
      }
      function accSoon(ico,name,sub){
        return '<div class="m5-expand m5-expand-soon"><div class="m5-exhead" onclick="toast(\'Coming soon.\')"><span class="m5-exchip" data-ico="'+ico+'"></span><span class="m5-extext"><span class="m5-exname">'+name+'</span><span class="m5-exsub">'+sub+'</span></span><span class="m5-soonpill">Coming soon</span></div></div>';
      }
      var FFLVIDEOS=[]; /* add {l:'Title',d:'note',url:'https://youtu.be/...'} items here as Jesse sends them */
      var vidLib = FFLVIDEOS.length
        ? acc('play','Family First Life Video Library','Our curated FFL training &amp; talks.',m5RowList(FFLVIDEOS))
        : accSoon('play','Family First Life Video Library','Curated FFL videos — coming soon.');
      var browse=
        acc('book','Books to Read','The reads top producers keep coming back to.','<div style="padding:2px 2px 0">'+bookCards+'</div>')+
        acc('headset','Things to Listen To','Podcasts, talks &amp; audio for the drive.',m5RowList(listenItems))+
        accSoon('play','Videos on Mindset &amp; Motivation','Short hits to reset your head — coming soon.')+
        vidLib;
      return '<h1 class="page">Self Development</h1><p class="sub">Books, listens, and videos the top producers use.</p>'+
        (typeof m5SearchBox==='function'?m5SearchBox('selfdev'):'')+
        '<div id="m5s-selfdev-results"></div><div id="m5s-selfdev-browse">'+browse+'</div>';
    };
  }
  if(typeof m5RowList==='function'){
    window.vSupport=function(){
      var items=[
        {l:'Register your numbers (reduce spam)',d:'How-to guide.',url:'https://docs.google.com/document/d/1Wu5M_mymae8s7S7SO-KrL3pWePNrRj6WjtERPUPWC0s/edit?tab=t.0'},
        {l:'Adding other state licenses',d:'Loom walkthrough.',url:'https://www.loom.com/share/5c9253a5d2ef4f3c82079d0c75bc4a2c'},
        {l:'Posting to the leaderboard',d:'How-to guide.',url:'https://docs.google.com/document/d/1rl5YRBlO0d2yrt93Vig2Wmc02wWkipqe0c40N48BOpE/edit'}
      ];
      return '<h1 class="page">General Support</h1><p class="sub">Quick how-tos and help — the miscellaneous stuff lives here.</p>'+m5RowList(items);
    };
  }
  if(typeof DAILY!=='undefined'&&typeof WEEK!=='undefined'){
    var m5vcall=function(e,day){var _idx=m5calReg(e,(day==null?null:day));var _cal=_idx>=0?'<button class="m5-crcal" onclick="m5AddCal('+_idx+')">＋ Calendar</button>':'';return '<div class="m5-callrow"><span class="m5-crchip">'+m5icon(m5CallIcon(e.n))+'</span><span class="m5-crtext"><span class="m5-crname">'+e.n+'</span><span class="m5-crtime">'+e.t+(e.note?' · '+e.note:'')+'</span></span><span class="m5-crbtns"><button class="m5-crjoin" onclick="window.open(\''+e.link+'\',\'_blank\')">Join</button>'+_cal+'</span></div>';};
    // Day-of-week anchored to Eastern time (the schedule is EST), so "Today"
    // is correct no matter what timezone the agent's phone/computer is set to.
    var m5ETParts=function(){
      try{
        var f=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'long',month:'long',day:'numeric'});
        var parts={}; f.formatToParts(new Date()).forEach(function(p){parts[p.type]=p.value;});
        var idx=DAYNAMES.indexOf(parts.weekday);
        return {day:(idx<0?new Date().getDay():idx), label:parts.weekday+', '+parts.month+' '+parts.day};
      }catch(e){
        var d=new Date().getDay(); return {day:d, label:DAYNAMES[d]};
      }
    };
    window.vVirtual=function(){
      window.m5CAL=[];
      var _et=m5ETParts(); var today=_et.day;
      var h='<h1 class="page">Virtual Calls/Events</h1><p class="sub">Today\'s calls, upcoming events, your full weekly schedule, and recordings — all in one place (all times ET).</p>';
      var _liveDials=null; for(var _i=0;_i<DAILY.length;_i++){ if(/live dials/i.test(DAILY[_i].n)){_liveDials=DAILY[_i];break;} }
      var _todayCalls=(WEEK[today]||[]);
      // 1) TODAY
      h+='<div class="m5-callsec m5-todaysec"><div class="m5-callsec-h m5-todayhd">Today · '+_et.label+' <span class="m5-etpill">Eastern</span></div>';
      if(_todayCalls.length){
        h+='<div class="m5-todaynote">You have '+_todayCalls.length+' scheduled team call'+(_todayCalls.length>1?'s':'')+' today, plus the everyday calls.</div>';
        h+=_todayCalls.map(function(e){return m5vcall(e,today);}).join('');
      }else{
        h+='<div class="m5-todaynote m5-restday">No scheduled <b>team</b> calls today'+(today===0?' — enjoy your Sunday!':'.')+' '+(_liveDials?'Live Dials still run, and your':'Your')+' everyday calls below run daily.</div>';
        if(_liveDials){ h+=m5vcall(_liveDials,null); }
      }
      h+='</div>';
      // 2) NEXT EVENT — Ignyte hero
      var _ig=(typeof imgData==='function'&&imgData('ignyte'))?imgData('ignyte'):'';
      h+='<div class="m5-evseclabel">Next Event</div>';
      h+='<div class="m5-evhero"'+(_ig?' style="background-image:url('+_ig+')"':'')+'><div class="m5-evhero-in">'+
        '<span class="m5-evbadge">Upcoming Event</span>'+
        '<div class="m5-evtitle">Ignyte Fall 2026 Sales Conference</div>'+
        '<div class="m5-evmeta">Thursday, September 10, 2026</div>'+
        '<div class="m5-cd" id="m5-cd-ignyte"></div>'+
        '<div class="m5-evbtns"><button class="m5-evbtn reg" onclick="window.open(\'https://www.eventbrite.com/e/ignyte-fall-2026-sales-conference-tickets-1990889795973\',\'_blank\')">🎟 Register Now</button>'+
        '<button class="m5-evbtn cal" onclick="m5AddIgnyte()">📅 Add to Calendar</button></div>'+
        '</div></div>';
      // 3) EVERY DAY
      h+='<div class="m5-callsec"><div class="m5-callsec-h">Every Day</div>'+DAILY.map(function(e){return m5vcall(e,null);}).join('')+'</div>';
      // 4) WEEKLY SCHEDULE
      h+='<div class="m5-daygrid">';
      [1,2,3,4,5,6,0].forEach(function(d){
        var evs=WEEK[d]||[];
        var body=evs.length?evs.map(function(e){return m5vcall(e,d);}).join('')
                 :(d===0&&_liveDials?m5vcall(_liveDials,null)+'<div class="m5-dayempty">No scheduled team calls — Live Dials run daily.</div>'
                                    :'<div class="m5-dayempty">Daily calls only.</div>');
        h+='<div class="m5-daycard'+(d===today?' today':'')+'"><div class="m5-daycard-h">'+DAYNAMES[d]+(d===today?'<span class="m5-todaypill">Today</span>':'')+'</div>'+body+'</div>';
      });
      h+='</div>';
      // 5) ANNUAL CONVENTION hero
      var _cv=(typeof imgData==='function'&&imgData('convention'))?imgData('convention'):'';
      h+='<div class="m5-evseclabel">Annual Convention</div>';
      h+='<div class="m5-evhero conv"'+(_cv?' style="background-image:url('+_cv+')"':'')+'><div class="m5-evhero-in">'+
        '<span class="m5-evbadge gold">Save the Date</span>'+
        '<div class="m5-evtitle">2027 FFL Annual Convention</div>'+
        '<div class="m5-evmeta">January 27–30, 2027 · Irving, Texas</div>'+
        '<div class="m5-cd" id="m5-cd-conv"></div>'+
        '<div class="m5-evbtns"><button class="m5-evbtn reg" onclick="window.open(\'https://familyfirstlife.com/annualconvention/\',\'_blank\')">🎟 Register Now</button>'+
        '<button class="m5-evbtn cal" onclick="m5AddConvention()">📅 Add to Calendar</button></div>'+
        '</div></div>';
      // 6) SCHEDULE SNAPSHOT
      if(typeof imgData==='function'&&imgData('schedule')){
        h+='<div class="m5-callsec-h" style="padding-left:2px;margin-top:6px">Weekly schedule — save it &amp; keep it handy</div>';
        h+='<div class="listcard" style="text-align:center"><img src="'+imgData('schedule')+'" style="width:100%;border-radius:12px;border:1px solid var(--line);box-shadow:var(--shadow);display:block" alt="FFL Success Zone Weekly Training Schedule"><div style="margin-top:10px"><button class="openbtn" onclick="dlImg(\'schedule\',\'weekly-training-schedule.jpg\')">⬇ Download the schedule</button></div></div>';
      }
      // 7) RECORDINGS
      h+='<div class="m5-callsec" style="margin-top:18px"><div class="m5-callsec-h">Call Recordings &amp; Repository</div>'+m5RowList(m5PairRows(REC))+'</div>';
      // 8) BOTTOM TRIO — Shawn + Reading + VBO
      h+='<div class="m5-evseclabel">Coaching &amp; Daily Shares</div><div class="m5-trio">';
      if(typeof IMG_SHAWN!=='undefined'){
        h+='<div class="m5-tcard"><img src="'+IMG_SHAWN+'" alt="Shawn Meaike Coaching Program"><div class="m5-tcard-b"><div class="m5-tcard-t">Shawn Meaike Coaching</div><div class="m5-tcard-d">Exclusive coaching — Fridays 12 PM ET.</div><button class="btn" onclick="window.open(\'https://www.pitchmetv.com/coaching-program\',\'_blank\')">Join — $9.97/mo →</button></div></div>';
      }
      if(typeof imgData==='function'&&imgData('reading')){
        h+='<div class="m5-tcard"><img src="'+imgData('reading')+'" alt="Morning Kickoff – (Mon–Sat) and Office Hours"><div class="m5-tcard-b"><div class="m5-tcard-t">Morning Kickoff – (Mon–Sat) and Office Hours</div><div class="m5-tcard-d">Mon–Sat 8:00–9:00 AM ET · mindset &amp; goals, then office hours for Q&amp;A and script practice.</div><button class="openbtn" onclick="dlImg(\'reading\',\'morning-kickoff.jpg\')">⬇ Download to share</button></div></div>';
      }
      if(typeof imgData==='function'&&imgData('vbo')){
        h+='<div class="m5-tcard"><img src="'+imgData('vbo')+'" alt="Virtual Business Overview"><div class="m5-tcard-b"><div class="m5-tcard-t">Virtual Business Overview</div><div class="m5-tcard-d">Every day · share to invite prospects.</div><button class="openbtn" onclick="dlImg(\'vbo\',\'vbo-everyday.png\')">⬇ Download to share</button></div></div>';
      }
      h+='</div>';
      setTimeout(function(){if(window.m5EvTick)window.m5EvTick();},30);
      return h;
    };
  }
}catch(e){}
window.m5ToggleExpand=function(el){var p=el.closest&&el.closest('.m5-expand');if(p)p.classList.toggle('open');};
window.m5FallbackCopy=function(t){try{var ta=document.createElement('textarea');ta.value=t;ta.style.position='fixed';ta.style.left='-9999px';ta.style.opacity='0';document.body.appendChild(ta);ta.focus();ta.select();document.execCommand('copy');document.body.removeChild(ta);}catch(e){}};
window.m5CopyMsg=function(id,btn){var el=document.getElementById(id);if(!el)return;var txt=el.innerHTML.replace(/<br\s*\/?>/gi,'\n').replace(/<\/p>\s*<p[^>]*>/gi,'\n\n').replace(/<[^>]+>/g,'');var d=document.createElement('textarea');d.innerHTML=txt;txt=d.value;function done(){var o=btn.getAttribute('data-orig');if(o===null){btn.setAttribute('data-orig',btn.innerHTML);}btn.classList.add('copied');btn.innerHTML='✓ Copied';setTimeout(function(){btn.classList.remove('copied');btn.innerHTML=btn.getAttribute('data-orig')||'Copy';},1600);}if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(done,function(){m5FallbackCopy(txt);done();});}else{m5FallbackCopy(txt);done();}};
/* ---------------- Mobile drawer nav (phones ≤768px) ---------------- */
function m5NavClose(){document.body.classList.remove('m5-navopen');}
function m5MobileInit(){
  try{
    if(!document.querySelector('.m5-backdrop')){
      var bd=document.createElement('div');bd.className='m5-backdrop';
      bd.addEventListener('click',m5NavClose);
      (document.body||document.documentElement).appendChild(bd);
    }
    var tb=document.querySelector('.topbar');
    if(tb&&!tb.querySelector('.m5-hamb')){
      var b=document.createElement('button');
      b.className='m5-hamb';b.setAttribute('aria-label','Open menu');
      b.innerHTML='<svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
      b.addEventListener('click',function(ev){ev.stopPropagation();document.body.classList.toggle('m5-navopen');});
      tb.insertBefore(b,tb.firstChild);
    }
    var sn=document.getElementById('sidenav');
    if(sn&&!sn.__m5bound){sn.__m5bound=1;sn.addEventListener('click',function(){setTimeout(m5NavClose,10);});}
    var sf=document.querySelector('.side-foot');
    if(sf&&!sf.__m5bound){sf.__m5bound=1;sf.addEventListener('click',m5NavClose);}
    if(!window.__m5resize){window.__m5resize=1;window.addEventListener('resize',function(){if(window.innerWidth>768)m5NavClose();});}
  }catch(e){}
}
/* ---------- Preview the unlicensed (pre-licensing) experience — sandbox, no data writes ---------- */
function m5PreviewBanner(on){
  var b=document.getElementById('m5-previewbar');
  if(on){
    if(!b){ b=document.createElement('div'); b.id='m5-previewbar';
      b.innerHTML='<span class="m5-pbdot" data-ico="user"></span><span class="m5-pbtxt"><b>Preview</b> &mdash; what your unlicensed new agent sees. Nothing is saved.</span><button class="m5-pbexit" onclick="m5ExitPreview()">Exit preview &#10005;</button>';
      (document.body||document.documentElement).appendChild(b);
    }
    document.body.classList.add('m5-previewing');
  }else{
    if(b)b.remove();
    document.body.classList.remove('m5-previewing');
  }
}
window.m5EnterPreview=function(){
  try{
    if(window.__m5preview) return;
    if(typeof store==='undefined'||!store.data||store.data.status!=='licensed') return;
    window.__m5preview=true;
    store.__realData=store.data; store.__realSave=store.save; store.__realSaveLocal=store._saveLocal;
    store.data={status:'unlicensed', first:(store.__realData.first||'there'), last:'', email:'', checks:{}, _preview:true};
    store.save=function(){}; store._saveLocal=function(){};
    m5PreviewBanner(true);
    if(typeof showPre==='function'){ showPre(store.data.first); }
    else { if(typeof syncChip==='function')syncChip(); if(typeof buildNav==='function')buildNav(); if(typeof go==='function')go('dashboard'); }
    try{window.scrollTo(0,0);}catch(e){}
  }catch(e){ window.__m5preview=false; }
};
window.m5ExitPreview=function(){
  try{
    if(!window.__m5preview) return;
    window.__m5preview=false;
    if(store.__realData) store.data=store.__realData;
    if(store.__realSave) store.save=store.__realSave;
    if(store.__realSaveLocal) store._saveLocal=store.__realSaveLocal;
    store.__realData=null; store.__realSave=null; store.__realSaveLocal=null;
    m5PreviewBanner(false);
    if(typeof m5HideAll==='function')m5HideAll();
    var app=document.getElementById('app'); if(app)app.classList.remove('hidden');
    if(typeof syncChip==='function')syncChip();
    if(typeof buildNav==='function')buildNav();
    if(typeof go==='function')go('dashboard'); else if(typeof render==='function')render('dashboard');
    try{window.scrollTo(0,0);}catch(e){}
  }catch(e){}
};
function m5Start(){_mo=new MutationObserver(function(){if(window.__m5t)clearTimeout(window.__m5t);window.__m5t=setTimeout(m5Reskin,40);});m5Reskin();m5MobileInit();}
if(document.body){m5Start();}else{document.addEventListener('DOMContentLoaded',m5Start);}
setTimeout(function(){m5Reskin();m5MobileInit();},400);
})();

/* ===== Browser Back button = previous in-app screen (Option A) ===== */
(function(){
  if(!window.history||!window.history.pushState) return;
  var _busy=false, _seeded=false;
  function snap(){
    var v=(typeof currentView==='function')?currentView():'dashboard';
    if(v==='academy'&&typeof m5acad!=='undefined'&&m5acad){
      return {m5:1,v:'academy',a:{view:m5acad.view,mod:m5acad.mod,les:m5acad.les}};
    }
    return {m5:1,v:v};
  }
  function record(){
    if(_busy) return;
    var s=snap();
    try{
      if(!_seeded){ history.replaceState(s,''); _seeded=true; }
      else { history.pushState(s,''); }
    }catch(e){}
  }
  function restore(s){
    if(!s||!s.m5) return;
    _busy=true;
    try{
      if(s.v==='academy'){
        if(typeof m5acad!=='undefined'&&s.a){ m5acad={view:s.a.view||'home',mod:s.a.mod||null,les:s.a.les||null}; }
        if(typeof render==='function') render('academy');
        var cr=document.getElementById('crumb'); if(cr) cr.textContent='Academy';
        document.querySelectorAll('.navitem').forEach(function(n){n.classList.toggle('active',n.dataset.view==='academy');});
        window.scrollTo(0,0);
      } else if(typeof go==='function'){ go(s.v); }
    }catch(e){}
    _busy=false;
  }
  function wrap(name){
    var f=window[name];
    if(typeof f!=='function') return;
    window[name]=function(){ var r=f.apply(this,arguments); if(!_busy) record(); return r; };
  }
  wrap('go'); wrap('acadGoMod'); wrap('acadGoLes'); wrap('acadGoHome');
  window.addEventListener('popstate', function(ev){ restore(ev.state); });
})();

/* ===== Client Retention / Service + Legacy Safeguard (Sales Tools) ===== */
function m5CretWho(){
  var nm=((store.data.first||'')+' '+(store.data.last||'')).trim()||'[Your name]';
  var ph=(((store.data.phone)||(typeof m5CurrentUser!=='undefined'&&m5CurrentUser.phone)||'[your number]')+'').trim();
  var em=(((store.data.email)||(typeof m5CurrentUser!=='undefined'&&m5CurrentUser.email)||'')+'').trim();
  return {nm:nm,ph:ph,em:em};
}
function m5CretFill(s){var w=m5CretWho();s=String(s||'').split('{AGENT}').join(w.nm).split('{PHONE}').join(w.ph);var ag=((store.data&&store.data.agency)||'').trim()||'Family First Life';s=s.split('[Your Agency Name]').join(ag);return s;}
function m5SaveAgency(){var el=document.getElementById('m5-agency-in');if(!el)return;store.data.agency=(el.value||'').trim();store.save();if(typeof toast==='function')toast('Agency saved ✓');}
var CRET_GEN=[
 {n:'1–3 Days After Sale',w:'Welcome & Questions Call',goal:'Answer questions and build trust.',
  call:`Hi [Client Name], this is {AGENT}, your life insurance agent with [Your Agency Name]. I'm calling to personally welcome you and check in on your new policy. I'm excited you've taken this step to protect your family and your financial future!

Do you have any questions so far about how your policy works or what to expect next? I'm here to make everything easy and clear for you.`,
  vm:`Hi [Client Name], this is {AGENT}, your life insurance agent with [Your Agency Name]. I just wanted to welcome you and check in to see if you had any questions about your new policy. You can reach me anytime at {PHONE}. Have a great day!`,
  text:`Hi [Client Name], this is {AGENT}, your life insurance agent with [Your Agency Name]. Just reaching out to welcome you and see if you had any questions about your new policy.`},
 {n:'2–3 Days Before First Payment',w:'Payment Reminder',goal:'Prevent a missed first payment.',
  call:`Hi [Client Name], this is {AGENT} with [Your Agency Name]. Just a quick friendly reminder — your first policy payment is scheduled in the next couple of days. I want to make sure everything's good to go so there's no interruption in your coverage.

Do you have any questions about the billing, or need to update your payment info in any way?`,
  vm:`Hi [Client Name], this is {AGENT} with [Your Agency Name]. Your first policy payment is coming up in the next couple of days. If you have any questions or need to update your payment info, give me a quick call as soon as you can at {PHONE}.`,
  text:`Hi [Client Name], it's {AGENT} with [Your Agency Name]. Just a quick reminder that your first policy payment is coming up. Let me know if you need anything.`},
 {n:'2 Weeks After Sale',w:'Check-In + Family Referral',goal:'Keep engagement high and see if others need help.',
  call:`Hi [Client Name], this is {AGENT} with [Your Agency Name], following up on your new policy. I wanted to check in and make sure you've received your policy in the mail — if not, that's not unusual, since they're usually larger packages, but it's good for me to check on.

Also, a lot of my clients, once they have their own coverage in place, start thinking about others who may need it too — is there anyone in your circle who might need the same kind of help you just got?`,
  vm:`Hi [Client Name], this is {AGENT} with [Your Agency Name], just checking in to see if you had any questions. I'm also happy to help any family members you may have in mind. Call me at {PHONE} if I can help with anything.`,
  text:`Hi [Client Name], it's {AGENT} with [Your Agency Name]. Just checking in to see if you have any questions — or if there's anyone in your family who may need help too.`},
 {n:'3 Days Before 2nd Payment',w:'Friendly Payment Reminder',goal:'Prevent an early lapse from a missed second payment.',
  call:`Hi [Client Name], this is {AGENT} with [Your Agency Name]. I wanted to give you a quick reminder that your second policy payment is coming up in a few days. Since this is still a new account, I just like to make sure everything's smooth and set up correctly.

Do you have any questions?`,
  vm:`Hi [Client Name], this is {AGENT} with [Your Agency Name]. Just a quick reminder that your second payment is coming up. Let me know if you need anything — you can reach me at {PHONE}.`,
  text:`Hi [Client Name], it's {AGENT} with [Your Agency Name]. Quick heads-up that your second policy payment is coming up. Let me know if you need anything.`},
 {n:'3 Months After Anniversary',w:'Questions & Family Help',goal:'Deepen the relationship and ask about referrals.',
  call:`Hi [Client Name], this is {AGENT}, your life insurance agent with [Your Agency Name]. I'm checking in now that you've had your policy for a few months. Do you have any questions about your coverage or how everything's been working?

Also, I find that once someone has their own plan in place, they start thinking about others who'd like the same peace of mind — is there anyone you'd like me to reach out to and help as well?`,
  vm:`Hi [Client Name], this is {AGENT} with [Your Agency Name]. I'm just checking in to see if you have any questions about your policy — or if there's someone else in your family I might be able to help. Call me at {PHONE} when you get a chance.`,
  text:`Hi [Client Name], it's {AGENT} with [Your Agency Name]. Checking in to see if you have any questions, or if there's anyone else in your family who may need help.`},
 {n:'6-Month Check-In',w:'Maintain Connection',goal:'Keep retention high and create a touchpoint.',
  call:`Hi [Client Name], this is {AGENT} with [Your Agency Name]. I'm just checking in — it's been about six months since we set up your policy, and I want to make sure everything's going well.

Is there anything you'd like to go over, or any questions I can answer for you?`,
  vm:`Hi [Client Name], this is {AGENT} with [Your Agency Name], checking in for your six-month mark. Let me know if you have any questions — you can reach me at {PHONE}.`,
  text:`Hi [Client Name], it's {AGENT} with [Your Agency Name]. Reaching out for your six-month policy check-in. Let me know if you have any questions or need help with anything.`},
 {n:'2 Weeks Before 1-Year Anniversary',w:'Book Policy Review',goal:'Set the annual review appointment.',
  call:`Hi [Client Name], this is {AGENT} with [Your Agency Name]. You're coming up on your one-year policy anniversary, and I like to celebrate that with a full policy review. It's a great time to see how everything's going, answer any questions, and talk about what's next.

Let's get that scheduled — do mornings or afternoons work better for you?`,
  vm:`Hi [Client Name], this is {AGENT} with [Your Agency Name]. Your policy anniversary is coming up, and I'd love to schedule a quick review with you. Give me a call back at {PHONE} and we'll get it set up.`,
  text:`Hi [Client Name], it's {AGENT} with [Your Agency Name]. You're coming up on your one-year policy anniversary — I'd like to schedule your annual review. What days or times work best for you?`}
];
var CRET_MISS=[
 {n:'First Missed Payment',w:'Friendly Courtesy Call',goal:'Gently alert the client and offer help.',
  call:`Hi [Client Name], this is {AGENT}, your life insurance agent with [Your Agency Name]. I wanted to give you a quick courtesy call — it looks like your most recent policy payment didn't go through. These things happen; it could be something as simple as your deposit hitting a day off.

I want to make sure everything stays on track so your coverage stays active — this policy is here to protect your family and build a strong foundation for your future. Would you like help updating your payment method or checking your billing info?`,
  vm:`Hi [Client Name], this is {AGENT} with [Your Agency Name]. I just wanted to let you know it looks like your most recent payment didn't go through. I'd love to help you get that resolved so there's no interruption in your coverage. Feel free to call or text me back at {PHONE} — happy to help!`,
  text:`Hi [Client Name], it's {AGENT} with [Your Agency Name]. It looks like your recent policy payment didn't go through. If it happened in error, or if you'd like help updating your billing info, just let me know.`},
 {n:'Second Attempt',w:'Escalated Follow-Up',goal:'Urge action while reinforcing the long-term benefits.',
  call:`Hi [Client Name], it's {AGENT} again with [Your Agency Name]. I'm following up because your policy is still showing an unpaid balance, and I'm concerned it's at risk of going out of good standing. I know how important this coverage is for your family's protection — and for the future value it's building for you.

Let's take a moment to get this back on track so there's no disruption in your benefits. I can help you right now over the phone, or walk you through how to update it online — whatever's easiest for you.`,
  vm:`Hi [Client Name], this is {AGENT} with [Your Agency Name], following up again. Your policy is still showing an unpaid balance, and I'd really like to help before it risks falling out of good standing. Please give me a call at {PHONE} — even if you just have questions or need help making the update.`,
  text:`Hi [Client Name], it's {AGENT} with [Your Agency Name]. Your policy is still showing a missed payment, and I'd like to help get it resolved before your benefits are at risk. Let me know if you need a hand.`},
 {n:'Final Call',w:'Policy at Immediate Risk of Lapse',goal:'Create urgency with care — the final chance to save the policy.',
  call:`Hi [Client Name], this is {AGENT} with [Your Agency Name], and I'm reaching out urgently. I want to make sure you're aware — your policy is now in danger of lapsing, which would mean your family is no longer protected and the future value you've been building would be lost. I know we set this policy up for a reason — to give you peace of mind and long-term security.

I don't want you to lose this coverage. If we can update your payment today, we can still save the policy and keep everything in force. Can we take care of that now, or would you like me to help you log in to make the payment?`,
  vm:`Hi [Client Name], this is {AGENT} with [Your Agency Name], reaching out urgently. Your policy is now in danger of lapsing due to a missed payment, and I'd really like to help before that happens. Please call me today at {PHONE} so we can keep your coverage in place.`,
  text:`Hi [Client Name], it's {AGENT} with [Your Agency Name]. Your policy is now at risk of lapsing. Please call or text me so I can help you keep your coverage active — I don't want you to lose it.`}
];
var CRET_BENE=[
 {n:'Day of Your Sale',w:'Text the Beneficiary — Introduce Yourself',goal:'Put a real person in their hands — not a 1-800 number.',
  text:`Hi [Name],
My name is {AGENT}, and I'm the life insurance agent who worked with [Client's first name] on their coverage. They named you as a beneficiary on their policy, and they wanted to make sure you had a real person to reach out to rather than just a 1-800 number and a stack of paperwork.
There's nothing you need to do right now — I just wanted to introduce myself and put my information in your hands. Whenever the time comes, you can call or text me directly. My job is to make the process simple: I'll walk you through the few steps needed and help get the funds released quickly so the immediate expenses are taken care of and you've got a little breathing room when you need it most.
Go ahead and save my number. I hope it's a long while before you ever need it — but when you do, I'll be here.
Real people helping real people.`}
];
var _cretN=0;
function m5CretCard(item){
  var w=m5CretWho();
  var sig='<br><br>'+w.nm+'<br>'+w.ph+(w.em?'<br>'+w.em:'');
  var blocks=[['Call Script',item.call],['Voicemail',item.vm],['Text Message',item.text]];
  var body=blocks.map(function(b){ if(!b[1])return ''; var id='cret'+(++_cretN); var html=m5CretFill(b[1]).replace(/\n/g,'<br>')+sig;
    return '<div class="m5-msgcard"><div class="m5-msgcard-h"><span class="m5-msgcard-t">'+b[0]+'</span><button class="m5-copybtn" onclick="m5CopyMsg(\''+id+'\',this)"><span data-ico="clip"></span> Copy</button></div><div class="m5-msgbody" id="'+id+'">'+html+'</div></div>';
  }).join('');
  return '<div class="m5-expand"><div class="m5-exhead" onclick="m5ToggleExpand(this)"><span class="m5-exchip" data-ico="msg"></span><span class="m5-extext"><span class="m5-exname">'+item.n+' — '+item.w+'</span><span class="m5-exsub">Goal: '+item.goal+'</span></span><span class="m5-exchev">›</span></div><div class="m5-exbody">'+body+'</div></div>';
}
function m5RetentionPanel(){
  _cretN=0;
  var w=m5CretWho();
  var ag=((store.data&&store.data.agency)||'').trim();
  var agLine=ag?('Your agency (<b>'+ag+'</b>) fills in automatically — change it anytime under Profile.'):('Your agency name defaults to <b>Family First Life</b>. Since most agents use their own agency name publicly, you can set yours once under <b>Profile</b> and it will fill in automatically from then on. You just fill in your client\'s name.');
  var intro='<div class="lc-sub">Simple copy-and-paste touchpoints to keep your clients happy and on the books — perfect for agents not yet using a CRM. Every script is written as <b>you</b> and already signed with your name, number, and email ('+w.nm+'). '+agLine+'</div>';
  var hd=function(t){return '<div style="font-size:12.5px;font-weight:800;color:#16233f;margin:20px 0 8px;text-transform:uppercase;letter-spacing:.03em">'+t+'</div>';};
  return '<div class="listcard" style="margin-top:16px"><h3>🔁 Client Retention / Service</h3>'+intro+
    hd('Reach out to the beneficiary')+CRET_BENE.map(m5CretCard).join('')+
    hd('General calls &middot; status: Submitted, In Underwriting, Approved, or Issued/Paid')+CRET_GEN.map(m5CretCard).join('')+
    hd('If they miss a payment &middot; status: Lapse Pending')+CRET_MISS.map(m5CretCard).join('')+
    '</div>';
}
function m5LegacyPanel(){
  var blurb='Legacy Safeguard University® was created to help you successfully offer the Legacy Safeguard end-of-life planning service and our industry-leading solutions to everyone you serve. Get access to tools and proven techniques that help you serve more clients, close more sales, and increase your income — all at the same time.';
  var rows=[['Quick Overview','A quick overview of the program.','https://integrity.com/legacysafeguard/'],['Member Site','Clients log in here to learn about this now-free service you provide for them.','https://legacysafeguard.com/'],['Legacy Safeguard University','Learn how this service benefits your clients.','https://legacysafeguarduniversity.com/'],['Agent Registration','Register your agent account to start offering the service.','https://legacysafeguarduniversity.com/my-account/'],['Client Enrollment','The form to enroll a client in Legacy Safeguard.','https://legacysafeguarduniversity.com/enrollment-form/'],['YouTube Overview Video','A short video overview of this free service.','https://www.youtube.com/watch?v=Sy2VygVyMnY']];
  return listPanel('🛡️ Legacy Safeguard',blurb,rows);
}

/* ===== Goal Card + Activity Tracker ===== */
var M5GC_BLOCKS=["8–10 AM","10–12 PM","12–2 PM","2–4 PM","4–6 PM","6–8 PM","8–10 PM"];
var M5GC_W={c:1,p:3,a:2,s:5};
var M5GC_DEFGOAL=40;
var M5GC_DOW=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];
var M5GC_MON=["January","February","March","April","May","June","July","August","September","October","November","December"];
var m5gcDate=null, m5gcView='day';
function m5gcIso(d){return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2);}
function m5gcAdd(d,n){var x=new Date(d);x.setDate(x.getDate()+n);return x;}
function m5gcParseD(s){var d=new Date(s+'T00:00:00');return isNaN(d.getTime())?new Date():d;}
function m5gcMoney(n){n=Math.round(n||0);return '$'+n.toLocaleString('en-US');}
function m5gcNum(n){return (Math.round((n||0)*100)/100).toLocaleString('en-US');}
function m5gcRatio(a,b){return b>0?a/b:0;}
function m5gcStore(){if(!store.data.goalcards||typeof store.data.goalcards!=='object')store.data.goalcards={};return store.data.goalcards;}
function m5gcBlank(){return M5GC_BLOCKS.map(function(){return [0,0,0,0,0];});}
function m5gcBlankPlan(){return M5GC_BLOCKS.map(function(){return false;});}
function m5gcStats(rec){var t={c:0,p:0,a:0,s:0,dials:0,pts:0,planned:0,worked:0,pw:0};if(!rec)return t;(rec.blocks||[]).forEach(function(b,i){if(!b)return;var dl=b[4]||0;var has=((b[0]||0)+(b[1]||0)+(b[2]||0)+(b[3]||0)+dl)>0;var pl=rec.planned&&rec.planned[i];t.c+=b[0]||0;t.p+=b[1]||0;t.a+=b[2]||0;t.s+=b[3]||0;t.dials+=dl;if(has)t.worked++;if(pl)t.planned++;if(pl&&has)t.pw++;});t.pts=t.c*M5GC_W.c+t.p*M5GC_W.p+t.a*M5GC_W.a+t.s*M5GC_W.s;return t;}
function m5gcHoursFor(rec,st){st=st||m5gcStats(rec);if(rec&&rec.hours!=null&&rec.hours!=='')return +rec.hours||0;return st.worked*2;}

function m5gcStyle(){return '<style>'+
'#m5gc-app .m5gcx-seg{display:inline-flex;background:#fff;border:1px solid var(--gcl);border-radius:12px;padding:4px;gap:4px;box-shadow:0 4px 12px rgba(20,35,63,.04)}'+
'#m5gc-app .m5gcx-seg button{border:0;background:transparent;padding:9px 20px;border-radius:9px;font-size:14px;font-weight:800;color:var(--gcs);cursor:pointer;font-family:inherit}'+
'#m5gc-app .m5gcx-seg button.on{background:var(--gcn);color:#fff}'+
'#m5gc-app .m5gcx-rangelab{font-size:12.5px;color:var(--gcs);margin:10px 2px 0}#m5gc-app .m5gcx-rangelab b{color:var(--gcn)}'+
'#m5gc-app .m5gcx-scroll{overflow-x:auto}'+
'#m5gc-app .m5gcx-stp{display:inline-flex;align-items:center;gap:3px}'+
'#m5gc-app .m5gcx-mn{width:22px;height:30px;border:1px solid var(--gcl);background:#f6f8fc;border-radius:7px;font-size:16px;font-weight:800;color:var(--gcn);cursor:pointer;line-height:1;padding:0;font-family:inherit}'+
'#m5gc-app .m5gcx-mn:hover{border-color:var(--gcg);background:#fdf8ea}'+
'#m5gc-app .m5gcx-stp input[type=number]{width:44px;-webkit-appearance:none;-moz-appearance:textfield}'+
'#m5gc-app .m5gcx-sub2{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px}'+
'#m5gc-app .m5gcx-money{display:flex;align-items:center;border:1px solid var(--gcl);border-radius:9px;background:#fff;padding:2px 10px}'+
'#m5gc-app .m5gcx-money span{color:var(--gcs);font-size:16px;font-weight:800}'+
'#m5gc-app .m5gc-fld .m5gcx-money input,#m5gc-app .m5gc-fld .m5gcx-money input:focus{border:0;outline:0;border-radius:0;box-shadow:none;font-size:16px;font-weight:800;color:var(--gci);width:100%;padding:8px 6px;background:transparent;font-family:inherit}'+
'#m5gc-app .m5gcx-sub{font-size:11px;color:var(--gcs);margin-top:5px;font-weight:600;text-transform:none;letter-spacing:0}#m5gc-app .m5gcx-sub a{color:#a9861d;font-weight:800}'+
'#m5gc-app .m5gcx-sec{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--gcs);font-weight:800;margin:20px 2px 9px}'+
'#m5gc-app .m5gcx-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:11px}'+
'#m5gc-app .m5gcx-stat{border:1px solid var(--gcl);border-radius:13px;padding:13px 15px;background:#fff}'+
'#m5gc-app .m5gcx-stat .k{font-size:12px;color:var(--gcs);font-weight:700}'+
'#m5gc-app .m5gcx-stat .v{font-size:25px;font-weight:800;letter-spacing:-.5px;margin-top:4px;color:var(--gcn)}'+
'#m5gc-app .m5gcx-stat .sub{font-size:11px;color:var(--gcs);margin-top:3px}'+
'#m5gc-app .m5gcx-stat.hl{background:linear-gradient(135deg,#16233f,#1f2f4f);border-color:#16233f}#m5gc-app .m5gcx-stat.hl .k{color:rgba(255,255,255,.7)}#m5gc-app .m5gcx-stat.hl .v{color:#fff}'+
'#m5gc-app .m5gcx-grid.worth .v{color:var(--gcgood)}'+
'#m5gc-app .m5gcx-frow{display:flex;align-items:center;gap:12px;margin:8px 0}'+
'#m5gc-app .m5gcx-frow .fl{width:120px;font-size:13px;font-weight:700;color:var(--gcn);flex:0 0 auto}'+
'#m5gc-app .m5gcx-frow .fbar{flex:1;height:24px;background:#eef2f8;border-radius:8px;overflow:hidden}'+
'#m5gc-app .m5gcx-frow .ff{height:100%;border-radius:8px;background:linear-gradient(90deg,#2c4a86,#4f78c8);display:flex;align-items:center;padding-left:10px;color:#fff;font-size:12px;font-weight:800;min-width:32px}'+
'#m5gc-app .m5gcx-frow .fn{width:88px;text-align:right;font-size:12px;color:var(--gcs);flex:0 0 auto}#m5gc-app .m5gcx-frow .fn b{color:var(--gcn);font-size:14px}'+
'#m5gc-app .m5gcx-note{font-size:12px;color:var(--gcs);margin-top:15px;line-height:1.5;background:#f4f7fc;border-radius:10px;padding:11px 14px;border:1px solid var(--gcl)}#m5gc-app .m5gcx-note b{color:var(--gcn)}'+
'#m5gc-app .m5gcx-tot{display:grid;grid-template-columns:repeat(auto-fit,minmax(92px,1fr));border:1px solid var(--gcl);border-radius:13px;overflow:hidden}'+
'#m5gc-app .m5gcx-tc{padding:11px 8px;text-align:center;border-right:1px solid var(--gcl);border-bottom:1px solid var(--gcl);background:#fff}'+
'#m5gc-app .m5gcx-tc .tk{font-size:9.5px;text-transform:uppercase;letter-spacing:.04em;color:var(--gcs);font-weight:800}'+
'#m5gc-app .m5gcx-tc .tv{font-size:21px;font-weight:800;color:var(--gcn);margin-top:2px}'+
'#m5gc-app .m5gcx-tc.acc{background:#0f1c33}#m5gc-app .m5gcx-tc.acc .tk{color:rgba(255,255,255,.6)}#m5gc-app .m5gcx-tc.acc .tv{color:#fff}'+
'#m5gc-app .m5gcx-tc.gold{background:#fbf7e9}#m5gc-app .m5gcx-tc.gold .tv{color:#a9861d}'+
'#m5gc-app .m5gcx-pdchart{display:flex;align-items:flex-end;gap:8px;height:160px;padding:16px 4px 0;border-bottom:1px solid var(--gcl)}'+
'#m5gc-app .m5gcx-pdcol{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%;min-width:0}'+
'#m5gc-app .m5gcx-pdbar{width:74%;max-width:44px;border-radius:6px 6px 0 0;background:linear-gradient(180deg,#2c4a86,#16233f);position:relative;display:flex;justify-content:center}'+
'#m5gc-app .m5gcx-pdbar.off{background:#e7ebf3}'+
'#m5gc-app .m5gcx-pdval{position:absolute;top:-17px;font-size:11px;font-weight:800;color:var(--gcn);white-space:nowrap}'+
'#m5gc-app .m5gcx-pdlabs{display:flex;gap:8px;margin-top:6px}'+
'#m5gc-app .m5gcx-pdlab{flex:1;text-align:center;font-size:10.5px;color:var(--gcs);min-width:0}#m5gc-app .m5gcx-pdlab b{display:block;color:var(--gcn);font-size:11.5px}#m5gc-app .m5gcx-pdlab .hh{display:block;font-size:10px;color:var(--gcs);margin-top:1px}#m5gc-app .m5gcx-pdlab.off b{color:#b7bfce}'+
'@media(max-width:720px){#m5gc-app .m5gcx-sub2{grid-template-columns:1fr}#m5gc-app .m5gcx-stp input[type=number]{width:38px}#m5gc-app .m5gcx-mn{width:20px}}'+
'</style>';}

function m5GoalCard(){var today=new Date();today.setHours(0,0,0,0);m5gcDate=m5gcIso(today);m5gcView='day';setTimeout(m5gcInit,0);return '<h1 class="page">🎯 Goal Card</h1><p class="sub">Plan your blocks, log your dials, and watch your activity build day over day.</p><div id="m5gc-app"></div>';}
function m5gcInit(){var host=document.getElementById('m5gc-app');if(!host)return;m5gcStore();host.innerHTML=m5gcStyle()+'<div class="m5gcx-seg" id="m5gc-seg"><button data-v="day" class="on">Daily</button><button data-v="week">Weekly</button><button data-v="month">Monthly</button></div><div class="m5gcx-rangelab" id="m5gc-rangelab"></div><div id="m5gc-view"></div>';var seg=document.getElementById('m5gc-seg');seg.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;[].forEach.call(seg.querySelectorAll('button'),function(x){x.classList.remove('on');});b.classList.add('on');m5gcView=b.dataset.v;m5gcRenderView();});m5gcRenderView();}

function m5gcRenderView(){var v=document.getElementById('m5gc-view');if(!v)return;if(m5gcView==='day'){v.innerHTML=m5gcDailyShell();m5gcBuildBody();m5gcWireDaily();m5gcRenderDaily();}else{m5gcRenderRollup();}m5gcRangeLabel();}

function m5gcDailyShell(){var st=m5gcStore();var rec=st[m5gcDate];var goal=(rec&&rec.goal)||M5GC_DEFGOAL;var ip=(rec&&rec.ip)||0;var hrs=(rec&&rec.hours!=null&&rec.hours!=='')?rec.hours:'';return '<div id="m5gc-printarea" class="m5gc-card">'+
 '<div class="m5gc-stitle">THE GOAL CARD</div><div class="m5gc-stars">★ ★ ★ ★ ★</div>'+
 '<div class="m5gc-ssub">Plan your blocks, then log your activity. Points and totals calculate automatically.</div>'+
 '<div class="m5gc-row2"><label class="m5gc-fld">Daily Point Goal<input id="m5gc-goal" type="number" min="0" value="'+goal+'"></label><label class="m5gc-fld">Date<input id="m5gc-date" type="date" value="'+m5gcDate+'"></label></div>'+
 '<div class="m5gc-prog"><div style="display:flex;justify-content:space-between;align-items:center"><span class="pt">Daily Goal Progress</span><span class="pt" id="m5gc-prog-txt">0 of '+goal+' points</span></div><div class="m5gc-barp"><i id="m5gc-prog-bar" style="width:0%"></i></div></div>'+
 '<div class="m5gcx-scroll"><table class="m5gc-act"><thead><tr><th>TIME</th><th>PLAN<small>working?</small></th><th>DIALS<small>activity</small></th><th>CONTACTS<small>1 pt</small></th><th>PRESENTATIONS<small>3 pts</small></th><th>APPOINTMENTS<small>2 pts</small></th><th>SALES<small>5 pts</small></th><th>ROW POINTS<small>auto</small></th></tr></thead><tbody id="m5gc-body"></tbody><tfoot><tr class="tot"><td>Daily Totals</td><td id="m5gc-f-plan">0</td><td id="m5gc-f-d">0</td><td id="m5gc-f-c">0</td><td id="m5gc-f-p">0</td><td id="m5gc-f-a">0</td><td id="m5gc-f-s">0</td><td id="m5gc-f-pts">0</td></tr></tfoot></table></div>'+
 '<div class="m5gcx-sub2">'+
   '<label class="m5gc-fld">Premium / IP written<span class="m5gcx-money"><span>$</span><input id="m5gc-ip" inputmode="numeric" value="'+(ip?m5gcNum(ip):'')+'" placeholder="0"></span></label>'+
   '<div class="m5gc-fld">Hours worked<span class="m5gcx-money"><input id="m5gc-hours" inputmode="decimal" value="'+hrs+'" placeholder="0"></span><span class="m5gcx-sub" id="m5gc-hours-sub"></span></div>'+
 '</div>'+
 '<div class="m5gc-btns m5gc-noprint"><button class="m5gc-btn s" onclick="m5gcSave()">Save Today’s Card</button><button class="m5gc-btn p" onclick="window.print()">Print Goal Card</button><button class="m5gc-btn g" onclick="m5gcReset()">Reset</button></div>'+
 '</div>'+
 '<div class="m5gc-card" id="m5gc-ana"></div>';}

function m5gcBuildBody(){var body=document.getElementById('m5gc-body');if(!body)return;var rec=m5gcStore()[m5gcDate];var blocks=rec&&rec.blocks?rec.blocks:m5gcBlank();var planned=rec&&rec.planned?rec.planned:m5gcBlankPlan();
 function cell(i,ci){var v=(blocks[i]&&blocks[i][ci])||0;return '<td><span class="m5gcx-stp"><button type="button" class="m5gcx-mn" data-b="'+i+'" data-c="'+ci+'" data-d="-1">−</button><input type="number" min="0" inputmode="numeric" data-b="'+i+'" data-c="'+ci+'" placeholder="0" value="'+(v?v:'')+'" onfocus="this.select()"><button type="button" class="m5gcx-mn" data-b="'+i+'" data-c="'+ci+'" data-d="1">+</button></span></td>';}
 var h='';M5GC_BLOCKS.forEach(function(tl,i){h+='<tr><td class="time">'+tl+'</td><td><input type="checkbox" data-plan="'+i+'"'+(planned[i]?' checked':'')+'></td>'+cell(i,4)+cell(i,0)+cell(i,1)+cell(i,2)+cell(i,3)+'<td class="rp" id="m5gc-rp-'+i+'">0</td></tr>';});
 body.innerHTML=h;}

function m5gcWireDaily(){var body=document.getElementById('m5gc-body');
 if(body){body.addEventListener('input',function(e){if(e.target.tagName==='INPUT'&&e.target.type==='number')m5gcRenderDaily();});
  body.addEventListener('change',function(e){if(e.target.type==='checkbox')m5gcRenderDaily();});
  body.addEventListener('click',function(e){var b=e.target.closest('.m5gcx-mn');if(!b)return;var inp=body.querySelector('input[type=number][data-b="'+b.dataset.b+'"][data-c="'+b.dataset.c+'"]');if(!inp)return;var nv=Math.max(0,(parseInt(inp.value||'0',10)||0)+(+b.dataset.d));inp.value=nv?nv:'';m5gcRenderDaily();});}
 var ge=document.getElementById('m5gc-goal');if(ge)ge.addEventListener('input',m5gcRenderDaily);
 var ipEl=document.getElementById('m5gc-ip');if(ipEl){ipEl.addEventListener('input',m5gcRenderDaily);ipEl.addEventListener('focus',function(){this.value=(''+this.value).replace(/[^0-9.]/g,'');});ipEl.addEventListener('blur',function(){var n=parseFloat((''+this.value).replace(/[^0-9.]/g,''))||0;this.value=n?m5gcNum(n):'';});}
 var hr=document.getElementById('m5gc-hours');if(hr)hr.addEventListener('input',m5gcRenderDaily);
 var de=document.getElementById('m5gc-date');if(de)de.addEventListener('change',function(){m5gcDate=this.value;m5gcRenderView();});}

function m5gcReadGrid(){var blocks=m5gcBlank(),planned=m5gcBlankPlan();document.querySelectorAll('#m5gc-body input[type=number]').forEach(function(inp){blocks[+inp.dataset.b][+inp.dataset.c]=Math.max(0,parseInt(inp.value||'0',10)||0);});document.querySelectorAll('#m5gc-body input[type=checkbox]').forEach(function(inp){planned[+inp.dataset.plan]=inp.checked;});return {blocks:blocks,planned:planned};}

function m5gcRenderDaily(){var g=m5gcReadGrid();var ge=document.getElementById('m5gc-goal');var goal=Math.max(1,parseInt((ge&&ge.value)||M5GC_DEFGOAL,10));
 var ipEl=document.getElementById('m5gc-ip');var ip=ipEl?(parseFloat((''+ipEl.value).replace(/[^0-9.]/g,''))||0):0;
 var hrEl=document.getElementById('m5gc-hours');var hoursOv=(hrEl&&(''+hrEl.value).trim()!=='')?(parseFloat((''+hrEl.value).replace(/[^0-9.]/g,''))||0):null;
 g.blocks.forEach(function(b,i){var rp=b[0]*M5GC_W.c+b[1]*M5GC_W.p+b[2]*M5GC_W.a+b[3]*M5GC_W.s;var cell=document.getElementById('m5gc-rp-'+i);if(cell){cell.textContent=rp;var tr=cell.parentNode;if(tr)tr.classList.toggle('planned',!!g.planned[i]);}});
 var rec={goal:goal,blocks:g.blocks,planned:g.planned,ip:ip,hours:hoursOv};m5gcStore()[m5gcDate]=rec;
 var st=m5gcStats(rec);var autoH=st.worked*2;var hours=hoursOv!=null?hoursOv:autoH;
 var set=function(id,v){var e=document.getElementById(id);if(e)e.textContent=v;};
 set('m5gc-f-plan',st.planned);set('m5gc-f-d',st.dials);set('m5gc-f-c',st.c);set('m5gc-f-p',st.p);set('m5gc-f-a',st.a);set('m5gc-f-s',st.s);set('m5gc-f-pts',st.pts);
 set('m5gc-prog-txt',st.pts+' of '+goal+' points');var pb=document.getElementById('m5gc-prog-bar');if(pb)pb.style.width=Math.min(100,Math.round(st.pts/goal*100))+'%';
 var hs=document.getElementById('m5gc-hours-sub');if(hs){hs.innerHTML=hoursOv!=null?('manual · blocks = '+autoH+'h · <a href="#" id="m5gc-hours-reset">use blocks</a>'):('from '+st.worked+' block'+(st.worked===1?'':'s')+' × 2 hrs (type to override)');var rr=document.getElementById('m5gc-hours-reset');if(rr)rr.onclick=function(e){e.preventDefault();var h2=document.getElementById('m5gc-hours');if(h2)h2.value='';m5gcRenderDaily();};}
 st.ip=ip;var close=m5gcRatio(st.s,st.p);var el=document.getElementById('m5gc-ana');if(!el)return;
 el.innerHTML='<div class="m5gc-dashh">What today’s numbers say</div><div class="m5gc-ssub" style="text-align:left;margin:2px 0 6px">Derived automatically from the card above.</div>'+
   m5gcxRates(st,hours)+m5gcxTakes(st)+m5gcxWorth(st)+
   '<div class="m5gcx-grid" style="margin-top:11px">'+
     m5gcxStat('Points',st.pts,'goal '+goal+' · '+Math.round(m5gcRatio(st.pts,goal)*100)+'%','hl')+
     m5gcxStat('Premium written',m5gcMoney(ip),'today','hl')+
     m5gcxStat('$ / hour worked',m5gcMoney(m5gcRatio(ip,hours)),'premium ÷ hours','')+
   '</div>'+
   '<div class="m5gcx-note">💡 Every dial today was worth <b>'+m5gcMoney(m5gcRatio(ip,st.dials))+'</b> in premium. It took about <b>'+(st.s?Math.round(m5gcRatio(st.dials,st.s)):'—')+' dials</b> and <b>'+(close?Math.round(1/close):'—')+' presentations</b> to land a sale — and you hit <b>'+st.pts+' of '+goal+'</b> points.</div>';}

function m5gcxStat(k,v,sub,cls){return '<div class="m5gcx-stat '+(cls||'')+'"><div class="k">'+k+'</div><div class="v">'+v+'</div><div class="sub">'+(sub||'')+'</div></div>';}
function m5gcxRates(t,hours){var close=m5gcRatio(t.s,t.p);var dph=hours?t.dials/hours:0;var dphS=Math.round(dph*10)/10;return '<div class="m5gcx-sec">Pace &amp; rates</div><div class="m5gcx-grid">'+
 m5gcxStat('Dials / hour',dphS,t.dials+' dials ÷ '+hours+' hrs')+
 m5gcxStat('Contact rate',Math.round(m5gcRatio(t.c,t.dials)*100)+'%','of dials reach someone')+
 m5gcxStat('Present. rate',Math.round(m5gcRatio(t.p,t.c)*100)+'%','of contacts get a pitch')+
 m5gcxStat('Close ratio',Math.round(close*100)+'%',t.s+' sale'+(t.s===1?'':'s')+' / '+t.p+' pres.')+'</div>';}
function m5gcxTakes(t){var per=[['1 contact',m5gcRatio(t.dials,t.c),100],['1 appointment',m5gcRatio(t.dials,t.a),78],['1 presentation',m5gcRatio(t.dials,t.p),62],['1 sale',m5gcRatio(t.dials,t.s),40]];var f='<div class="m5gcx-sec">What it takes to get one</div>';per.forEach(function(p){f+='<div class="m5gcx-frow"><div class="fl">'+p[0]+'</div><div class="fbar"><div class="ff" style="width:'+p[2]+'%">'+(p[1]?Math.round(p[1]):'—')+'</div></div><div class="fn"><b>'+(p[1]?Math.round(p[1]):'—')+'</b> dials</div></div>';});return f;}
function m5gcxWorth(t){return '<div class="m5gcx-sec">What your activity is worth</div><div class="m5gcx-grid worth">'+
 m5gcxStat('Per dial',m5gcMoney(m5gcRatio(t.ip,t.dials)),'every dial you make')+
 m5gcxStat('Per contact',m5gcMoney(m5gcRatio(t.ip,t.c)),'every person you reach')+
 m5gcxStat('Per presentation',m5gcMoney(m5gcRatio(t.ip,t.p)),'every pitch you give')+
 m5gcxStat('Avg per sale',m5gcMoney(m5gcRatio(t.ip,t.s)),'average premium written')+'</div>';}

function m5gcSave(){m5gcRenderDaily();if(typeof store.save==='function')store.save();if(typeof toast==='function')toast('Goal Card saved ✓');}
function m5gcReset(){var ge=document.getElementById('m5gc-goal');var goal=Math.max(1,parseInt((ge&&ge.value)||M5GC_DEFGOAL,10));m5gcStore()[m5gcDate]={goal:goal,blocks:m5gcBlank(),planned:m5gcBlankPlan(),ip:0,hours:null};var ip=document.getElementById('m5gc-ip');if(ip)ip.value='';var hr=document.getElementById('m5gc-hours');if(hr)hr.value='';m5gcBuildBody();m5gcRenderDaily();}

function m5gcListFor(){var d=m5gcParseD(m5gcDate),out=[];if(m5gcView==='week'){var mon=(d.getDay()+6)%7;var m=m5gcAdd(d,-mon);for(var i=0;i<7;i++)out.push(m5gcIso(m5gcAdd(m,i)));}else{var end=new Date(d.getFullYear(),d.getMonth()+1,0).getDate();var last=Math.min(d.getDate(),end);for(var day=1;day<=last;day++)out.push(m5gcIso(new Date(d.getFullYear(),d.getMonth(),day)));}return out;}
function m5gcAgg(list){var t={c:0,p:0,a:0,s:0,dials:0,pts:0,ip:0,hours:0,worked:0};list.forEach(function(k){var rec=m5gcStore()[k];if(!rec)return;var st=m5gcStats(rec);if(st.worked>0)t.worked++;t.c+=st.c;t.p+=st.p;t.a+=st.a;t.s+=st.s;t.dials+=st.dials;t.pts+=st.pts;t.ip+=(rec.ip||0);t.hours+=m5gcHoursFor(rec,st);});return t;}

function m5gcRangeLabel(){var el=document.getElementById('m5gc-rangelab');if(!el)return;var d=m5gcParseD(m5gcDate);if(m5gcView==='day'){el.innerHTML='Showing <b>'+M5GC_DOW[d.getDay()]+', '+(d.getMonth()+1)+'/'+d.getDate()+'</b>. Use the date box on the card to log a different day.';}else if(m5gcView==='week'){var mon=(d.getDay()+6)%7;var m=m5gcAdd(d,-mon),su=m5gcAdd(m,6);var t=m5gcAgg(m5gcListFor());el.innerHTML='Showing <b>the week of '+(m.getMonth()+1)+'/'+m.getDate()+' – '+(su.getMonth()+1)+'/'+su.getDate()+'</b> (Mon–Sun) — <b>'+t.worked+'</b> day'+(t.worked===1?'':'s')+' worked.';}else{var t2=m5gcAgg(m5gcListFor());el.innerHTML='Showing <b>'+M5GC_MON[d.getMonth()]+'</b> (month to date) — <b>'+t2.worked+'</b> day'+(t2.worked===1?'':'s')+' worked.';}}

function m5gcRenderRollup(){var host=document.getElementById('m5gc-view');if(!host)return;var list=m5gcListFor();var t=m5gcAgg(list);var worked=t.worked,hours=t.hours,pts=t.pts,goalTot=M5GC_DEFGOAL*worked;
 var title=(m5gcView==='week'?'This week at a glance':'This month at a glance');
 if(!worked){host.innerHTML='<div class="m5gc-card"><div class="m5gc-dashh">📊 '+title+'</div><div class="m5gc-hint">No saved days in this range yet. Log and save a Goal Card and your '+(m5gcView==='week'?'weekly':'monthly')+' totals, per-day breakdown, and averages fill in here automatically.</div></div>';return;}
 var tc=function(k,v,cls){return '<div class="m5gcx-tc '+(cls||'')+'"><div class="tk">'+k+'</div><div class="tv">'+v+'</div></div>';};
 var strip='<div class="m5gcx-sec">Totals — everything you did '+(m5gcView==='week'?'this week':'this month')+'</div><div class="m5gcx-tot">'+
   tc('Days worked',worked,'acc')+tc('Hours',m5gcNum(hours),'acc')+tc('Dials',m5gcNum(t.dials))+tc('Contacts',m5gcNum(t.c))+tc('Present.',m5gcNum(t.p))+tc('Appts',m5gcNum(t.a))+tc('Sales',m5gcNum(t.s))+tc('Premium',m5gcMoney(t.ip),'gold')+tc('Points',m5gcNum(pts),'gold')+'</div>';
 var maxD=1;list.forEach(function(k){var r=m5gcStore()[k];if(r){var dd=m5gcStats(r).dials;if(dd>maxD)maxD=dd;}});
 var bars='',labs='';list.forEach(function(k){var r=m5gcStore()[k];var st=r?m5gcStats(r):null;var dt=m5gcParseD(k);var workedDay=st&&st.worked>0;var dials=st?st.dials:0;var hh=st?m5gcHoursFor(r,st):0;var hpct=workedDay?Math.max(6,Math.round(dials/maxD*100)):4;bars+='<div class="m5gcx-pdcol"><div class="m5gcx-pdbar'+(workedDay?'':' off')+'" style="height:'+hpct+'%">'+(workedDay?'<span class="m5gcx-pdval">'+dials+'</span>':'')+'</div></div>';labs+='<div class="m5gcx-pdlab'+(workedDay?'':' off')+'"><b>'+M5GC_DOW[dt.getDay()]+'</b>'+(dt.getMonth()+1)+'/'+dt.getDate()+'<span class="hh">'+(workedDay?m5gcNum(hh)+'h':'off')+'</span></div>';});
 var perday='<div class="m5gcx-sec">Dials per day'+(m5gcView==='week'?' (Mon–Sun)':'')+'</div><div class="m5gcx-pdchart">'+bars+'</div><div class="m5gcx-pdlabs">'+labs+'</div>';
 var avg='<div class="m5gcx-sec">Per working day (averages)</div><div class="m5gcx-grid">'+
   m5gcxStat('Points / day',Math.round(m5gcRatio(pts,worked)),'avg on days worked','hl')+
   m5gcxStat('Dials / day',Math.round(m5gcRatio(t.dials,worked)),'avg on days worked')+
   m5gcxStat('Hours / day',(m5gcRatio(hours,worked)).toFixed(1),'avg on days worked')+'</div>'+
   '<div class="m5gcx-sec">What you made</div><div class="m5gcx-grid">'+
   m5gcxStat('Made / hour',m5gcMoney(m5gcRatio(t.ip,hours)),m5gcNum(hours)+' hrs on the phones','hl')+
   m5gcxStat('Made / day',m5gcMoney(m5gcRatio(t.ip,worked)),'avg on days worked','hl')+
   m5gcxStat('Total premium',m5gcMoney(t.ip),(m5gcView==='week'?'this week':'this month'))+'</div>';
 var note='<div class="m5gcx-note">Over <b>'+worked+' day'+(worked===1?'':'s')+'</b> worked you put in <b>'+m5gcNum(hours)+' hours</b> ('+m5gcRatio(hours,worked).toFixed(1)+'/day), averaged <b>'+Math.round(m5gcRatio(pts,worked))+' points/day</b>, and wrote <b>'+m5gcMoney(t.ip)+'</b>. That works out to <b>'+m5gcMoney(m5gcRatio(t.ip,t.dials))+'</b> per dial and <b>'+m5gcMoney(m5gcRatio(t.ip,hours))+'</b> per hour on the phones.</div>';
 host.innerHTML='<div class="m5gc-card">'+
   '<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px"><span class="m5gc-dashh">📊 '+title+'</span><span class="pt">'+pts+' of '+goalTot+' pts</span></div>'+
   '<div class="m5gc-barp" style="margin-top:10px"><i style="width:'+Math.min(100,Math.round(m5gcRatio(pts,goalTot)*100))+'%"></i></div>'+
   strip+perday+avg+m5gcxRates(t,hours)+m5gcxTakes(t)+m5gcxWorth(t)+note+
   '</div>';}

/* ===== Calls / Events — calendar (.ics) + countdown ===== */
window.m5CAL=window.m5CAL||[];
var M5_BYDAY=['SU','MO','TU','WE','TH','FR','SA'];
function m5pad2(n){return (n<10?'0':'')+n;}
function m5icsEsc(s){return String(s).replace(/([,;\\])/g,'\\$1').replace(/\n/g,'\\n');}
function m5nowStamp(){var d=new Date();return d.getUTCFullYear()+m5pad2(d.getUTCMonth()+1)+m5pad2(d.getUTCDate())+'T'+m5pad2(d.getUTCHours())+m5pad2(d.getUTCMinutes())+m5pad2(d.getUTCSeconds())+'Z';}
function m5nextDOW(dow){var d=new Date();d.setHours(0,0,0,0);var t=(dow==null?d.getDay():dow);var diff=(t-d.getDay()+7)%7;d.setDate(d.getDate()+diff);return d;}
function m5fmtLocal(d,mins){var hh=Math.floor(mins/60),mm=mins%60;return d.getFullYear()+m5pad2(d.getMonth()+1)+m5pad2(d.getDate())+'T'+m5pad2(hh)+m5pad2(mm)+'00';}
var M5_VTZ=['BEGIN:VTIMEZONE','TZID:America/New_York','BEGIN:DAYLIGHT','TZOFFSETFROM:-0500','TZOFFSETTO:-0400','TZNAME:EDT','DTSTART:19700308T020000','RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU','END:DAYLIGHT','BEGIN:STANDARD','TZOFFSETFROM:-0400','TZOFFSETTO:-0500','TZNAME:EST','DTSTART:19701101T020000','RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU','END:STANDARD','END:VTIMEZONE'];
function m5download(fn,text){try{var b=new Blob([text],{type:'text/calendar;charset=utf-8'});var url=URL.createObjectURL(b);var a=document.createElement('a');a.href=url;a.download=fn;document.body.appendChild(a);a.click();setTimeout(function(){document.body.removeChild(a);URL.revokeObjectURL(url);},120);}catch(e){}}
function m5calReg(e,day){if(e.allday||e.sessions)return -1;var byday;if(e.days&&e.days.length){byday=e.days.map(function(d){return M5_BYDAY[d];}).join(',');}else if(day!=null){byday=M5_BYDAY[day];}else{return -1;}var rrule=e.recur||('FREQ=WEEKLY;BYDAY='+byday);var dur=e.dur||(/reading|huddle/i.test(e.n)?30:60);var fd=(e.days&&e.days.length)?e.days[0]:day;window.m5CAL.push({n:e.n,s:e.s,dur:dur,link:e.link,rrule:rrule,day:fd});return window.m5CAL.length-1;}
window.m5AddCal=function(i){var c=window.m5CAL[i];if(!c)return;var d=m5nextDOW(c.day);var st=m5fmtLocal(d,c.s);var en=m5fmtLocal(d,c.s+c.dur);var uid=c.n.replace(/[^a-z0-9]/gi,'').toLowerCase()+'-'+c.day+'@ffloptimum';var L=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Optimum Portal//Calls//EN','CALSCALE:GREGORIAN','METHOD:PUBLISH'].concat(M5_VTZ,['BEGIN:VEVENT','UID:'+uid,'DTSTAMP:'+m5nowStamp(),'DTSTART;TZID=America/New_York:'+st,'DTEND;TZID=America/New_York:'+en,'RRULE:'+c.rrule,'SUMMARY:'+m5icsEsc(c.n),'DESCRIPTION:'+m5icsEsc('Optimum team call. Join: '+c.link),'LOCATION:'+m5icsEsc(c.link),'URL:'+c.link,'BEGIN:VALARM','TRIGGER:-PT10M','ACTION:DISPLAY','DESCRIPTION:'+m5icsEsc('Reminder: '+c.n),'END:VALARM','END:VEVENT','END:VCALENDAR']);m5download(c.n.replace(/[^a-z0-9]+/gi,'-').toLowerCase()+'.ics',L.join('\r\n'));if(typeof toast==='function')toast('Calendar invite downloaded ✓');};
window.m5AddIgnyte=function(){var L=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Optimum Portal//Events//EN','CALSCALE:GREGORIAN','METHOD:PUBLISH','BEGIN:VEVENT','UID:ignyte-fall-2026@ffloptimum','DTSTAMP:'+m5nowStamp(),'DTSTART;VALUE=DATE:20260910','DTEND;VALUE=DATE:20260911','SUMMARY:'+m5icsEsc('Ignyte Fall 2026 Sales Conference'),'DESCRIPTION:'+m5icsEsc('FFL Optimum — Ignyte Fall 2026 Sales Conference. Register: https://www.eventbrite.com/e/ignyte-fall-2026-sales-conference-tickets-1990889795973'),'LOCATION:TBC','URL:https://www.eventbrite.com/e/ignyte-fall-2026-sales-conference-tickets-1990889795973','BEGIN:VALARM','TRIGGER:-P1D','ACTION:DISPLAY','DESCRIPTION:Ignyte is tomorrow','END:VALARM','END:VEVENT','END:VCALENDAR'];m5download('ignyte-fall-2026.ics',L.join('\r\n'));if(typeof toast==='function')toast('Calendar invite downloaded ✓');};
window.m5AddConvention=function(){var L=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Optimum Portal//Events//EN','CALSCALE:GREGORIAN','METHOD:PUBLISH','BEGIN:VEVENT','UID:ffl-annual-convention-2027@ffloptimum','DTSTAMP:'+m5nowStamp(),'DTSTART;VALUE=DATE:20270127','DTEND;VALUE=DATE:20270131','SUMMARY:'+m5icsEsc('2027 FFL Annual Convention'),'DESCRIPTION:'+m5icsEsc('Family First Life Annual Convention — Irving, Texas. Register: https://familyfirstlife.com/annualconvention/'),'LOCATION:'+m5icsEsc('Irving, Texas'),'URL:https://familyfirstlife.com/annualconvention/','BEGIN:VALARM','TRIGGER:-P1W','ACTION:DISPLAY','DESCRIPTION:FFL Annual Convention next week','END:VALARM','END:VEVENT','END:VCALENDAR'];m5download('ffl-annual-convention-2027.ics',L.join('\r\n'));if(typeof toast==='function')toast('Calendar invite downloaded ✓');};
window.m5IgnyteTarget=new Date(2026,8,10,0,0,0);
window.m5ConvTarget=new Date(2027,0,27,0,0,0);
window.m5cdRender=function(el,target){var ms=target-new Date();if(ms<=0){el.innerHTML='<div class="u"><div class="n">Now</div><div class="l">Live</div></div>';return;}var s=Math.floor(ms/1000),d=Math.floor(s/86400),h=Math.floor(s%86400/3600),m=Math.floor(s%3600/60),ss=s%60;function u(n,l){return '<div class="u"><div class="n">'+n+'</div><div class="l">'+l+'</div></div>';}el.innerHTML=u(d,'Days')+u(m5pad2(h),'Hrs')+u(m5pad2(m),'Min')+u(m5pad2(ss),'Sec');};
window.m5EvTick=function(){var a=document.getElementById('m5-cd-ignyte');if(a)window.m5cdRender(a,window.m5IgnyteTarget);var b=document.getElementById('m5-cd-conv');if(b)window.m5cdRender(b,window.m5ConvTarget);};
if(!window.m5EvInt){window.m5EvInt=setInterval(function(){window.m5EvTick();},1000);}

/* ================= AGENCY DASHBOARD (scoped to your downline) ================= */
/* Resources: which carriers take which alternative payment methods */
window.m5PaymentsPanel=function(){
  function grp(title,carriers){ return '<div style="margin-top:15px"><div style="font-size:12px;font-weight:800;color:#a9861d;text-transform:uppercase;letter-spacing:.05em;margin-bottom:9px">'+title+'</div><div style="display:flex;flex-wrap:wrap;gap:8px">'+carriers.map(function(c){ return '<span style="background:#f2f5fb;border:1px solid #e3e8f2;border-radius:999px;padding:7px 14px;font-size:13px;font-weight:600;color:#16233f">'+c+'</span>'; }).join('')+'</div></div>'; }
  return '<div class="listcard" style="margin-top:16px"><h3>💳 Who takes Direct Express / Chime / Cash App?</h3><div class="lc-sub">Carriers that accept these payment methods.</div>'
    + grp('Direct Express', ['Corebridge','Transamerica','Instabrain'])
    + grp('Chime / Cash App', ['American Amicable','Transamerica','Instabrain','Aflac','Aetna','Ethos'])
    + '</div>';
};
/* Resources: Product Playbooks — IUL, Mortgage Protection, Annuities */
window.m5ProductPanel=function(){
  function lk(l,d,url){ return '<a class="m5-row" href="'+url+'" target="_blank" rel="noopener"><span class="ri"></span><span class="m5-rtext"><span class="rl">'+l+'</span>'+(d?'<span class="rd">'+d+'</span>':'')+'</span><span class="ra">↗</span></a>'; }
  function sh(t){ return '<div style="font-size:11.5px;font-weight:800;color:#a9861d;text-transform:uppercase;letter-spacing:.04em;margin:14px 0 6px 2px">'+t+'</div>'; }
  function nt(html){ return '<div style="font-size:12.5px;color:#55617d;line-height:1.55;margin:6px 0;padding:10px 12px;background:#f7f9fc;border-left:3px solid #dbe3f0;border-radius:8px">'+html+'</div>'; }
  function sec(icon,title,inner){ return '<div class="m5-seclabel" style="margin-top:24px">'+icon+' '+title+'</div><div class="m5-list">'+inner+'</div>'; }
  var MAIL='<a href="mailto:Support@fflnational.com">Support@fflnational.com</a>';
  var CC='<a href="mailto:wealthbuildersgroupllc@gmail.com">wealthbuildersgroupllc@gmail.com</a>';
  var iul=''
    + lk('IUL Explainer Video (Optimum-branded)','','https://youtu.be/fKs0Lho_Sb0')
    + lk('Epic IUL Overview — Dan','One of the best IUL educators — great overview plus a deeper dive.','https://www.youtube.com/watch?v=Ik1_Q0iicxU')
    + lk('IUL Script','Built for a 1-call close where appropriate — pivot to a structured meeting when needed.','https://docs.google.com/document/d/1SyIokJ963Ruj9bRMFlhE0UST5ObJ5YWeRZCS2MII9Ls/edit?usp=sharing')
    + lk('IUL Decision Tree','Which IUL company or product to write — start here.','https://drive.google.com/file/d/157kcSaRkBH5bR37ZiRPgM5ypCgr0sKNR/view?usp=sharing')
    + sh('Contracting to write NLG or F&amp;G')
    + nt('<b>National Life Group (NLG):</b> head to <b>SureLC</b> (via the Gateway) and request NLG contracting.')
    + nt('<b>Fidelity &amp; Guaranty (F&amp;G):</b> email '+MAIL+' and CC '+CC+', and ask to contract with F&amp;G.')
    + sh('Good people to follow')
    + lk('Doug Andrew (YouTube)','Good IUL info — no need to pay for any courses.','https://www.youtube.com/@missedfortune')
    + lk('David McKnight (YouTube)','Building tax-free money for the future and retirement.','https://www.youtube.com/@DavidMcKnight')
    + sh('National Life Group illustrations')
    + lk('Max DB — Focus Flex Life illustration','','https://www.loom.com/share/8385237c46e14910b1ff9b47f11a85bc')
    + lk('Minimum DB / Max Cash — Flex Life illustration','','https://www.loom.com/share/b90a23619484438f84e4fa438112f3a5')
    + lk('General NLG Basic Illustration','','https://drive.google.com/file/d/1cWqnw1-ZfQdROqDr3RgrVY6-Z090kZK6/view?usp=sharing')
    + sh('Carrier sites &amp; training')
    + lk('Transamerica IUL site','','https://www.transamerica.com/ffiul2-express?SubscriberID=45173604&MID=523010189&SubscriberKey=0033s000012jEC3AAM&BatchID=1&DataSource=ANTY_TSIA_Wells_Fargo_RBC_NY-June25')
    + lk('SRS (Simplified Retirement Solutions) — all recordings','','https://www.youtube.com/playlist?list=PLsM9LUd7nnb5m-i5JycNwMpsxb--UfHt5')
    + lk('Americo IUL training site','','https://americoiul.com/');
  var book=''
    + lk('Money, Wealth, Life Insurance — PDF','Read it, listen to it, and send it to clients.','https://drive.google.com/file/d/15PzFArtvvAIGaiVeyjZvCDKRAlj9ETpS/view?usp=sharing')
    + lk('Money, Wealth, Life Insurance — Audiobook','','https://drive.google.com/file/d/1q1W-3EK197gpOFJn9l8VX-bxjShUzUKx/view?usp=sharing');
  var mp=''
    + lk('Quintessential MP Overview — John Wetmore','','https://www.youtube.com/watch?v=egJ-vjY1vnw')
    + lk('Mortgage Protection Script','','https://docs.google.com/document/d/1A1Ne23k4X-FdGi99Ks_LMmh0wj1MVWaqDZNVK0u6xi0/edit?tab=t.0');
  var ann=''
    + lk('Learn Annuities from the GOAT','Integrity Annuity Training Program.','https://integrityannuitytrainingprogram.com/')
    + sh('Contracting')
    + nt('<b>Athene (our main FIA carrier):</b> email '+MAIL+' and CC '+CC+', and ask to contract with Athene.');
  return '<div class="listcard" style="margin-top:16px"><h3>📚 Product Playbooks</h3><div class="lc-sub">Everything by product — training, scripts, illustrations, and contracting steps.</div>'
    + sec('📈','IUL', iul)
    + sec('📖','Recommended read — Money, Wealth, Life Insurance', book)
    + sec('🏠','Mortgage Protection', mp)
    + sec('💰','Annuities', ann)
    + '</div>';
};
window.m5Ag={loaded:false,err:'',agents:[],popularity:{},filter:'all',sortKey:'joined',sortDir:-1,q:'',refreshing:false,lastSync:0};
/* Lightweight engagement counter — bumps a per-section counter on nav. Guarded; never throws into nav. */
window.m5TrackSection=function(view){
  try{
    if(typeof store==='undefined'||!store.data) return;
    if(!view||view==='dashboard'||view==='agency') return;
    if(store.data.admin===true) return;
    if(!store.data.sectionOpens||typeof store.data.sectionOpens!=='object') store.data.sectionOpens={};
    store.data.sectionOpens[view]=(store.data.sectionOpens[view]||0)+1;
    if(typeof store.save==='function') store.save();
  }catch(e){}
};
window.m5AgIsAdmin=function(){ return (typeof store!=='undefined'&&store.data&&store.data.admin===true); };
/* Team size = everyone the backend returned for you, minus yourself. The backend now
   scopes the roster to your downline, so this is your team and nobody else's. */
window.m5AgTeamSize=function(){
  var me=((typeof store!=='undefined'&&store.data&&store.data.email)||'').trim().toLowerCase();
  var a=m5Ag.agents||[], n=0;
  for(var i=0;i<a.length;i++){ if(String(a[i].email||'').trim().toLowerCase()!==me) n++; }
  return n;
};
window.m5AgHead=function(){
  return '<h1 class="page"><span data-ico="dash" style="vertical-align:-3px"></span> Agency Dashboard</h1>'
       + '<p class="sub">'+(m5AgIsAdmin()?'Your team\'s live progress, straight from your sheet.'
                                         :'Where you track everyone you bring into the business.')+'</p>';
};
/* Shown to anyone whose downline is empty. Never a bare table with no rows — that reads
   as broken. This reads as an invitation. */
window.m5AgEmpty=function(){
  return '<div class="agz">'
    + '<span class="agz-kick">Nothing here yet</span>'
    + '<h2>You haven\'t recruited anyone — yet.</h2>'
    + '<p>The day you do, this page fills up: whether they\'ve logged in, how far along their license is, whether they\'ve started Fast Start, and if they\'re actually dialing.</p>'
    + '<div class="agz-ctas">'
      + '<a class="agz-cta gold" onclick="go(\'agencybuild\')"><span class="a">→</span><span class="t">Check out the Agency Builder</span><span class="d">See exactly what a team does to your income — the override cascade, run on your own numbers.</span></a>'
      + '<a class="agz-cta ghost" onclick="go(\'recruiting\')"><span class="a">→</span><span class="t">Not sure how to recruit?</span><span class="d">Scripts, talk tracks, who to approach and what to say — it\'s all on the Recruiting tab.</span></a>'
    + '</div></div>'
    + '<div class="agz-prev"><p class="agz-prevh">What shows up here once you do</p>'
    + '<div class="ag-card agz-ghost">'
      + '<div class="agz-stats"><div class="agz-stat"><b>3</b><span>Team</span></div><div class="agz-stat"><b>2</b><span>Licensed</span></div><div class="agz-stat"><b>1</b><span>Dialing</span></div></div>'
      + '<table class="agz-tbl"><thead><tr><th>Agent</th><th>Status</th><th>License</th></tr></thead><tbody>'
      + '<tr><td class="nm">Dana W.</td><td><span class="agz-pill lic">Licensed</span></td><td><div class="agz-bar"><i class="g" style="width:100%"></i></div></td></tr>'
      + '<tr><td class="nm">Marcus T.</td><td><span class="agz-pill pre">Pre-lic</span></td><td><div class="agz-bar"><i style="width:50%"></i></div></td></tr>'
      + '<tr><td class="nm">Priya N.</td><td><span class="agz-pill lic">Licensed</span></td><td><div class="agz-bar"><i class="g" style="width:100%"></i></div></td></tr>'
      + '</tbody></table></div></div>';
};
window.m5AgencyDash=function(){
  var adm=m5AgIsAdmin();
  var cached=(typeof store!=='undefined'&&store.data&&typeof store.data.teamCount==='number')?store.data.teamCount:null;
  /* Someone we already know has no team gets the splash instantly — no roster call and no
     six-second wait to be told they have nobody. We still refresh quietly underneath in
     case they have recruited since last time. */
  if(!adm && !m5Ag.loaded && cached===0){ m5AgFetch(true); return m5AgHead()+m5AgEmpty(); }
  if(!m5Ag.loaded){ m5AgFetch(); return m5AgHead()+'<div class="ag-load">Loading your team…</div>'; }
  if(m5Ag.err) return m5AgHead()+'<div class="ag-load">'+(m5Ag.err==='forbidden'?'We could not match your login to the roster. Let Jesse know and he will get it sorted.':'Network issue — reopen this page in a moment.')+'</div>';
  if(!adm && m5AgTeamSize()===0) return m5AgHead()+m5AgEmpty();
  return m5AgRender();
};
// Collapse a person split across two rows by an email/phone change: same full name,
// where one row carries progress (loggedIn) and the other doesn't. Keeps the current-email
// (intake) row and overlays the progress from the stale-email row.
window.m5AgDedupe=function(agents){
  agents=agents||[];
  var DROP_EMAILS={'ckocis0429@gmail.com':1};  // stray duplicate registration rows to hide
  agents=agents.filter(function(a){ return !DROP_EMAILS[String(a.email||'').trim().toLowerCase()]; });
  var groups={};
  for(var i=0;i<agents.length;i++){
    var nk=String(agents[i].name||'').trim().toLowerCase().replace(/\s+/g,' ');
    if(!nk||nk.indexOf(' ')<0) continue;
    (groups[nk]=groups[nk]||[]).push(i);
  }
  var drop={};
  for(var nk in groups){
    var g=groups[nk]; if(g.length!==2) continue;
    var a=agents[g[0]], b=agents[g[1]];
    if(!!a.loggedIn===!!b.loggedIn) continue;   // only the "one has progress, one doesn't" case
    var base=a.loggedIn?b:a, prog=a.loggedIn?a:b, dropIdx=a.loggedIn?g[0]:g[1];
    base.loggedIn=true;
    base.licensed=base.licensed||prog.licensed;
    base.firstLogin=prog.firstLogin||base.firstLogin||'';
    base.lastLogin=prog.lastLogin||base.lastLogin||'';
    ['gylPct','fsPct','acadPct','daysToLic'].forEach(function(k){ if(base[k]===''||base[k]==null) base[k]=prog[k]; });
    base.appliedOn=base.appliedOn||prog.appliedOn||'';
    base.npnOn=base.npnOn||prog.npnOn||'';
    base.gcUsing=base.gcUsing||prog.gcUsing;
    base.gcCards=Math.max(base.gcCards||0,prog.gcCards||0);
    base.gcCards30=Math.max(base.gcCards30||0,prog.gcCards30||0);
    drop[dropIdx]=true;
  }
  var out=[]; for(var i=0;i<agents.length;i++){ if(!drop[i]) out.push(agents[i]); }
  return out;
};
/* silent=true means the splash is already on screen and we are only checking whether
   they have recruited since last time. In that mode we never repaint over the splash
   unless there is now somebody to show, and a failed check leaves the splash alone
   rather than replacing it with an error. */
window.m5AgFetch=function(silent){
  /* Both the Agency page AND the dashboard recruit cards wait on this fetch, so repaint
     whichever of the two is actually on screen. Hardcoding 'agency' here meant the roster
     landed for a recruiter sitting on their dashboard and nothing ever redrew. */
  var repaint=function(){
    try{
      if(typeof currentView!=='function'||typeof render!=='function') return;
      var v=currentView();
      if(v==='agency'||v==='dashboard') render(v);
    }catch(e){}
  };
  try{
    if(typeof BACKEND_URL==='undefined'||!BACKEND_URL){ m5Ag.loaded=true; m5Ag.err='network'; return; }
    var email=((store.data&&store.data.email)||'').trim().toLowerCase();
    var phone=(store.data&&store.data.phone)||'';
    fetch(BACKEND_URL,{method:'POST',body:JSON.stringify({action:'roster',email:email,phone:phone})})
      .then(function(r){return r.json();})
      .then(function(j){
        m5Ag.loaded=true;
        if(j&&j.ok){
          m5Ag.agents=m5AgDedupe(j.agents||[]); m5Ag.popularity=j.popularity||{}; m5Ag.err=''; m5Ag.lastSync=Date.now();
          /* Cache the team size so the next visit knows instantly whether to show the
             splash, instead of making everyone wait on a roster call to find out. */
          try{ store.data.teamCount=m5AgTeamSize(); if(typeof store.save==='function') store.save(); }catch(e){}
        } else { m5Ag.err=(j&&j.error)||'error'; }
        if(silent && (m5Ag.err || m5AgTeamSize()===0)) return;   /* splash stays put */
        repaint();
      })
      .catch(function(){ m5Ag.loaded=true; m5Ag.err='network'; if(!silent) repaint(); });
  }catch(e){ m5Ag.loaded=true; m5Ag.err='network'; }
};
// Re-pull the roster on demand (button), without touching login or navigation.
window.m5AgRefresh=function(){
  if(m5Ag.refreshing) return;
  m5Ag.refreshing=true;
  var btn=document.getElementById('m5ag-refresh');
  if(btn){ btn.disabled=true; btn.setAttribute('data-busy','1'); btn.innerHTML='<span class="ag-spin"></span> Refreshing…'; }
  var done=function(){ m5Ag.refreshing=false; if(typeof currentView==='function'&&currentView()==='agency'&&typeof render==='function') render('agency'); };
  try{
    if(typeof BACKEND_URL==='undefined'||!BACKEND_URL){ done(); return; }
    var email=((store.data&&store.data.email)||'').trim().toLowerCase();
    var phone=(store.data&&store.data.phone)||'';
    fetch(BACKEND_URL,{method:'POST',body:JSON.stringify({action:'roster',email:email,phone:phone})})
      .then(function(r){return r.json();})
      .then(function(j){ if(j&&j.ok){ m5Ag.agents=m5AgDedupe(j.agents||[]); m5Ag.popularity=j.popularity||{}; m5Ag.err=''; m5Ag.lastSync=Date.now(); try{ store.data.teamCount=m5AgTeamSize(); if(typeof store.save==='function') store.save(); }catch(e){} } else { m5Ag.err=(j&&j.error)||'error'; } done(); })
      .catch(function(){ done(); });
  }catch(e){ done(); }
};
function m5AgSyncLabel(){
  if(!m5Ag.lastSync) return '';
  var s=Math.round((Date.now()-m5Ag.lastSync)/1000);
  if(s<10) return 'Updated just now';
  if(s<60) return 'Updated '+s+'s ago';
  var m=Math.floor(s/60); if(m<60) return 'Updated '+m+(m===1?' min ago':' mins ago');
  var h=Math.floor(m/60); return 'Updated '+h+(h===1?' hr ago':' hrs ago');
}
window.m5AgSet=function(f){ m5Ag.filter=f; if(typeof render==='function') render('agency'); };
window.m5AgSort=function(k){ if(m5Ag.sortKey===k){ m5Ag.sortDir*=-1; } else { m5Ag.sortKey=k; m5Ag.sortDir=1; } if(typeof render==='function') render('agency'); };
function m5AgDays(iso){ if(!iso)return null; var d=new Date(iso); if(isNaN(d.getTime()))return null; return Math.floor((Date.now()-d.getTime())/864e5); }
function m5AgDiff(a,b){ if(!a||!b)return null; var d1=new Date(a),d2=new Date(b); if(isNaN(d1.getTime())||isNaN(d2.getTime()))return null; return Math.round((d2.getTime()-d1.getTime())/864e5); }
function m5AgNum(v){ if(v===''||v==null)return null; var n=Number(v); return isNaN(n)?null:n; }
function m5AgFilt(){ var q=(m5Ag.q||'').trim().toLowerCase(); return (m5Ag.agents||[]).filter(function(a){ if(q && String(a.name||'').toLowerCase().indexOf(q)<0) return false; if(m5Ag.filter==='lic')return a.licensed; if(m5Ag.filter==='unl')return !a.licensed; if(m5Ag.filter==='active'){var d=m5AgDays(a.lastLogin);return d!=null&&d<=7;} return true; }); }
window.m5AgSearch=function(v){ m5Ag.q=v; var tb=document.getElementById('m5ag-tbody'); if(tb) tb.innerHTML=m5AgRows(); var c=document.getElementById('m5ag-count'); if(c) c.textContent=m5AgFilt().length; };
function m5AgRows(){
  var A=m5AgFilt().slice();
  var k=m5Ag.sortKey, dir=m5Ag.sortDir;
  A.sort(function(a,b){ var va=m5AgSortVal(a,k), vb=m5AgSortVal(b,k); if(va<vb)return -1*dir; if(va>vb)return 1*dir; return 0; });
  if(!A.length) return '<tr><td colspan="10" style="text-align:center;padding:22px;color:#8a93a9">No agents match that search.</td></tr>';
  return A.map(function(a){
    var lic=a.licensed;
    var licCell= lic? '<span style="color:#1f7a44;font-weight:800">✓</span>' : m5AgMiniBar(m5AgNum(a.gylPct),'#2f6df0');
    var fsCell= lic? m5AgMiniBar(m5AgNum(a.fsPct),'#1f9d55') : '—';
    var acCell= lic? m5AgMiniBar(m5AgNum(a.acadPct),'#c9a227') : '—';
    var last= a.lastLogin? m5AgAgo(a.lastLogin) : '<span style="color:#b5561f">Never logged in</span>';
    var rec= m5AgRecruiter(a);
    var recCell= rec? m5AgEsc(rec) : '<span style="color:#b7bfce">—</span>';
    return '<tr><td><b>'+m5AgEsc(a.name)+'</b></td><td>'+recCell+'</td><td><span class="ag-pill '+(lic?'lic':'unl')+'">'+(lic?'Licensed':'Unlicensed')+'</span></td><td>'+m5AgDate(a.joined)+'</td><td>'+(a.source==='Manual'?'Manual':'Form')+'</td><td>'+licCell+'</td><td>'+fsCell+'</td><td>'+acCell+'</td><td>'+last+'</td><td>'+(a.gcCards||0)+'</td></tr>';
  }).join('');
}
function m5AgEsc(s){ return String(s==null?'':s).replace(/[&<>]/g,function(c){return ({'&':'&amp;','<':'&lt;','>':'&gt;'})[c];}); }
function m5AgDate(iso){ if(!iso)return '—'; var d=new Date(iso); if(isNaN(d.getTime()))return '—'; return d.toLocaleDateString('en-US',{month:'short',day:'numeric'}); }
function m5AgAgo(iso){ var d=m5AgDays(iso); if(d==null)return '—'; if(d<=0)return 'Today'; if(d===1)return 'Yesterday'; if(d<30)return d+' days ago'; return m5AgDate(iso); }
function m5AgFB(f,lab){ return '<button class="ag-fbtn'+(m5Ag.filter===f?' on':'')+'" onclick="m5AgSet(\''+f+'\')">'+lab+'</button>'; }
function m5AgStat(k,v,s){ return '<div class="ag-stat"><div class="k">'+k+'</div><div class="v">'+v+'</div>'+(s?'<div class="s">'+s+'</div>':'')+'</div>'; }
function m5AgFunnel(rows,total){
  return rows.map(function(r){ var pct= total? Math.round(r[1]/total*100):0;
    return '<div class="ag-funnel-row"><div class="ag-funnel-lab">'+r[0]+'</div><div class="ag-funnel-bar"><div class="ag-funnel-fill" style="width:'+Math.max(pct,4)+'%;background:'+r[2]+'">'+r[1]+'</div></div><div class="ag-funnel-pct">'+pct+'%</div></div>';
  }).join('');
}
function m5AgMix(l1,v1,l2,v2,c1,c2){
  var t=(v1+v2)||1; var p1=Math.round(v1/t*100), p2=100-p1;
  return '<div class="ag-mixbar"><div class="ag-mixseg" style="width:'+p1+'%;background:'+c1+'">'+(p1>12?p1+'%':'')+'</div><div class="ag-mixseg" style="width:'+p2+'%;background:'+c2+'">'+(p2>12?p2+'%':'')+'</div></div><div class="ag-legend"><span><span class="ag-dot" style="background:'+c1+'"></span>'+l1+' · '+v1+'</span><span><span class="ag-dot" style="background:'+c2+'"></span>'+l2+' · '+v2+'</span></div>';
}
function m5AgBucket(vals,edges){ var counts=[]; for(var i=0;i<=edges.length;i++)counts.push(0); vals.forEach(function(v){ var placed=false; for(var i=0;i<edges.length;i++){ if(v<=edges[i]){counts[i]++;placed=true;break;} } if(!placed)counts[counts.length-1]++; }); return counts; }
function m5AgTimeCard(title,sub,vals,labels,color,edges){
  edges=edges||[7,14,21,30,45];
  var counts=m5AgBucket(vals,edges);
  var avg= vals.length? Math.round(vals.reduce(function(s,x){return s+x;},0)/vals.length):0;
  var max=Math.max.apply(null,counts.concat([1]));
  var bars=counts.map(function(c,i){ var h=Math.round(c/max*100); return '<div class="ag-bar"><div class="bv">'+c+'</div><div class="bfill" style="height:'+Math.max(h,3)+'%;background:'+color+'"></div><div class="bl">'+(labels[i]||'')+'</div></div>'; }).join('');
  return '<div class="ag-card"><h3>'+title+'</h3><p class="sub">'+sub+'</p><div class="ag-big">'+avg+' <span style="font-size:14px;color:#8a93a9">days avg</span></div><div class="sub" style="margin:2px 0 0">'+(vals.length? vals.length+' with data':'no data yet')+'</div><div class="ag-bars">'+bars+'</div></div>';
}
function m5AgMiniBar(pct,color){ pct=(pct==null)?0:pct; return '<span class="ag-mini"><span style="width:'+Math.max(0,Math.min(100,pct))+'%;background:'+color+'"></span></span>'+pct+'%'; }
function m5AgEngScore(a){ return (a.logins||0)*3 + (a.sectionsUsed||0) + (a.gcCards||0); }
function m5AgTopEngagers(){
  var A=(m5Ag.agents||[]).filter(function(a){return a.loggedIn;}).map(function(a){ return {a:a,s:m5AgEngScore(a)}; }).filter(function(x){return x.s>0;});
  A.sort(function(x,y){return y.s-x.s;});
  var top=A.slice(0,5); var max=top.length?top[0].s:1; var body;
  if(!top.length){ body='<div class="ag-soon" style="padding:16px"><div class="t">No engagement yet</div>As agents log in and open sections, your most active people rank here.</div>'; }
  else { body=top.map(function(x,i){ var a=x.a; return '<div class="ag-eng"><div class="ag-engn">'+(i+1)+'</div><div style="flex:1;min-width:0"><div class="ag-engname">'+m5AgEsc(a.name)+'</div><div class="ag-engmeta">'+(a.licensed?'Licensed':'Unlicensed')+' · '+(a.logins||0)+' logins · '+(a.sectionsUsed||0)+' sections · '+(a.gcCards||0)+' cards</div><div class="ag-engbarwrap"><span style="width:'+Math.round(x.s/max*100)+'%"></span></div></div><div class="ag-engscore">'+x.s+'</div></div>'; }).join(''); }
  return '<div class="ag-card"><h3>Top engagers</h3><p class="sub">Ranked by logins, sections opened &amp; Goal Card activity.</p>'+body+'</div>';
}
function m5AgNavLabel(v){ try{ if(typeof NAV!=='undefined'){ for(var i=0;i<NAV.length;i++){ if(NAV[i].v===v) return NAV[i].t; } } }catch(e){} return v; }
function m5AgPopular(){
  var pop=m5Ag.popularity||{}; var arr=[]; for(var k in pop){ if(pop.hasOwnProperty(k)) arr.push([k,pop[k]]); }
  arr.sort(function(a,b){return b[1]-a[1];}); arr=arr.slice(0,10);
  var max=arr.length?arr[0][1]:1; var body;
  if(!arr.length){ body='<div class="ag-soon" style="padding:16px"><div class="t">No section opens tracked yet</div>Once agents start moving around the portal, the sections they open most show up here.</div>'; }
  else { body=arr.map(function(r){ return '<div class="ag-poprow"><div class="ag-poplab">'+m5AgEsc(m5AgNavLabel(r[0]))+'</div><div class="ag-popbar"><span style="width:'+Math.round(r[1]/max*100)+'%"></span></div><div class="ag-popval">'+r[1]+'</div></div>'; }).join(''); }
  return '<div class="ag-card" style="margin-bottom:18px"><h3>What\'s popular</h3><p class="sub">Which portal sections agents open most — what\'s landing, and what to promote.</p>'+body+'</div>';
}
function m5AgSortVal(a,k){
  if(k==='statusS')return a.licensed?1:0;
  if(k==='licV')return a.licensed?101:(m5AgNum(a.gylPct)||0);
  if(k==='fsV')return m5AgNum(a.fsPct)||0;
  if(k==='acV')return m5AgNum(a.acadPct)||0;
  if(k==='lastV')return a.lastLogin?(new Date(a.lastLogin)).getTime():0;
  if(k==='joined')return a.joined?(new Date(a.joined)).getTime():0;
  if(k==='gcCards')return a.gcCards||0;
  if(k==='source')return a.source||'';
  if(k==='recruiter')return m5AgRecruiter(a).toLowerCase();
  return (a.name||'').toLowerCase();
}
function m5AgRecruiter(a){
  /* The hand-typed override table that used to sit here is gone (19 Aug 2026). Every one
     of those eight people now carries a correct Recruiter Email in Portal Registrations,
     verified by auditDownline, so the sheet is the only source of truth. Fix a recruiter
     in the sheet and a refresh picks it up — no rebuild. */
  // Real recruiter from the Portal Registrations sheet (via backend payload).
  var rf=String(a.recruiterFirst||'').trim(), rl=String(a.recruiterLast||'').trim();
  if(rf||rl) return (rf+' '+rl).trim();
  // 3) Fallbacks: self-registered via the form defaults to Jesse; otherwise blank.
  if((a.source||'')==='Form')return 'Jesse Stamm';
  return '';
}
function m5AgTable(){
  var k=m5Ag.sortKey, dir=m5Ag.sortDir;
  var cols=[['name','Agent'],['recruiter','Recruiter'],['statusS','Status'],['joined','Joined'],['source','Source'],['licV','① License'],['fsV','② Fast Start'],['acV','③ Academy'],['lastV','Last active'],['gcCards','Goal cards']];
  var head=cols.map(function(c){ var arrow=(k===c[0])?(dir>0?' ▲':' ▼'):''; return '<th onclick="m5AgSort(\''+c[0]+'\')">'+c[1]+arrow+'</th>'; }).join('');
  var n=m5AgFilt().length;
  var search='<input id="m5ag-search" type="search" placeholder="🔎 Search name…" value="'+m5AgEsc(m5Ag.q||'')+'" oninput="m5AgSearch(this.value)" style="padding:9px 13px;border:1px solid #dbe2ee;border-radius:10px;font-size:13.5px;min-width:210px;font-family:inherit;outline:none;background:#fff">';
  return '<div class="ag-card" style="padding:0;overflow:hidden"><div style="padding:16px 20px 10px"><div style="display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap"><h3 style="margin:0">'+(m5AgIsAdmin()?'Agent roster':'Your team')+'</h3>'+search+'</div><p class="sub" style="margin:6px 0 0">'+(m5AgIsAdmin()?'Every agent':'Everyone you have recruited')+', all three tracks side by side. Click any column to sort. Showing <span id="m5ag-count">'+n+'</span>.</p></div><div class="ag-tablewrap"><table class="ag-table"><thead><tr>'+head+'</tr></thead><tbody id="m5ag-tbody">'+m5AgRows()+'</tbody></table></div></div>';
}
function m5AgRender(){
  var A=m5Ag.agents||[];
  var total=A.length;
  var loggedIn=A.filter(function(a){return a.loggedIn;}).length;
  var licensed=A.filter(function(a){return a.licensed;}).length;
  var unlic=total-licensed;
  var active7=A.filter(function(a){var d=m5AgDays(a.lastLogin);return d!=null&&d<=7;}).length;
  var li=A.filter(function(a){return a.loggedIn;});
  var avgComp= li.length? Math.round(li.reduce(function(s,a){ var p= a.licensed? (m5AgNum(a.fsPct)||0) : (m5AgNum(a.gylPct)||0); return s+p; },0)/li.length):0;
  var fFs=A.filter(function(a){return (m5AgNum(a.fsPct)||0)>=100;}).length;
  var fAc=A.filter(function(a){return (m5AgNum(a.acadPct)||0)>=100;}).length;
  var srcMan=A.filter(function(a){return a.source==='Manual';}).length;
  var srcForm=total-srcMan;
  var licDays=A.map(function(a){ return m5AgDiff(a.firstLogin, a.npnOn||a.appliedOn); }).filter(function(x){return x!=null&&x>=0;});
  var fsDays=A.map(function(a){return m5AgNum(a.fsDays);}).filter(function(x){return x!=null&&x>=0;});
  var acDays=A.map(function(a){return m5AgNum(a.acadDays);}).filter(function(x){return x!=null&&x>=0;});
  var gcUsing=A.filter(function(a){return a.gcUsing;}).length;
  var gcCards30=A.reduce(function(s,a){return s+(a.gcCards30||0);},0);
  var h='<div class="ag-wrap">';
  h+='<div class="ag-head"><div><h1 class="page" style="margin:0"><span data-ico="dash" style="vertical-align:-3px"></span> Agency Dashboard</h1><p class="sub" style="margin:4px 0 0">Your whole team\'s progress, live from your sheet · '+total+' agents on the roster.</p></div><div class="ag-headr"><button id="m5ag-refresh" class="ag-refresh" onclick="m5AgRefresh()"'+(m5Ag.refreshing?' disabled':'')+'>'+(m5Ag.refreshing?'<span class="ag-spin"></span> Refreshing…':'↻ Refresh')+'</button>'+(m5AgSyncLabel()?'<span class="ag-synced">'+m5AgSyncLabel()+'</span>':'')+'</div></div>';
  h+='<div class="ag-filters">'+m5AgFB('all','All agents')+m5AgFB('lic','Licensed')+m5AgFB('unl','Unlicensed')+m5AgFB('active','Active (7d)')+'</div>';
  h+='<div class="ag-stats">'
    +m5AgStat('Total agents',total,'on the roster')
    +m5AgStat('Logged in',loggedIn,total?Math.round(loggedIn/total*100)+'% of roster':'')
    +m5AgStat('Licensed',licensed,'')
    +m5AgStat('Unlicensed',unlic,'in the pipeline')
    +m5AgStat('Active (7d)',active7,'logged in this week')
    +m5AgStat('Avg completion',avgComp+'%','of logged-in agents')
    +'</div>';
  h+='<div class="ag-grid2">';
  h+='<div class="ag-card"><h3>Onboarding funnel</h3><p class="sub">Where the roster sits — and where people fall off.</p>'
    +m5AgFunnel([['Added to portal',total,'#16233f'],['Logged in',loggedIn,'#2f6df0'],['Got licensed',licensed,'#3f7be0'],['Fast Start done',fFs,'#5a93e6'],['Academy done',fAc,'#8fbaf0']],total)+'</div>';
  h+='<div class="ag-card"><h3>Roster mix</h3><p class="sub">Licensed vs unlicensed, and how they arrived.</p>'
    +m5AgMix('Licensed',licensed,'Unlicensed',unlic,'#2f6df0','#e67a3a')+'<div style="height:10px"></div>'
    +m5AgMix('Self-registered',srcForm,'Manual add',srcMan,'#1f9d55','#c9a227')+'</div>';
  h+='</div>';
  h+='<div class="ag-grid3">';
  h+=m5AgTimeCard('① Time to get licensed','First login → NPN entered.',licDays,['0-7','8-14','15-21','22-30','31-45','45+'],'#2f6df0');
  h+=m5AgTimeCard('② Time through Fast Start','License → Fast Start done.',fsDays,['0-3','4-7','8-14','15-21','22-30','30+'],'#1f9d55',[3,7,14,21,30]);
  h+=m5AgTimeCard('③ Time through Academy','First login → Academy complete.',acDays,['0-7','8-14','15-21','22-30','31-45','45+'],'#c9a227');
  h+='</div>';
  h+='<div class="ag-grid2">';
  h+=m5AgTopEngagers();
  h+='<div class="ag-card"><h3>Goal Card adoption</h3><p class="sub">Who\'s planning &amp; logging their activity.</p><div style="display:flex;gap:32px;flex-wrap:wrap"><div><div class="ag-big">'+gcUsing+' <span style="font-size:15px;color:#8a93a9">/ '+total+'</span></div><div class="sub" style="margin-top:2px">using the Goal Card</div></div><div><div class="ag-big">'+gcCards30+'</div><div class="sub" style="margin-top:2px">cards logged (30d)</div></div></div></div>';
  h+='</div>';
  h+=m5AgPopular();
  h+=m5AgTable();
  h+='</div>';
  return h;
}

/* ===== Resources / Sales Tools search ===== */
function m5sEsc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'})[c];});}
function m5sHi(s,q){ s=m5sEsc(s); if(!q) return s; var i=s.toLowerCase().indexOf(q.toLowerCase()); if(i<0) return s; return s.slice(0,i)+'<mark>'+s.slice(i,i+q.length)+'</mark>'+s.slice(i+q.length); }
function m5sAct(url){
  if(!url||url==='#') return "";
  if(url.indexOf('go:')===0) return "go('"+url.slice(3)+"')";
  return "window.open('"+url.replace(/'/g,"\\'")+"','_blank')";
}
// direct-set section openers (avoid the toggle in openRes/openSales)
window.m5sOpenRes=function(k){ try{ resOpen=k; render('resources'); }catch(e){} };
window.m5sOpenSales=function(k){ try{ salesOpen=k; render('sales'); }catch(e){} };
window.m5sOpenCarrier=function(n){ try{ salesOpen='carriers'; carrierOpen=n; render('sales'); }catch(e){} };

// Build the searchable index for a scope. Each entry: {icon,title,desc,group,act}
// act is a JS string run on click.
function m5sIndex(scope){
  var out=[];
  function push(icon,title,desc,group,act){ out.push({icon:icon,title:title||'',desc:desc||'',group:group||'',act:act||''}); }
  if(scope==='res'){
    if(typeof RES_TILES==='undefined') return out;
    RES_TILES.forEach(function(t){
      if(t.link){ push(t.i,t.t,t.s,t.t,m5sAct(t.link)); return; }
      var rows = (t.reuse==='scripts' && typeof SCRIPTS_L!=='undefined') ? SCRIPTS_L : (t.items||[]);
      if(rows.length){
        rows.forEach(function(r){ push(t.i,r[0],r[1],t.t, r[2]?m5sAct(r[2]):"window.m5sOpenRes('"+t.k+"')"); });
        push(t.i,t.t,t.s,t.t,"window.m5sOpenRes('"+t.k+"')"); // section itself
      } else {
        push(t.i,t.t,t.s,t.t,"window.m5sOpenRes('"+t.k+"')"); // panel-only sections (videos, payments, products)
      }
    });
  } else if(scope==='selfdev'){
    if(typeof BOOKS!=='undefined'){ BOOKS.forEach(function(b){ push('📚',b.t,(b.by||''),'Books to Read', b.pdf?m5sAct(b.pdf):"toast('Opening Amazon…')"); }); }
    push('🎧','Jim Rohn — Building Your Network Marketing Business','Classic audio on building the business.','Things to Listen To',"toast('Link coming soon.')");
    push('🎧','Charisma on Command (YouTube)','Presence, connection & communication.','Things to Listen To',m5sAct('https://www.youtube.com/@Charismaoncommand'));
    push('▶️','Videos on Mindset & Motivation','Coming soon.','Videos on Mindset & Motivation',"toast('Coming soon.')");
    push('▶️','Family First Life Video Library','Coming soon.','Family First Life Video Library',"toast('Coming soon.')");
  } else {
    // sales
    var S=(typeof SCRIPTS_L!=='undefined')?SCRIPTS_L:[];
    var E=(typeof EAPP_L!=='undefined')?EAPP_L:[];
    var C=(typeof CE_L!=='undefined')?CE_L:[];
    var P=(typeof PRES_L!=='undefined')?PRES_L:[];
    var G=(typeof GUIDES!=='undefined')?GUIDES:[];
    var CA=(typeof CARRIERS!=='undefined')?CARRIERS:[];
    S.forEach(function(r){ push('📝',r[0],r[1],'Sales Scripts', r[2]?m5sAct(r[2]):"window.m5sOpenSales('scripts')"); });
    E.forEach(function(r){ push('💻',r[0],r[1],'Electronic Applications', r[2]?m5sAct(r[2]):"window.m5sOpenSales('eapp')"); });
    C.forEach(function(r){ push('🎓',r[0],r[1],'Continuing Education', r[2]?m5sAct(r[2]):"window.m5sOpenSales('ce')"); });
    P.forEach(function(r){ push('📊',r[0],r[1],'Presentation Materials', r[2]?m5sAct(r[2]):"window.m5sOpenSales('pres')"); });
    G.forEach(function(r){ push('🏢',r[0],'','Carrier Portals', m5sAct(r[1])); });
    CA.forEach(function(c){ push('🏢',c.name,(c.tags&&c.tags.length?c.tags.join(' · '):'')+(c.links&&c.links.length?' — '+c.links.length+' link'+(c.links.length===1?'':'s'):''),'Carrier Portals',"window.m5sOpenCarrier('"+String(c.name).replace(/'/g,"\\'")+"')"); });
    var TT=(typeof RES_TILES!=='undefined')?((RES_TILES.find(function(x){return x.k==='tools';})||{}).items||[]):[];
    TT.forEach(function(r){ push('🛠️',r[0],r[1],'Tools We Use', r[2]?m5sAct(r[2]):"window.m5sOpenSales('tools')"); });
    // section tiles themselves (so typing the tool name surfaces it)
    [['📝','Sales Scripts','All call scripts','scripts'],['🔁','Client Retention/Service','Copy-paste client touchpoints','retention'],['🛡️','Legacy Safeguard','Free end-of-life planning you offer clients','legacy'],['💻','Electronic Applications','Carrier e-app platforms','eapp'],['🏢','Carrier Portals','Portals, training, guides','carriers'],['🎓','Continuing Education','CE & compliance','ce'],['📊','Presentation Materials','Illustrations, needs analysis','pres'],['🖥️','Sales Presentations','Decks for every product','deck'],['🛠️','Tools We Use','Gear we recommend','tools']].forEach(function(t){ push(t[0],t[1],t[2],t[1],"window.m5sOpenSales('"+t[3]+"')"); });
  }
  return out;
}
window.m5SearchBox=function(scope){
  return '<div class="m5s-wrap"><span class="m5s-mag">🔎</span>'+
    '<input id="m5s-'+scope+'-input" type="search" autocomplete="off" placeholder="Search '+(scope==='res'?'resources':scope==='selfdev'?'self development':'sales tools')+' — by name or description…" oninput="m5Search(\''+scope+'\',this.value)">'+
    '<button class="m5s-clr" id="m5s-'+scope+'-clr" aria-label="Clear" onclick="m5SearchClear(\''+scope+'\')">✕</button></div>';
};
window.m5SearchClear=function(scope){ var i=document.getElementById('m5s-'+scope+'-input'); if(i){ i.value=''; i.focus(); } m5Search(scope,''); };
window.m5Search=function(scope,val){
  val=(val||'').trim();
  var results=document.getElementById('m5s-'+scope+'-results');
  var browse=document.getElementById('m5s-'+scope+'-browse');
  var clr=document.getElementById('m5s-'+scope+'-clr');
  if(clr) clr.className='m5s-clr'+(val?' show':'');
  if(!results) return;
  if(!val){ results.innerHTML=''; if(browse) browse.style.display=''; return; }
  if(browse) browse.style.display='none';
  var q=val.toLowerCase();
  var idx=m5sIndex(scope);
  var seen={}, hits=[];
  idx.forEach(function(e){
    if(e.title.toLowerCase().indexOf(q)>=0 || (e.desc||'').toLowerCase().indexOf(q)>=0 || e.group.toLowerCase().indexOf(q)>=0){
      var key=e.title+'|'+e.group; if(seen[key]) return; seen[key]=1; hits.push(e);
    }
  });
  if(!hits.length){
    results.innerHTML='<div class="m5s-empty"><div class="big">🔎</div>No matches for &ldquo;'+m5sEsc(val)+'&rdquo;.<br>Try a shorter word.</div>';
    return;
  }
  var rows=hits.map(function(e){
    var d=e.desc?'<div class="ld">'+m5sHi(e.desc,val)+'</div>':'';
    var grp=e.group?'<span class="m5s-grp">'+m5sEsc(e.group)+'</span>':'';
    var act=m5sEsc(e.act);
    return '<div class="li m5s-hit" onclick="'+act+'"><div><div class="lt">'+m5sHi(e.title,val)+grp+'</div>'+d+'</div>'+
      '<button class="openbtn" onclick="event.stopPropagation();'+act+'">Open</button></div>';
  }).join('');
  results.innerHTML='<div class="listcard"><div class="m5s-rescount">'+hits.length+' result'+(hits.length===1?'':'s')+' for &ldquo;'+m5sEsc(val)+'&rdquo;</div>'+rows+'</div>';
};
/* ==================== NEW-RECRUIT ACTION CARDS ====================
   Driven entirely by the scoped roster + the sheet. No hardcoded names.
   Backfill: anyone already here only gets a card if they joined in the last 30 days,
   so nobody opens the portal to a wall of stale cards. Anyone who joins from the ship
   date forward keeps their card until the checklist is finished or the recruiter
   kills it — the recruiter is always allowed to kill it. */
var M5_RC_EPOCH = Date.parse('2026-08-19T00:00:00Z');
var M5_RC_BACKFILL_DAYS = 30;

window.m5RcState=function(){
  if(!store.data.recruitCards||typeof store.data.recruitCards!=='object') store.data.recruitCards={};
  return store.data.recruitCards;
};
window.m5RcFor=function(em){ var s=m5RcState(); if(!s[em]||typeof s[em]!=='object') s[em]={}; return s[em]; };
function m5RcSave(){ try{ if(typeof store.save==='function') store.save(); }catch(e){} }
function m5RcRepaint(){ try{ if(typeof currentView==='function'&&currentView()==='dashboard'&&typeof render==='function') render('dashboard'); }catch(e){} }
function m5RcEsc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function m5RcNorm(s){ return String(s==null?'':s).trim().toLowerCase().replace(/\s+/g,' '); }
function m5RcFirst(a){ var n=String(a.name||'').trim().split(/\s+/)[0]; return n||'They'; }
function m5RcDays(iso){ var t=iso?Date.parse(iso):NaN; if(isNaN(t)) return null; return Math.floor((Date.now()-t)/864e5); }
function m5RcAgo(d){ if(d===null) return ''; if(d<=0) return 'today'; if(d===1) return 'yesterday'; if(d<30) return d+' days ago'; var m=Math.round(d/30); return m<=1?'a month ago':m+' months ago'; }

/* ---- messages (names swap in) ---- */
function m5RcMsg(kind,n,d){
  d=(typeof d==='number'&&d>0)?d:0;
  var M={
  u1:"Hey "+n+" — really glad you're on board.\n\nQuick recap so nothing slips: first job is getting licensed, and we aim for your exam within two weeks.\n\nTwo things this week:\n1. Register for your pre-licensing course\n2. Put your exam date on the calendar and text me the date\n\nIt's all laid out in the portal — check each step off as you go so I can see where you're at and jump in if you get stuck.\n\nWhat questions do you have?",
  u3:"Hey "+n+" — I noticed the course registration and exam date aren't checked off in the portal yet.\n\nNot chasing you — I just want to make sure nothing's in the way.\n\nAre you still on track for the exam? If something's come up, tell me and we may be able to work around it.\n\nWhere are you at?",
  u4:"Hey "+n+" — it's been "+(d?d+" days":"a couple of weeks")+" since you came on, and two weeks was the window we talked about for your exam.\n\nWhere are you with it?\n\nIf you're close, let's get the date locked in. If it's stalled out, let's figure out what's in the way — that part's fixable. I'd rather know than guess.",
  l1:"Hey "+n+" — welcome aboard, glad to have you.\n\nSince you're already licensed we can move fast. First priority is getting your contracting submitted — that's what unlocks your carriers and everything after it. It's right at the top of Fast Start in the portal.\n\nGet that in today if you can.\n\nAnd make sure to reach out if you have any questions and keep me updated on your progress.",
  n1:"Congratulations "+n+" — you're licensed. That's the hard part done.\n\nNow everything shifts to Fast Start. First priority is getting your contracting submitted — that unlocks your carriers and gets you cleared to dial.\n\nJump in the portal today and start working through it.\n\nLet me know if you have any questions and keep me updated on your progress.",
  l3:"Hey "+n+" — checking in on where contracting landed.\n\nGetting you cleared to dial is the whole game right now — until that's done you can't work. If something's sitting in a queue or you're waiting on a carrier, let me know.\n\nWhat's outstanding?",
  l4:"Hey "+n+" — the portal still shows you haven't marked yourself cleared to dial.\n\nThat step is you telling me you're ready, so I don't want to assume. Is something still in the way, or is it just not ticked?\n\nWhat's outstanding?",
  quiet:"Hey "+n+" — haven't seen you in the Optimum Agent Portal for a while, so I wanted to check in.\n\nNo pressure and no lecture. I just don't want you stuck on something I could sort out in five minutes.\n\nAre you still good to move forward? And if the timing's changed on your end, that's OK too — just tell me where your head's at."
  };
  return M[kind]||'';
}

/* ---- pace: is this person moving, slipping, or gone quiet? ----
   Anything recent outranks everything else — a login in the last 3 days keeps the
   card calm no matter what else is unticked. Zero progress on day two is normal;
   stopped progress is the thing worth a phone call. */
function m5RcPace(a,days){
  var ll=m5RcDays(a.lastLogin);
  if(ll!==null&&ll<=3) return {s:'ok'};
  if((a.gcCards30||0)>0) return {s:'ok'};
  var n=m5RcFirst(a);
  if(!a.loggedIn){
    var need=a.licensed?3:2;
    if(days>=need) return {s:'stall',k:'never',why:n+" has never logged into the portal, "+days+" days after signing up."};
    return {s:'ok'};
  }
  /* Logged in and then stopped is NOT the same as never started, and the heading has to
     say which. Telling a recruiter their agent "hasn't gotten started" when he has is the
     fastest way to make them stop trusting the card. */
  if(ll!==null&&ll>=7) return {s:'stall',k:'quiet',why:n+" hasn't logged in for "+ll+" days."};
  if(ll!==null&&ll>=4) return {s:'slip',why:n+" hasn't logged in for "+ll+" days."};
  return {s:'ok'};
}

/* ---- the steps for one recruit ---- */
function m5RcSteps(a,days,c){
  var st=(a.steps&&typeof a.steps==='object')?a.steps:{};
  var n=m5RcFirst(a), S=[];
  if(!a.licensed){
    /* "Started working the steps" also falls out of the Get-Licensed percentage: anything
       above zero means they have ticked at least one pre-licensing step. Using that as a
       fallback means this box is right even when the backend has not sent step-level
       detail — which is the whole point of the box. */
    var _gp=Number(String(a.gylPct==null?'':a.gylPct).replace('%','').trim());
    if(isNaN(_gp)) _gp=0;
    var started=!!a.loggedIn&&(!!(st.pre_1||st.pre_2||st.pre_3||st.pre_4||st.pre_5||st.pre_6)||_gp>0);
    S.push({k:'s1',you:true,done:!!c.s1,t:'Confirm first steps with '+n+' within 24 hours',
      d:'Re-welcome them, reset the expectation, and point at their next two steps. Some of this likely happened already — this is making sure it landed.',msg:'u1'});
    S.push({k:'s2',you:false,done:started,t:n+' has logged in and started working the steps',
      d:'Not just registered — registering is how they got here. This is whether they have come back and checked anything off.'});
    S.push({k:'s3',you:false,done:!!(st.pre_2&&st.pre_3),t:n+' is enrolled in pre-licensing with an exam date set',
      d:'The two that actually matter. Ticks itself when they check them off in the portal — the course link is already in there, you do not need to send it.',
      msg:(days>=5&&!(st.pre_2&&st.pre_3))?'u3':''});
    if(days>=14) S.push({k:'s4',you:true,done:!!c.s4,t:'Two-week check-in with '+n,
      d:'Two weeks is the window you set with them, so this is the moment to ask directly.',msg:'u4'});
  } else {
    var just=(c.lic0===0);
    S.push({k:'s1',you:true,done:!!c.s1,t:'Confirm first steps with '+n+' within 24 hours',
      d:just?'They can produce now — everything shifts to Fast Start and contracting.':'They can produce right away, so speed is everything. Get them pointed at Fast Start today.',msg:just?'n1':'l1'});
    S.push({k:'s2',you:false,done:!!st.c_nlc,t:n+' has submitted their contracting',
      d:'Not all of Fast Start — just the piece that unlocks everything else.',
      msg:(days>=14&&!st.c_nlc)?'l3':''});
    S.push({k:'s3',you:false,done:!!st.s_call,t:n+' has completed their strategy call',
      d:'The call with their manager where next steps get set.'});
    S.push({k:'s4',you:false,done:!!st.gl_ready,t:n+' has marked themselves cleared to dial',
      d:'This step is them saying they are ready. If it is not ticked they are not really ready — worth asking what is in the way.',
      msg:(days>=14&&!st.gl_ready)?'l4':''});
  }
  return S;
}

/* ---- which recruits get a card right now ---- */
window.m5RcCards=function(){
  var me=((store.data&&store.data.email)||'').trim().toLowerCase();
  var list=[], A=(typeof m5Ag!=='undefined'&&m5Ag.agents)?m5Ag.agents:[];
  for(var i=0;i<A.length;i++){
    var a=A[i], em=String(a.email||'').trim().toLowerCase();
    if(!em||em===me) continue;
    var jt=a.joined?Date.parse(a.joined):NaN;
    if(isNaN(jt)) continue;                                  /* no join date -> never card them */
    var days=Math.floor((Date.now()-jt)/864e5);
    if(days<0) days=0;
    /* backfill window only applies to people who were already here on ship day */
    if(jt<M5_RC_EPOCH && days>M5_RC_BACKFILL_DAYS) continue;
    var c=m5RcFor(em);
    if(c.dismissed) continue;
    if(typeof c.lic0!=='number'){ c.lic0=a.licensed?1:0; m5RcSave(); }
    var steps=m5RcSteps(a,days,c);
    var done=0,auton=0,autodone=0;
    for(var s=0;s<steps.length;s++){ if(steps[s].done) done++; if(!steps[s].you){ auton++; if(steps[s].done) autodone++; } }
    if(done===steps.length) continue;                        /* job finished — card retires itself */
    /* A licensed recruit who is contracted, has done their strategy call and has marked
       himself cleared to dial IS onboarded. That is the outcome the card existed for, so
       it retires whether or not the recruiter ever ticked their own box. The unlicensed
       card does not do this — it hands over to the licensed card when they pass. */
    if(a.licensed && auton>0 && autodone===auton) continue;
    /* Direct vs indirect. Prefer recruiter EMAIL — the one key that cannot drift. Falls
       back to name only while the backend has not been redeployed with recruiterEmail. */
    var myEm=me, myNm=m5RcNorm((store.data.name||'')||((store.data.first||'')+' '+(store.data.last||'')));
    var rEm=String(a.recruiterEmail||'').trim().toLowerCase();
    var rNm=m5RcNorm((a.recruiterFirst||'')+' '+(a.recruiterLast||''));
    var direct = rEm ? (rEm===myEm) : (rNm? (rNm===myNm) : true);
    var under=((a.recruiterFirst||'')+' '+(a.recruiterLast||'')).trim();
    var m={a:a,em:em,c:c,days:days,steps:steps,done:done,pace:m5RcPace(a,days),
           justLic:(c.lic0===0&&a.licensed),direct:direct,under:under};
    m.sig=m5RcSig(m);
    /* Collapsed, but something changed since — reopen it and say so. */
    if(c.collapsed && c.sig && c.sig!==m.sig){ delete c.collapsed; delete c.sig; c.reopened=1; m5RcSave(); }
    m.collapsed=!!c.collapsed;
    m.reopened=!!c.reopened;
    list.push(m);
  }
  list.sort(function(x,y){ return x.days-y.days; });
  return list;
};

/* A fingerprint of everything about this recruit that would be NEWS to their recruiter.
   Saved when a card is collapsed; if it no longer matches, the card springs back open.
   Deliberately excludes the day counter and the recruiter's own checkboxes — neither is
   news, and reopening on those would train people to ignore the reopening. */
function m5RcSig(m){
  var auto=0;
  for(var i=0;i<m.steps.length;i++){ if(!m.steps[i].you&&m.steps[i].done) auto++; }
  return [m.steps.length,auto,m.pace.s,(m.a.licensed?1:0)].join('|');
}

/* ---- actions ---- */
window.m5RcCollapse=function(em,sig){
  var c=m5RcFor(em); c.collapsed=(new Date()).toISOString(); c.sig=sig; m5RcSave(); m5RcRepaint();
};
window.m5RcExpand=function(em){
  var c=m5RcFor(em); delete c.collapsed; delete c.sig; delete c.reopened; m5RcSave(); m5RcRepaint();
};
window.m5RcToggle=function(em,k){
  var c=m5RcFor(em); c[k]=c[k]?false:(new Date()).toISOString(); m5RcSave(); m5RcRepaint();
};
window.m5RcAsk=function(em){ m5RcFor(em)._ask=1; m5RcRepaint(); };
window.m5RcKeep=function(em){ delete m5RcFor(em)._ask; m5RcRepaint(); };
window.m5RcKill=function(em){ var c=m5RcFor(em); delete c._ask; c.dismissed=(new Date()).toISOString(); m5RcSave(); m5RcRepaint(); };
window.m5RcMsgOpen=function(btn,id){
  var el=document.getElementById(id); if(!el) return;
  var open=el.style.display!=='none'; el.style.display=open?'none':'block';
  if(btn){ btn.classList.toggle('open',!open); }
};
window.m5RcCopy=function(btn,id){
  var el=document.getElementById(id+'-t'); if(!el) return;
  var txt=el.textContent||'';
  function ok(){ var o=btn.getAttribute('data-o'); if(o===null){ btn.setAttribute('data-o',btn.textContent); }
    btn.textContent='Copied ✓'; setTimeout(function(){ btn.textContent=btn.getAttribute('data-o')||'Copy'; },1600); }
  try{ if(navigator.clipboard&&navigator.clipboard.writeText){ navigator.clipboard.writeText(txt).then(ok,ok); return; } }catch(e){}
  try{ var t=document.createElement('textarea'); t.value=txt; document.body.appendChild(t); t.select(); document.execCommand('copy'); document.body.removeChild(t); }catch(e){}
  ok();
};
window.m5RcShowAll=function(){ window.m5RcAll=true; m5RcRepaint(); };

/* ---- render ---- */
function m5RcMsgBlock(id,kind,n,label,days){
  var txt=m5RcMsg(kind,n,days); if(!txt) return '';
  return '<button class="nr-msgbtn" onclick="m5RcMsgOpen(this,\''+id+'\')"><span>▸</span> '+(label||'View &amp; copy message')+'</button>'
    + '<div class="nr-msg" id="'+id+'" style="display:none"><p id="'+id+'-t">'+m5RcEsc(txt)+'</p>'
    + '<div class="nr-msgfoot"><button class="nr-copy" onclick="m5RcCopy(this,\''+id+'\')">Copy</button>'
    + '<span class="nr-msgnote">Send it however you normally talk to them.</span></div></div>';
}
function m5RcDigits(a){ var d=String((a&&a.phone)||'').replace(/\D/g,''); return d.length>=10?d.slice(-10):''; }
function m5RcPhoneFmt(d){ return '('+d.slice(0,3)+') '+d.slice(3,6)+'-'+d.slice(6); }
/* Copy FIRST, unconditionally, THEN try to open the texting app.
   On a phone, Messages opens and the copy was invisible. On a Mac with iMessage down, or on
   Windows where sms: goes nowhere at all, the number is already on the clipboard and the
   button says so. The browser cannot tell us whether an sms: link landed, so we never claim
   it did — the confirmation only promises the thing we actually know happened. */
window.m5RcText=function(btn,digits,fmt){
  var done=function(){
    if(!btn) return;
    if(btn.getAttribute('data-o')===null||btn.getAttribute('data-o')===undefined) btn.setAttribute('data-o',btn.innerHTML);
    btn.innerHTML='Number copied ✓'; btn.classList.add('ok');
    setTimeout(function(){ btn.classList.remove('ok'); btn.innerHTML=btn.getAttribute('data-o')||'Text'; },2600);
  };
  try{
    if(navigator.clipboard&&navigator.clipboard.writeText){ navigator.clipboard.writeText(fmt).then(done,done); }
    else { var t=document.createElement('textarea'); t.value=fmt; document.body.appendChild(t); t.select();
           try{ document.execCommand('copy'); }catch(e){} document.body.removeChild(t); done(); }
  }catch(e){ done(); }
  try{ window.location.href='sms:+1'+digits; }catch(e){}
};
function m5RcContact(a){
  var d=m5RcDigits(a); if(!d) return '';
  var f=m5RcPhoneFmt(d);
  return '<div class="nr-contact">'
    + '<a class="nr-tel" href="tel:+1'+d+'"><span class="ico">📞</span>'+f+'</a>'
    + '<button class="nr-text" onclick="m5RcText(this,\''+d+'\',\''+f+'\')">Text</button>'
    + '</div>';
}
function m5RcCard(m,idx){
  var a=m.a, n=m5RcFirst(a), warn=(m.pace.s==='stall');
  var cls='nr'+(warn?' t-warn':(m.justLic?' t-promo':''));
  var pct=Math.round(m.done/m.steps.length*100);
  /* Two chips, always. The first says where they stand on licensing and never changes
     duty; the second says what is happening with them. The old single chip meant a card
     that went orange silently dropped the licence status, which is the one fact a
     recruiter needs to know what to even say to them. */
  var chip=warn?(m.pace.k==='quiet'?'Gone quiet':'Never started'):(m.direct?'New recruit':'In your downline');
  var licChip = m.justLic ? '<span class="nr-chip lic new">🎉 Newly licensed</span>'
              : (a.licensed ? '<span class="nr-chip lic">Licensed</span>'
                            : '<span class="nr-chip unl">Unlicensed</span>');
  var head;
  if(m.justLic) head='🎉 <b>'+m5RcEsc(a.name||n)+'</b> just got licensed — here is what is next';
  else if(warn) head=m5RcEsc(a.name||n)+(m.pace.k==='quiet'?' has gone quiet':' has not gotten started');
  /* Never tell someone they recruited a person they did not recruit. */
  else if(!m.direct) head='<b>'+m5RcEsc(a.name||n)+'</b> joined your agency';
  else head='🎉 Congratulations — you recruited <b>'+m5RcEsc(a.name||n)+'</b>';
  var meta=m.justLic?'Licensed today · your job just changed':('Joined '+m5RcAgo(m.days));
  if(!m.direct && m.under) meta+=' · <span class="nr-under">Under '+m5RcEsc(m.under)+'</span>';
  var h='<div class="'+cls+'">';
  if(m.c._ask){
    h+='<div class="nr-confirm"><p>Remove the card for '+m5RcEsc(a.name||n)+'? You will not get it back.</p>'
      +'<div class="nr-row"><button class="nr-btn warn" onclick="m5RcKill(\''+m.em+'\')">Remove</button>'
      +'<button class="nr-btn" onclick="m5RcKeep(\''+m.em+'\')">Keep it</button></div></div>';
  }
  h+='<div class="nr-top"><div><div class="nr-chips">'+licChip+'<span class="nr-chip">'+chip+'</span></div><div class="nr-h">'+head+'</div>'
   + '<div class="nr-meta">'+meta+'</div>'+m5RcContact(a)+'</div>'
   + '<div class="nr-ctl">'
   + '<button class="nr-collapse" onclick="m5RcCollapse(\''+m.em+'\',\''+m.sig+'\')"><span class="car">▲</span> Collapse</button>'
   + '<button class="nr-x" title="Remove this card for good" onclick="m5RcAsk(\''+m.em+'\')">✕</button></div></div>';
  if(m.reopened){ h+='<div class="nr-reopen">↩︎ Reopened — something changed for '+m5RcEsc(n)+' since you collapsed this.</div>'; }
  if(warn&&m.pace.why){
    h+='<div class="nr-alert">⚠️ '+m5RcEsc(m.pace.why)+' A call now is worth more than one next week.'
      +m5RcMsgBlock('nrq'+idx,'quiet',n,'View &amp; copy message',m.days)+'</div>';
  } else if(m.pace.s==='slip'&&m.pace.why){
    h+='<div class="nr-alert" style="background:var(--nrab);border-color:#f0e0bd;color:#7a5a10">⏳ '+m5RcEsc(m.pace.why)+'</div>';
  }
  h+='<div class="nr-prog"><div class="nr-bar"><i style="width:'+pct+'%"></i></div><span class="nr-pct">'+m.done+' of '+m.steps.length+'</span></div>';
  h+='<ul class="nr-steps">';
  for(var i=0;i<m.steps.length;i++){
    var s=m.steps[i];
    var box=s.you
      ? '<button class="nr-box'+(s.done?' on':'')+'" onclick="m5RcToggle(\''+m.em+'\',\''+s.k+'\')" aria-label="toggle"></button>'
      : '<span class="nr-box auto'+(s.done?' on':'')+'" title="Ticks itself from '+m5RcEsc(n)+'’s own activity"></span>';
    var tag=s.you?'':(s.done?'<span class="nr-tag ok">auto ✓</span>':'<span class="nr-tag wait">waiting on '+m5RcEsc(n)+'</span>');
    h+='<li class="nr-step'+(s.done?' done':'')+'">'+box+'<div class="nr-body"><div class="nr-t">'+m5RcEsc(s.t)+tag+'</div>'
      +'<div class="nr-d">'+m5RcEsc(s.d)+'</div>'
      +(s.msg?m5RcMsgBlock('nrm'+idx+'-'+i,s.msg,n,'View &amp; copy message',m.days):'')+'</div></li>';
  }
  h+='</ul>';
  h+='<div class="nr-foot">'
   + (!m.direct&&m.under?'<span class="nr-fnote">'+m5RcEsc(m.under)+' owns this one — if something needs chasing, start there.</span>':'')
   + '<button class="nr-dash" onclick="go(\'agency\')">Open Agency Dashboard →</button></div>';
  h+='</div>';
  return h;
}
function m5RcRow(m){
  var n=m5RcFirst(m.a), warn=(m.pace.s==='stall');
  return '<div class="nr-row'+(warn?' warn':'')+'">'
    + '<button class="nr-expand" onclick="m5RcExpand(\''+m.em+'\')"><span class="car">▼</span> Expand</button>'
    + '<span class="nr-rname">'+m5RcEsc(m.a.name||n)+'</span>'
    + '<span class="nr-rmeta">'+m.done+' of '+m.steps.length
    + (m.direct?'':'<span class="nr-runder"> · under '+m5RcEsc(m.under||'someone else')+'</span>')+'</span>'
    + '<button class="nr-x" title="Remove this card for good" onclick="m5RcAsk(\''+m.em+'\')">✕</button></div>';
}
window.m5RcRender=function(){
  try{
    if(typeof store==='undefined'||!store.data) return '';
    /* Only pay for a roster call if we have reason to think there is a team. */
    var tc=(typeof store.data.teamCount==='number')?store.data.teamCount:null;
    if(typeof m5Ag==='undefined') return '';
    if(!m5Ag.loaded){
      if(tc===0) return '';
      if(typeof m5AgFetch==='function') m5AgFetch(true);
      return '';
    }
    if(m5Ag.err) return '';
    var list=m5RcCards(); if(!list.length) return '';
    /* Confetti the first time we see one of their people flip to licensed. */
    for(var q=0;q<list.length;q++){
      if(list[q].justLic&&!list[q].c.celebrated){
        list[q].c.celebrated=(new Date()).toISOString(); m5RcSave();
        try{ if(typeof m5Confetti==='function') setTimeout(m5Confetti,320); }catch(e){}
      }
    }
    /* Collapsed rows are one line each, so they never count against the cap — otherwise
       collapsing three just promotes three more and the pile never shrinks. Handled people
       sink to the bottom; live ones stay up top. */
    var open=[], shut=[];
    for(var k=0;k<list.length;k++){ (list[k].collapsed?shut:open).push(list[k]); }
    var cap=(window.m5RcAll===true)?open.length:3;
    var out='<div class="nr-wrap">';
    for(var i=0;i<open.length&&i<cap;i++) out+=m5RcCard(open[i],i);
    if(open.length>cap) out+='<button class="nr-more" onclick="m5RcShowAll()">Show '+(open.length-cap)+' more new recruit'+((open.length-cap)===1?'':'s')+'</button>';
    if(shut.length){
      out+='<div class="nr-shut"><div class="nr-shuth">Handled for now · '+shut.length+'</div>';
      for(var j=0;j<shut.length;j++) out+=m5RcRow(shut[j]);
      out+='</div>';
    }
    return out+'</div>';
  }catch(e){ return ''; }
};

</script>
"""
