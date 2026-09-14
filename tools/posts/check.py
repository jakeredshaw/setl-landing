#!/usr/bin/env python3
"""Validate blog post modules against tools/posts/BRIEF.md.  Usage: python3 tools/posts/check.py tools/posts/*.py"""
import importlib.util, re, sys, os

KNOWN = {"how-to-stop-scrolling-in-bed", "best-app-blocker-for-sleep", "does-it-take-23-minutes-to-refocus",
         "screens-melatonin-and-sleep", "screen-time-limits-not-working", "how-to-use-downtime-on-iphone",
         "how-to-reduce-screen-time-on-iphone", "what-is-an-app-blocker", "best-screen-time-apps-for-iphone",
         "opal-alternatives", "bedtime-procrastination", "how-to-stop-doomscrolling", "phone-addiction-signs",
         "why-apps-are-addictive", "app-blocker-for-adhd", "how-much-screen-time-is-too-much",
         "does-grayscale-reduce-screen-time"}
PAGES = {"/", "/app-blocker.html", "/screen-time-blocker.html", "/apple-screen-time-alternative.html",
         "/setl-sleep.html", "/setl-sessions.html", "/setl-vs-opal.html", "/pricing.html", "/about.html",
         "/mission.html", "/blog/"} | {"/blog/%s.html" % s for s in KNOWN}
PRODUCT = {"/app-blocker.html", "/screen-time-blocker.html", "/apple-screen-time-alternative.html",
           "/setl-sleep.html", "/setl-sessions.html"}

def words(h): return len(re.sub(r"<[^>]+>", " ", h).split())

def check(path):
    spec = importlib.util.spec_from_file_location("p", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    P, errs = m.POST, []
    need = ["slug", "title", "h1", "desc", "tagline", "minutes", "primary", "keywords", "intro", "answer", "body", "sources", "faq", "related"]
    errs += ["missing " + k for k in need if k not in P]
    if errs: return errs
    kw = P["primary"].lower()
    if os.path.basename(path) != P["slug"] + ".py": errs.append("filename must be slug.py")
    if len(P["title"]) > 60: errs.append("title %d chars > 60" % len(P["title"]))
    if not P["title"].endswith("| SETL"): errs.append("title should end with | SETL")
    if not 135 <= len(P["desc"]) <= 155: errs.append("desc %d chars, want 135-155" % len(P["desc"]))
    for k in ("title", "h1", "desc", "answer"):
        if kw not in P[k].lower(): errs.append("primary keyword missing from " + k)
    if kw not in re.sub(r"<[^>]+>", " ", P["body"]).lower()[:900]: errs.append("primary keyword not in first ~100 words of body")
    if not any(kw in h.lower() for h in re.findall(r"<h2>(.*?)</h2>", P["body"])): errs.append("primary keyword not in any h2")
    if len(P["intro"].split()) > 30: errs.append("intro > 30 words")
    if not 40 <= len(P["answer"].split()) <= 60: errs.append("answer %d words, want 40-60" % len(P["answer"].split()))
    w = words(P["body"])
    if not 900 <= w <= 1400: errs.append("body %d words, want 900-1400" % w)
    if not 5 <= len(P["faq"]) <= 6: errs.append("faq needs 5-6 items")
    for q, a in P["faq"]:
        if len(a.split()) > 50: errs.append("faq answer > 50 words: " + q)
    blob = " ".join([P["title"], P["h1"], P["desc"], P["intro"], P["answer"], P["body"]] + [q + a for q, a in P["faq"]])
    if re.search("[—–]| - |&mdash;|&ndash;", blob): errs.append("dash found (em/en/spaced hyphen)")
    if "!" in re.sub(r"<[^>]+>", "", blob): errs.append("exclamation mark")
    n = len(P["sources"])
    cited = set(int(x) for x in re.findall(r'href="#fn(\d+)"', P["body"]))
    if cited != set(range(1, n + 1)): errs.append("footnotes cited %s but %d sources" % (sorted(cited), n))
    for lbl, u in P["sources"]:
        if not u.startswith("https://"): errs.append("source url not https: " + u)
    links = set(re.findall(r'href="(/[^"#]*)"', P["body"]))
    bad = [l for l in links if l not in PAGES]
    if bad: errs.append("unknown internal links: %s" % bad)
    if len(links) < 3: errs.append("need >= 3 internal links in body, found %d" % len(links))
    if not links & PRODUCT: errs.append("need a link to a product page")
    for r in P["related"]:
        if r not in KNOWN or r == P["slug"]: errs.append("bad related slug " + r)
    if re.search(r"<h1|<script|style=", P["body"]): errs.append("no h1/script/style in body")
    return errs

bad = 0
for p in sys.argv[1:]:
    e = check(p)
    print(("OK   " if not e else "FAIL ") + p + ("" if not e else "\n  - " + "\n  - ".join(e)))
    bad += bool(e)
sys.exit(1 if bad else 0)
