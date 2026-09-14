#!/usr/bin/env python3
"""Generate SETL's content pages: about, mission, pricing, compare, blog hub + 4 posts, 404.

Run from anywhere:  python3 tools/build_pages.py
Edit copy, prices or sources here, then rerun; never hand-edit the generated HTML.
One template so nav, footer, meta and structured data can never drift between pages."""
import json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # repo root; this file lives in tools/
SITE = "https://www.setlsleep.com"
PUBLISHED = "2026-09-14"
AUTHOR = "Jacob Redshaw"

ORG = {"@type": "Organization", "@id": SITE + "/#org", "name": "SETL", "url": SITE + "/",
       "logo": SITE + "/assets/icon-512.png",
       "sameAs": []}

# ---------- verified sources (checked 2026-09-14) ----------
SRC = {
 "ofcom": ("Ofcom, Online Nation 2025 (published 10 December 2025)",
           "https://www.ofcom.org.uk/media-use-and-attitudes/online-habits/from-apps-to-ai-search-how-the-uk-goes-online-in-2025"),
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
 "lally": ("Lally et al., European Journal of Social Psychology, 2010",
           "https://onlinelibrary.wiley.com/doi/abs/10.1002/ejsp.674"),
 "sunbreak": ("Sunbreak on the UK App Store", "https://apps.apple.com/gb/app/sunbreak-nightly-app-blocker/id6752121964"),
}
def src(key, text=None):
    t, u = SRC[key]
    return '<a href="%s" rel="noopener" target="_blank">%s</a>' % (u, html.escape(text or t))

NAV_LINKS = [("/blog/", "Blog"), ("/pricing.html", "Pricing"), ("/about.html", "About"), ("/mission.html", "Mission")]

def nav(current):
    links = "".join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if h == current else "", t) for h, t in NAV_LINKS)
    menu = "".join('<a href="%s">%s</a>' % (h, t) for h, t in NAV_LINKS + [("/setl-vs-opal.html", "SETL vs Opal"), ("/", "Join the waitlist")])
    return ('<header class="nav" role="banner">'
            '<a class="brand" href="/" aria-label="SETL home"><img class="ic" src="/assets/nav-ic.png" alt="" width="23" height="25">'
            '<img class="wm" src="/assets/nav-wm.png" alt="SETL" width="56" height="11"></a>'
            '<nav class="links" aria-label="Primary">%s<a class="try" href="/">Join waitlist</a></nav>'
            '<details><summary>Menu</summary><nav class="menu" aria-label="Menu">%s</nav></details>'
            '</header>') % (links, menu)

FOOT = ('<footer class="foot"><div class="wrap">'
        '<img class="ic" src="/assets/nav-ic.png" alt="" width="46" height="50">'
        '<p class="brandline">SETL</p><p class="tag">The sleep app blocker, built night first.</p>'
        '<nav aria-label="Footer">'
        '<a href="/">Home</a><a href="/blog/">Blog</a><a href="/pricing.html">Pricing</a>'
        '<a href="/about.html">About</a><a href="/mission.html">Mission</a>'
        '<a href="/setl-vs-opal.html">SETL vs Opal</a><a href="/privacy.html">Privacy</a>'
        '</nav>'
        '<p class="meta">&copy; <span data-year>2026</span> SETL. Built in the UK.</p>'
        '</div></footer>')

def crumbs_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}

def page(path, title, desc, body, current="", ld=None, body_class="", og_type="website", extra_head=""):
    url = SITE + ("/" + path if not path.endswith("index.html") else "/" + path[:-len("index.html")])
    url = url.replace("//index", "/")
    graph = [ORG] + (ld or [])
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
<link rel="stylesheet" href="/assets/site.css?v=1">
{extra_head}<script type="application/ld+json">{ld}</script>
</head>
<body{bc}>
<a class="skip" href="#main">Skip to content</a>
{nav}
<main id="main">
{body}
</main>
{foot}
<script src="/assets/site.js?v=1" defer></script>
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
<p class="lead rv d1">Join the SETL waitlist. Your first night is free when we launch.</p>
<div class="btn-row rv d2"><a class="btn" href="/">Join the waitlist</a><a class="btn ghost" href="/pricing.html">See pricing</a></div>
</div></section>"""

built = []

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
<p>Before SETL, I was a copywriter. I wrote for brands including JD Sports and Manchester United.</p>
<p>My job was attention. Find the line that stops a thumb mid scroll, then keep it there.</p>
<p>I was good at it. Which meant I understood exactly what was happening to me every night.</p>
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
""", "Our goal is a billion bedtimes kept. We are starting with yours.",
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

about_body = """<section class="story-hero"><div class="narrow">
<img class="moon" src="/assets/disc-classic.webp" alt="" width="190" height="190">
<span class="eyebrow rv"><i></i>Our story</span>
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

built.append(page("about.html",
  "About SETL | The Founder Story Behind the Sleep App Blocker",
  "Why SETL exists: an ADHD founder and former copywriter who could not stop scrolling at night, and the science that made him build a sleep app blocker.",
  about_body, "/about.html", body_class="story",
  ld=[{"@type": "AboutPage", "name": "About SETL", "url": SITE + "/about.html",
       "about": {"@id": SITE + "/#org"},
       "mainEntity": {"@type": "Person", "name": AUTHOR, "jobTitle": "Founder", "worksFor": {"@id": SITE + "/#org"}}},
      crumbs_ld([("Home", "/"), ("About", "/about.html")])]))

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
mission_body = """<section class="goal"><div class="narrow">
<span class="eyebrow rv"><i></i>Our mission</span>
<p class="big rv d1" style="margin-top:34px" data-countto="1000000000" aria-label="One billion">1,000,000,000</p>
<p class="label rv d2">Bedtimes kept. That is the goal.</p>
<h1 class="rv d2" style="margin-top:34px;font-size:var(--t-xl)">Give the world its evenings back.</h1>
<p class="lead rv d3">One night where the phone goes to sleep first, a billion times over.</p>
</div></section>
<section class="sec"><div class="wrap">
<div class="sec-head center"><h2 class="rv">Why it matters</h2>
<p class="lead rv d1">These are not our numbers. They are the world's, and every one is sourced.</p></div>
<div class="grid g4">%s</div>
</div></section>
<section class="sec"><div class="wrap">
<div class="sec-head"><h2 class="rv">What we strive for</h2>
<p class="lead rv d1">Six promises that decide what SETL is, and what it will never become.</p></div>
<div class="principles">%s</div>
</div></section>
<section class="sec"><div class="narrow center">
<h2 class="rv">Focus is not a personality trait.</h2>
<p class="lead rv d1">It is what is left when nothing is pulling at you. SETL removes the pull.</p>
<div class="btn-row rv d2"><a class="btn" href="/about.html">Read the founder story</a><a class="btn ghost" href="/blog/">Read the research</a></div>
</div></section>
%s""" % (stat_html, pr_html, CTA)
built.append(page("mission.html",
  "Our Mission | SETL, A Billion Bedtimes Kept",
  "SETL's mission is a billion bedtimes kept: less screen time at night, better sleep and real focus by day. Here is what we stand for.",
  mission_body, "/mission.html",
  ld=[{"@type": "WebPage", "name": "Our mission", "url": SITE + "/mission.html", "about": {"@id": SITE + "/#org"}},
      crumbs_ld([("Home", "/"), ("Mission", "/mission.html")])]))

# =====================================================================
# PRICING
# =====================================================================
included = ["Night blocking at your bedtime", "SETL Sessions for daytime focus", "SETL Plans for nights off",
            "Sleep Reserve Lock Screen widget", "Post bedtime nudges", "The full moon collection"]
inc = "".join("<li>%s</li>" % x for x in included)
faqs = [
 ("How does the free night work?", "Start SETL tonight for free. Cancel before tomorrow evening and you pay nothing."),
 ("Is SETL cheaper than Opal?", "Yes. SETL is $39.99 a year. Opal Pro is $99.99 a year, so SETL costs 60% less."),
 ("Can I cancel anytime?", "Yes. Subscriptions are handled by Apple, so you cancel in your iPhone settings in a few taps."),
 ("What does SETL actually block?", "The apps you choose, at the times you choose. Everything else on your phone works normally."),
 ("Does SETL work on Android or Mac?", "Not yet. SETL is iPhone only for now, built on Apple's Screen Time framework."),
 ("Can SETL see my apps or messages?", "No. Apple gives SETL private tokens, so we never learn which apps you picked."),
]
faq_html = "".join('<details class="rv"><summary>%s</summary><p>%s</p></details>' % (q, a) for q, a in faqs)
pricing_body = """<section class="hero center"><div class="narrow">
<span class="eyebrow rv"><i></i>Pricing</span>
<h1 class="rv d1">Simple pricing. First night free.</h1>
<p class="lead rv d2">Every plan unlocks everything. Cancel before tomorrow evening and you pay nothing.</p>
</div></section>
<section style="padding-bottom:clamp(64px,11vw,110px)"><div class="wrap">
<div class="plans">
<article class="plan rv"><h3>Weekly</h3><p class="price">$2.99<small>/week</small></p><p class="per">Try it week by week.</p><ul>%s</ul><a class="btn ghost" href="/">Join the waitlist</a></article>
<article class="plan best rv d1"><span class="badge">BEST VALUE</span><h3>Annual</h3><p class="price">$3.33<small>/month</small></p><p class="per">Billed $39.99 a year. Save 44%% on monthly.</p><ul>%s</ul><a class="btn" href="/">Join the waitlist</a></article>
<article class="plan rv d2"><h3>Monthly</h3><p class="price">$5.99<small>/month</small></p><p class="per">Steady and simple. Cancel anytime.</p><ul>%s</ul><a class="btn ghost" href="/">Join the waitlist</a></article>
</div>
<p class="fn center" style="margin-top:22px">Launch prices in US dollars, charged by Apple. Local App Store prices may differ.</p>
</div></section>
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
<section class="sec"><div class="narrow">
<div class="sec-head"><h2 class="rv">Questions</h2></div>
<div class="faq">%s</div>
</div></section>
%s""" % (inc, inc, inc, src("opal", "Opal's pricing page"), faq_html, CTA)
built.append(page("pricing.html",
  "SETL Pricing | App Blocker from $3.33 a Month",
  "SETL pricing: $39.99 a year ($3.33 a month), $5.99 a month or $2.99 a week, first night free. A screen time app blocker for 60% less than Opal.",
  pricing_body, "/pricing.html",
  ld=[{"@type": "SoftwareApplication", "name": "SETL", "operatingSystem": "iOS",
       "applicationCategory": "LifestyleApplication", "url": SITE + "/pricing.html",
       "offers": [
         {"@type": "Offer", "name": "Annual", "price": "39.99", "priceCurrency": "USD"},
         {"@type": "Offer", "name": "Monthly", "price": "5.99", "priceCurrency": "USD"},
         {"@type": "Offer", "name": "Weekly", "price": "2.99", "priceCurrency": "USD"}],
       "publisher": {"@id": SITE + "/#org"}},
      {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q,
        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
      crumbs_ld([("Home", "/"), ("Pricing", "/pricing.html")])]))

# =====================================================================
# SETL vs OPAL
# =====================================================================
rows = [
 ("Built around", "Bedtime first, then your day", "Daytime focus, with a Sleep Mode"),
 ("Price per year", "$39.99", "$99.99 (Pro)"),
 ("Price per month", "$5.99", "$19.99 (Pro)"),
 ("Lifetime plan", '<span class="no">No</span>', "$399"),
 ("Free option", "First night free", "Free plan with 1 rule, plus free trials"),
 ("Automatic night blocking", '<span class="yes">Yes</span>', '<span class="yes">Yes</span>, Sleep Mode'),
 ("Daytime focus sessions", '<span class="yes">Yes</span>, SETL Sessions', '<span class="yes">Yes</span>'),
 ("Plan nights off in advance", '<span class="yes">Yes</span>, SETL Plans', "Schedules"),
 ("Hours left until morning", '<span class="yes">Yes</span>, Sleep Reserve widget', "Not a core feature"),
 ("iPhone", '<span class="yes">Yes</span>', '<span class="yes">Yes</span>'),
 ("Android and Mac", '<span class="no">Not yet</span>', '<span class="yes">Yes</span>'),
]
tbl = "".join('<tr><th scope="row">%s</th><td class="us">%s</td><td>%s</td></tr>' % r for r in rows)
vs_body = """<section class="hero center"><div class="narrow">
<span class="eyebrow rv"><i></i>Opal alternative</span>
<h1 class="rv d1">SETL vs Opal</h1>
<p class="lead rv d2">Opal is built for your workday. SETL is built for your bedtime, at less than half the price.</p>
</div></section>
<section style="padding-bottom:clamp(64px,11vw,110px)"><div class="wrap">
<div class="tablewrap rv"><table class="cmp">
<caption class="fn" style="caption-side:bottom;text-align:left;padding:14px 20px">Opal details from %s, checked September 2026. SETL prices are launch prices.</caption>
<thead><tr><th scope="col"></th><th scope="col">SETL</th><th scope="col">Opal</th></tr></thead>
<tbody>%s</tbody></table></div>
</div></section>
<section class="sec"><div class="wrap">
<div class="grid g2">
<div class="card rv"><span class="n">CHOOSE SETL IF</span><h3>Your problem starts at bedtime.</h3>
<p>You lose evenings to your phone, want it locked at night, and want to pay $39.99 a year.</p></div>
<div class="card rv d1"><span class="n">CHOOSE OPAL IF</span><h3>You need Mac or Android.</h3>
<p>You want one blocker across a laptop and phone, a free plan, or a one off lifetime licence.</p></div>
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
<div class="sources"><h2>Sources</h2><ol><li id="s1">%s</li><li id="s2">%s</li><li>%s</li></ol></div>
</div></section>
%s""" % (src("opal", "Opal's pricing page"), tbl, src("norway"), src("aasm"), src("opal"), CTA)
built.append(page("setl-vs-opal.html",
  "SETL vs Opal (2026) | The Opal Alternative Built for Bedtime",
  "SETL vs Opal compared: price, night blocking, daytime sessions and devices. An honest look at the cheaper Opal alternative for sleep.",
  vs_body, "",
  ld=[{"@type": "WebPage", "name": "SETL vs Opal", "url": SITE + "/setl-vs-opal.html"},
      crumbs_ld([("Home", "/"), ("SETL vs Opal", "/setl-vs-opal.html")])]))

# =====================================================================
# BLOG POSTS
# =====================================================================
POSTS = []

def post(slug, title, h1, desc, tagline, minutes, intro, body, sources, related, keywords):
    POSTS.append((slug, h1, desc, tagline, minutes))
    url = "/blog/%s.html" % slug
    rel = "".join('<a class="post-card" href="/blog/%s.html"><span class="tagline">%s</span><h3>%s</h3><p>%s</p></a>' %
                  (s, t, h, d) for s, h, d, t in related)
    src_list = "".join("<li>%s</li>" % src(k) for k in sources)
    b = """<article><header class="article-head"><div class="narrow">
<p class="crumbs"><a href="/">Home</a> / <a href="/blog/">Blog</a></p>
<span class="eyebrow"><i></i>%s</span>
<h1 style="margin-top:20px;font-size:clamp(34px,6.4vw,54px)">%s</h1>
<p class="lead" style="margin-top:18px">%s</p>
<p class="meta">By %s &middot; <time datetime="%s">14 September 2026</time> &middot; %d min read</p>
</div></header>
<div class="narrow"><div class="prose">%s</div>
<div class="sources"><h2>Sources</h2><ol>%s</ol></div>
<div class="related"><h2>Keep reading</h2><div class="posts">%s</div></div>
</div></article>
%s""" % (tagline, html.escape(h1), html.escape(intro), AUTHOR, PUBLISHED, minutes, body.strip(), src_list, rel, CTA)
    built.append(page("blog/%s.html" % slug, title, desc, b, "/blog/", og_type="article",
        ld=[{"@type": "BlogPosting", "headline": h1, "description": desc, "url": SITE + url,
             "datePublished": PUBLISHED, "dateModified": PUBLISHED, "inLanguage": "en-GB",
             "keywords": keywords, "image": SITE + "/assets/og.jpg",
             "author": {"@type": "Person", "name": AUTHOR, "url": SITE + "/about.html"},
             "publisher": {"@id": SITE + "/#org"}, "mainEntityOfPage": SITE + url},
            crumbs_ld([("Home", "/"), ("Blog", "/blog/"), (h1, url)])]))

R = {
 "scroll": ("how-to-stop-scrolling-in-bed", "How to stop scrolling in bed", "Seven fixes for screen time at night that do not depend on willpower.", "Sleep"),
 "blocker": ("best-app-blocker-for-sleep", "The best app blocker for sleep in 2026", "What a screen blocker app should do at night, and how the options compare.", "App blockers"),
 "focus": ("does-it-take-23-minutes-to-refocus", "Does it take 23 minutes to refocus?", "Where the famous distraction figure really comes from.", "Focus"),
 "science": ("screens-melatonin-and-sleep", "Screens, melatonin and sleep", "What your phone does to your body clock after dark.", "Science"),
}
def rl(*keys): return [R[k] for k in keys]

post("how-to-stop-scrolling-in-bed",
 "How to Stop Scrolling in Bed: 7 Fixes | SETL",
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
<p>An app blocker that switches on automatically at bedtime removes the nightly argument. Apple's free Downtime is a start, though it can be dismissed in a tap.</p>
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
<p>SETL (say it like settle) was built for exactly this. Set your bedtime once, and SETL puts your distracting apps to sleep before you do. <a href="/pricing.html">Your first night is free</a>.</p>
""",
 ["aasm", "norway"], rl("blocker", "science", "focus"),
 "stop scrolling in bed, screen time at night, doomscrolling, bedtime app blocker, SETL")

post("best-app-blocker-for-sleep",
 "Best App Blocker for Sleep in 2026 | SETL",
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
<h3>Apple Downtime</h3>
<p>Free and already on your iPhone. It schedules limits well, but "Ignore Limit" is one tap away, which makes it weak at midnight.</p>
<h3>Opal</h3>
<p>A polished focus app for iPhone, Android and Mac, with a Sleep Mode. Opal Pro costs $99.99 a year, and there is a free plan with one rule.<sup><a href="#fn3">3</a></sup></p>
<h3>Sunbreak</h3>
<p>A nightly app blocker that locks apps at bedtime and can alert an accountability partner if you break your pact.<sup><a href="#fn4">4</a></sup></p>
<h3>SETL</h3>
<p>Built bedtime first. SETL blocks your chosen apps at the time you set, plans nights off with SETL Plans, and brings the same block into your day with SETL Sessions. <strong>$39.99 a year</strong>, first night free.</p>
<p>See the full <a href="/setl-vs-opal.html">SETL vs Opal comparison</a>.</p>

<div class="callout"><strong>The honest answer:</strong> the best app blocker is the one you cannot talk yourself out of at 1am. Test that first, then compare features.</div>
""",
 ["aasm", "norway", "opal", "sunbreak"], rl("scroll", "focus", "science"),
 "app blocker, screen blocker app, best app blocker for sleep, screen time app, Opal alternative, SETL")

post("does-it-take-23-minutes-to-refocus",
 "Does It Take 23 Minutes to Refocus? | SETL",
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
 "focus, distraction, 23 minutes to refocus, attention span, deep work, SETL")

post("screens-melatonin-and-sleep",
 "Screens, Melatonin and Sleep | SETL",
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
 "screen time sleep, phone before bed, melatonin, blue light, digital eye strain, SETL")

# ---- fix per-post footnote anchors: sources list items get ids fn1..n in order ----
for slug, *_ in POSTS:
    p = os.path.join(ROOT, "blog", slug + ".html")
    s = open(p, encoding="utf-8").read()
    i = s.find('<div class="sources"><h2>Sources</h2><ol>')
    head, tail = s[:i], s[i:]
    n = [0]
    def num(m):
        n[0] += 1
        return '<li id="fn%d">' % n[0]
    import re
    tail = re.sub(r"<li>", num, tail, count=tail.count("<li>") - tail[tail.find('<div class="related">'):].count("<li>"))
    open(p, "w", encoding="utf-8").write(head + tail)

# =====================================================================
# BLOG HUB
# =====================================================================
cards = "".join('<a class="post-card rv%s" href="/blog/%s.html"><span class="tagline">%s</span><h3>%s</h3><p>%s</p><span class="meta">%d min read</span></a>' %
                ("" if i % 2 == 0 else " d1", slug, tag, html.escape(h1), html.escape(desc.split(".")[0] + "."), mins)
                for i, (slug, h1, desc, tag, mins) in enumerate(POSTS))
hub = """<section class="hero center"><div class="narrow">
<span class="eyebrow rv"><i></i>The SETL blog</span>
<h1 class="rv d1">Sleep, screen time and focus.</h1>
<p class="lead rv d2">Short, sourced reads on why we scroll, what it costs, and how to stop.</p>
</div></section>
<section style="padding-bottom:clamp(64px,11vw,110px)"><div class="wrap"><div class="posts">%s</div></div></section>
%s""" % (cards, CTA)
built.append(page("blog/index.html",
  "SETL Blog | Sleep, Screen Time and Focus",
  "The SETL blog: sourced articles on screen time at night, app blockers, sleep science and focus. Learn how to stop scrolling and sleep better.",
  hub, "/blog/",
  ld=[{"@type": "Blog", "name": "SETL Blog", "url": SITE + "/blog/", "publisher": {"@id": SITE + "/#org"},
       "blogPost": [{"@type": "BlogPosting", "headline": h1, "url": SITE + "/blog/%s.html" % slug} for slug, h1, *_ in POSTS]},
      crumbs_ld([("Home", "/"), ("Blog", "/blog/")])]))

# =====================================================================
# 404
# =====================================================================
nf = """<section class="hero center" style="min-height:80vh"><div class="narrow">
<img src="/assets/disc-twilight.webp" alt="" width="150" height="150" style="width:150px;margin:0 auto 30px;opacity:.9">
<h1>This page has gone to sleep.</h1>
<p class="lead" style="margin:18px auto 0">It is not here, but plenty else is.</p>
<div class="btn-row"><a class="btn" href="/">Back to SETL</a><a class="btn ghost" href="/blog/">Read the blog</a></div>
</div></section>"""
p404 = page("404.html", "Page not found | SETL", "This page could not be found.", nf, "")
s = open(os.path.join(ROOT, "404.html"), encoding="utf-8").read()
s = s.replace('<meta name="robots" content="index,follow,max-image-preview:large">', '<meta name="robots" content="noindex">')
open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8").write(s)

print("built:", *built, "404.html", sep="\n  ")
