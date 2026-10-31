# Decisions and backlog

Carried over from the "Agent Onboarding and Coaching" Cowork project on 31 Oct 2026.
The standing rules themselves are in `../CLAUDE.md`. Backend internals (sheet tabs, the
Apps Script source, its failure modes) are kept privately, not in this public repo.

## Data the portal already collects

- Check-offs store an **ISO timestamp**, not `true`, since 18 Aug 2026. Before that date there
  is no per-step history.
- Milestones: `t_firstLogin`, `t_licensed`, `t_fsDone`, `t_acadDone`, `t_lastLogin`. Also the
  `logins` count (unreliable: it has shown 0 next to a real `lastLogin`), `sectionOpens`
  counts, and Goal Card per-day rows.
- Roster fields: `joined, loggedIn, licensed, firstLogin, lastLogin, gylPct, fsPct, acadPct,
  daysToLic, fsDays, acadDays, appliedOn, npnOn, gcUsing, gcCards, gcCards30, logins,
  sectionsUsed, source, recruiterFirst, recruiterLast`.
- Rule: record state changes only. No clickstream logging; Sheets is the wrong place for it.

## Decided but not built

| Feature | Status | What's locked | Blocked on |
|---|---|---|---|
| **Downline scoping** of the Agency Dashboard | Designed 18 Aug | Full downline, all levels. A hierarchy table (agent, upline) beats the ref-code recruiter, which beats Jesse. Cycle guard. A 60-120 s cache that Refresh bypasses. An "Unassigned" filter for Jesse. | The backend source; a hierarchy backfill (on 18 Aug only a small minority of agents had any recruiter on record) |
| **New-Recruit Action Card** | Copy and mechanic approved 18-19 Aug | Persistent card, not a modal. Four states, copy verbatim. Gate on `joined` on or after a launch-date constant; "just got licensed" fires regardless. Jesse wants his own cards as a one-time cleanup queue. Cleared to dial = the `golive` module (`gl_gate`, `gl_ready`, `gl_goal`, `gl_leads`); strategy call = `s_call`. State is server-side, per recruiter x recruit. | Downline scoping ships first |
| **Pace logic** (on pace / slipping / stalled) | Targets confirmed 19 Aug | Unlicensed: day 2 login, day 3 started, day 4 enrolled, day 6 exam date, day 21 licensed. Licensed: day 1 login, day 3 Fast Start, day 5 contracting, day 14 cleared to dial, day 21 first Goal Card. Never flag anyone active in the last 3-7 days. | The card |
| **Archive / block** | Designed 6-8 Oct | One `status` column (`active / archived / blocked`) honoured by `lookup`. Archive alone keeps access; a removal is archive **and** block. Never delete rows. | The backend source |
| **Attribution** (recruiting phase 0) | Recommended 16 Oct | Hidden `source` / `campaign` fields on `register.html` from URL params, passed through `action:'register'`. Backfill existing rows as `ffl-national` (assumed). | The backend source |
| **Address + NPN on the agent card** | Frontend done | Home address to admins (and the agent's own recruiter) only; NPN to all. | A backend change |
| **`state` on the roster payload** | Recommended 30 Sep | So blank or malformed states are visible | A backend change |
| **Production Dashboard** | Mockup, parked | Actuals for calendar periods, rolling averages in "Your pace". Gate it on having Goal Card data. | Jesse's call on how "money sold per week" is calculated |
| **Ask Optimum: "what do I do next?"** | Requested | Reads the agent's own Get Licensed / Fast Start / Academy progress and points to their real next step. | Content |
| "Room per dial" -> **"Seconds left per dial"** | Suggested | | Jesse hasn't ruled |

Also outstanding: the 8 hard-coded recruiter overrides (`EXC` in `m5AgRecruiter`) belong in
the sheet, then out of the code. One stray-duplicate email is hard-coded in `m5AgDedupe`'s
`DROP_EMAILS`; removing it un-hides that duplicate row, so it goes only once the row is
archived server-side (and it stays in git history either way).

## Academy flags inherited from v3.6

0.0 and 1.3 held (Jesse has not cleared their new videos); T.1 Coming Soon pending review;
Part 8's Daily Focus `e1`/`sd1` name ids the widget no longer has; 2.5.3's Script Navigator
URL is bare while 2.4.1 deep-links `?script=veteran`; the production doc's "1280x720
thumbnails" is wrong (posters are 9:16); the Part 10 inventory covers Academy and Fast Start
only. Detail: the v3.6 release record (not yet in this repo).
