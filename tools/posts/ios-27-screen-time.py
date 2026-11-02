POST = {
 "slug": "ios-27-screen-time",
 "title": "iOS 27 Screen Time: Everything That Changed | SETL",
 "h1": "iOS 27 Screen Time: everything that changed",
 "desc": "iOS 27 Screen Time renamed Downtime and App Limits, added category allowances and separate weekday schedules. Here is what changed and where to find it.",
 "tagline": "Screen Time",
 "minutes": 6,
 "primary": "ios 27 screen time",
 "keywords": "ios 27 screen time, screen time schedule, time allowances, downtime renamed, app limits renamed, ios 27 parental controls",
 "intro": "Apple rebuilt Screen Time in iOS 27 and renamed the two settings everybody used. If you cannot find Downtime, this is why.",
 "answer": "iOS 27 Screen Time replaced Downtime with Screen Time Schedule and replaced App Limits with Time Allowances. Allowances are now a single daily budget across categories that you can fine tune per category, and schedules can run different routines on weekdays and weekends.",
 "body": """
<p>If you have updated and gone looking for Downtime, stop looking. <strong>iOS 27 Screen Time</strong> renamed it. Apple rebuilt this part of Settings, and the two features almost everybody relied on now have different names and work slightly differently.</p>

<p>Nothing was taken away. But every guide written before autumn 2026, including most of the ones still at the top of Google, tells you to tap things that are no longer there.</p>

<h2>The two renames, in one line each</h2>

<div class="tablewrap"><table class="cmp"><thead><tr><th>Used to be called</th><th>Now called</th></tr></thead><tbody>
<tr><td>Downtime</td><td><strong>Screen Time Schedule</strong></td></tr>
<tr><td>App Limits</td><td><strong>Time Allowances</strong></td></tr>
</tbody></table></div>

<p>Apple's own support guide now tells you to tap Screen Time, then tap Screen Time Schedule or Time Allowances.<sup><a href="#fn1">1</a></sup> Same place in Settings, different words on the buttons.</p>

<p>One thing worth knowing before you start: Apple says you need iOS 27, iPadOS 27, macOS 27, watchOS 27, visionOS 27 or later to use all the latest Screen Time features.<sup><a href="#fn1">1</a></sup> If you are on a mixed set of devices, the older ones will not show everything.</p>

<h2>What actually changed in iOS 27 Screen Time, not just the names</h2>

<h3>Time Allowances are now one budget, not many limits</h3>

<p>The old App Limits made you set a separate limit per app or per category. Thirty minutes of social, an hour of entertainment, and so on. It worked, but it meant a lot of fiddling, and most people set three limits and never touched it again.</p>

<p>Time Allowances inverts it. You set <strong>a daily time budget that spans all categories</strong>, then fine tune by adjusting the time allotted to any individual category.<sup><a href="#fn2">2</a></sup></p>

<p>That is a better default. One number is easier to think about than nine, and a single budget stops the thing where you are under every individual limit but have still spent five hours on the phone.</p>

<h3>Schedules can now be different on weekdays and weekends</h3>

<p>The old Downtime let you set one window, or set custom days with a lot of tapping. Screen Time Schedules now let you choose which apps are accessible at different times of day, with separate routines for weekdays and weekends.<sup><a href="#fn2">2</a></sup></p>

<p>This is the change most worth using. A single bedtime that applies seven nights a week is wrong twice: too early on Friday and Saturday, too late to be useful if you set it for the weekend. Two routines fixes it.</p>

<h3>Schedules can allow categories rather than just block everything</h3>

<p>Old Downtime was close to all or nothing: most apps became unavailable unless you had put them in Always Allowed. The newer schedules are built around choosing which apps are accessible in a given window, so you can have a school window, a homework window and an evening window that each let different things through.</p>

<h2>How to set up Screen Time Schedule in iOS 27</h2>

<ol>
<li>Open <strong>Settings</strong>.</li>
<li>Tap <strong>Screen Time</strong>.</li>
<li>Tap <strong>Screen Time Schedule</strong>.</li>
<li>Turn it on and set the start and end times.</li>
<li>Set a different routine for weekends if you want one.</li>
<li>Go back and check <strong>Always Allowed</strong>, because anything in there ignores your schedule completely. Most people leave more in there than they realise.</li>
</ol>

<h2>How to set up Time Allowances</h2>

<ol>
<li><strong>Settings</strong>, then <strong>Screen Time</strong>, then <strong>Time Allowances</strong>.</li>
<li>Set your overall daily budget first. Be honest. If you are on five hours, setting it to one hour means you blow through it by lunchtime and start ignoring it.</li>
<li>Then adjust individual categories if one is doing most of the damage.</li>
<li>Set a Screen Time passcode, and make it one you do not know by heart.</li>
</ol>

<h2>The part that did not change</h2>

<p>When a Time Allowance runs out, you can still tap your way past it. The button has moved around over the years but the behaviour is the same: the limit tells you that you are over, and then lets you continue.</p>

<p>That is a deliberate design choice by Apple and it is the right one for a feature that ships to everybody. But it is also why a lot of people set limits, ignore them for a month, and conclude that Screen Time does not work.</p>

<p>It is worth being careful about how strongly anyone states this, including me. The one published study I can find that tested Apple's Downtime and App Limits directly reported no significant reduction in screen time, but only 17 people finished it, so treat it as a pilot and not a verdict.<sup><a href="#fn3">3</a></sup></p>

<p>What is better established is that reducing phone use genuinely helps. A 2025 randomised controlled trial in BMC Medicine had 58 students hold under two hours a day for three weeks and found improvements in stress, wellbeing, depressive symptoms and sleep quality against a control group. Usage then climbed back towards baseline once the limit stopped.<sup><a href="#fn4">4</a></sup></p>

<p>Which is the real lesson. The benefit is real, and it lasts about as long as the friction does.</p>

<h2>Where SETL fits</h2>

<p>Set up Screen Time Schedule properly first. It is free, it is already on your phone, and for a lot of people it is enough. If you have done that and still find yourself tapping past it, the gap is enforcement rather than features, which is what an <a href="/apple-screen-time-alternative.html">Apple Screen Time alternative</a> is actually for. SETL is built on the same Apple framework, blocks automatically at your bedtime, and makes ending a block early a deliberate hold rather than a tap. If you want the longer comparison, read <a href="/blog/screen-time-limits-not-working.html">why screen time limits stop working</a> or see the <a href="/screen-time-blocker.html">screen time blocker</a> page.</p>
""",
 "sources": [
   ("Apple Support, Set schedules with Screen Time on iPhone", "https://support.apple.com/guide/iphone/set-schedules-with-screen-time-iphb0c7313c9/26/ios/26"),
   ("Apple Support, Use Screen Time to manage your child's iPhone or iPad", "https://support.apple.com/en-us/108806"),
   ("Vu TH and Tagliabue M, Active nudging towards digital well-being, Frontiers in Psychiatry, 2025", "https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2025.1602997/full"),
   ("Pieh C et al., Smartphone screen time reduction improves mental health, BMC Medicine, 2025", "https://pubmed.ncbi.nlm.nih.gov/39985031/"),
 ],
 "faq": [
  ("What happened to Downtime in iOS 27?",
   "Apple renamed it. Downtime is now called Screen Time Schedule. You find it in the same place, Settings then Screen Time, and it does the same job with more control over which apps are allowed in each window."),
  ("What are Time Allowances on iPhone?",
   "Time Allowances replaced App Limits in iOS 27. Instead of a separate limit per app, you set one daily budget that spans all categories, then adjust individual categories if you want to."),
  ("Do I need iOS 27 for the new Screen Time features?",
   "Yes. Apple says all the latest Screen Time features need iOS 27, iPadOS 27, macOS 27, watchOS 27 or visionOS 27 and later. Older devices in your family will not show everything."),
  ("Can you still ignore a Screen Time limit in iOS 27?",
   "Yes. When an allowance runs out you can still choose to carry on. That is why people who have already drifted past Apple's limits often look for something with stricter enforcement."),
  ("Can Screen Time Schedule be different at the weekend?",
   "Yes, and this is the best new feature. Schedules support separate routines for weekdays and weekends, so you do not have to pick one bedtime that is wrong on Friday and wrong on Monday."),
  ("Why can I not find App Limits any more?",
   "Because it is now called Time Allowances. Nothing was removed. Guides written before autumn 2026 still use the old name, which is why the instructions do not match your phone."),
 ],
 "related": ["how-to-use-downtime-on-iphone", "screen-time-limits-not-working", "how-to-reduce-screen-time-on-iphone"],
}
