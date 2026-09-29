# optimum-portal
## Before you push index.html

Always start from the latest `main` (`git pull`) before editing `index.html`. Building a change on an older copy silently throws away everything pushed since.

**Ask Optimum** (the AI helper for agents) is loaded by one line near the bottom of `index.html`:

```html
<script src="ask-optimum.js?v=2" defer></script>
```

Keep that line. Without it, the Ask Optimum button, the dashboard ask bar and the pre-licensing "Questions while you get licensed?" card all disappear for every agent. The chat itself lives in `brain.html` and `ask-optimum.js`.
