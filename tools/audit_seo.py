#!/usr/bin/env python3
"""SEO audit of every generated page: titles, descriptions, h1, FAQ + schema, links, dashes."""
import re, json, os, glob, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages = [p for p in glob.glob(os.path.join(ROOT, "*.html")) + glob.glob(os.path.join(ROOT, "blog", "*.html"))]
exists = lambda href: os.path.exists(os.path.join(ROOT, href.lstrip("/"), "index.html") if href.endswith("/") else os.path.join(ROOT, href.lstrip("/")))
fail = 0
for p in sorted(pages):
    rel = os.path.relpath(p, ROOT); s = open(p, encoding="utf-8").read(); e = []
    if rel in ("404.html",): continue
    t = html.unescape(re.search(r"<title>(.*?)</title>", s).group(1)); d = re.search(r'name="description" content="(.*?)"', s)
    if len(t) > 60: e.append("title %d" % len(t))
    if not d or len(html.unescape(d.group(1))) > 160: e.append("description missing/long")
    if len(re.findall(r"<h1[ >]", s)) != 1: e.append("h1 count %d" % len(re.findall(r"<h1[ >]", s)))
    lds = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    types = []
    for l in lds:
        try: types += [g.get("@type") for g in json.loads(l).get("@graph", [])]
        except Exception as x: e.append("bad JSON-LD %s" % x)
    if rel != "privacy.html":
        if "FAQPage" not in types: e.append("no FAQPage schema")
        if 'class="faq"' not in s and "faq" not in s.lower(): e.append("no visible FAQ")
    for href in set(re.findall(r'href="(/[^"#?]*)', s)):
        if href.startswith("/assets") or href == "/": continue
        if not exists(href): e.append("broken link " + href)
    text = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    if rel != "index.html" and re.search("[—–]| - ", text): e.append("dash in copy")
    print(("OK   " if not e else "FAIL ") + "%-48s %-62s %s" % (rel, t, "; ".join(e)))
    fail += bool(e)
print("\n%d page(s) with issues" % fail)
