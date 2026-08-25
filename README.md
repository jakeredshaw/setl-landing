# SETL — Waitlist Landing Page

Static landing page for SETL. Deploys to Vercel with zero config (`index.html` at repo root).

## Structure
- `index.html` — the entire page (CSS + JS inlined, most imagery embedded as base64)
- `assets/` — product screenshots and moon image
- `logo.svg` — SETL mark

## Waitlist -> Google Sheet

Signups append a row to a Google Sheet. No CRM, no email platform, no monthly cost.

**One-time setup (about 10 minutes, all on your side):**

1. Create a new Google Sheet. Name it something like `SETL Waitlist`.
2. In that sheet: **Extensions > Apps Script**. Delete the placeholder code.
3. Paste in the contents of `waitlist-sheet/Code.gs` from this repo. Save.
4. **Deploy > New deployment**, pick type **Web app**:
   - Execute as: **Me**
   - Who has access: **Anyone**
5. Authorise when Google prompts (it will warn the app is unverified — it is your
   own script, so continue through the advanced link).
6. Copy the deployment URL. It ends in `/exec`.
7. Paste that URL into `ENDPOINT` in `index.html` (search for `var ENDPOINT=''`).

The sheet fills in with four columns: Email, Signed up (UTC), Source (hero or
footer), Notes. Duplicate emails are rejected server-side.

**If you later want to email that list**, export the sheet as CSV and import it
into any email tool. Nothing here locks you in.

## Status

- Baseline: `setl-v18.html` from the design chat.
- Waitlist forms are wired up, with validation, a bot honeypot, loading and error
  states, and a "You're on the list" success state. **They stay inert until
  `ENDPOINT` is filled in** — an unconfigured form shows an error rather than
  pretending to succeed.
- `@font-face` references `setl-font.woff2`, which is not in the repo. The page falls
  back to General Sans (Fontshare) -> Inter Tight (Google Fonts) until that file is added.

### MISSING ASSET — blocks deploy

`assets/scr-tomorrow.png` is referenced by the Tomorrow feature section but is **not
in the repo**. Save the SETL app screenshot (the Tonight screen with the streak
counter, moon dial and the Tomorrow tab) to that exact path. Until then the section
renders with an empty phone screen.

Existing app screenshots in `assets/` predate the Tomorrow tab, so none of them can
stand in for it.

### Numbers behind the "SETL saves you" counter

The counter derives everything from one input: **1h 47m saved per day**.

    107 min/day x 365.25 days x 87 years = 3,400,112 min
      = 56,669 hours = 2,361 days = 77.6 months = 6.46 years

Displayed as 1h 47m -> 78 months -> 6.5 years. Change the daily figure and both
downstream numbers must be recomputed.

**1h 47m/day is a product claim, not arithmetic.** It needs a basis you can
point to before this page is public. The 87-year life expectancy is also an
assumption worth stating on the page or in a footnote.

### Unverified claims on the page — resolve before launch

Two elements in the hero assert things that need to be true:

- **"15,000+ WAITLIST JOINED"** — a hard signup number.
- **"New & Upcoming App 2026"** inside an award laurel with an Apple mark — reads as
  an Apple editorial award.

If either is not literally true, it should be removed or replaced before this page is
public. See `no-invented-proof` in the project notes.

## Local preview
```
python3 -m http.server 8000
```
Then open http://localhost:8000
