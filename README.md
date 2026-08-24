# SETL — Waitlist Landing Page

Static landing page for SETL. Deploys to Vercel with zero config (`index.html` at repo root).

## Structure
- `index.html` — the entire page (CSS + JS inlined, most imagery embedded as base64)
- `assets/` — product screenshots and moon image
- `logo.svg` — SETL mark

## Status
- Baseline: `setl-v18.html` from the design chat, committed unmodified.
- **Waitlist forms are not wired up yet** — both `<form class="wait">` elements use
  `onsubmit="return false"`, so submitted emails are discarded. Must be connected to a
  real capture endpoint before launch.
- `@font-face` references `setl-font.woff2`, which is not in the repo. The page falls
  back to General Sans (Fontshare) → Inter Tight (Google Fonts) until that file is added.

## Local preview
```
python3 -m http.server 8000
```
Then open http://localhost:8000
