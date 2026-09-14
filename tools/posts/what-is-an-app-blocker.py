POST = {
 "slug": "what-is-an-app-blocker",
 "title": "What Is an App Blocker? How They Work on iPhone | SETL",
 "h1": "What is an app blocker, and how does it work?",
 "desc": "An app blocker stops you opening chosen apps at set times. Here's how app blockers work on iPhone with Apple's Screen Time API and what to look for.",
 "tagline": "App blockers",
 "minutes": 6,
 "primary": "app blocker",
 "keywords": "app blocker, app blockers, how app blockers work, block apps on iPhone, screen blocker app, website blocker, SETL",
 "intro": "App blockers are everywhere, but few explain what happens behind the shield screen. Here's how they work on iPhone, the main types, and how to choose one.",
 "answer": "An app blocker is an app that stops you opening chosen apps or websites during schedules, sessions or limits you set. On iPhone, app blockers use Apple's Screen Time framework: Family Controls for permission, Managed Settings to apply the block, and Device Activity for timing. Apple gives them private tokens, so they never see your picks.",
 "body": """<p>If your thumb opens an app before your brain has decided to, an app blocker is built for exactly that moment. It puts a wall between you and the apps you lose time in. On iPhone, it does this through tools Apple built into iOS.</p>
<p>An app blocker is an app that stops you opening chosen apps or websites during times, sessions or limits you set in advance. You make the decision once, calmly, instead of again and again in the moment.</p>

<h2>What does an app blocker actually do?</h2>
<p>Every app blocker does three jobs. It asks for permission. It watches the clock or your usage. Then it covers the apps you picked when a rule kicks in.</p>
<p>That cover is called a shield. You tap a social app and, instead of your feed, you see a screen saying the app is blocked. Apple says shields appear when someone goes over a usage limit or tries to open an app during restricted hours, and developers can change how the shield looks.<sup><a href="#fn1">1</a></sup></p>

<h2>How do app blockers work on iPhone?</h2>
<p>On iPhone, one app can't simply reach into another app and switch it off. Instead, app blockers use Apple's Screen Time framework. Apple's documentation describes it as several frameworks working together to restrict, authorise and monitor device use.<sup><a href="#fn2">2</a></sup></p>
<ol>
<li><strong>Family Controls handles permission.</strong> It is how an app gets authorised to provide controls on a device.<sup><a href="#fn3">3</a></sup> Since iOS 16, you can authorise an app for yourself, not just for a child, and your iPhone confirms it with Face ID or Touch ID.<sup><a href="#fn4">4</a></sup></li>
<li><strong>Managed Settings applies the block.</strong> With your permission, an app can use it to restrict certain settings and features on your device in a way Apple calls privacy preserving.<sup><a href="#fn2">2</a></sup></li>
<li><strong>Device Activity handles timing.</strong> It lets an app monitor app and website activity on a schedule. The app can be warned when a schedule starts or ends, or when you are close to a usage threshold. Apple's own example is a bedtime schedule.<sup><a href="#fn5">5</a></sup></li>
</ol>
<p>The timing runs through a small app extension that the system calls when a schedule or threshold is reached.<sup><a href="#fn6">6</a></sup> So you set things up once, and iOS applies the block at the right moment.</p>

<h2>Why can't an app blocker see which apps you chose?</h2>
<p>This is the part most people never hear about. When you pick apps inside a blocker built on Screen Time, you are using a picker that Apple controls. Apple describes it as a way to choose apps, websites and categories without revealing those choices to the app.<sup><a href="#fn7">7</a></sup></p>
<p>What the app receives is a set of opaque values, usually called tokens.<sup><a href="#fn7">7</a></sup> A token stands in for "the app you picked" without saying which app it is. The blocker hands the tokens back to iOS, and iOS knows what to shield.</p>
<p>Apple also says that if you revoke an app's permission, the tokens it was given are voided.<sup><a href="#fn8">8</a></sup> Switching off access really does switch the blocker off.</p>

<h2>What types of app blockers are there?</h2>
<p>Most app blockers mix a few of these styles. Knowing them helps you match a tool to the way you actually slip.</p>
<ul>
<li><strong>Schedules.</strong> Apps lock at set times, such as bedtime or work hours. Useful when your problem shows up at the same time each day.</li>
<li><strong>Sessions.</strong> You start a block for a set length, like 50 minutes of study, and it ends by itself.</li>
<li><strong>Limits.</strong> You get a daily allowance for an app or category, and it locks when the time is used up. In iOS 27, Apple's built in version is called Time Allowances.<sup><a href="#fn9">9</a></sup></li>
<li><strong>Friction.</strong> Instead of a wall, you get a pause. one sec, for example, says it delays access to apps rather than blocking them completely, and shows a deep breath animation first.<sup><a href="#fn10">10</a></sup></li>
<li><strong>Hardware.</strong> Some blockers pair the app with a physical object. Brick says it creates physical separation, so ending a block needs a rescan of its small device.<sup><a href="#fn11">11</a></sup></li>
</ul>
<p>Many app blockers also work as a website blocker. Apple's picker lists web domains as well as apps and categories, so a blocker built on it can cover sites too.<sup><a href="#fn7">7</a></sup></p>

<h2>Is an app blocker different from Apple Screen Time?</h2>
<p>Apple Screen Time is built into your iPhone, and for some people it is enough. In the iOS 27 user guide, Apple describes Schedules for when you can use apps and Time Allowances for how long.<sup><a href="#fn9">9</a></sup></p>
<p>On iOS 26, the same ideas were called Downtime and App Limits. Apple's iOS 26 guide says that by default, Screen Time limits can be ignored once reached. To fully block apps during Downtime, you need a Screen Time passcode and the Block at Downtime setting.<sup><a href="#fn12">12</a></sup></p>
<p>A dedicated screen blocker app builds on the same Apple framework but adds its own design, such as sessions, stricter rules, friction or planned nights off. For more on this, read why <a href="/blog/screen-time-limits-not-working.html">Screen Time limits stop working</a>, or compare options on our <a href="/apple-screen-time-alternative.html">Apple Screen Time alternative</a> page.</p>

<h2>Who are app blockers for?</h2>
<p>You don't need a crisis to use one. App blockers tend to suit people who:</p>
<ul>
<li>lose the last hour before sleep to scrolling in bed</li>
<li>study or do deep work and keep drifting to their phone</li>
<li>have found that willpower runs out at the worst possible time</li>
<li>want a firm boundary for a season, like exams or a big project</li>
</ul>
<p>If nights are your weak spot, our guide on <a href="/blog/how-to-stop-scrolling-in-bed.html">how to stop scrolling in bed</a> is a good next read. An app blocker is a tool, not a treatment. It does not treat ADHD, insomnia or addiction.</p>

<h2>What should you look for when you block apps on iPhone?</h2>
<ol>
<li><strong>Apple's Screen Time framework.</strong> It is the official route on iPhone, and it is what gives you private tokens.</li>
<li><strong>Clear privacy.</strong> Check what the app says about where your usage data is kept.</li>
<li><strong>The right strictness.</strong> Too easy to skip and it won't hold. Too rigid and you will stop using it.</li>
<li><strong>Rules that fit real life.</strong> Look for a simple way to handle a wedding or a night shift without deleting all your settings.</li>
<li><strong>Honest pricing.</strong> Compare the yearly price, not only the weekly one, and check how to cancel.</li>
<li><strong>Your devices.</strong> Some blockers are iPhone only. Others also cover Android or Mac.</li>
</ol>
<p>If sleep is your main goal, we compare options in <a href="/blog/best-app-blocker-for-sleep.html">the best app blocker for sleep</a>.</p>

<h2>Where SETL fits</h2>
<p>SETL is an <a href="/app-blocker.html">iPhone app blocker built bedtime first</a>. You set your bedtime once and your chosen apps are blocked every night, with SETL Sessions for daytime focus. It runs on Apple's Screen Time framework, so SETL never learns which apps you picked. It is on a waitlist ahead of launch.</p>""",
 "sources": [
  ("Apple Developer Documentation, Managed Settings UI, 2026", "https://developer.apple.com/documentation/managedsettingsui"),
  ("Apple Developer Documentation, Managed Settings, 2026", "https://developer.apple.com/documentation/managedsettings"),
  ("Apple Developer Documentation, Family Controls, 2026", "https://developer.apple.com/documentation/familycontrols"),
  ("Apple Developer Documentation, AuthorizationCenter requestAuthorization(for:), 2026", "https://developer.apple.com/documentation/familycontrols/authorizationcenter/requestauthorization(for:)"),
  ("Apple Developer Documentation, Device Activity, 2026", "https://developer.apple.com/documentation/deviceactivity"),
  ("Apple Developer Documentation, DeviceActivityMonitor, 2026", "https://developer.apple.com/documentation/deviceactivity/deviceactivitymonitor"),
  ("Apple Developer Documentation, FamilyActivityPicker, 2026", "https://developer.apple.com/documentation/familycontrols/familyactivitypicker"),
  ("Apple Developer Documentation, FamilyActivitySelection, 2026", "https://developer.apple.com/documentation/familycontrols/familyactivityselection"),
  ("Apple Support, iPhone User Guide (iOS 27), Set Screen Time Schedules and Time Allowances, 2026", "https://support.apple.com/guide/iphone/set-schedules-with-screen-time-iphb0c7313c9/ios"),
  ("App Store, one sec | screen time + focus, checked September 2026", "https://apps.apple.com/us/app/one-sec-screen-time-focus/id1532875441"),
  ("Brick LLC, FAQs, checked September 2026", "https://getbrick.com/pages/faq"),
  ("Apple Support, iPhone User Guide (iOS 26), Set schedules with Screen Time on iPhone, 2025", "https://support.apple.com/guide/iphone/set-schedules-with-screen-time-iphb0c7313c9/26.0/ios/26.0"),
 ],
 "faq": [
  ("Do app blockers work on iPhone?", "Yes. On iPhone, app blockers use Apple's Screen Time framework. Once you give permission, an app can shield the apps and websites you choose on a schedule, during a session or after a daily limit."),
  ("Can an app blocker see which apps I use?", "Not when it uses Apple's picker. Apple gives the app opaque tokens for the apps you choose, so it can block them without learning which apps they are."),
  ("Is an app blocker the same as Screen Time?", "Not quite. Screen Time is Apple's built in tool. A dedicated app blocker uses the same Apple framework but adds its own rules, such as sessions, stricter blocks, friction or planned nights off."),
  ("Can an app blocker block websites too?", "Many can. Apple's picker lets you choose web domains as well as apps and categories, so a blocker built on Apple's framework can cover sites alongside apps."),
  ("Does an app blocker lock my whole phone?", "No. It blocks only the apps, categories or websites you choose. Everything you leave off the list keeps working as normal."),
  ("Is an app blocker a treatment for phone addiction?", "No. An app blocker is a tool that makes a habit easier to change. It does not treat ADHD, insomnia or addiction. If your phone use worries you, speak to your doctor."),
 ],
 "related": ["best-screen-time-apps-for-iphone", "screen-time-limits-not-working", "best-app-blocker-for-sleep"],
}
