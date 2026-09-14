# SETL blog brief (for writers)

Site: https://www.setlsleep.com. SETL (say it like "settle") is an iPhone app blocker built bedtime first.
Goal: rank on Google and get cited by AI search (ChatGPT, Perplexity, Google AI Overviews) for the target keywords of each post.

## Output
One Python file per post: `tools/posts/<slug>.py`, defining a single dict `POST`:

```python
POST = {
 "slug": "what-is-an-app-blocker",
 "title": "What Is an App Blocker? How They Work on iPhone | SETL",  # <= 60 chars, primary keyword at the START
 "h1": "What is an app blocker, and how does it work?",               # contains the primary keyword
 "desc": "...",          # 135 to 155 chars, contains the primary keyword, reads like an answer
 "tagline": "App blockers",  # one of: Screen Time, App blockers, Sleep, Focus, Psychology, Science
 "minutes": 7,           # reading time = words / 200, rounded
 "primary": "app blocker",
 "keywords": "app blocker, app blockers, how app blockers work, block apps on iPhone, SETL",
 "intro": "...",         # plain text, max 30 words
 "answer": "...",        # plain text, 40 to 60 words. The direct answer to the title question. Rendered as a Quick answer box at the top. This is what AI search quotes, so make it self contained and factual.
 "body": """<h2>..</h2><p>..</p>""",   # HTML, 900 to 1400 words
 "sources": [("Publisher, Title, Year", "https://...")],  # in the order first cited
 "faq": [("Question people actually search?", "Answer, 1 to 3 sentences, max 50 words.")],  # 5 or 6 items
 "related": ["slug-a", "slug-b", "slug-c"],   # 3 slugs from the URL list below
}
```

Allowed body HTML: `h2 h3 p ul ol li strong em a sup blockquote`, `<div class="callout"><strong>Label:</strong> text</div>`,
and tables as `<div class="tablewrap"><table class="cmp"><thead>..</thead><tbody>..</tbody></table></div>`.
Footnotes: `<sup><a href="#fn1">1</a></sup>`, numbered by position in `sources`. Every source must be cited at least once.
Do not repeat the h1, intro, answer, sources or FAQ inside body (the template renders those).

## SEO and AI search rules
- Primary keyword in: title (first words), h1, desc, the answer, the first 100 words of body, at least one h2.
- Secondary keywords used naturally in h2s and body. Never stuff: read it aloud, it must sound human.
- Several h2s phrased as the questions people type ("How do app blockers work on iPhone?").
- Include at least one list or numbered steps; a comparison table where it genuinely helps.
- Put one clear definition sentence early ("An app blocker is ...").
- At least 3 internal links inside body with descriptive keyword anchor text (not "click here"), to URLs below. At least one must be a product page (/app-blocker.html, /screen-time-blocker.html, /apple-screen-time-alternative.html, /setl-sleep.html or /setl-sessions.html).
- One short section near the end, "Where SETL fits" (or similar), 2 to 4 sentences, honest, linking to the most relevant product page.

## Voice
- UK English spelling (colour, realise, behaviour). Short sentences, reading age about 12. Paragraphs of 1 to 3 sentences.
- Warm, direct, confident, zero hype. Talk to "you".
- NO DASHES in copy: no em dash, no en dash, no spaced hyphen used as punctuation. Avoid hyphenated compounds where you can ("self interruption", "one off"). Hyphens only in proper names, URLs or things like "20-20-20".
- No exclamation marks. No "In today's fast paced world" filler.

## Accuracy rules (hard, non negotiable; this is a UK business under the DMCC Act and CAP Code)
- Every statistic, study finding, price or feature of another product must come from a page you actually opened this session, and be cited. Prefer primary sources: journals, Apple Support, Ofcom, AASM, NHS, CDC, NIH, official app sites and App Store listings.
- If you cannot verify a number, do not use it. Never round a number into a stronger claim. Say who was studied (e.g. "US adults", "university students").
- Correlation is not causation; say "linked to", not "causes", unless the study shows causation.
- Never invent quotes, testimonials, reviews, user numbers, or SETL results. Do NOT mention any SETL beta results or time saved figures.
- No medical claims. SETL does not treat ADHD, insomnia or addiction. Health posts end with: `<p class="fn">This article is general information, not medical advice. Speak to your doctor about ongoing sleep, attention or mental health concerns.</p>`
- Competitors: only facts from their own site or App Store page, stated neutrally with "checked September 2026". Be fair; mention genuine strengths. No disparagement.

## SETL facts you may use (nothing beyond this)
- iPhone only for now (Android and Mac not yet). Built on Apple's Screen Time framework; Apple gives SETL private tokens, so SETL never learns which apps you picked, and Screen Time data stays on the phone.
- SETL Sleep: set your bedtime once; your chosen apps are blocked automatically at bedtime every night.
- SETL Sessions: daytime focus blocks. Pick the apps, pick how long. The block ends itself when time is up; opening early needs a deliberate press and hold, not a single tap.
- SETL Plans: plan nights off in advance (weddings, night shifts, birthdays).
- Sleep Reserve: Lock Screen widget showing how much of the night is left for sleep. Post bedtime nudges.
- Moon collection: moons you earn by keeping nights.
- Pricing (launch, USD, via Apple): $39.99 a year (shown as $3.33 a month), $5.99 a month, $2.99 a week. Free nights: 7 on yearly, 3 on monthly, 1 on weekly. Cancel in iPhone settings.
- Currently a waitlist ahead of launch (CTA is "Join the waitlist" at https://www.setlsleep.com/).
- Founder: Jacob Redshaw, UK, ADHD, former copywriter. Do not add other biography.

## URL list (internal links)
Product and core pages:
- / (home, join the waitlist)
- /app-blocker.html (app blocker for iPhone)
- /screen-time-blocker.html (screen time blocker, screen time restrictor, screen timer blocker)
- /apple-screen-time-alternative.html (Apple Screen Time, Downtime, alternative)
- /setl-sleep.html (SETL Sleep, bedtime app blocker, sleep app blocker)
- /setl-sessions.html (focus app blocker, deep work, study)
- /setl-vs-opal.html (Opal alternative comparison)
- /pricing.html, /about.html, /mission.html, /blog/
Existing posts (/blog/<slug>.html):
- how-to-stop-scrolling-in-bed, best-app-blocker-for-sleep, does-it-take-23-minutes-to-refocus, screens-melatonin-and-sleep
New posts being written now (safe to link):
- screen-time-limits-not-working, how-to-use-downtime-on-iphone, how-to-reduce-screen-time-on-iphone
- what-is-an-app-blocker, best-screen-time-apps-for-iphone, opal-alternatives
- bedtime-procrastination, how-to-stop-doomscrolling, phone-addiction-signs, why-apps-are-addictive
- app-blocker-for-adhd, how-much-screen-time-is-too-much, does-grayscale-reduce-screen-time

## Self check before you finish (run it)
`python3 tools/posts/check.py tools/posts/<slug>.py` from the repo root. Fix every failure, then rerun until OK.
