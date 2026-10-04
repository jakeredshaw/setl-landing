#!/usr/bin/env python3
"""Flip the whole site from waitlist to launched, in one command.

    python3 tools/go_live.py https://apps.apple.com/gb/app/setl/id1234567890

Rewrites the generator's launch switch, swaps the homepage waitlist forms for App Store
buttons, and adds the store link to the structured data. Run tools/build_pages.py after.
Use --dry to see what would change."""
import json, re, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
url = next((a for a in sys.argv[1:] if a.startswith("http")), None)
dry = "--dry" in sys.argv
if not url:
    sys.exit("Give the App Store URL:  python3 tools/go_live.py https://apps.apple.com/...")

changes = []

# 1. the generator switch drives every content page CTA
p = os.path.join(ROOT, "tools", "build_pages.py"); s = open(p).read()
s2 = s.replace("LAUNCHED = False", "LAUNCHED = True").replace('APP_STORE_URL = ""', 'APP_STORE_URL = "%s"' % url)
changes.append(("tools/build_pages.py", s != s2, p, s2))

# 2. the homepage: waitlist wording and the store link in schema
p = os.path.join(ROOT, "index.html"); s = open(p, encoding="utf-8").read(); s2 = s
swaps = [
 ("Join the waitlist and get up to 7 nights free when SETL launches.", "Download SETL and your first 7 nights are free."),
 ("Up to 7 nights free when we launch. No card needed to join.", "7 nights free on the yearly plan. Cancel any time in Settings."),
 ("SETL is launching on iPhone soon. Join the waitlist and get up to 7 nights free when we launch.",
  "SETL is on the App Store now, with 7 nights free on the yearly plan."),
 (">Join the waitlist<", ">Download on the App Store<"),
 (">Join waitlist<", ">Download<"),
]
for a, b in swaps:
    s2 = s2.replace(a, b)
# the waitlist forms become App Store buttons
form = re.compile(r'<form class="wait[^"]*"[^>]*>.*?</form>', re.S)
n_forms = len(form.findall(s2))
s2 = form.sub('<div class="btn-row"><a class="btn" href="%s" rel="noopener">Download on the App Store</a></div>' % url, s2)
print("waitlist forms replaced:", n_forms)
m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s2, re.S)
g = json.loads(m.group(1))
for n in g["@graph"]:
    if n.get("@type") == "SoftwareApplication":
        n["installUrl"] = url
        n["downloadUrl"] = url
s2 = s2[:m.start(1)] + json.dumps(g, ensure_ascii=False) + s2[m.end(1):]
changes.append(("index.html", s != s2, p, s2))

for name, changed, path, new in changes:
    print(("would update " if dry else "updated ") + name if changed else "no change needed in " + name)
    if changed and not dry:
        open(path, "w", encoding="utf-8").write(new)
if not dry:
    print("\nNow run:  python3 tools/build_pages.py && sh tools/ping_indexnow.sh")
    print("Then check the waitlist form is gone from the hero, and commit.")
