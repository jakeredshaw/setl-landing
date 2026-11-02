POST = {
 "slug": "screen-time-not-working",
 "title": "Screen Time Not Working? Seven Fixes in Order | SETL",
 "h1": "Screen Time not working: seven things to check",
 "desc": "Screen Time not working on your iPhone? Seven causes in order of likelihood, starting with the one that accounts for most of it, and when to stop fixing.",
 "tagline": "Screen Time",
 "minutes": 6,
 "primary": "screen time not working",
 "keywords": "screen time not working, screen time not blocking apps, screen time schedule not working, downtime not working iphone, screen time broken",
 "intro": "Seven causes, ordered by how often they turn out to be the answer. The first one explains most cases and takes two minutes.",
 "answer": "Screen Time not working is usually caused by apps in your Always Allowed list, which ignore blocks entirely. Other common causes are knowing the passcode by heart, using the website version of a blocked app, setting an allowance instead of a schedule, and iOS 27 renaming the settings.",
 "body": """
<p><strong>Screen Time not working</strong> is rarely a bug. In nearly every case it is one of a handful of settings doing exactly what they are designed to do, in a way nobody told you about.</p>

<p>Work down this list in order. The first item accounts for most cases.</p>

<h2>1. Always Allowed is overriding everything</h2>

<p>This is the answer most of the time.</p>

<p>Go to <strong>Settings</strong>, then <strong>Screen Time</strong>, then <strong>Always Allowed</strong>. Anything on that list ignores your blocks completely. Not limited, not delayed. Exempt.</p>

<p>Strip it down to Phone and Messages. Remove any browser especially, because an allowed browser is a route to every site you just blocked.</p>

<p>More detail in <a href="/blog/always-allowed-screen-time.html">the Always Allowed explainer</a>.</p>

<h2>2. You know the passcode</h2>

<p>If you can type your Screen Time passcode without thinking about it, nothing is really blocked. You have a prompt that costs four seconds.</p>

<p>Generate a random passcode, write it on paper, and put the paper somewhere that costs you a walk. Or have someone else set it and not tell you. This single step converts the entire feature from advisory to real.</p>

<h2>3. You are looking for a setting that was renamed</h2>

<p>In iOS 27, Downtime became <strong>Screen Time Schedule</strong> and App Limits became <strong>Time Allowances</strong>. Apple's guide now says to tap Screen Time, then tap Screen Time Schedule or Time Allowances.<sup><a href="#fn1">1</a></sup></p>

<p>Nothing was removed. But most guides online still use the old names, so you can spend twenty minutes convinced a feature has been deleted when it has only been relabelled.</p>

<p>Apple also says all the latest Screen Time features need iOS 27 or later across your devices.<sup><a href="#fn1">1</a></sup> If one device in a family is older, it will not show everything.</p>

<h2>4. You set an allowance when you wanted a schedule</h2>

<p>These do different jobs and people frequently set the wrong one.</p>

<p>A <strong>Time Allowance</strong> is a daily budget. When it runs out you are told, and then you may continue. By design.</p>

<p>A <strong>Screen Time Schedule</strong> makes apps unavailable during hours you choose in advance.</p>

<p>If your complaint is that the block does not stop you, you probably have an allowance and want a schedule. See <a href="/blog/time-allowances-vs-screen-time-schedule.html">which to use</a>.</p>

<h2>5. You are using the website, not the app</h2>

<p>Blocking an app has no effect on the same service in Safari, and the reverse is also true. They are separate systems.</p>

<p>This one is easy to miss because it does not feel like cheating. You blocked the app, you kept your word, and you spent an hour on the site anyway. Fix it with Web Content restrictions, covered in <a href="/blog/how-to-block-websites-on-iphone.html">how to block websites on iPhone</a>.</p>

<h2>6. The block starts too late</h2>

<p>Not a malfunction, a design error. If your schedule starts at the moment you want to be asleep, it arrives after the decision has already been made and lost.</p>

<p>Start it 30 minutes earlier. Once you are lying down holding the phone, no setting is going to rescue the situation.</p>

<h2>7. It genuinely is a glitch</h2>

<p>Occasionally it is. Signs: the schedule shows as on but nothing happens at all, or limits reset themselves, or settings do not sync between your devices.</p>

<p>Standard things to try, in order: restart the phone, check for an iOS update, turn Screen Time off and back on, and if you use Family Sharing, check whether the settings are being managed from another device. If it still fails after that, it is worth contacting Apple Support rather than continuing to guess.</p>

<p>One thing to rule out before blaming the software: whether the apps you think you selected are the apps you actually selected. Picking apps by category rather than individually is quick, and it also means a service you care about may sit in a category you did not tick. Open your schedule, look at the specific list, and confirm the thing you keep opening at midnight is genuinely in it. A surprising share of apparent glitches are a block that is working perfectly on apps you never use.</p>

<h2>When Screen Time not working is not the real problem</h2>

<p>Here is the honest part. If you have worked through all seven and the block technically functions but you keep switching it off, the feature is not broken. It is working as intended and you are overriding it, which is a different problem and not one more settings change will solve.</p>

<p>That is not a character failing either. Apple built Screen Time to be easily reversible, because it ships to everyone and a tool you cannot escape would be a liability. Reversibility is a deliberate feature, and it is the exact feature that makes it insufficient for some people.</p>

<p>Worth knowing that the one published study testing Apple's Downtime and App Limits directly found no significant reduction in screen time, though only 17 people completed it, so treat it as a pilot rather than proof.<sup><a href="#fn2">2</a></sup></p>

<div class="callout"><strong>Start here:</strong> Settings, Screen Time, Always Allowed, and delete everything except Phone and Messages. Then set a passcode you have not memorised. Those two steps fix most cases.</div>

<h2>Where SETL fits</h2>

<p>If any of the seven above was your problem, fix it and spend nothing. SETL is an <a href="/app-blocker.html">iPhone app blocker</a> for the last case only, where the settings are right and the undoing is the issue: it runs automatically at your bedtime and ending a block early is a deliberate press and hold rather than a tap. See also <a href="/apple-screen-time-alternative.html">the Apple Screen Time alternative page</a>.</p>
""",
 "sources": [
   ("Apple Support, Set schedules with Screen Time on iPhone", "https://support.apple.com/guide/iphone/set-schedules-with-screen-time-iphb0c7313c9/26/ios/26"),
   ("Vu TH and Tagliabue M, Active nudging towards digital well-being, Frontiers in Psychiatry, 2025", "https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2025.1602997/full"),
 ],
 "faq": [
  ("Why is Screen Time not blocking my apps?",
   "Most often because those apps are in your Always Allowed list, which exempts them from blocks entirely. Check Settings, then Screen Time, then Always Allowed, and strip it to Phone and Messages."),
  ("Why can I not find Downtime on my iPhone?",
   "It was renamed in iOS 27. Downtime is now Screen Time Schedule and App Limits are now Time Allowances. Nothing was removed, but most online guides still use the old names."),
  ("Why does my Screen Time limit let me carry on?",
   "Because that is what an allowance does. It reports that your time is spent and then permits you to continue. If you want apps to actually become unavailable, use a Screen Time Schedule instead."),
  ("How do I stop myself turning Screen Time off?",
   "Use a random passcode you have not memorised, written on paper and stored somewhere inconvenient, or have someone else set it. Anyone who knows the passcode can disable everything in seconds."),
  ("Is Screen Time broken or am I doing it wrong?",
   "Usually the latter, and usually Always Allowed. Genuine glitches show up as a schedule that is on but does nothing at all, or settings that will not sync. Restart, update, then contact Apple Support."),
  ("What if everything is set correctly and I still override it?",
   "Then it is working as designed. Apple made Screen Time easily reversible on purpose, and that reversibility is exactly what makes it insufficient for some people."),
 ],
 "related": ["always-allowed-screen-time", "screen-time-limits-not-working", "ios-27-screen-time"],
}
