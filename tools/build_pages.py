#!/usr/bin/env python3
"""Generate SETL's content pages: about, mission, pricing, compare, keyword landing pages, blog hub + posts, 404, sitemap, llms.txt.

Run from anywhere:  python3 tools/build_pages.py
Edit copy, prices or sources here, then rerun; never hand-edit the generated HTML.
One template so nav, footer, meta and structured data can never drift between pages."""
import json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # repo root; this file lives in tools/
SITE = "https://www.setlsleep.com"
PUBLISHED = "2026-09-14"
AUTHOR = "Jacob Redshaw"

ORG = {"@type": "Organization", "@id": SITE + "/#org", "name": "SETL", "url": SITE + "/",
       "logo": SITE + "/assets/icon-512.png", "slogan": "Focus on Life.",
       "sameAs": ["https://www.instagram.com/setl.sleep/"]}

# ---------- verified sources (checked 2026-09-14) ----------
SRC = {
 "ofcom": ("Ofcom, Online Nation 2025 report (UK internet users aged 18+, May 2025)",
           "https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-research/online-nation/2025/online-nations-report-2025.pdf?v=409837"),
 "aasm": ("American Academy of Sleep Medicine, Sleep Prioritization Survey, 2,007 US adults, June 2025",
          "https://aasm.org/americans-are-doomscrolling-at-bedtime-prioritizing-screen-time-over-sleep/"),
 "norway": ("Hjetland et al., Frontiers in Psychiatry, 2025, 45,202 students aged 18 to 28",
            "https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2025.1548273/full"),
 "chang": ("Chang et al., Proceedings of the National Academy of Sciences, 2015",
           "https://www.pnas.org/doi/10.1073/pnas.1418490112"),
 "mark47": ("University of California, on Gloria Mark's attention research",
            "https://www.universityofcalifornia.edu/news/cant-pay-attention-youre-not-alone"),
 "gallup": ("Gallup Business Journal interview with Gloria Mark, 2006",
            "https://news.gallup.com/businessjournal/23146/too-many-interruptions-work.aspx"),
 "chi08": ("Mark, Gudith and Klocke, The Cost of Interrupted Work, CHI 2008",
           "https://ics.uci.edu/~gmark/chi08-mark.pdf"),
 "aaoblue": ("American Academy of Ophthalmology, Should You Be Worried About Blue Light?",
             "https://www.aao.org/eye-health/tips-prevention/should-you-be-worried-about-blue-light"),
 "aaodev": ("American Academy of Ophthalmology, Digital Devices and Your Eyes",
            "https://www.aao.org/eye-health/tips-prevention/digital-devices-your-eyes"),
 "opal": ("Opal, pricing page (US prices)", "https://www.opalapp.com/pricing"),
 "opalstore": ("Opal on the US App Store", "https://apps.apple.com/us/app/opal-screen-time-for-focus/id1497465230"),
 "opalsleep": ("Opal Help, How do I use Sleep Mode?", "https://opalapp.com/help/how-do-i-use-sleep-mode"),
 "lally": ("Lally et al., European Journal of Social Psychology, 2010",
           "https://onlinelibrary.wiley.com/doi/abs/10.1002/ejsp.674"),
 "onesec": ("one sec, official site", "https://one-sec.app/"),
 "screenzen": ("ScreenZen, official site", "https://screenzen.co/"),
 "brick": ("Brick, official site", "https://getbrick.com/"),
 "brickfaq": ("Brick, FAQ", "https://getbrick.com/pages/faq"),
 "sunbreaksite": ("Sunbreak, official site", "https://www.getsunbreak.com/"),
 "sunbreak": ("Sunbreak on the UK App Store", "https://apps.apple.com/gb/app/sunbreak-nightly-app-blocker/id6752121964"),
 "applest": ("Apple Support, Use Screen Time on your iPhone or iPad", "https://support.apple.com/en-us/108806"),
 "apple27": ("Apple, iPhone User Guide (iOS 27), Set Screen Time schedules and time allowances",
             "https://support.apple.com/guide/iphone/set-schedules-with-screen-time-iphb0c7313c9/ios"),
 "apple26": ("Apple, iPhone User Guide (iOS 26), Downtime and App Limits",
             "https://support.apple.com/guide/iphone/set-schedules-with-screen-time-iphb0c7313c9/26.0/ios/26.0"),
 "opaltm": ("USPTO record for OPAL, Reg. No. 6,290,844, Opal OS Corporation",
            "https://tsdr.uspto.gov/#caseNumber=88823503&caseType=SERIAL_NO&searchType=statusSearch"),
}
def src(key, text=None):
    t, u = SRC[key]
    return '<a href="%s" rel="noopener" target="_blank">%s</a>' % (u, html.escape(text or t))

# ---------- SETL beta result (founder supplied; keep the evidence on file) ----------
# Set SHOW_BETA = False to pull the figures from every page at once.
SHOW_BETA = True
BETA_DAY_MIN = 243                      # 4h 3m average daily screen time saved per beta tester
BETA_NOTE = ("Average daily reduction in screen time reported by SETL beta testers in 2026, against usual screen time "
             "of 5 to 7 hours a day. Week and month figures multiply that average out. The lifetime figure assumes daily "
             "use from age 15 to 87. Individual results vary.")
def beta_strip(heading="What SETL gave back in beta", lead="The average tester's screen time, cut every single day."):
    if not SHOW_BETA:
        return ""
    wk, mo = BETA_DAY_MIN * 7 / 60, BETA_DAY_MIN * 30.44 / 60
    life = BETA_DAY_MIN / 1440 * (87 - 15)
    stats = [("4h 3m", "Less screen time a day. About 3 hours by day and 1 hour at night."),
             ("%dh" % wk, "Handed back every week."),
             ("%dh" % mo, "Every month. That is more than %d full days." % (mo // 24)),
             ("%d years" % life, "Across a lifetime of daily use.")]
    cells = "".join('<div class="stat rv%s"><b>%s</b><p>%s</p></div>' % (["", " d1", " d2", " d3"][i], a, b)
                    for i, (a, b) in enumerate(stats))
    return ('<section class="sec"><div class="wrap"><div class="sec-head center"><h2 class="rv">%s</h2>'
            '<p class="lead rv d1">%s</p></div><div class="grid g4">%s</div>'
            '<p class="fn center" style="margin:18px auto 0;max-width:70ch">%s</p></div></section>') % (heading, lead, cells, BETA_NOTE)

# ---------- FAQ: visible on the page and mirrored as FAQPage structured data ----------
def faq_section(faqs, heading):
    items = "".join('<details class="rv"><summary>%s</summary><p>%s</p></details>' % (html.escape(q), a) for q, a in faqs)
    return ('<section class="sec" id="faq"><div class="narrow"><div class="sec-head"><h2 class="rv">%s</h2></div>'
            '<div class="faq">%s</div></div></section>') % (html.escape(heading), items)

def faq_ld(faqs):
    import re as _re
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer":
            {"@type": "Answer", "text": _re.sub(r"<[^>]+>", "", a)}} for q, a in faqs]}

MENU_LINKS = [("/setl-sleep.html", "SETL Sleep"), ("/setl-sessions.html", "SETL Sessions"), ("/app-blocker.html", "App blocker"),
              ("/pricing.html", "Pricing"), ("/setl-vs-opal.html", "SETL vs Opal"), ("/blog/", "Blog"), ("/about.html", "About"),
              ("/mission.html", "Mission"), ("/#get", "Join the waitlist")]
NAV_LINKS = [("/app-blocker.html", "App blocker"), ("/blog/", "Blog"), ("/pricing.html", "Pricing"), ("/about.html", "About")]
PRODUCT_LINKS = [("/setl-sleep.html", "SETL Sleep"), ("/setl-sessions.html", "SETL Sessions"),
                 ("/app-blocker.html", "App blocker for iPhone"), ("/screen-time-blocker.html", "Screen time blocker"),
                 ("/apple-screen-time-alternative.html", "Apple Screen Time alternative"), ("/setl-vs-opal.html", "SETL vs Opal")]

def nav(current):
    links = "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == current else "", t) for h, t in NAV_LINKS)
    menu = "".join('<a href="%s">%s</a>' % (h, t) for h, t in
                   MENU_LINKS)
    return ('<header class="nav" role="banner">'
            '<a class="brand" href="/" aria-label="SETL home"><img class="ic" src="/assets/nav-ic.png" alt="" width="23" height="25">'
            '<img class="wm" src="/assets/nav-wm.png" alt="SETL" width="56" height="11"></a>'
            '<div class="navr"><nav class="links" aria-label="Primary">%s</nav>'
            '<details class="nmenu"><summary>Menu</summary><nav class="menu" aria-label="Menu">%s</nav></details></div>'
            '</header>') % (links, menu)

FOOT = ('<footer class="foot"><div class="wrap">'
        '<img class="ic" src="/assets/nav-ic.png" alt="" width="46" height="50">'
        '<p class="brandline">SETL</p><p class="tag">Focus on Life.</p><p class="goalline">On a mission to give the world a billion hours back.</p>'
        '<nav aria-label="Products">' + "".join('<a href="%s">%s</a>' % l for l in PRODUCT_LINKS) + '</nav>'
        '<nav aria-label="Footer">'
        '<a href="/">Home</a><a href="/blog/">Blog</a><a href="/pricing.html">Pricing</a>'
        '<a href="/about.html">About</a><a href="/founder-story.html">Founder story</a><a href="/mission.html">Mission</a><a href="/privacy.html">Privacy</a><a href="https://www.instagram.com/setl.sleep/" rel="noopener" target="_blank">Instagram</a>'
        '</nav>'
        '<p class="meta">&copy; <span data-year>2026</span> SETL. Built in the UK.</p>'
        '</div></footer>')

def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}

def page(path, title, desc, body, current="", ld=None, body_class="", og_type="website", extra_head="",
         faq=None, faq_title="Frequently asked questions"):
    assert len(title) <= 60, "title too long (%d): %s" % (len(title), title)
    assert len(desc) <= 160, "description too long (%d): %s" % (len(desc), path)
    url = SITE + ("/" + path if not path.endswith("index.html") else "/" + path[:-len("index.html")])
    url = url.replace("//index", "/")
    graph = [ORG] + (ld or [])
    if faq:
        sec = faq_section(faq, faq_title)
        i = body.rfind(CTA)
        body = body[:i] + sec + body[i:] if i >= 0 else body + sec
        graph.append(faq_ld(faq))
    SITEMAP.append(path)
    doc = """<!doctype html>
<html lang="en-GB" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#000000">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="SETL">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site}/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{site}/assets/og.jpg">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/icon-32.png?v=3">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/icon-180.png?v=3">
<link rel="preconnect" href="https://api.fontshare.com" crossorigin>
<link rel="preconnect" href="https://cdn.fontshare.com" crossorigin>
<link href="https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600,700&display=swap" rel="stylesheet">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css?v=4">
<link rel="alternate" type="application/rss+xml" title="SETL Blog" href="/feed.xml">
{extra_head}<script type="application/ld+json">{ld}</script>
</head>
<body{bc}>
<a class="skip" href="#main">Skip to content</a>
{nav}
<main id="main">
{body}
</main>
{foot}
<script src="/assets/site.js?v=2" defer></script>
</body>
</html>
""".format(title=html.escape(title), desc=html.escape(desc), url=url, site=SITE, og_type=og_type,
           extra_head=extra_head,
           ld=json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False),
           bc=(' class="%s"' % body_class) if body_class else "", nav=nav(current), body=body, foot=FOOT)
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(doc)
    return path

CTA = """<section class="cta-band"><div class="narrow">
<h2 class="rv">Your phone can go to sleep first.</h2>
<p class="lead rv d1">Join the SETL waitlist. Get up to 7 nights free when we launch.</p>
<div class="btn-row rv d2"><a class="btn" href="/">Join the waitlist</a><a class="btn ghost" href="/pricing.html">See pricing</a></div>
</div></section>"""

built = []
SITEMAP = []

def sources_block(keys, start=1):
    return '<div class="sources"><h2>Sources</h2><ol start="%d">%s</ol></div>' % (start, "".join(
        '<li id="s%d">%s</li>' % (i + start, src(k)) for i, k in enumerate(keys)))

def prose_sec(h2, inner, keys=None, start=1):
    """start: first footnote number, so two sourced sections on one page never share ids."""
    return ('<section class="sec"><div class="narrow"><div class="sec-head"><h2 class="rv">%s</h2></div>'
            '<div class="prose rv">%s</div>%s</div></section>') % (h2, inner, sources_block(keys, start) if keys else "")

def cards_sec(h2, lead, cards, cols="g3"):
    c = "".join('<div class="card rv%s"><span class="n">%s</span><h3>%s</h3><p>%s</p></div>' % (["", " d1", " d2"][i % 3], n, h, p)
                for i, (n, h, p) in enumerate(cards))
    return ('<section class="sec"><div class="wrap"><div class="sec-head%s"><h2 class="rv">%s</h2>%s</div>'
            '<div class="grid %s">%s</div></div></section>') % (" center" if lead else "", h2,
            ('<p class="lead rv d1">%s</p>' % lead) if lead else "", cols, c)

def table_sec(h2, head, rows, note):
    t = "".join('<tr><th scope="row">%s</th><td>%s</td><td class="us">%s</td></tr>' % r for r in rows)
    return ('<section class="sec"><div class="wrap"><div class="sec-head"><h2 class="rv">%s</h2></div>'
            '<div class="tablewrap rv"><table class="cmp"><thead><tr><th scope="col"></th><th scope="col">%s</th><th scope="col">%s</th></tr></thead>'
            '<tbody>%s</tbody></table></div><p class="fn" style="margin-top:14px">%s</p></div></section>') % (h2, head[0], head[1], t, note)

COMPARISONS = [("/setl-vs-opal.html", "Opal"), ("/setl-vs-sunbreak.html", "Sunbreak"), ("/setl-vs-one-sec.html", "one sec"),
               ("/setl-vs-screenzen.html", "ScreenZen"), ("/setl-vs-brick.html", "Brick"),
               ("/apple-screen-time-alternative.html", "Apple Screen Time")]
MARK = {"ok": "Yes", "mid": "Partly", "no": "No"}

def vs_cell(who, st, txt, us=False):
    return ('<div class="vcell%s"><span class="vwho">%s</span><i class="vdot %s" role="img" aria-label="%s"></i>'
            '<span class="vtxt">%s</span></div>') % (" us" if us else "", who, st, MARK[st], txt)

def vs_block(rival, rows, note):
    body = "".join('<div class="vrow rv"><p class="vlbl">%s</p>%s%s</div>' %
                   (lbl, vs_cell("SETL", a[0], a[1], True), vs_cell(rival, b[0], b[1])) for lbl, a, b in rows)
    return ('<div class="vs2" role="table" aria-label="SETL compared with %s">'
            '<div class="vhead" aria-hidden="true"><span></span><b class="us">SETL</b><b>%s</b></div>%s</div>'
            '<p class="fn center" style="margin-top:18px">%s</p>') % (rival, rival, body, note)

def compare_strip(current):
    links = "".join('<a class="chip" href="%s">SETL vs %s</a>' % (h, t) for h, t in COMPARISONS if h != current)
    return ('<section class="sec" style="padding-top:0"><div class="narrow center">'
            '<p class="kicker rv">Compare SETL</p><div class="chips rv">%s</div></div></section>') % links

FEATURES = [
 ("SETL SLEEP", "Blocks apps at bedtime", 'Set your bedtime once. Your chosen apps lock automatically every night. <a href="/setl-sleep.html">About SETL Sleep</a>.'),
 ("SETL SESSIONS", "Blocks apps on demand", 'Pick the apps and how long, and get deep work in the day. <a href="/setl-sessions.html">About SETL Sessions</a>.'),
 ("SETL PLANS", "Nights off, planned ahead", "Weddings, birthdays, night shifts. Book them weeks ahead and SETL steps aside."),
 ("SLEEP RESERVE", "Your night in one number", "A Lock Screen widget that shows how much of the night is left for sleep."),
 ("PRIVATE", "Nothing leaves your phone", "Apple gives SETL private tokens, so we never learn which apps you block."),
 ("PRICE", "From $3.33 a month", 'Billed $39.99 a year, with 7 nights free. <a href="/pricing.html">See pricing</a>.'),
]


# =====================================================================
# ABOUT
# =====================================================================
chapters = [
 ("22:30", "The pattern", "Every night ended the same way.", """
<p>I have ADHD, and I have always had more ideas than hours.</p>
<p>The laptop would close, the lights would go off, and my phone would come to bed with me.</p>
<p>Five more minutes. Then another five. I would look up and it would be gone midnight, again.</p>
<p>I was not lazy, and I was never short of goals. I just could not stop the one thing standing between me and them.</p>
""", "The hardest part of the day was never the work. It was the end of it.", "", ""),

 ("23:15", "The job", "I used to write the words that keep you scrolling.", """
<p>Before SETL, I was a nine figure copywriter. I wrote for brands including JD Sports and Manchester United.</p>
<p>My job was attention. Find the line that stops a thumb mid scroll, then keep it there.</p>
<p>I learned the psychology from the inside. Curiosity. Reward. The quiet pull of just one more.</p>
<p>I was good at it. Which meant I understood exactly what was happening to me every night.</p>
<p>So I stepped out of it. Now I want to help everyone else step out too, because it is built to be addictive.</p>
""", "Knowing how the trick works does not stop it working on you.", "", ""),

 ("00:40", "Everyone around me", "Then I noticed it was not just me.", """
<p>Look around any group of friends after ten at night. Faces lit blue, half in the conversation.</p>
<p>Mine were ambitious people in demanding jobs, in offices and on building sites and in their own businesses. They were also exhausted, and quietly blaming themselves for it.</p>
<p>Tired eyes. Headaches by Thursday. Mornings that started already behind.</p>
""", "Nobody I knew had a discipline problem. Every one of us had a phone problem.",
 """<div class="factrow">
<div class="fact rv"><b>0</b><p>Evidence that screens damage your retina, according to the American Academy of Ophthalmology.</p><span class="fn">%s</span></div>
<div class="fact rv d1"><b>Real</b><p>Eye strain, dryness and headaches from long screen use. We blink less while we stare.</p><span class="fn">%s</span></div>
</div>""" % (src("aaoblue", "AAO, blue light"), src("aaodev", "AAO, digital devices")), ""),

 ("01:30", "The science", "So I did what I always do. I read the research.", """
<p>I had spent time in the health supplement world, where you learn fast to separate a study from a sales pitch.</p>
<p>The sleep research was not subtle. Bright screens in the evening push your body clock later.</p>
<p>In one well known study, people who read on a tablet before bed took longer to fall asleep, produced less melatonin and felt less alert the next morning than when they read a paper book.</p>
<p>In 2025, researchers following 45,202 young adults found that every extra hour on a screen in bed came with about 24 fewer minutes of sleep.</p>
<p>And in the daytime, attention researcher Gloria Mark found we now hold focus on one screen for around 47 seconds before switching.</p>
""", "It was never a willpower problem. It was a design problem.",
 """<div class="factrow">
<div class="fact rv"><b>24 min</b><p>Less sleep for each extra hour of screen use in bed.</p><span class="fn">%s</span></div>
<div class="fact rv d1"><b>47 sec</b><p>Average time we hold attention on one screen.</p><span class="fn">%s</span></div>
</div>""" % (src("norway", "Frontiers in Psychiatry, 2025"), src("mark47", "Gloria Mark, UC Irvine")), ""),

 ("02:15", "What did not work", "I tried everything that relies on willpower at midnight.", """
<p>App timers I snoozed. Screen Time limits I dismissed with one tap. Grayscale mode that lasted about a week.</p>
<p>I tried routines, breathing, reading in bed. Some nights I reached for sleep aids, and I did not want that to become the plan.</p>
<p>At midnight, the tired version of me lost every single time. Every fix had the same flaw.</p>
""", "Every fix asked the most tired version of me to make the best decision.",
 """<p class="fn" style="margin-top:22px">This is my experience, not medical advice. If you take medication for sleep or ADHD, talk to your doctor before changing anything.</p>""", ""),

 ("03:00", "Building SETL", "So I built the thing I needed.", """
<p>The idea was simple. Make the decision once, in daylight, when you are thinking clearly.</p>
<p>Then let the phone go to sleep first, so there is nothing left to argue with at midnight.</p>
<p>I put my own money and a great deal of time into building it, as a young founder with no big company behind me.</p>
<p>SETL (say it like settle) is the result. A sleep app blocker, built night first, that looks after your daytime focus too.</p>
""", "The best time to make a midnight decision is lunchtime.", "", ""),

 ("06:30", "The morning", "This is what it is all for.", """
<p>Not a perfect life. Just mornings that start on your side.</p>
<p>The work gets done. The training happens. You are actually present for the people in front of you.</p>
<p>That is what an early night gives you back. I want everyone to have it.</p>
""", "Our goal is a billion hours given back. We are starting with tonight.",
 """<div class="signoff rv"><img src="/assets/nav-ic.png" alt="" width="46" height="46">
<div><b>Jacob Redshaw</b><span>Founder, SETL</span></div></div>
<div class="btn-row rv d1"><a class="btn" href="/">Join the waitlist</a><a class="btn ghost" href="/mission.html">Read our mission</a></div>""", "dawn"),
]
clock = "".join('<li data-hour="%d">%s<b>%s</b></li>' % (i, t, lbl) for i, (t, lbl, *_ ) in enumerate(chapters))
chap_html = ""
for i, (t, lbl, h2, prose, pull, extra, cls) in enumerate(chapters):
    chap_html += """<section class="chapter %s" data-hour="%d" data-time="%s" aria-labelledby="ch%d">
<p class="time rv" aria-hidden="true">%s</p>
<h2 id="ch%d" class="rv d1">%s</h2>
<div class="prose rv d2">%s</div>
<p class="pull rv">%s</p>
%s
</section>""" % (cls, i, t, i, t, i, html.escape(h2), prose.strip(), html.escape(pull), extra)

ABOUT_FAQ = [
 ("What is SETL?", "SETL (say it like settle) is an iPhone app blocker built for bedtime. SETL Sleep locks your distracting apps at the time you set, and SETL Sessions blocks them during the day when you need to focus."),
 ("How does SETL work?", "SETL is built on Apple's Screen Time framework. You choose the apps and the times, and iOS blocks them for you. Nothing about your usage leaves your phone."),
 ("Who is behind SETL?", "SETL is built in the UK by founder Jacob Redshaw, a nine figure copywriter with ADHD who spent his career on attention and now builds tools that give it back. <a href=\"/founder-story.html\">Read the founder story</a>."),
 ("Is SETL the same as settle sleep?", "Yes. SETL is pronounced settle, and many people search for it as settle sleep or SETL Sleep. SETL Sleep is the bedtime app blocker inside the SETL app."),
 ("Is SETL a medical app?", "No. SETL is a screen time and app blocking tool, not a treatment for ADHD, insomnia or any condition. Speak to your doctor about ongoing sleep problems."),
 ("Where is SETL based?", "SETL is built in the UK and launching on iPhone. <a href=\"/\">Join the waitlist</a> and get up to 7 nights free."),
]
about_body = """<section class="hero center"><div class="narrow">
<span class="eyebrow rv"><i></i>About SETL</span>
<h1 class="rv d1">Built for the hardest hour of the day.</h1>
<p class="lead rv d2">SETL is an iPhone app blocker built bedtime first. This is what it does, the research behind it, and who builds it.</p>
<div class="btn-row rv d3"><a class="btn" href="/">Join the waitlist</a><a class="btn ghost" href="/pricing.html">See pricing</a></div>
</div></section>
""" + prose_sec("What is SETL?", """
<p><strong>SETL</strong> (say it <em>settle</em>) is an app blocker for iPhone. You choose the apps that take your evenings, and you choose the time they close.</p>
<p>After that, nothing is left to decide. Your apps lock themselves at bedtime, every night.</p>
<p>It is built on Apple's Screen Time framework, so your usage never leaves your phone, and SETL never learns which apps you picked.</p>
""") + cards_sec("Three tools, one app", "", [
 ("SETL SLEEP", "Your night, protected", 'Your chosen apps close at bedtime, automatically. <a href="/setl-sleep.html">See SETL Sleep</a>.'),
 ("SETL SESSIONS", "Your day, on demand", 'Pick the apps and the length, and focus properly. <a href="/setl-sessions.html">See SETL Sessions</a>.'),
 ("SETL PLANS", "Real life, allowed", "Book the nights you want your apps open, weeks ahead."),
]) + prose_sec("Why SETL exists", """
<p>Half of US adults use a screen in bed every day, and 38% say it is making their sleep worse.<sup><a href="#s1">1</a></sup></p>
<p>The cost is measurable. In a 2025 study of 45,202 students, each extra hour on a screen in bed was linked to about <strong>24 minutes less sleep</strong>.<sup><a href="#s2">2</a></sup></p>
<p>None of that is a discipline problem. Feeds are built to keep going, and bedtime is when you have the least left to fight with.</p>
<p>So SETL moves the decision earlier, into daylight, when you are thinking clearly. <a href="/mission.html">Read our mission</a>.</p>
""", ["aasm", "norway"]) + beta_strip() + """
<section class="sec"><div class="wrap"><div class="sec-head"><h2 class="rv">Who builds SETL</h2></div>
<div class="founder rv">
<img src="/assets/disc-classic.webp" alt="" width="120" height="120">
<div>
<b>Jacob Redshaw</b><span class="role">Founder, SETL. Built in the UK.</span>
<p>I am a nine figure copywriter. My job was attention: find the line that stops a thumb, then hold it there. I know that psychology from the inside, and it still beat me every night.</p>
<p>I have ADHD, and no amount of trying harder fixed my bedtime. So I built the thing that decides for me, and now I want to help other people step out of it too.</p>
<a class="btn ghost" href="/founder-story.html">Read the full story</a>
</div>
</div></div></section>
""" + cards_sec("What SETL will never do", "Three promises we hold ourselves to.", [
 ("PRIVACY", "Sell or share your data", 'Apple gives SETL private tokens. We cannot see which apps you block. <a href="/privacy.html">Read the policy</a>.'),
 ("HONESTY", "Invent a number", "Every statistic on this site links to its source. If we cannot source it, we do not say it."),
 ("FAIRNESS", "Charge premium prices", 'Everything is included, for $39.99 a year. <a href="/setl-vs-opal.html">Compare us with Opal</a>.'),
]) + CTA

built.append(page("about.html",
  "About SETL: The iPhone App Blocker Built for Bedtime",
  "About SETL, the iPhone app blocker built bedtime first. What SETL Sleep and SETL Sessions do, the research behind them, and who builds it.",
  about_body, "/about.html", faq=ABOUT_FAQ, faq_title="About SETL: common questions",
  ld=[{"@type": "AboutPage", "name": "About SETL", "url": SITE + "/about.html",
       "about": {"@id": SITE + "/#org"},
       "mainEntity": {"@id": SITE + "/#org"}},
      crumbs_ld([("Home", "/"), ("About", "/about.html")])]))

# ---------------- FOUNDER STORY (the night, told as one scroll) ----------------
FOUNDER_FAQ = [
 ("Who founded SETL?", "SETL was founded by Jacob Redshaw in the UK. He is a nine figure copywriter with ADHD who spent his career writing copy designed to hold attention."),
 ("Why did a copywriter build an app blocker?", "Because he knew exactly how apps hold you, and it still worked on him every night. Knowing the trick does not stop the trick."),
 ("Why is SETL built for bedtime first?", "Because bedtime is when willpower is lowest and the cost is highest. A lost night takes the next day with it."),
 ("Is the founder story medical advice?", "No. It is one person's experience. Speak to your doctor about sleep, ADHD or medication."),
 ("How do you say SETL?", "Like settle. SETL Sleep sounds like settle sleep."),
]
founder_body = """<section class="story-hero"><div class="narrow">
<img class="moon" src="/assets/disc-classic.webp" alt="" width="190" height="190">
<span class="eyebrow rv"><i></i>Founder story</span>
<h1 class="rv d1" style="margin-top:22px">Built by someone who could not put his phone down.</h1>
<p class="lead rv d2" style="margin:22px auto 0">The story behind SETL, told across one night. Keep scrolling and watch it get light.</p>
<p class="scrollhint rv d3">22:30 to 06:30</p>
</div></section>
<div class="wrap story-layout">
<aside class="clock" aria-label="Story timeline"><ol>%s</ol></aside>
<div>
<div class="timechip" aria-hidden="true"><span>22:30</span></div>
%s
</div>
</div>
%s""" % (clock, chap_html, CTA)
built.append(page("founder-story.html",
  "SETL Founder Story: Why I Built an App Blocker",
  "The SETL founder story, told across one night: ADHD, a career spent writing copy that holds attention, and the app blocker that came out of it.",
  founder_body, "", body_class="story", faq=FOUNDER_FAQ, faq_title="The founder story: FAQs",
  ld=[{"@type": "AboutPage", "name": "SETL founder story", "url": SITE + "/founder-story.html",
       "mainEntity": {"@type": "Person", "name": AUTHOR, "jobTitle": "Founder", "nationality": "GB",
                      "description": "Founder of SETL and a nine figure copywriter, formerly writing for brands including JD Sports and Manchester United.",
                      "worksFor": {"@id": SITE + "/#org"}}},
      crumbs_ld([("Home", "/"), ("About", "/about.html"), ("Founder story", "/founder-story.html")])]))

# =====================================================================
# MISSION
# =====================================================================
stats = [
 ("4h 30m", "UK adults spend online every day. 77% of it is on a smartphone.", "ofcom", "Ofcom, 2025"),
 ("50%", "Of US adults use a screen in bed every single day.", "aasm", "AASM, 2025"),
 ("24 min", "Less sleep for each extra hour on a screen in bed.", "norway", "Frontiers in Psychiatry, 2025"),
 ("47 sec", "Average time we hold attention on one screen before switching.", "mark47", "Gloria Mark, UC Irvine"),
]
stat_html = "".join('<div class="stat rv%s"><b>%s</b><p>%s</p><span class="fn">%s</span></div>' %
                    ([""," d1"," d2"," d3"][i], s[0], s[1], src(s[2], s[3])) for i, s in enumerate(stats))
principles = [
 ("Protect the night first.", "Your evening decides tomorrow. SETL starts there, then looks after your day."),
 ("Take the decision away.", "Willpower runs out by midnight. Decide once in daylight and let SETL hold the line."),
 ("Keep it private.", "Your Screen Time data never leaves your phone. We cannot see which apps you block."),
 ("Tell the truth.", "No invented numbers. If we cannot source a statistic, it does not go on this site."),
 ("Keep it fair.", "Full access for $39.99 a year. Less than half of Opal's annual price."),
 ("Build for real life.", "Weddings, night shifts, birthdays. Plan your nights off and SETL steps aside."),
]
pr_html = "".join('<div class="principle rv"><h3>%s</h3><p>%s</p></div>' % (a, b) for a, b in principles)
MANIFESTO = [
 ("We are not short of time.", "We are short of attention. The hours are there. Something else is spending them."),
 ("The pull is designed.", "A feed has no bottom and no natural place to stop. Somebody chose that, and it is working."),
 ("Willpower is the wrong tool.", "It runs lowest exactly where you need it most: late, dark, tired, in bed."),
 ("So we move the decision.", "Choose your bedtime in daylight, while you are thinking clearly, and let your phone keep the promise."),
 ("Win the night, win the day.", "Sleep is not the reward for a good day. It is the reason you get one."),
]
man_html = "".join('<div class="stanza rv"><h3>%s</h3><p>%s</p></div>' % (a, b) for a, b in MANIFESTO)
_yr = BETA_DAY_MIN * 365 / 60                      # hours one person wins back in a year, at the beta average
GOAL_HOURS = 1000000000
people = "{:,}".format(int(round(GOAL_HOURS / _yr / 1000) * 1000))
scale = [("%s people" % people, "Each getting a full year of hours back, at the beta average of 4 hours 3 minutes a day."),
         ("114,000 years", "A billion hours, laid end to end."),
         ("%d days" % (_yr / 24), "What one person wins back in a single year.")]
scale_html = "".join('<div class="stat rv%s"><b>%s</b><p>%s</p></div>' % ([""," d1"," d2"][i], a, b) for i, (a, b) in enumerate(scale))
MISSION_FAQ = [
 ("What is SETL's mission?", "A billion hours given back. SETL blocks the apps that take your evenings so that time returns to sleep, to focus and to the people in the room."),
 ("What is the SETL manifesto?", "That attention is not a character flaw. Feeds are built to hold you, willpower is lowest at night, so the decision should be made earlier and enforced for you."),
 ("How much screen time does SETL save?", "In SETL's 2026 beta, testers reported an average of 4 hours 3 minutes less screen time a day: about 3 hours in the day and 1 hour at night."),
 ("How much screen time do adults have?", "Ofcom found UK adults spent 4 hours 30 minutes a day online in 2025, with 77% of that time on a smartphone."),
 ("Does screen time in bed affect sleep?", "Research links it. A 2025 study of 45,202 students found each extra hour of screen use in bed was linked to about 24 minutes less sleep."),
 ("Does SETL collect my data?", "No. SETL uses Apple's Screen Time framework, which gives it private tokens, so we never see which apps you block. <a href=\"/privacy.html\">Read our privacy policy</a>."),
]
mission_body = """<section class="goal"><div class="narrow">
<span class="eyebrow rv"><i></i>Our mission</span>
<p class="big rv d1" style="margin-top:34px" data-countto="1000000000" aria-label="One billion">1,000,000,000</p>
<p class="label rv d2">Hours given back. That is the goal.</p>
<h1 class="rv d2" style="margin-top:34px;font-size:var(--t-xl)">Give the world a billion hours back.</h1>
<p class="lead rv d3">Every hour SETL blocks is an hour returned to sleep, to work, and to the people in front of you.</p>
</div></section>
<section class="sec"><div class="wrap">
<div class="sec-head center"><h2 class="rv">What a billion hours looks like</h2>
<p class="lead rv d1">Big numbers hide their size. Here is this one, three ways.</p></div>
<div class="grid g3">%s</div>
<p class="fn center" style="margin:18px auto 0;max-width:70ch">%s</p>
</div></section>
<section class="sec manifesto"><div class="narrow">
<span class="eyebrow rv"><i></i>The SETL manifesto</span>
<h2 class="rv d1" style="margin-top:22px">Attention is not a character flaw.</h2>
%s
<p class="lead rv" style="margin-top:34px">That is the whole product, and the whole company.</p>
</div></section>
<section class="sec"><div class="wrap">
<div class="sec-head center"><h2 class="rv">Why it matters</h2>
<p class="lead rv d1">These are not our numbers. They are the world's, and every one is sourced.</p></div>
<div class="grid g4">%s</div>
</div></section>
%s
<section class="sec"><div class="wrap">
<div class="sec-head"><h2 class="rv">What we strive for</h2>
<p class="lead rv d1">Six promises that decide what SETL is, and what it will never become.</p></div>
<div class="principles">%s</div>
</div></section>
<section class="sec"><div class="narrow center">
<h2 class="rv">Focus is not a personality trait.</h2>
<p class="lead rv d1">It is what is left when nothing is pulling at you. SETL removes the pull.</p>
<div class="btn-row rv d2"><a class="btn" href="/founder-story.html">Read the founder story</a><a class="btn ghost" href="/blog/">Read the research</a></div>
</div></section>
%s""" % (scale_html, BETA_NOTE, man_html, stat_html,
         beta_strip("What we have handed back so far", "In beta, SETL cut the average tester's screen time every day."),
         pr_html, CTA)
built.append(page("mission.html",
  "SETL Mission: A Billion Hours Given Back",
  "SETL's mission is a billion hours given back: less screen time, better sleep and real focus. Read the SETL manifesto and what we stand for.",
  mission_body, "/mission.html", faq=MISSION_FAQ, faq_title="Screen time and our mission: FAQs",
  ld=[{"@type": "WebPage", "name": "Our mission", "url": SITE + "/mission.html", "about": {"@id": SITE + "/#org"}},
      crumbs_ld([("Home", "/"), ("Mission", "/mission.html")])]))

# =====================================================================
# PRICING
# =====================================================================
included = ["Night blocking at your bedtime", "SETL Sessions for daytime focus", "SETL Plans for nights off",
            "Sleep Reserve Lock Screen widget", "Post bedtime nudges", "The full moon collection"]
inc = "".join("<li>%s</li>" % x for x in included)
faqs = [
 ("How much does SETL cost?", "SETL costs $39.99 a year (just $3.33 a month), $5.99 a month, or $2.99 a week. Every plan includes SETL Sleep, SETL Sessions and SETL Plans."),
 ("How do the free nights work?", "Every plan starts free: 7 nights on yearly, 3 nights on monthly and 1 night on weekly. Cancel before your free nights end and you pay nothing."),
 ("Is SETL cheaper than Opal?", "Yes. SETL is $39.99 a year. Opal Pro is $99.99 a year on Opal's US pricing page, so SETL costs 60% less. <a href=\"/setl-vs-opal.html\">Compare SETL vs Opal</a>."),
 ("Is there a free app blocker for iPhone?", "Apple Screen Time is free and built in, but a limit you set for yourself is easy to ignore. SETL is a paid app blocker with up to 7 nights free. <a href=\"/apple-screen-time-alternative.html\">See how they compare</a>."),
 ("Can I cancel anytime?", "Yes. Subscriptions are handled by Apple, so you cancel in your iPhone settings in a few taps."),
 ("What does SETL actually block?", "The apps you choose, at the times you choose. Everything else on your phone, like calls and alarms, works normally."),
 ("Does SETL work on Android or Mac?", "Not yet. SETL is an iPhone app blocker for now, built on Apple's Screen Time framework."),
 ("Can SETL see my apps or messages?", "No. Apple gives SETL private tokens, so we never learn which apps you picked."),
]
pricing_body = """<section class="hero center"><div class="narrow">
<span class="eyebrow rv"><i></i>Pricing</span>
<h1 class="rv d1">Simple pricing. Up to 7 nights free.</h1>
<p class="lead rv d2">Every plan unlocks everything. Cancel before your free nights end and you pay nothing.</p>
</div></section>
<section style="padding-bottom:clamp(64px,11vw,110px)"><div class="wrap">
<div class="plans">
<article class="plan rv"><h3>Weekly</h3><p class="price">$2.99<small>/week</small></p><p class="per">1 night free, then week by week.</p><ul>%s</ul><a class="btn ghost" href="/">Join the waitlist</a></article>
<article class="plan best rv d1"><span class="badge">BEST VALUE</span><h3>Annual</h3><p class="price">$3.33<small>/month</small></p><p class="per">7 nights free. Billed $39.99 a year, save 44%% on monthly.</p><ul>%s</ul><a class="btn" href="/">Join the waitlist</a></article>
<article class="plan rv d2"><h3>Monthly</h3><p class="price">$5.99<small>/month</small></p><p class="per">3 nights free. Cancel anytime.</p><ul>%s</ul><a class="btn ghost" href="/">Join the waitlist</a></article>
</div>
<p class="fn center" style="margin-top:22px">Launch prices in US dollars, charged by Apple. Local App Store prices may differ.</p>
<div class="trustrow rv">
<div><b>Free to start</b><span>7 nights on yearly, 3 on monthly, 1 on weekly.</span></div>
<div><b>Cancel in two taps</b><span>Handled by Apple, in your iPhone settings.</span></div>
<div><b>Private by design</b><span>Your Screen Time data never leaves your phone.</span></div>
<div><b>Everything included</b><span>No feature is held back for a higher tier.</span></div>
</div>
</div></section>
%s
<section class="sec"><div class="wrap">
<div class="sec-head center"><h2 class="rv">The same job as Opal, for less.</h2>
<p class="lead rv d1">Compare a year of SETL with a year of Opal Pro.</p></div>
<div class="save rv">
<div class="col us"><b>$39.99</b><span>SETL, per year</span></div>
<div class="vs">VS</div>
<div class="col them"><b>$99.99</b><span>Opal Pro, per year</span></div>
<span class="pill">60%% less. You keep $60 a year</span>
</div>
<p class="fn center" style="margin-top:14px">Opal price from %s, US, September 2026. <a href="/setl-vs-opal.html">See the full comparison</a>.</p>
</div></section>
%s""" % (inc, inc, inc, cards_sec("What every plan includes", "One price, the whole app. No add ons, no upsells.", FEATURES), src("opal", "Opal's pricing page"), CTA)
built.append(page("pricing.html",
  "SETL Pricing: Screen Time App Blocker from $3.33/Month",
  "SETL pricing: $39.99 a year ($3.33 a month), $5.99 a month or $2.99 a week, with up to 7 nights free. A screen time app blocker for 60% less than Opal.",
  pricing_body, "/pricing.html", faq=faqs, faq_title="SETL pricing FAQs",
  ld=[{"@type": "SoftwareApplication", "name": "SETL", "operatingSystem": "iOS",
       "applicationCategory": "LifestyleApplication", "url": SITE + "/pricing.html",
       "offers": [
         {"@type": "Offer", "name": "Annual", "price": "39.99", "priceCurrency": "USD"},
         {"@type": "Offer", "name": "Monthly", "price": "5.99", "priceCurrency": "USD"},
         {"@type": "Offer", "name": "Weekly", "price": "2.99", "priceCurrency": "USD"}],
       "publisher": {"@id": SITE + "/#org"}},
      crumbs_ld([("Home", "/"), ("Pricing", "/pricing.html")])]))

# =====================================================================
# SETL vs OPAL
# =====================================================================
# status per cell: ok (green), mid (amber), no (red). SETL cells are never "no".
rows = [
 ("Built around", ("ok", "Bedtime first, then your day"), ("ok", "Daytime focus, with a Sleep Mode")),
 ("Price per year", ("ok", "$39.99"), ("no", "$99.99 for Pro")),
 ("Price per month", ("ok", "$5.99"), ("no", "$19.99 for Pro")),
 ("Free to start", ("ok", "7 nights free on yearly"), ("ok", "Free plan with 1 rule")),
 ("Automatic bedtime blocking", ("ok", "Yes, every night"), ("ok", "Yes, Sleep Mode")),
 ("Daytime focus sessions", ("ok", "Yes, SETL Sessions"), ("ok", "Yes, focus sessions")),
 ("Nights off, planned ahead", ("ok", "Yes, SETL Plans"), ("ok", "Yes, with schedules")),
 ("Sleep left, on your Lock Screen", ("ok", "Yes, Sleep Reserve"), ("no", "Not listed")),
 ("Private by design", ("ok", "Screen Time data stays on iPhone"), ("ok", "Browsing data stays on device")),
 ("Devices", ("mid", "iPhone"), ("ok", "iPhone, Android and Mac")),
]
tbl = "".join('<div class="vrow rv"><p class="vlbl">%s</p>%s%s</div>' % (lbl, vs_cell("SETL", a[0], a[1], True), vs_cell("Opal", b[0], b[1]))
              for lbl, a, b in rows)   # the Opal page keeps its own longer layout
VS_FAQ = [
 ("Is SETL a good Opal alternative?", "If your screen time problem is worst at night, yes. SETL is an app blocker built bedtime first, with daytime focus sessions, for $39.99 a year against Opal Pro's $99.99."),
 ("What is the difference between SETL and Opal?", "Opal is a focus app for iPhone, Android and Mac with a Sleep Mode. SETL is iPhone only and built around bedtime, with SETL Plans for nights off and a Sleep Reserve widget."),
 ("How much does Opal cost?", "On Opal's US pricing page, checked September 2026: a free plan, Opal Pro at $99.99 a year or $19.99 a month, and a $399 lifetime plan."),
 ("Is there a cheaper app like Opal?", "SETL costs $39.99 a year, $5.99 a month or $2.99 a week, which is less than half of Opal Pro's yearly price. <a href=\"/blog/opal-alternatives.html\">See more Opal alternatives</a>."),
 ("Does SETL work on Android like Opal?", "Not yet. SETL is iPhone only for now. If you need one blocker across Android or Mac, Opal covers those platforms."),
 ("Is SETL affiliated with Opal?", "No. Opal is a registered trademark of Opal OS Corporation, and SETL is an independent app built in the UK."),
]
vs_body = """<section class="hero center"><div class="narrow">
<span class="eyebrow rv"><i></i>Opal alternative</span>
<h1 class="rv d1">SETL vs Opal</h1>
<p class="lead rv d2">Opal is built for your workday. SETL is built for your bedtime, at less than half the price.</p>
</div></section>
<section style="padding-bottom:clamp(64px,11vw,110px)"><div class="wrap">
<div class="vs2" role="table" aria-label="SETL vs Opal comparison">
<div class="vhead" aria-hidden="true"><span></span><b class="us">SETL</b><b>Opal</b></div>
%s
</div>
<p class="fn center" style="margin-top:18px">Opal details from %s, its App Store listing and help centre, checked September 2026. SETL prices are launch prices.</p>
</div></section>
<section class="sec"><div class="wrap">
<div class="grid g2">
<div class="card rv"><span class="n">CHOOSE SETL IF</span><h3>Your problem starts at bedtime.</h3>
<p>You lose evenings to your phone, want it locked at night, and want to pay $39.99 a year.</p></div>
<div class="card rv d1"><span class="n">CHOOSE OPAL IF</span><h3>You need Mac or Android.</h3>
<p>You want one blocker across Android, Mac and iPhone, a free plan, or a one off $399 lifetime licence.</p></div>
</div>
</div></section>
<section class="sec"><div class="narrow">
<div class="sec-head"><h2 class="rv">Why a bedtime first app blocker?</h2></div>
<div class="prose rv">
<p>Most screen time apps treat the night as one setting among many. SETL starts there.</p>
<p>The research is clear on why. In a 2025 study of 45,202 young adults, each extra hour on a screen in bed meant about 24 fewer minutes of sleep.<sup><a href="#s1">1</a></sup></p>
<p>Half of US adults use a screen in bed every day.<sup><a href="#s2">2</a></sup> A lost night costs the next day's focus too.</p>
<p>Read <a href="/blog/best-app-blocker-for-sleep.html">how to choose the best app blocker for sleep</a>, or see <a href="/pricing.html">SETL pricing</a>.</p>
</div>
<div class="sources"><h2>Sources</h2><ol><li id="s1">%s</li><li id="s2">%s</li><li>%s</li><li>%s</li></ol></div>
<p class="fn" style="margin-top:18px" id="tm">Opal is a registered trademark of Opal OS Corporation. SETL is not affiliated with, endorsed by or sponsored by Opal. Product names are used only to identify and compare products.</p>
</div></section>
%s%s""" % (tbl, src("opal", "Opal's pricing page"), src("norway"), src("aasm"), src("opal"), src("opaltm"), compare_strip("/setl-vs-opal.html"), CTA)
built.append(page("setl-vs-opal.html",
  "SETL vs Opal (2026): The Cheaper Opal Alternative",
  "SETL vs Opal compared: price, night blocking, focus sessions and devices. An honest look at the Opal alternative built for bedtime, 60% cheaper.",
  vs_body, "", faq=VS_FAQ, faq_title="SETL vs Opal: FAQs",
  ld=[{"@type": "WebPage", "name": "SETL vs Opal", "url": SITE + "/setl-vs-opal.html"},
      crumbs_ld([("Home", "/"), ("SETL vs Opal", "/setl-vs-opal.html")])]))

# =====================================================================
# HEAD TO HEAD PAGES
# =====================================================================
def versus(slug, rival, title, desc, h1, lead, intro, rows, note, cards, faq, keys):
    body = ("""<section class="hero center"><div class="narrow">
<span class="eyebrow rv"><i></i>SETL vs %s</span>
<h1 class="rv d1">%s</h1>
<p class="lead rv d2">%s</p>
<div class="btn-row rv d3"><a class="btn" href="/">Join the waitlist</a><a class="btn ghost" href="/pricing.html">See pricing</a></div>
</div></section>
<section class="sec" style="padding-top:clamp(8px,2vw,20px)"><div class="wrap">%s</div></section>
""" % (rival, h1, lead, vs_block(rival, rows, note))
      + prose_sec("How SETL and %s differ" % rival, intro, keys)
      + cards_sec("Which one fits you", "", cards)
      + compare_strip("/" + slug) + CTA)
    built.append(page(slug, title, desc, body, "", faq=faq, faq_title="SETL vs %s: FAQs" % rival,
      ld=[{"@type": "WebPage", "name": "SETL vs %s" % rival, "url": SITE + "/" + slug, "description": desc,
           "isPartOf": {"@id": SITE + "/#site"}, "publisher": {"@id": SITE + "/#org"}},
          crumbs_ld([("Home", "/"), ("SETL vs %s" % rival, "/" + slug)])]))

versus("setl-vs-sunbreak.html", "Sunbreak",
 "SETL vs Sunbreak: Two Bedtime App Blockers Compared",
 "SETL vs Sunbreak compared: bedtime blocking, unlock times, accountability partners, daytime focus and price. Two iPhone app blockers built for sleep.",
 "SETL vs Sunbreak", "Both block your apps at bedtime. They disagree about what happens next.",
 """
<p>Sunbreak and SETL are the two iPhone app blockers built around sleep rather than the workday, so this is the closest comparison on the site.</p>
<p>Sunbreak locks your apps at bedtime and keeps them locked <strong>until sunrise at your location</strong>, and it can name a friend who gets an email automatically if you break your bedtime.<sup><a href="#s1">1</a></sup></p>
<p>SETL blocks at the bedtime you set, then hands the day back to you with <a href="/setl-sessions.html">SETL Sessions</a> and books your nights off in advance with SETL Plans.</p>
<p>One leans on social pressure. The other leans on removing the decision. Both beat willpower at midnight.</p>""",
 [("Built for bedtime", ("ok", "Yes, night first"), ("ok", "Yes, night first")),
  ("When apps unlock", ("ok", "The wake time you choose"), ("ok", "Sunrise at your location")),
  ("Daytime focus blocks", ("ok", "Yes, SETL Sessions"), ("no", "Not listed")),
  ("Nights off, planned ahead", ("ok", "Yes, SETL Plans"), ("no", "Not listed")),
  ("Accountability partner", ("mid", "No. It stays between you and your phone"), ("ok", "Yes, a friend gets an email")),
  ("Sleep left, on your Lock Screen", ("ok", "Yes, Sleep Reserve"), ("no", "Not listed")),
  ("Price", ("ok", "$39.99 a year, 7 nights free"), ("mid", "Free with in app purchases, plan price not published")),
  ("Devices", ("ok", "iPhone"), ("ok", "iPhone and iPad")),
 ],
 'Sunbreak details from its own site and App Store listing, checked September 2026. SETL prices are launch prices.',
 [("CHOOSE SETL IF", "You want your day covered too", 'You lose evenings and hours of the working day, and you want one app for both. <a href="/setl-sessions.html">See SETL Sessions</a>.'),
  ("CHOOSE SUNBREAK IF", "Shame is your motivator", "You want a friend told automatically when you break bedtime, and you like waking with the sun."),
  ("EITHER WAY", "Stop the midnight scroll", 'Both are far stronger at night than a limit you can wave away. <a href="/blog/best-app-blocker-for-sleep.html">Compare the field</a>.')],
 [("Is SETL or Sunbreak better for sleep?", "Both block apps at bedtime. SETL adds daytime focus sessions and planned nights off; Sunbreak adds an accountability partner and unlocks at sunrise."),
  ("Does SETL have an accountability partner?", "No. SETL keeps it between you and your phone by removing the decision at bedtime, rather than telling a friend afterwards."),
  ("How much does Sunbreak cost?", "Sunbreak is listed on the App Store as free with in app purchases, and no plan price is published on its site, checked September 2026."),
  ("How much does SETL cost?", 'SETL is $39.99 a year, $5.99 a month or $2.99 a week, with 7 nights free on the yearly plan. <a href="/pricing.html">See pricing</a>.'),
  ("Do both work on iPhone only?", "SETL is iPhone only for now. Sunbreak is on iPhone and iPad, and says Android is on its roadmap.")],
 ["sunbreaksite", "sunbreak"])

versus("setl-vs-one-sec.html", "one sec",
 "SETL vs one sec: Block Apps or Pause Before Them",
 "SETL vs one sec compared: blocking apps at bedtime versus a breathing pause before each app opens. Features, platforms and price, checked 2026.",
 "SETL vs one sec", "A pause before you open, or a door that is already closed.",
 """
<p>These two app blockers solve the same problem in opposite ways.</p>
<p><strong>one sec</strong> interrupts the moment you open an app, with a breathing exercise or a prompt before it lets you through, and says its essentials are free.<sup><a href="#s1">1</a></sup></p>
<p><strong>SETL</strong> does not wait for that moment. Your chosen apps are closed from your bedtime until morning, so at 1am there is nothing to breathe through.</p>
<p>A pause is gentler. A block is stronger when you are tired. Read <a href="/blog/what-is-an-app-blocker.html">how app blockers work</a>.</p>""",
 [("Main method", ("ok", "Blocks chosen apps outright"), ("ok", "Adds a pause before an app opens")),
  ("Built around", ("ok", "Bedtime first, then your day"), ("ok", "The moment you reach for an app")),
  ("Automatic every night", ("ok", "Yes, at your bedtime"), ("no", "Not its design")),
  ("Nights off, planned ahead", ("ok", "Yes, SETL Plans"), ("no", "Not listed")),
  ("Sleep left, on your Lock Screen", ("ok", "Yes, Sleep Reserve"), ("no", "Not listed")),
  ("Free option", ("ok", "7 nights free on yearly"), ("ok", "Essentials are free")),
  ("Price", ("ok", "$39.99 a year"), ("mid", "Individual price not published on its site")),
  ("Devices", ("mid", "iPhone"), ("ok", "iPhone, Android and browser extensions")),
 ],
 'one sec details from its own site, checked September 2026. SETL prices are launch prices.',
 [("CHOOSE SETL IF", "The problem is the night", "You keep losing evenings, and you want the apps simply gone until morning."),
  ("CHOOSE ONE SEC IF", "You want a gentler nudge", "You would rather be asked to think for a second than be shut out, and you need Android or a laptop too."),
  ("WORTH KNOWING", "Friction and blocking differ", 'Friction slows a habit. Blocking removes the option. <a href="/blog/why-apps-are-addictive.html">Why that matters</a>.')],
 [("Is SETL or one sec better?", "It depends on when you slip. one sec interrupts you as you open an app. SETL blocks your chosen apps completely from bedtime until morning."),
  ("Is one sec free?", "one sec says its essentials are free, with paid features beyond that. Its site does not publish an individual price, checked September 2026."),
  ("Does one sec block apps at bedtime?", "Its design is a pause at the moment you open an app rather than an automatic nightly block, which is what SETL Sleep does."),
  ("Does SETL work on Android?", "Not yet. SETL is iPhone only for now, while one sec lists iPhone, Android and browser extensions."),
  ("Can I use both?", "Yes. Some people use a pause during the day and a hard block at night, which is what SETL is built for.")],
 ["onesec"])

versus("setl-vs-screenzen.html", "ScreenZen",
 "SETL vs ScreenZen: Free App Blocker or Built for Bed",
 "SETL vs ScreenZen compared: a free cross platform screen time app against an iPhone app blocker built for bedtime. Features, price and who each suits.",
 "SETL vs ScreenZen", "One is free on everything. One is built for the hour you lose.",
 """
<p><strong>ScreenZen</strong> is free. Its site calls it "the only free screen time app for iOS, macOS, Windows and Android", supported by donations, with waits before apps open, daily limits and scheduled blocks.<sup><a href="#s1">1</a></sup></p>
<p>That is a genuinely strong offer, and if budget is the deciding factor you should try it.</p>
<p><strong>SETL</strong> is paid, iPhone only, and narrower on purpose: everything in it exists to protect the hours around your bedtime, then your focus during the day.</p>
<p>See where both sit among <a href="/blog/best-screen-time-apps-for-iphone.html">the best screen time apps for iPhone</a>.</p>""",
 [("Price", ("ok", "$39.99 a year, 7 nights free"), ("ok", "Free, donation supported")),
  ("Built around", ("ok", "Bedtime first, then your day"), ("ok", "Waits, limits and focus blocks")),
  ("Automatic bedtime blocking", ("ok", "Yes, every night"), ("ok", "Yes, scheduled blocks")),
  ("Nights off, planned ahead", ("ok", "Yes, SETL Plans"), ("no", "Not listed")),
  ("Sleep left, on your Lock Screen", ("ok", "Yes, Sleep Reserve"), ("no", "Not listed")),
  ("Rewards for keeping nights", ("ok", "Yes, the moon collection"), ("no", "Not listed")),
  ("Devices", ("mid", "iPhone"), ("ok", "iOS, macOS, Windows and Android")),
 ],
 'ScreenZen details from its own site, checked September 2026. SETL prices are launch prices.',
 [("CHOOSE SETL IF", "Bedtime is the battle", "You want one app that guards the night, plans your exceptions, and makes keeping it feel like progress."),
  ("CHOOSE SCREENZEN IF", "Price decides it", "You want a capable blocker at no cost, across a laptop and a phone."),
  ("HONEST NOTE", "Free is hard to beat", 'Pay for SETL because the night matters most to you, not because free tools do nothing. <a href="/pricing.html">See what you get</a>.')],
 [("Is ScreenZen really free?", "Yes. ScreenZen says it is completely free and donation supported, across iOS, macOS, Windows and Android, checked September 2026."),
  ("Why pay for SETL if ScreenZen is free?", "Because SETL is built for one job: the hours around your bedtime, with planned nights off, a Sleep Reserve widget and rewards for nights you keep."),
  ("Which is better for sleep?", "SETL is designed for bedtime first. ScreenZen can schedule blocks too, but its design covers screen time generally."),
  ("Does ScreenZen work on iPhone?", "Yes, and also on macOS, Windows and Android. SETL is iPhone only for now."),
  ("How much is SETL?", 'SETL is $39.99 a year, $5.99 a month or $2.99 a week, with 7 nights free on yearly. <a href="/pricing.html">See pricing</a>.')],
 ["screenzen"])

versus("setl-vs-brick.html", "Brick",
 "SETL vs Brick: App Blocker App or Physical Device",
 "SETL vs Brick compared: a $59 physical device you tap to block apps, against an iPhone app blocker that locks your apps at bedtime automatically.",
 "SETL vs Brick", "One asks you to carry something. One asks you to decide once.",
 """
<p><strong>Brick</strong> is a small physical device. You choose your apps, tap your phone on the Brick to start a session, and your phone stays blocked until you physically tap it again. It costs <strong>$59.00</strong> and works with iPhones on iOS 17.0 or later and Android 12.0 or later.<sup><a href="#s1">1</a></sup></p>
<p>Ending a block needs a rescan, and there is a Strict Mode plus a small number of emergency unlocks if you lose it.<sup><a href="#s2">2</a></sup></p>
<p><strong>SETL</strong> needs nothing extra. You set your bedtime once and your apps close on their own, every night, with no object to remember or leave in another room.</p>""",
 [("Hardware needed", ("ok", "None, just your iPhone"), ("mid", "Yes, a $59 device to carry")),
  ("Starts by itself at bedtime", ("ok", "Yes, automatically"), ("no", "No, you tap to start a session")),
  ("Cost", ("ok", "$39.99 a year, 7 nights free"), ("ok", "$59.00 one off")),
  ("If you lose the thing", ("ok", "Nothing to lose"), ("mid", "A limited number of emergency unlocks")),
  ("Daytime focus blocks", ("ok", "Yes, SETL Sessions"), ("ok", "Yes, tap to start")),
  ("Nights off, planned ahead", ("ok", "Yes, SETL Plans"), ("no", "Not listed")),
  ("Devices", ("mid", "iPhone"), ("ok", "iPhone and Android")),
 ],
 'Brick details from its own site and FAQ, checked September 2026. SETL prices are launch prices.',
 [("CHOOSE SETL IF", "You will not carry a gadget", "You want the block to happen whether or not you remember anything, every single night."),
  ("CHOOSE BRICK IF", "You want real distance", "Leaving the unlock in another room genuinely helps you, and a one off payment suits you better."),
  ("WORTH KNOWING", "They can work together", 'Brick covers deliberate sessions. SETL covers the night you were not planning to lose. <a href="/setl-sleep.html">See SETL Sleep</a>.')],
 [("Is Brick better than an app blocker?", "Brick adds physical distance, which some people need. It only blocks when you tap it, so it does not cover the night you did not plan for."),
  ("How much does Brick cost?", "Brick's site lists the device at $59.00 as a one off purchase, checked September 2026. SETL is $39.99 a year."),
  ("Does Brick work with iPhone?", "Yes. Brick's site says it works with iPhones on iOS 17.0 or later and Android devices on 12.0 or later."),
  ("What happens if I lose my Brick?", "Brick's FAQ describes a limited number of emergency unlocks. With SETL there is nothing to lose, because the block lives on your phone."),
  ("Does SETL start blocking on its own?", "Yes. You set your bedtime once and SETL Sleep blocks your chosen apps automatically every night.")],
 ["brick", "brickfaq"])

# =====================================================================
# BLOG POSTS
# =====================================================================
POSTS = []          # every post spec, in site order; rendered after all are collected

def post(slug, title, h1, desc, tagline, minutes, intro, body, sources, related, keywords, answer="", faq=None, primary=""):
    POSTS.append(dict(slug=slug, title=title, h1=h1, desc=desc, tagline=tagline, minutes=minutes, intro=intro,
                      body=body, sources=sources, related=related, keywords=keywords, answer=answer, faq=faq or [],
                      primary=primary))

R = {"scroll": "how-to-stop-scrolling-in-bed", "blocker": "best-app-blocker-for-sleep",
     "focus": "does-it-take-23-minutes-to-refocus", "science": "screens-melatonin-and-sleep"}
def rl(*keys): return [R[k] for k in keys]

post("how-to-stop-scrolling-in-bed",
 "How to Stop Scrolling in Bed: 7 Fixes That Work | SETL",
 "How to stop scrolling in bed: 7 fixes that actually work",
 "Can't stop scrolling in bed? Seven evidence-based ways to cut screen time at night that don't rely on willpower, from the team behind SETL.",
 "Sleep", 6,
 "Half of adults take a screen to bed every night. Here is how to stop, without relying on willpower.",
 """
<p>If you keep telling yourself "five more minutes" and losing an hour, you are not unusual. <strong>50% of US adults use a screen in bed every day</strong>, and 38% say it is making their sleep worse.<sup><a href="#fn1">1</a></sup></p>
<p>The cost is measurable. A 2025 study of 45,202 young adults found that each extra hour on a screen after going to bed came with about <strong>24 minutes less sleep</strong> and noticeably higher odds of insomnia symptoms.<sup><a href="#fn2">2</a></sup></p>
<p>Here is what actually helps.</p>

<h2>Why willpower fails at night</h2>
<p>Bedtime is when you are most tired and least able to make a good decision. Every scroll is a fresh choice, and every choice is made by the worst rested version of you.</p>
<p>The fixes that work have one thing in common. <strong>They make the decision before you are tired.</strong></p>

<h2>1. Decide your bedtime in daylight</h2>
<p>Pick a time while you are thinking clearly. Work back from your alarm and the sleep you actually need.</p>

<h2>2. Let the phone lock itself</h2>
<p>An app blocker that switches on automatically at bedtime removes the nightly argument. Apple's free Screen Time schedules (Downtime in iOS 26) are a start, though limits you set for yourself are easy to override.</p>
<p>A dedicated <a href="/blog/best-app-blocker-for-sleep.html">sleep app blocker</a> is built to be harder to undo when you are half asleep.</p>

<h2>3. Charge it outside the bedroom</h2>
<p>If the phone is not within reach, the scroll never starts. Use a cheap alarm clock instead.</p>

<h2>4. Block the apps, not the phone</h2>
<p>You still need calls, alarms and maps. Block the handful of apps that pull you in, and leave the rest alone.</p>

<h2>5. Make the screen boring</h2>
<p>Grayscale mode strips out the colour that makes feeds rewarding. It helps, though most people switch it off within weeks.</p>

<h2>6. Plan your nights off</h2>
<p>A rule that ignores weddings and night shifts gets abandoned. Schedule exceptions ahead of time so the rule survives real life.</p>

<h2>7. Replace the scroll</h2>
<p>A paper book, a podcast on a timer, or simply lights out. The habit needs somewhere else to go.</p>

<div class="callout"><strong>The pattern behind all seven:</strong> decide once, while you are rested, and let the environment do the enforcing at night.</div>

<h2>Where SETL fits</h2>
<p>SETL (say it like settle) was built for exactly this. Set your bedtime once, and SETL puts your distracting apps to sleep before you do. <a href="/pricing.html">Get up to 7 nights free</a>.</p>
""",
 ["aasm", "norway"], rl("blocker", "science", "focus"),
 "stop scrolling in bed, screen time at night, doomscrolling, bedtime app blocker, SETL", primary="stop scrolling in bed",
 answer="To stop scrolling in bed, decide your bedtime while you are rested and let something else enforce it. Charge your phone outside the bedroom, block the few apps that pull you in, plan nights off ahead, and use an app blocker that locks those apps automatically at bedtime.",
 faq=[("How do I stop scrolling on my phone in bed?", "Make the decision before you are tired. Set a bedtime in daylight, charge the phone out of reach, and use a bedtime app blocker like <a href=\"/setl-sleep.html\">SETL Sleep</a> to lock distracting apps automatically."),
      ("Why can't I stop scrolling at night?", "Bedtime is when you are most tired, and every scroll is a fresh choice. Feeds are designed to keep going, so willpower alone rarely wins at midnight."),
      ("Does scrolling in bed affect sleep?", "Research links it. A 2025 study of 45,202 students found each extra hour on a screen in bed was linked to about 24 minutes less sleep."),
      ("What app stops you scrolling at night?", "Apple's Downtime is free but easy to dismiss. SETL is an iPhone app blocker built for bedtime that blocks your chosen apps automatically every night."),
      ("Is it bad to use your phone before bed?", "Many adults do: half of US adults use a screen in bed daily, and 38% say it worsens their sleep. Cutting time in bed is the simplest change.")])

post("best-app-blocker-for-sleep",
 "Best App Blocker for Sleep in 2026 (Compared) | SETL",
 "The best app blocker for sleep in 2026",
 "What makes the best app blocker for sleep? How screen blocker apps work on iPhone, and how Apple Downtime, Opal, Sunbreak and SETL compare.",
 "App blockers", 7,
 "Most app blockers were built for the workday. Here is what one needs to do when the problem is bedtime.",
 """
<p>An app blocker, sometimes called a screen blocker app, stops chosen apps from opening at set times. On iPhone they are built on Apple's Screen Time framework.</p>
<p>That framework is designed for privacy. The app receives <strong>opaque tokens</strong> for the apps you pick, so a well built blocker never learns what you use.</p>

<h2>What a sleep app blocker needs to do</h2>
<p>Blocking during the day and blocking at bedtime are different jobs. At night, four things matter.</p>
<h3>It switches on by itself</h3>
<p>If you have to start it, you will not. The block should begin at your bedtime, every night, automatically.</p>
<h3>It is hard to undo at midnight</h3>
<p>A one tap override is a willpower test you will fail when tired. Look for deliberate friction before an app unlocks.</p>
<h3>It understands real life</h3>
<p>Nights off for events and shift work, planned in advance, so the rule does not collapse the first time life gets in the way.</p>
<h3>It keeps your data on the phone</h3>
<p>Your usage patterns are personal. A good blocker processes them on the device and never uploads them.</p>

<h2>The main options</h2>
<h3>Apple Screen Time</h3>
<p>Free and already on your iPhone. In iOS 27 its bedtime tool is a Screen Time Schedule; in iOS 26 it was Downtime. When Block at Downtime is off, downtime only shows a reminder, and when you set limits for yourself, you know the passcode.<sup><a href="#fn5">5</a></sup></p>
<h3>Opal</h3>
<p>A polished focus app for iPhone, Android and Mac, with a Sleep Mode. Opal Pro costs $99.99 a year, and there is a free plan with one rule.<sup><a href="#fn3">3</a></sup></p>
<h3>Sunbreak</h3>
<p>A nightly app blocker that locks apps at bedtime and can alert an accountability partner if you break your pact.<sup><a href="#fn4">4</a></sup></p>
<h3>SETL</h3>
<p>Built bedtime first. SETL blocks your chosen apps at the time you set, plans nights off with SETL Plans, and brings the same block into your day with SETL Sessions. <strong>$39.99 a year</strong>, with 7 nights free.</p>
<p>See the full <a href="/setl-vs-opal.html">SETL vs Opal comparison</a>.</p>

<div class="callout"><strong>The honest answer:</strong> the best app blocker is the one you cannot talk yourself out of at 1am. Test that first, then compare features.</div>
""",
 ["aasm", "norway", "opal", "sunbreak", "apple26"], ["what-is-an-app-blocker", "best-screen-time-apps-for-iphone", "opal-alternatives"],
 "app blocker, screen blocker app, best app blocker for sleep, screen time app, Opal alternative, SETL", primary="best app blocker for sleep",
 answer="The best app blocker for sleep switches on by itself at bedtime, is hard to undo when you are half asleep, lets you plan nights off, and keeps your data on your phone. Apple Downtime is free, Opal suits daytime focus, and SETL is built bedtime first.",
 faq=[("What is the best app blocker for sleep?", "One that blocks apps automatically at bedtime and is hard to undo at 1am. SETL is built bedtime first for iPhone, from $3.33 a month billed yearly."),
      ("What is a screen blocker app?", "A screen blocker app stops chosen apps opening at set times. On iPhone they use Apple's Screen Time framework. <a href=\"/app-blocker.html\">See how SETL blocks apps</a>."),
      ("Is Apple Downtime a good app blocker for sleep?", "It is free and schedules well (a Screen Time Schedule in iOS 27), but limits you set for yourself are easy to override. <a href=\"/apple-screen-time-alternative.html\">Compare Apple Screen Time and SETL</a>."),
      ("Is SETL cheaper than Opal?", "Yes. SETL is $39.99 a year and Opal Pro is $99.99 a year on Opal's US pricing page, checked September 2026."),
      ("Do app blockers see my data?", "Well built iPhone app blockers do not. Apple gives them private tokens for the apps you choose, so SETL never learns which apps you block.")])

post("does-it-take-23-minutes-to-refocus",
 "Does It Take 23 Minutes to Refocus After a Distraction?",
 "Does it really take 23 minutes to refocus?",
 "The '23 minutes to refocus' figure is everywhere. Where it really comes from, what the research found, and what it means for focus.",
 "Focus", 5,
 "It is one of the most shared facts about focus. The real story is more interesting, and more useful.",
 """
<p>You have probably read that it takes <strong>23 minutes and 15 seconds</strong> to get back on task after an interruption. It appears in books, talks and a lot of productivity apps.</p>
<p>So where does it come from?</p>

<h2>The source is an interview</h2>
<p>The figure traces back to attention researcher <strong>Gloria Mark</strong> of the University of California, Irvine, quoted in a 2006 interview with Gallup.<sup><a href="#fn2">2</a></sup></p>
<p>It is a real estimate from someone who has spent decades studying attention. But it is often cited to a study that does not actually contain that number.</p>

<h2>What the study actually found</h2>
<p>Mark's 2008 paper, <em>The Cost of Interrupted Work</em>, found something surprising. People who were interrupted finished tasks <strong>faster</strong>, not slower.<sup><a href="#fn3">3</a></sup></p>
<p>The cost showed up elsewhere. They reported <strong>more stress, more frustration and more time pressure</strong>. Interruptions did not only steal time. They made the work feel worse.</p>

<h2>The number that holds up</h2>
<p>Mark's more recent research tracks how long people stay on one screen before switching. In her early studies it was about two and a half minutes.</p>
<p>Today it averages <strong>around 47 seconds</strong>.<sup><a href="#fn1">1</a></sup> And much of that switching is self interruption. We break our own focus.</p>

<div class="callout"><strong>The takeaway:</strong> the exact minutes matter less than the pattern. Constant switching raises stress, and the phone is the easiest switch in the room.</div>

<h2>What to do with this</h2>
<p>If most interruptions are self inflicted, the fix is to remove the option, not to try harder.</p>
<ul>
<li>Block your most distracting apps during focused work.</li>
<li>Decide the session length before you start.</li>
<li>Protect your sleep, because tired brains switch more.</li>
</ul>
<p>That is what SETL Sessions are for. Pick the apps, pick how long, and get deep work on demand. Read <a href="/blog/how-to-stop-scrolling-in-bed.html">how to stop scrolling in bed</a> next.</p>
""",
 ["mark47", "gallup", "chi08"], rl("science", "scroll", "blocker"),
 "focus, distraction, 23 minutes to refocus, attention span, deep work, SETL", primary="23 minutes to refocus",
 answer="The claim that it takes 23 minutes to refocus comes from a 2006 interview with researcher Gloria Mark, not a single study result. Her 2008 study found interrupted people worked faster but felt more stressed, and her later research found attention on one screen now lasts around 47 seconds.",
 faq=[("Does it really take 23 minutes to refocus?", "The 23 minutes figure comes from Gloria Mark in a 2006 Gallup interview. It is an informed estimate, but it is often wrongly cited to a study that does not contain it."),
      ("How long is the average attention span on a screen?", "Gloria Mark's research found people now switch screens after around 47 seconds on average, down from about two and a half minutes in her early studies."),
      ("Do interruptions make you slower?", "Not always. In Mark's 2008 study, interrupted people finished faster, but reported more stress, frustration and time pressure."),
      ("How do I stop distractions when working?", "Remove the option. Block your most distracting apps for a set time with a focus app blocker like <a href=\"/setl-sessions.html\">SETL Sessions</a>."),
      ("What is deep work?", "Deep work means long, uninterrupted focus on one demanding task. It needs protection from the self interruptions phones make so easy.")])

post("screens-melatonin-and-sleep",
 "Screen Time Before Bed: Melatonin and Sleep | SETL",
 "Screens, melatonin and sleep: what your phone does after dark",
 "How screen time at night affects melatonin, your body clock and sleep, and what screens really do to your eyes. Sourced and plainly explained.",
 "Science", 6,
 "What the research says about phones, light and sleep, and the popular myth about your eyes.",
 """
<p>Screens at night affect sleep in two ways. The light shifts your body clock, and the content keeps your brain switched on.</p>

<h2>Light and your body clock</h2>
<p>Your body releases <strong>melatonin</strong> as evening falls, which helps signal that it is time to sleep. Bright light in the evening pushes that process later.</p>
<p>In a 2015 study in PNAS, adults read on a light emitting tablet or a printed book for four hours before bed, over several evenings.<sup><a href="#fn1">1</a></sup></p>
<p>With the tablet, they <strong>took longer to fall asleep</strong>, produced <strong>less melatonin</strong>, had a <strong>later body clock</strong>, less REM sleep, and felt <strong>less alert the next morning</strong>.</p>

<h2>Time in bed on a screen</h2>
<p>A large 2025 study of <strong>45,202</strong> students in Norway looked at screen use after getting into bed.<sup><a href="#fn2">2</a></sup></p>
<p>Each extra hour was linked to about <strong>24 minutes less sleep</strong> and higher odds of insomnia symptoms. Interestingly, the type of activity mattered less than the time spent.</p>
<p>That is a strong argument for limiting time on the phone in bed, whatever you are doing on it.</p>

<h2>How common it is</h2>
<p><strong>Half of US adults</strong> use a screen in bed every day, and 38% say it makes their sleep worse.<sup><a href="#fn3">3</a></sup></p>

<h2>What screens do not do to your eyes</h2>
<p>A popular claim says screen light damages your retina. According to the American Academy of Ophthalmology, <strong>there is no scientific evidence</strong> that blue light from devices causes that damage.<sup><a href="#fn4">4</a></sup></p>
<p>The discomfort is still real. Long screen sessions cause <strong>digital eye strain</strong>: dry, tired eyes and headaches, partly because we blink less while staring.<sup><a href="#fn5">5</a></sup></p>
<div class="callout"><strong>Try the 20-20-20 rule.</strong> Every 20 minutes, look at something 20 feet away for 20 seconds.</div>

<h2>What actually helps</h2>
<ul>
<li>Stop using the phone in bed, rather than just dimming it.</li>
<li>Keep a consistent bedtime, set while you are rested.</li>
<li>Let an app blocker enforce it, so you are not negotiating at midnight.</li>
</ul>
<p>This is the problem SETL was built for. <a href="/about.html">Read why we built it</a>.</p>
<p class="fn">This article is general information, not medical advice. Speak to your doctor about ongoing sleep problems.</p>
""",
 ["chang", "norway", "aasm", "aaoblue", "aaodev"], rl("scroll", "blocker", "focus"),
 "screen time sleep, phone before bed, melatonin, blue light, digital eye strain, SETL", primary="screen time before bed",
 answer="Screen time before bed affects sleep in two ways. Bright screens in the evening can delay melatonin and your body clock, and time on the phone in bed pushes sleep later. Screens do not damage your retina, according to ophthalmologists, but they do cause eye strain.",
 faq=[("Does screen time before bed affect melatonin?", "Yes, in research. A 2015 PNAS study found reading on a light emitting tablet before bed reduced melatonin, delayed the body clock and made people less alert the next morning."),
      ("How long before bed should I stop using my phone?", "There is no single proven cut off. The strongest evidence is against time on a screen in bed, so keeping the phone out of bed is a good start."),
      ("Does blue light from phones damage your eyes?", "According to the American Academy of Ophthalmology, there is no scientific evidence that blue light from devices damages your eyes. Digital eye strain is real, though."),
      ("Does night mode stop screens affecting sleep?", "Dimming helps with light, but the Norway study found time in bed on a screen mattered more than the activity. Less time on the phone in bed is the bigger lever."),
      ("What is the 20-20-20 rule?", "Every 20 minutes, look at something 20 feet away for 20 seconds. It is a simple way to ease digital eye strain.")])

# ---- posts written as modules in tools/posts/<slug>.py (see tools/posts/BRIEF.md) ----
import importlib.util, glob, re
TOPIC_ORDER = ["how-to-stop-scrolling-in-bed", "best-app-blocker-for-sleep", "what-is-an-app-blocker",
               "screen-time-limits-not-working", "how-to-use-downtime-on-iphone", "how-to-reduce-screen-time-on-iphone",
               "best-screen-time-apps-for-iphone", "opal-alternatives", "bedtime-procrastination", "how-to-stop-doomscrolling",
               "phone-addiction-signs", "why-apps-are-addictive", "app-blocker-for-adhd", "how-much-screen-time-is-too-much",
               "does-grayscale-reduce-screen-time", "does-it-take-23-minutes-to-refocus", "screens-melatonin-and-sleep"]
for f in sorted(glob.glob(os.path.join(ROOT, "tools", "posts", "*.py"))):
    if os.path.basename(f) == "check.py":
        continue
    try:
        spec = importlib.util.spec_from_file_location("post_" + os.path.basename(f)[:-3], f)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        POSTS.append(dict(mod.POST))
    except Exception as e:
        print("SKIPPED post module", f, e)
POSTS.sort(key=lambda p: TOPIC_ORDER.index(p["slug"]) if p["slug"] in TOPIC_ORDER else 99)
REG = {p["slug"]: p for p in POSTS}

CAT_SLUG = {"App blockers": "app-blockers", "Screen Time": "screen-time", "Sleep": "sleep",
            "Psychology": "psychology", "Focus": "focus", "Science": "science"}

def post_card(slug, cls="", big=False):
    p = REG[slug]
    blurb = html.escape(p["desc"].split(". ")[0].rstrip(".") + ".")
    return ('<a class="post-card%s%s" data-cat="%s" href="/blog/%s.html">'
            '<span class="tagline">%s</span><h3>%s</h3><p>%s</p><span class="meta">%d min read</span></a>' %
            (" big" if big else "", cls, CAT_SLUG.get(p["tagline"], "sleep"), slug,
             html.escape(p["tagline"]), html.escape(p["h1"]), blurb, p["minutes"]))

for P in POSTS:
    slug, url = P["slug"], "/blog/%s.html" % P["slug"]
    srcs = [SRC[s] if isinstance(s, str) else tuple(s) for s in P["sources"]]
    src_list = "".join('<li id="fn%d"><a href="%s" rel="noopener" target="_blank">%s</a></li>' % (i + 1, u, html.escape(t))
                       for i, (t, u) in enumerate(srcs))
    rel = "".join(post_card(s) for s in P["related"] if s in REG)
    answer = ('<div class="answer rv"><span>Quick answer</span><p>%s</p></div>' % html.escape(P["answer"])) if P["answer"] else ""
    b = """<article><header class="article-head"><div class="narrow">
<p class="crumbs"><a href="/">Home</a> / <a href="/blog/">Blog</a></p>
<span class="eyebrow"><i></i>%s</span>
<h1 style="margin-top:20px;font-size:clamp(34px,6.4vw,54px)">%s</h1>
<p class="lead" style="margin-top:18px">%s</p>
<p class="meta">By <a href="/about.html">%s</a> &middot; <time datetime="%s">14 September 2026</time> &middot; %d min read</p>
</div></header>
<div class="narrow">%s<div class="prose">%s</div>
<div class="sources"><h2>Sources</h2><ol>%s</ol></div>
<div class="authorbox"><img src="/assets/nav-ic.png" alt="" width="44" height="48">
<div><b>Jacob Redshaw</b><span>Founder of SETL, the iPhone app blocker built bedtime first. Former copywriter, now building the tool he needed. <a href="/founder-story.html">Read his story</a>.</span></div></div>
</div></article>
%s<section class="sec" style="padding-top:0"><div class="narrow"><div class="related"><h2>Keep reading</h2><div class="posts">%s</div></div></div></section>
%s""" % (html.escape(P["tagline"]), html.escape(P["h1"]), html.escape(P["intro"]), AUTHOR, PUBLISHED, P["minutes"],
         answer, P["body"].strip(), src_list, "%FAQ%", rel, CTA)
    faq_html = faq_section(P["faq"], "%s: FAQs" % (P["primary"][:1].upper() + P["primary"][1:])) if P["faq"] else ""
    b = b.replace("%FAQ%", faq_html)
    ld = [{"@type": "BlogPosting", "headline": P["h1"], "description": P["desc"], "url": SITE + url,
           "datePublished": PUBLISHED, "dateModified": PUBLISHED, "inLanguage": "en-GB",
           "keywords": P["keywords"], "image": SITE + "/assets/og.jpg",
           "about": P["primary"] or P["h1"],
           "author": {"@type": "Person", "name": AUTHOR, "url": SITE + "/about.html"},
           "publisher": {"@id": SITE + "/#org"}, "mainEntityOfPage": SITE + url,
           "citation": [u for _, u in srcs]},
          crumbs_ld([("Home", "/"), ("Blog", "/blog/"), (P["h1"], url)])]
    if P["faq"]:
        ld.append(faq_ld(P["faq"]))
    built.append(page("blog/%s.html" % slug, P["title"], P["desc"], b, "/blog/", og_type="article", ld=ld))

# =====================================================================
# BLOG HUB  (grouped by topic so each group heading carries its keyword)
# =====================================================================
GROUPS = [("App blockers", "App blockers and screen time apps"), ("Screen Time", "Apple Screen Time and cutting screen time"),
          ("Sleep", "Sleep and scrolling in bed"), ("Psychology", "Why we scroll: phone addiction and app design"),
          ("Focus", "Focus, ADHD and distraction"), ("Science", "The science of screens and sleep")]
FEATURED = "how-to-stop-scrolling-in-bed"
chips = "".join('<a class="chip" href="#%s">%s</a>' % (CAT_SLUG[t], t) for t, _ in GROUPS if any(p["tagline"] == t for p in POSTS))
hub_secs = ""
for tag, heading in GROUPS:
    items = [p for p in POSTS if p["tagline"] == tag and p["slug"] != FEATURED]
    if items:
        hub_secs += ('<section class="sec" id="%s" style="padding-top:0"><div class="wrap">'
                     '<h2 class="rv" style="margin-bottom:22px">%s</h2><div class="posts">%s</div></div></section>') % (
            CAT_SLUG[tag], heading, "".join(post_card(p["slug"], " rv") for p in items))
hub = """<section class="hero center"><div class="narrow">
<span class="eyebrow rv"><i></i>The SETL blog</span>
<h1 class="rv d1">Screen time, app blockers, sleep and focus.</h1>
<p class="lead rv d2">Short, sourced reads on why we scroll, what it costs, and how to stop. Every number links to the study it came from.</p>
<div class="chips rv d3">%s</div>
</div></section>
<section class="sec" style="padding-top:clamp(10px,3vw,24px)"><div class="wrap">
<p class="kicker rv">Start here</p>
<div class="posts one">%s</div>
</div></section>
%s
%s""" % (chips, post_card(FEATURED, " rv", big=True), hub_secs, CTA)
HUB_FAQ = [
 ("What does the SETL blog cover?", "Sourced guides on app blockers, Apple Screen Time, reducing screen time, scrolling in bed, bedtime procrastination, phone addiction and focus."),
 ("Who writes the SETL blog?", "Jacob Redshaw, founder of SETL. Every statistic links to its original source, and nothing is published without one."),
 ("What is the best way to stop scrolling at night?", "Decide your bedtime while you are rested, then let something else enforce it. <a href=\"/blog/how-to-stop-scrolling-in-bed.html\">Read seven fixes</a> or see <a href=\"/setl-sleep.html\">SETL Sleep</a>."),
 ("What is an app blocker?", "An app blocker stops chosen apps from opening at set times. <a href=\"/app-blocker.html\">SETL is an app blocker for iPhone</a> built for bedtime."),
 ("Is the SETL blog medical advice?", "No. It is general information based on published research. Speak to your doctor about ongoing sleep, attention or mental health concerns."),
]
built.append(page("blog/index.html",
  "SETL Blog: Screen Time, App Blockers, Sleep and Focus",
  "The SETL blog: sourced guides to app blockers, Apple Screen Time, reducing screen time, doomscrolling, phone addiction, sleep and focus.",
  hub, "/blog/", faq=HUB_FAQ, faq_title="SETL blog FAQs",
  ld=[{"@type": "Blog", "name": "SETL Blog", "url": SITE + "/blog/", "publisher": {"@id": SITE + "/#org"},
       "blogPost": [{"@type": "BlogPosting", "headline": p["h1"], "url": SITE + "/blog/%s.html" % p["slug"]} for p in POSTS]},
      crumbs_ld([("Home", "/"), ("Blog", "/blog/")])]))

# =====================================================================
# KEYWORD LANDING PAGES  (one search intent per page)
# =====================================================================
def reads_sec(h2, slugs):
    cards = "".join(post_card(s, " rv") for s in slugs if s in REG)
    return ('<section class="sec"><div class="wrap"><div class="sec-head"><h2 class="rv">%s</h2></div>'
            '<div class="posts">%s</div></div></section>') % (h2, cards) if cards else ""

def landing(path, title, desc, eyebrow, h1, lead, sections, faq, faq_title, name, about):
    hero = """<section class="hero center"><div class="narrow">
<span class="eyebrow rv"><i></i>%s</span>
<h1 class="rv d1">%s</h1>
<p class="lead rv d2">%s</p>
<div class="btn-row rv d3"><a class="btn" href="/">Join the waitlist</a><a class="btn ghost" href="/pricing.html">See pricing</a></div>
</div></section>""" % (eyebrow, h1, lead)
    built.append(page(path, title, desc, hero + "".join(sections) + CTA, "/" + path, faq=faq, faq_title=faq_title,
        ld=[{"@type": "WebPage", "name": name, "url": SITE + "/" + path, "description": desc, "about": about,
             "isPartOf": {"@id": SITE + "/#site"}, "publisher": {"@id": SITE + "/#org"}},
            {"@type": "SoftwareApplication", "name": "SETL", "alternateName": ["SETL Sleep", "setl", "settle sleep"],
             "operatingSystem": "iOS", "applicationCategory": "LifestyleApplication", "url": SITE + "/",
             "offers": {"@type": "Offer", "price": "39.99", "priceCurrency": "USD"}, "publisher": {"@id": SITE + "/#org"}},
            crumbs_ld([("Home", "/"), (name, "/" + path)])]))

BETA_FAQ = ("How much screen time does SETL save?",
            "In SETL's 2026 beta, testers reported an average of 4 hours 3 minutes less screen time a day: about 3 hours in the day and 1 hour at night.")
def with_beta(faqs):
    return faqs + ([BETA_FAQ] if SHOW_BETA else [])


# ---- 1. App blocker ----
landing("app-blocker.html",
 "App Blocker for iPhone: Block Apps at Bedtime | SETL",
 "SETL is an app blocker for iPhone that locks distracting apps at bedtime and in focus sessions, automatically. Private, simple, from $3.33 a month.",
 "App blocker for iPhone", "The app blocker that puts your phone to bed first.",
 "SETL blocks the apps you choose, at the times you choose, automatically. Nights first, then your day.",
 [prose_sec("What is an app blocker?", """
<p>An <strong>app blocker</strong> is an app that stops chosen apps from opening at set times, or for a set length of time.</p>
<p>On iPhone, app blockers are built on Apple's Screen Time framework. That lets them block apps like TikTok, Instagram, YouTube or games without ever seeing what you do in them.</p>
<p>Most app blockers were designed for the workday. SETL is the app blocker built for the hardest moment to put a phone down: <strong>bedtime</strong>.</p>
<p>New to this? Read <a href="/blog/what-is-an-app-blocker.html">what an app blocker is and how app blockers work</a>.</p>"""),
  cards_sec("How to block apps on iPhone with SETL", "Three steps, once. Then it runs every night.", [
   ("01", "Pick your apps", "Choose the apps that steal your evenings. Social, video, games, anything."),
   ("02", "Set your bedtime", "Decide once, in daylight, while you are thinking clearly."),
   ("03", "Let SETL block them", "At bedtime your chosen apps lock automatically. Everything you did not pick keeps working."),
  ]),
  cards_sec("Everything in the SETL app blocker", "", FEATURES),
  beta_strip(),
  prose_sec("Why an app blocker works when willpower does not", """
<p>At midnight, every scroll is a new decision, made by the most tired version of you.</p>
<p>That version of you is busy. <strong>50% of US adults use a screen in bed every day</strong>, and 38% say it makes their sleep worse.<sup><a href="#s1">1</a></sup></p>
<p>An app blocker makes the decision once, earlier, and holds it. That is the whole idea behind SETL.</p>
<p>Compare the options in <a href="/blog/best-app-blocker-for-sleep.html">the best app blocker for sleep</a>, or see <a href="/setl-vs-opal.html">SETL vs Opal</a>.</p>""", ["aasm"]),
  reads_sec("App blocker guides", ["what-is-an-app-blocker", "best-app-blocker-for-sleep", "best-screen-time-apps-for-iphone", "app-blocker-for-adhd"])],
 with_beta([
  ("What is the best app blocker for iPhone?", 'The best app blocker is the one you cannot talk yourself out of at 1am. SETL blocks apps automatically every night and costs $39.99 a year. <a href="/blog/best-app-blocker-for-sleep.html">Compare app blockers</a>.'),
  ("How do app blockers work on iPhone?", "iPhone app blockers use Apple's Screen Time framework. You choose apps, the blocker receives private tokens for them, and iOS blocks those apps during the times you set."),
  ("Can an app blocker block TikTok and Instagram at night?", "Yes. With SETL you pick TikTok, Instagram or any other app, set your bedtime, and SETL blocks them automatically every night."),
  ("Is there a free app blocker for iPhone?", 'Apple Screen Time is free and built in, but limits you set for yourself are easy to ignore. SETL is paid, with up to 7 nights free. <a href="/apple-screen-time-alternative.html">Compare them</a>.'),
  ("Will an app blocker stop my calls and alarms?", "No. SETL only blocks the apps you choose. Calls, alarms and every app you did not pick keep working."),
  ("Does SETL work on Android?", "Not yet. SETL is an app blocker for iPhone only for now."),
 ]), "App blocker FAQs", "App blocker for iPhone", "app blocker")

# ---- 2. Screen time blocker / restrictor ----
landing("screen-time-blocker.html",
 "Screen Time Blocker & Restrictor App for iPhone | SETL",
 "Want a screen time blocker or screen time restrictor? SETL cuts screen time on iPhone by blocking distracting apps at bedtime and while you focus.",
 "Screen time blocker", "A screen time blocker that actually holds the line.",
 "Trackers show you the damage. SETL blocks the apps that cause it, at night and on demand in the day.",
 [prose_sec("What is a screen time blocker?", """
<p>A <strong>screen time blocker</strong>, sometimes called a <strong>screen time restrictor</strong> or <strong>screen timer blocker</strong>, cuts your screen time by blocking apps, not just measuring them.</p>
<p>A tracker tells you how long you spent. A blocker stops the time being spent.</p>
<p>There is a lot of it to win back. UK adults spent <strong>4 hours 30 minutes a day online</strong> in 2025, and 77% of that time was on a smartphone.<sup><a href="#s1">1</a></sup></p>
<p>And it costs sleep. In a study of 45,202 students, each extra hour on a screen in bed was linked to about <strong>24 minutes less sleep</strong>.<sup><a href="#s2">2</a></sup></p>
<p>Start with <a href="/blog/how-to-reduce-screen-time-on-iphone.html">how to reduce screen time on iPhone</a>.</p>""", ["ofcom", "norway"]),
  table_sec("Screen time tracker vs screen time blocker", ("Tracker or timer", "SETL screen time blocker"), [
   ("What it does", "Reports your screen time, or warns you when a timer runs out", "Blocks the apps you choose, on a schedule or for a session"),
   ("At midnight", "Relies on you choosing to stop", "Your apps are already locked at bedtime"),
   ("In the day", "Daily limits per app", "SETL Sessions: pick apps, pick how long"),
   ("Nights off", "Change settings by hand", "Planned ahead with SETL Plans"),
   ("Your data", "Varies by app", "Stays on your iPhone"),
  ], "A general comparison of how trackers and blockers work. See <a href=\"/apple-screen-time-alternative.html\">Apple Screen Time vs SETL</a> for a specific one."),
  cards_sec("Two ways SETL restricts screen time", "Night and day, from one app.", [
   ("NIGHT", "SETL Sleep", 'Your distracting apps lock at bedtime, every night, automatically. <a href="/setl-sleep.html">See SETL Sleep</a>.'),
   ("DAY", "SETL Sessions", 'A screen timer blocker for focus. Choose apps and a length, and they unlock when time is up. <a href="/setl-sessions.html">See SETL Sessions</a>.'),
   ("REAL LIFE", "SETL Plans", "Book the nights you want your apps open, so the rule survives weddings and night shifts."),
  ]),
  beta_strip("How much screen time SETL cut in beta"),
  reads_sec("Screen time guides", ["how-to-reduce-screen-time-on-iphone", "how-much-screen-time-is-too-much", "best-screen-time-apps-for-iphone", "does-grayscale-reduce-screen-time"])],
 with_beta([
  ("What is a screen time restrictor?", "A screen time restrictor is an app that limits when you can use certain apps. SETL restricts screen time by blocking your chosen apps at bedtime and during focus sessions."),
  ("What is a screen timer blocker?", "A screen timer blocker blocks chosen apps for a set length of time. SETL Sessions works this way: pick the apps, pick how long, and they unlock when the session ends."),
  ("How do I restrict screen time on my iPhone?", 'Apple Screen Time has Screen Time Schedules and Time Allowances in Settings (Downtime and App Limits in iOS 26). For blocking that runs automatically every night, use an app blocker like SETL. <a href="/blog/how-to-reduce-screen-time-on-iphone.html">Full guide</a>.'),
  ("How much screen time is too much?", 'There is no official daily limit for adults. A better test is what it replaces: sleep, focus and time with people. <a href="/blog/how-much-screen-time-is-too-much.html">Read more</a>.'),
  ("Can I block screen time only at night?", "Yes. SETL Sleep blocks your chosen apps only at bedtime, so your phone works normally during the day unless you start a SETL Session."),
 ]), "Screen time blocker FAQs", "Screen time blocker", "screen time blocker")

# ---- 3. Apple Screen Time alternative ----
landing("apple-screen-time-alternative.html",
 "Apple Screen Time Alternative for Bedtime | SETL",
 "Apple Screen Time limits too easy to ignore? SETL is an Apple Screen Time alternative for iPhone that blocks distracting apps at bedtime, automatically.",
 "Apple Screen Time alternative", "An Apple Screen Time alternative for the 1am you.",
 "Screen Time is brilliant at showing you the problem. SETL is built to stop it at bedtime.",
 [prose_sec("What Apple Screen Time does well", """
<p><strong>Apple Screen Time</strong> is free and already on your iPhone. It shows how you use your phone and lets you set limits.</p>
<p>In iOS 27, a <strong>Screen Time Schedule</strong> sets when apps are available and <strong>Time Allowances</strong> set how long you can use them.<sup><a href="#s1">1</a></sup> In iOS 26, the equivalent features were <strong>Downtime</strong> and <strong>App Limits</strong>.<sup><a href="#s2">2</a></sup></p>
<p>If Screen Time is working for you, keep using it. Honestly.</p>
<p>New to it? Here is <a href="/blog/how-to-use-downtime-on-iphone.html">how to use Downtime on iPhone</a>.</p>""", ["apple27", "apple26"]),
  prose_sec("Why Apple Screen Time limits get ignored", """
<p>Screen Time was built with families in mind. A parent sets the passcode, and the child lives with the limits.</p>
<p>When you set limits for yourself, you are both the parent and the child. You know the passcode. And at midnight, you are the one asking for more time.</p>
<p>Apple's iOS 26 guide says that when Block at Downtime is off, downtime only shows you a reminder.<sup><a href="#s3">3</a></sup></p>
<p>That is not a flaw in you. It is a mismatch between the tool and the moment. Read <a href="/blog/screen-time-limits-not-working.html">why Screen Time limits stop working</a>.</p>""", ["apple26"], start=3),
  table_sec("Apple Screen Time vs SETL", ("Apple Screen Time", "SETL"), [
   ("Price", "Free, built in", "$39.99 a year, 7 nights free"),
   ("Bedtime blocking", "Screen Time Schedule (Downtime in iOS 26)", "SETL Sleep, automatic every night"),
   ("Daytime focus", "Time Allowances (App Limits in iOS 26)", "SETL Sessions: pick apps and how long"),
   ("Nights off", "Edit your schedule", "Planned weeks ahead with SETL Plans"),
   ("Night at a glance", "Not a feature", "Sleep Reserve Lock Screen widget"),
   ("Reports", "Detailed usage reports", "Focused on blocking, not reports"),
   ("Built for", "Families and personal limits", "Adults who scroll at night"),
  ], "Apple Screen Time features from Apple Support, checked September 2026. SETL prices are launch prices."),
  cards_sec("Use them together", "SETL is built on Apple's Screen Time framework, so they work side by side.", [
   ("KEEP", "Screen Time reports", "See where your hours go, for free."),
   ("ADD", "SETL at bedtime", 'Let <a href="/setl-sleep.html">SETL Sleep</a> lock your apps every night without the midnight argument.'),
   ("GAIN", "Focus in the day", 'Start a <a href="/setl-sessions.html">SETL Session</a> when you need deep work.'),
  ]),
  beta_strip(),
  reads_sec("Apple Screen Time guides", ["screen-time-limits-not-working", "how-to-use-downtime-on-iphone", "how-to-reduce-screen-time-on-iphone"])],
 with_beta([
  ("Is Apple Screen Time enough to stop scrolling at night?", "For some people, yes. If you set your own passcode and keep ignoring your limits at bedtime, an app blocker built for night, like SETL, can help."),
  ("Why are my Screen Time limits not working?", 'Often because you set them for yourself and know the passcode, so the limit is a request, not a rule. <a href="/blog/screen-time-limits-not-working.html">Read the fixes</a>.'),
  ("What is the best alternative to Apple Screen Time?", "It depends on your problem. For daytime focus across devices, apps like Opal suit many people. For bedtime scrolling on iPhone, SETL is built for exactly that."),
  ("Does SETL replace Apple Screen Time?", "No. SETL is built on Apple's Screen Time framework and asks for Screen Time permission. You can keep Screen Time for reports and use SETL to block apps."),
  ("Is Apple Screen Time free?", "Yes. Screen Time is built into iPhone at no cost. SETL costs $39.99 a year, $5.99 a month or $2.99 a week, with up to 7 nights free."),
 ]), "Apple Screen Time FAQs", "Apple Screen Time alternative", "Apple Screen Time")

# ---- 4. SETL Sleep ----
landing("setl-sleep.html",
 "SETL Sleep: The Bedtime App Blocker for iPhone",
 "SETL Sleep (say it settle sleep) blocks your distracting apps at bedtime every night, automatically, so you stop scrolling in bed and get to sleep.",
 "SETL Sleep&trade;", "SETL Sleep puts your phone to bed before you do.",
 "Set your bedtime once. Every night after that, your distracting apps go to sleep on time. No willpower needed.",
 [prose_sec("What is SETL Sleep?", """
<p><strong>SETL Sleep</strong> (say it <em>settle sleep</em>) is the bedtime app blocker inside SETL.</p>
<p>You choose the apps that keep you up and set a bedtime. At that time, every night, SETL blocks them automatically.</p>
<p>It exists because bedtime is when willpower is weakest. <strong>Half of US adults use a screen in bed every day</strong>, and 38% say it makes their sleep worse.<sup><a href="#s1">1</a></sup></p>
<p>In a 2025 study of 45,202 students, each extra hour on a screen in bed was linked to about <strong>24 minutes less sleep</strong>.<sup><a href="#s2">2</a></sup></p>""", ["aasm", "norway"]),
  cards_sec("How SETL Sleep works", "Decide once. Sleep every night.", [
   ("01", "Choose your apps", "Pick the ones that turn five minutes into an hour."),
   ("02", "Set your bedtime", "Choose it while you are rested, not at midnight."),
   ("03", "Put the phone to sleep", "At bedtime your apps lock on their own. Calls and alarms keep working."),
  ]),
  cards_sec("Built for real nights", "", [
   ("SETL PLANS", "Nights off, booked ahead", "Weddings, birthdays, holidays and night shifts. SETL steps aside on the nights you choose."),
   ("SLEEP RESERVE", "Your night in one number", "A Lock Screen widget showing how much of the night is left for sleep."),
   ("MOONS", "A reason to keep going", "Earn a collection of moons as you keep your bedtimes."),
  ]),
  beta_strip("What SETL gave back in beta", "About 1 hour a night, and 3 more in the day."),
  prose_sec("Stop scrolling in bed, for good", """
<p>The fix that lasts is not trying harder. It is deciding earlier and letting your phone do the enforcing.</p>
<p>Read <a href="/blog/how-to-stop-scrolling-in-bed.html">how to stop scrolling in bed</a>, what drives <a href="/blog/bedtime-procrastination.html">bedtime procrastination</a>, and <a href="/blog/screens-melatonin-and-sleep.html">what screens do to your sleep</a>.</p>
<p class="fn">SETL is not a medical device and does not treat sleep disorders. Speak to your doctor about ongoing sleep problems.</p>"""),
  reads_sec("Sleep guides", ["how-to-stop-scrolling-in-bed", "bedtime-procrastination", "screens-melatonin-and-sleep", "best-app-blocker-for-sleep"])],
 with_beta([
  ("What is SETL Sleep?", "SETL Sleep is a bedtime app blocker for iPhone. Set your bedtime once, and SETL blocks your chosen distracting apps automatically at that time every night."),
  ("How do you pronounce SETL?", "SETL is pronounced settle, so SETL Sleep sounds like settle sleep."),
  ("How does SETL Sleep stop me scrolling in bed?", "It removes the decision. Your apps lock at bedtime before the scroll starts, so there is nothing to argue with at midnight."),
  ("What if I have a late night planned?", "Use SETL Plans to book nights off in advance, like a wedding or a night shift, and SETL Sleep steps aside for those nights."),
  ("Is SETL Sleep a sleep tracker?", "No. SETL Sleep does not track your sleep. It blocks the apps that keep you awake, and Sleep Reserve shows how much of the night is left."),
  ("How much does SETL Sleep cost?", 'SETL Sleep is included in every SETL plan: $39.99 a year, $5.99 a month or $2.99 a week, with up to 7 nights free. <a href="/pricing.html">See pricing</a>.'),
 ]), "SETL Sleep FAQs", "SETL Sleep", "SETL Sleep bedtime app blocker")

# ---- 5. SETL Sessions ----
landing("setl-sessions.html",
 "SETL Sessions: Focus App Blocker for Deep Work | SETL",
 "SETL Sessions is a focus app blocker for iPhone. Pick the apps, pick how long, and get deep work on demand for study, work, the gym and more.",
 "SETL Sessions&trade;", "Deep work on demand.",
 "Pick the apps. Pick how long. SETL Sessions blocks your distractions until the time is up.",
 [prose_sec("What is a focus app blocker?", """
<p>A <strong>focus app blocker</strong> blocks distracting apps for a set length of time, so you can do one thing properly.</p>
<p><strong>SETL Sessions</strong> brings the same blocking as SETL Sleep into your day. Choose the apps, choose how long, and start.</p>
<p>The block ends by itself when the session is over. If you really need an app sooner, you press and hold to open it. A deliberate choice, not a reflex tap.</p>
<p>Why it matters: attention researcher Gloria Mark found we now hold attention on one screen for <strong>around 47 seconds</strong> before switching.<sup><a href="#s1">1</a></sup> Read <a href="/blog/does-it-take-23-minutes-to-refocus.html">what distraction really costs</a>.</p>""", ["mark47"]),
  cards_sec("What people use SETL Sessions for", "", [
   ("WORK", "Deep work", "Protect the hours where the real work happens."),
   ("STUDY", "Revision and exams", "Put social apps away until the chapter is done."),
   ("ADHD", "Fewer choices to fight", 'Removing the option can be easier than resisting it. <a href="/blog/app-blocker-for-adhd.html">App blockers and ADHD</a>.'),
   ("TRAINING", "The gym", "Rest between sets, not between reels."),
   ("PEOPLE", "Dates and quality time", "Be in the room you are actually in."),
   ("CALLS", "Meetings", "Stay present while the call is on."),
  ]),
  beta_strip("What SETL gave back in beta", "About 3 hours a day, and 1 more at night."),
  reads_sec("Focus guides", ["does-it-take-23-minutes-to-refocus", "app-blocker-for-adhd", "how-to-stop-doomscrolling", "why-apps-are-addictive"])],
 with_beta([
  ("What is SETL Sessions?", "SETL Sessions is a focus app blocker for iPhone. Pick the apps to block and how long for, and SETL blocks them until the session ends."),
  ("Can I end a SETL Session early?", "Yes. Press and hold to open your apps sooner. It is deliberate on purpose, so a reflex tap cannot undo your focus."),
  ("Is SETL Sessions good for studying?", "Yes. Start a session before revision, block social and video apps, and they unlock by themselves when your study block is done."),
  ("Can an app blocker help with ADHD focus?", 'Many people find removing the option easier than resisting it. SETL is not a treatment for ADHD. <a href="/blog/app-blocker-for-adhd.html">Read more</a>.'),
  ("Is SETL Sessions included in SETL?", "Yes. SETL Sessions, SETL Sleep and SETL Plans are included in every plan, from $3.33 a month billed yearly."),
 ]), "SETL Sessions FAQs", "SETL Sessions", "focus app blocker")

# =====================================================================
# 404
# =====================================================================
nf = """<section class="hero center" style="min-height:80vh"><div class="narrow">
<img src="/assets/disc-twilight.webp" alt="" width="150" height="150" style="width:150px;margin:0 auto 30px;opacity:.9">
<h1>This page has gone to sleep.</h1>
<p class="lead" style="margin:18px auto 0">It is not here, but plenty else is.</p>
<div class="btn-row"><a class="btn" href="/">Back to SETL</a><a class="btn ghost" href="/blog/">Read the blog</a></div>
</div></section>"""
page("404.html", "Page not found | SETL", "This page could not be found.", nf, "")
SITEMAP.remove("404.html")
s = open(os.path.join(ROOT, "404.html"), encoding="utf-8").read()
s = s.replace('<meta name="robots" content="index,follow,max-image-preview:large">', '<meta name="robots" content="noindex">')
open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(s)

# =====================================================================
# SITEMAP + llms.txt
# =====================================================================
def loc(p): return SITE + "/" + (p[:-len("index.html")] if p.endswith("index.html") else p)
PRIO = {"pricing.html": "0.9", "setl-sleep.html": "0.9", "app-blocker.html": "0.9", "screen-time-blocker.html": "0.9",
        "apple-screen-time-alternative.html": "0.9", "setl-sessions.html": "0.8", "setl-vs-opal.html": "0.8",
        "blog/index.html": "0.8", "about.html": "0.7", "mission.html": "0.6"}
urls = [("", "1.0", "weekly")] + [(p, PRIO.get(p, "0.7"), "monthly") for p in SITEMAP] + [("privacy.html", "0.3", "yearly")]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    "  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>\n" % (loc(p), PUBLISHED, f, pr)
    for p, pr, f in urls) + "</urlset>\n"
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sm)

rss_items = "".join("""  <item>
    <title>%s</title>
    <link>%s</link>
    <guid isPermaLink="true">%s</guid>
    <description>%s</description>
    <category>%s</category>
    <pubDate>Mon, 14 Sep 2026 09:00:00 +0100</pubDate>
  </item>
""" % (html.escape(p["h1"]), SITE + "/blog/%s.html" % p["slug"], SITE + "/blog/%s.html" % p["slug"],
       html.escape(p["desc"]), html.escape(p["tagline"])) for p in POSTS)
open(os.path.join(ROOT, "feed.xml"), "w", encoding="utf-8").write("""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>SETL Blog</title>
  <link>%s/blog/</link>
  <atom:link href="%s/feed.xml" rel="self" type="application/rss+xml"/>
  <description>Sourced guides to app blockers, screen time, sleep and focus, from SETL.</description>
  <language>en-gb</language>
%s</channel>
</rss>
""" % (SITE, SITE, rss_items))

llms = ["# SETL: Focus on Life.", "",
 "> SETL (pronounced settle) is an iPhone app blocker built bedtime first. SETL Sleep blocks chosen distracting apps automatically "
 "at bedtime every night; SETL Sessions blocks them on demand for daytime focus; SETL Plans schedules nights off. Built in the UK "
 "by founder Jacob Redshaw. Pricing: $39.99 a year ($3.33 a month), $5.99 a month or $2.99 a week. Free nights: 7 on yearly, 3 on monthly, 1 on weekly. iPhone only.", "",
 "Also searched as: SETL Sleep, setl, settle sleep, SETL app blocker.", "",
 "Instagram: https://www.instagram.com/setl.sleep/", ""]
if SHOW_BETA:
    llms += ["In SETL's 2026 beta, testers reported an average of 4 hours 3 minutes less screen time a day (about 3 hours by day, 1 hour at night).", ""]
llms += ["## Product pages"] + ["- [%s](%s)" % (t, SITE + h) for h, t in PRODUCT_LINKS] + [
 "- [Pricing](%s/pricing.html)" % SITE, "- [About SETL and its founder](%s/about.html)" % SITE, "- [Mission](%s/mission.html)" % SITE, "",
 "## Guides"] + ["- [%s](%s/blog/%s.html): %s" % (p["h1"], SITE, p["slug"], p["desc"]) for p in POSTS] + [""]
open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write("\n".join(llms))

# IndexNow: tell Bing (and the engines behind several AI assistants) the moment a page changes.
open(os.path.join(ROOT, "tools", "indexnow_urls.txt"), "w").write("\n".join([loc(p) for p, _, _ in urls]))

print("built %d pages:" % len(built), *built, sep="\n  ")
