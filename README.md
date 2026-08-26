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

### SETL Sessions section — wrong image

The Sessions section is a duplicate of the Sleep Reserve section, so it is
currently showing the **Sleep Reserve device render**. That image says
"7h 30m left until wake-up", which contradicts the copy next to it about
daytime focus.

Replace it with the Sessions screen ("Unblock distractions for... / Hold to
unblock"). Drop the file into `assets/` and swap the `src` on the `.glow` img
inside the section marked `<!-- SETL SESSIONS -->`.

### Numbers behind the "SETL saves you" counter

The counter derives everything from one input: **1h 47m saved per day**.

    107 min/day x 365.25 days x 87 years = 3,400,112 min
      = 56,669 hours = 2,361 days = 77.6 months = 6.46 years

Displayed as 1h 47m -> 78 months -> 6.5 years. Change the daily figure and both
downstream numbers must be recomputed.

**1h 47m/day is a product claim, not arithmetic.** It needs a basis you can
point to before this page is public. The 87-year life expectancy is also an
assumption worth stating on the page or in a footnote.

## Swapping the phone screenshots

Every phone on the page except the hero one is drawn by CSS. The image you drop
in is a **plain screenshot with no phone around it** - the frame, bezel, side
buttons and shadow are all CSS. Just save the file over the right name:

| Section                | File                    | Screen to capture              |
|------------------------|-------------------------|--------------------------------|
| Sleep Reserve          | `assets/scr-reserve.png`| Tonight tab, Sleep Reserve      |
| SETL Sessions          | `assets/scr-sessions.png`| Focus session running          |

Steps: take the screenshot in the Simulator (Cmd-S saves to the Desktop), rename
it to the file name above, drop it into `assets/`, refresh. Nothing else to
change - no code edit, no resizing, no cropping.

**Do not send a screenshot that already has a phone drawn around it.** It will
be framed twice and look like a phone inside a phone. Bare screen only.

If a file is missing the frame removes itself, so the section still reads
correctly instead of showing an empty black phone.

### The hero phone is different

`assets/setl-device.png` is a pre-rendered image with the phone body baked into
the pixels, so it has no CSS frame. To change it you either supply another
render of the same kind, or send a bare Tonight screenshot and it can be moved
onto the CSS frame like the other two - after which all three work the same way.

### Instagram link needs the real handle

The community block links to `https://instagram.com/SETL_HANDLE`. Replace
SETL_HANDLE with the actual account before launch - as it stands the button
goes to a profile that does not exist.

### The four figures in "What SETL buys you"

    90%   better focus, night and day
    100%  a streamlined bedtime
    92%   more discipline after a week
    92%   more disciplined everywhere else

None of these are derived from anything in this repo - unlike the counter,
which at least computes from a single stated input. They are outcome claims
about what the product does to people, stated as percentages, on a commercial
page. They need a study, a sample size and a method behind them, or they need
to become qualitative statements.

Note the last two are both 92% and read as near-duplicates; likely a slip.

### Reviews — must be real before launch

Three named, five-star testimonials sit under the SETL Sleep block. They are
attributed to specific people and make specific claims:

- an ADHD outcome ("my ADHD brain finally switches off")
- a price anchor ("I would genuinely pay $1,000")
- a physical health outcome ("the bags under my eyes are gone")

A testimonial is a factual claim about a real person's experience. These need
to be genuine and attributable, with permission to publish, or they need to
come down. Health and pricing claims are the two categories that attract the
most scrutiny.

Avatars are initials, not photographs, by design - see the commit note.

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
