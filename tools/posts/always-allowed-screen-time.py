POST = {
 "slug": "always-allowed-screen-time",
 "title": "Always Allowed in Screen Time: Fix the Leak | SETL",
 "h1": "Always Allowed is why your Screen Time block does nothing",
 "desc": "Always Allowed in Screen Time overrides your schedule completely. Why that list is the most common reason blocks fail, and exactly what to leave in it.",
 "tagline": "Screen Time",
 "minutes": 6,
 "primary": "always allowed",
 "keywords": "always allowed, always allowed screen time, screen time not blocking apps, downtime not working, screen time schedule leak",
 "intro": "If your schedule is on and apps still open, this is almost certainly why. It takes two minutes to fix and almost nobody checks it.",
 "answer": "Always Allowed is a list of apps that ignore your Screen Time schedule entirely. Anything in it stays available during a block. It is the most common reason a Screen Time Schedule appears not to work, and it should contain only Phone and Messages.",
 "body": """
<p>If you have set up a Screen Time block and apps still open during it, you almost certainly have things sitting in <strong>Always Allowed</strong>.</p>

<p>This is the single most common reason people conclude Apple's blocking does not work, give up, and go looking for a paid app they may not need.</p>

<h2>What Always Allowed actually does</h2>

<p>It is a list of exceptions. Anything on it is available at all times, regardless of what your Screen Time Schedule says. Not limited. Not delayed. Simply exempt.</p>

<p>So you can have a perfectly configured schedule running from 10pm to 7am, with the right apps selected, and still open the exact app you were trying to avoid, because at some point it ended up on the exceptions list.</p>

<p>The schedule is not broken. It is being overridden, silently, by a setting on a different screen that you configured once and forgot.</p>

<h2>Why things end up in there</h2>

<p>Three ways, and all of them are reasonable at the time.</p>

<p><strong>Apple put some there by default.</strong> Phone is normally allowed, which is correct, and you should leave it.</p>

<p><strong>You added things during setup.</strong> This is the big one. You were working through the settings, thinking about edge cases, and you allowed four or five apps because you could imagine needing them. That was a sensible instinct applied at the wrong moment, because the version of you configuring Screen Time is optimistic and imaginative about emergencies.</p>

<p><strong>You added one in a moment of need.</strong> You needed something once, during a block, and the quickest route was to allow it permanently. That was six weeks ago and it has been exempt ever since.</p>

<h2>How to check and fix Always Allowed</h2>

<ol>
<li>Open <strong>Settings</strong>.</li>
<li>Tap <strong>Screen Time</strong>.</li>
<li>Tap <strong>Always Allowed</strong>.</li>
<li>Look at the list. Be prepared to be annoyed by what is in it.</li>
<li>Remove everything except what you would genuinely need at 3am in an emergency.</li>
</ol>

<p>Note that in iOS 27 the surrounding settings were renamed: Downtime is now Screen Time Schedule and App Limits are now Time Allowances. Apple's guide tells you to tap Screen Time, then tap Screen Time Schedule or Time Allowances.<sup><a href="#fn1">1</a></sup> Always Allowed sits alongside them.</p>

<h2>What to leave in the list</h2>

<div class="tablewrap"><table class="cmp"><thead><tr><th>App</th><th>Keep it?</th><th>Why</th></tr></thead><tbody>
<tr><td>Phone</td><td>Yes</td><td>Someone might genuinely need to reach you</td></tr>
<tr><td>Messages</td><td>Probably</td><td>Same reason, though it is also a feed if you let it be</td></tr>
<tr><td>A separate alarm app</td><td>Only if you use one</td><td>The built in Clock is unaffected by blocks anyway</td></tr>
<tr><td>Maps</td><td>No</td><td>You are asleep. You are not navigating.</td></tr>
<tr><td>Safari or any browser</td><td>No</td><td>Allowing a browser cancels almost every block you have set</td></tr>
<tr><td>Email</td><td>No</td><td>Nothing arriving by email at 1am requires you</td></tr>
<tr><td>Any social app</td><td>No</td><td>This is the thing you were trying to block</td></tr>
<tr><td>Music or podcasts</td><td>Your call</td><td>Harmless for most people, a loophole for some</td></tr>
</tbody></table></div>

<p>The browser line is the one worth repeating. A browser is a route to everything you just blocked. Leaving Safari permanently allowed converts a careful block into a mild inconvenience, since the websites still work. If that applies to you, see <a href="/blog/how-to-block-websites-on-iphone.html">how to block websites on iPhone</a>.</p>

<h2>The principle behind it</h2>

<p>When you are configuring this, you are imagining emergencies. That is the wrong frame, because the question is not what you might conceivably need. It is what you would actually be unable to manage without for eight hours while asleep.</p>

<p>Almost nothing passes that test. A phone call covers nearly every genuine emergency, and if something is urgent enough to matter at 2am, someone will ring rather than message you on an app.</p>

<p>The useful test when adding anything: would a stranger watching me add this think I was protecting myself, or building a door.</p>

<p>It helps to notice that the exceptions list is the only part of Screen Time you configure while fully awake and in no difficulty at all. Everything else about a block is experienced at the hard moment, at night, when you want it gone. The exceptions are decided in the calm. That asymmetry sounds like it should make the list trustworthy, and it does the opposite, because the calm version of you is the one most willing to be reasonable about hypothetical needs. Being reasonable is exactly what you were trying to stop doing at midnight.</p>

<h2>Three other reasons a block appears not to work</h2>

<p>If Always Allowed is clean and apps still open, check these in order.</p>

<p><strong>You know the passcode.</strong> Anyone with the Screen Time passcode can switch everything off in seconds. If you can type it without thinking, you have a reminder rather than a block. Use a random one, write it on paper, store it somewhere inconvenient.</p>

<p><strong>You are using the website.</strong> Blocking an app leaves the browser version untouched. Very common and very easy to miss.</p>

<p><strong>You set a Time Allowance rather than a Schedule.</strong> An allowance tells you when the time is spent and then lets you continue. A schedule makes the apps unavailable during set hours. For a specific problem hour you want the schedule. See <a href="/blog/time-allowances-vs-screen-time-schedule.html">which of the two to use</a>.</p>

<div class="callout"><strong>Two minutes, right now:</strong> Settings, Screen Time, Always Allowed. Delete everything except Phone and Messages. This fixes more broken blocks than any other single action.</div>

<h2>Where SETL fits</h2>

<p>Fix Always Allowed first. It is free and it may be the only thing wrong. SETL is an <a href="/app-blocker.html">iPhone app blocker</a> for the case where your settings are correct and you keep undoing them anyway: it runs at your bedtime without being opened and ending a block early is a deliberate hold rather than a tap. For the full picture on this year's changes, read <a href="/blog/ios-27-screen-time.html">the iOS 27 Screen Time guide</a>.</p>
""",
 "sources": [
   ("Apple Support, Set schedules with Screen Time on iPhone", "https://support.apple.com/guide/iphone/set-schedules-with-screen-time-iphb0c7313c9/26/ios/26"),
 ],
 "faq": [
  ("What is Always Allowed in Screen Time?",
   "A list of apps that ignore your Screen Time schedule completely. Anything on it stays available during a block, which makes it the most common reason a block appears not to work."),
  ("Where is Always Allowed on iPhone?",
   "Settings, then Screen Time, then Always Allowed. It sits alongside Screen Time Schedule and Time Allowances, which are the iOS 27 names for Downtime and App Limits."),
  ("What should I leave in Always Allowed?",
   "Phone, and probably Messages. Nothing else. Remove browsers especially, because allowing Safari gives you a route to every website you just blocked."),
  ("Why do apps still open during my Screen Time Schedule?",
   "Almost always Always Allowed. If that list is clean, check whether you know the passcode by heart, whether you are using the website instead of the app, or whether you set an allowance rather than a schedule."),
  ("Does Always Allowed override App Limits too?",
   "Yes. Apps on the list are exempt from your restrictions generally, which is the point of the feature. It is useful for Phone and actively harmful for anything else."),
  ("Should I allow Messages during a block?",
   "Probably, so people can reach you, but be aware that group chats function as a feed. If your late nights are spent in Messages rather than social apps, take it off the list."),
 ],
 "related": ["ios-27-screen-time", "screen-time-schedule-iphone", "screen-time-limits-not-working"],
}
