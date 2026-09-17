"""v0.4 cross-cutting patch: owner's third review (2026-09-17).

Regenerates the shared header (Technology / Programs / Events dropdowns) and footer on every page, applies the
owner's 18 directives to the existing pages (partners strip, green counter, linked steps, Vimeo clips, hours,
FieldhouseUSA link + map pin, new membership names, no "15% off", BOOM colours, red stats, FAQ hero + styling +
questions, Download-the-app anchor, Vimeo privacy note, sitemap), and appends the v0.4 CSS and JS.

Run from anywhere:  python scripts/patch_v04.py     (idempotent: a replacement already present is skipped)
Header/footer templates live here: edit nav() / FOOTER and re-run, never the eight copies.
"""
import re, os, json, html as htmlmod
from pathlib import Path

os.chdir(Path(__file__).resolve().parent.parent)

def rep(s, a, b, f, expect=1, atleast=False):
    if b in s and a not in s:
        return s
    n = s.count(a)
    ok = (n >= 1) if atleast else (n == expect)
    assert ok, (f, 'expected', 'at least 1' if atleast else expect, 'found', n, a[:100])
    return s.replace(a, b)

def rep_re(s, pattern, b, f):
    m = re.search(pattern, s, re.S)
    if not m:
        assert b in s, (f, 'anchor not found and replacement absent', pattern[:80])
        return s
    return s[:m.start()] + b + s[m.end():]

BOOK = 'https://shoot360-prod.saloncloudsplus.io/ghl/athlete-info'
FH = 'https://aurorafieldhouseusa.com/'
GMAPS = 'https://maps.google.com/?cid=8030805088891520148'
MAP_Q = 'Aurora+FieldhouseUSA,+14200+E+Alameda+Ave,+Aurora,+CO+80012'
BADGES = ('<a class="badge-app" href="https://apps.apple.com/us/app/shoot-360/id1177068011" target="_blank" rel="noopener"><img src="assets/img/badge-appstore.svg" alt="Download on the App Store" width="120" height="40" loading="lazy"></a>'
          '<a class="badge-app" href="https://play.google.com/store/apps/details?id=com.Shoot360.Mobile" target="_blank" rel="noopener"><img src="assets/img/badge-googleplay.png" alt="Get it on Google Play" width="646" height="250" loading="lazy"></a>')
VIMEO_Q = 'autoplay=1&amp;muted=1&amp;loop=1&amp;autopause=0&amp;title=0&amp;byline=0&amp;portrait=0&amp;badge=0&amp;dnt=1'  # background=1 is a paid-tier feature: the player answers 401 with it on this basic account
OLD_VIMEO_Q = 'background=1&amp;' + VIMEO_Q
def vimeo(vid, title, cap, cls='reveal'):
    return (f'<div class="vimeo {cls}"><iframe src="https://player.vimeo.com/video/{vid}?{VIMEO_Q}" title="{title}" loading="lazy" '
            f'allow="autoplay; fullscreen; picture-in-picture" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>'
            f'<span class="cap">{cap}</span></div>')
VIMEO_SHOOT = ('720241338', 'Splash Meter shooting court: arc, depth and alignment read on every shot', 'Shooting court')
VIMEO_PASS = ('720257389', 'High-tech passing and ball-handling skill court', 'Skill court')

# page file -> nav key for aria-current / open-parent
PAGES = {'index.html': 'home', 'technology.html': 'technology', 'publications.html': 'technology', 'memberships.html': 'memberships',
         'programs.html': 'programs', 'events.html': 'events', 'faq.html': 'faq', 'contact.html': 'contact', 'legal.html': 'legal'}

def nav(cur):
    def a(href, label, key):
        ac = ' aria-current="page"' if key == cur else ''
        return f'<li><a href="{href}"{ac}>{label}</a></li>'
    def sub(label, key, sid, items):
        op = ' open-parent' if key == cur else ''
        lis = '\n            '.join(
            f'<li><a href="{h}"{" target=\"_blank\" rel=\"noopener\"" if h.startswith("http") else ""}>{l}</a></li>' for h, l in items)
        return (f'<li class="has-sub{op}">\n'
                f'          <button type="button" class="sub-toggle" aria-expanded="false" aria-controls="{sid}">{label}</button>\n'
                f'          <ul id="{sid}" class="sub">\n            {lis}\n          </ul>\n        </li>')
    return f'''<!-- [NAV] -->
<header class="nav">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Shoot 360 Denver — home"><img src="assets/img/logo-red-white.png" alt="Shoot 360 Basketball" width="720" height="245"></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Open menu"><span></span>Menu</button>
    <nav aria-label="Primary">
      <ul id="primary-nav" class="nav-links">
        {sub('Technology', 'technology', 'sub-tech', [('technology.html', 'The technology'), ('publications.html', 'Publications'), ('technology.html#app', 'Download the app')])}
        {a('memberships.html', 'Memberships', 'memberships')}
        {sub('Programs', 'programs', 'sub-programs', [('programs.html', 'All programs'), ('programs.html#classes', 'Classes'), ('programs.html#camps', 'Camps'), ('programs.html#leagues', 'Leagues'), ('https://www.teamevo.org/', 'Basketball Club'), ('mailto:info@shoot360denver.com?subject=Private%20training', 'Private Training')])}
        {sub('Events', 'events', 'sub-events', [('events.html#special', 'Special events'), ('events.html#parties', 'Parties'), ('events.html#date-night', 'Date nights')])}
        {a('faq.html', 'FAQ', 'faq')}
        {a('contact.html', 'Visit Us', 'contact')}
        <li class="nav-cta"><a class="btn btn-primary btn-sm" href="memberships.html">New Membership</a></li>
      </ul>
    </nav>
  </div>
</header>'''

FOOTER = f'''<!-- [FT] -->
<footer class="ft">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="brand" href="index.html" aria-label="Shoot 360 Denver — home"><img src="assets/img/logo-red-white.png" alt="Shoot 360 Basketball" width="720" height="245" loading="lazy"></a>
        <p>NBA-grade shooting and skills technology inside FieldhouseUSA in Aurora, Colorado. The future of the game is here.</p>
        <p class="ft-app">Classes, camps, leagues and drop-ins are booked in the Shoot 360 app.</p>
        <div class="badges">{BADGES}</div>
      </div>
      <div><h3>Visit</h3><ul><li><a href="{FH}" target="_blank" rel="noopener">FieldhouseUSA</a><br>14200 E Alameda Ave<br>Aurora, CO 80012</li><li><a href="tel:+17202625501">720-262-5501</a></li><li><a href="mailto:info@shoot360denver.com">info@shoot360denver.com</a></li></ul></div>
      <div><h3>Hours</h3><ul><li>Mon – Fri: 2 – 9 PM</li><li>Sat – Sun: 10 AM – 5 PM</li><li>Homeschool: Mon – Fri 2 – 4 PM</li></ul></div>
      <div><h3>Explore</h3><ul><li><a href="technology.html">Technology</a></li><li><a href="publications.html">Publications</a></li><li><a href="memberships.html">Memberships</a></li><li><a href="programs.html">Programs</a></li><li><a href="events.html">Events &amp; Parties</a></li><li><a href="faq.html">FAQ</a></li><li><a href="contact.html">Visit Us</a></li><li><a href="https://www.teamevo.org/" target="_blank" rel="noopener">Basketball Club — Team EVO</a></li><li><a href="https://www.instagram.com/shoot360denver/" target="_blank" rel="noopener">Instagram @shoot360denver</a></li><li><a href="https://www.facebook.com/shoot360denver" target="_blank" rel="noopener">Facebook</a></li><li><a href="{GMAPS}" target="_blank" rel="noopener">Reviews on Google</a></li></ul></div>
    </div>
    <div class="legal">
      <span>© 2026 Shoot 360 Denver. An independently owned and operated Shoot 360 location.</span>
      <span><a href="legal.html#privacy">Privacy</a> · <a href="legal.html#services">Data &amp; third-party services</a> · <a href="legal.html#disclaimer">Disclaimer</a> · <a href="legal.html#accessibility">Accessibility</a></span>
    </div>
  </div>
</footer>'''

# ---------------------------------------------------------------- FAQ (single source: HTML list + FAQPage JSON-LD)
TBD = lambda v: f'<span class="tbd">{v}</span>'
FAQ = [
 ('q-start', 'What is Shoot 360?', 'A technology-based basketball training facility. Dedicated shooting courts with the patented Splash Meter™ give instant feedback on arc, depth and alignment; high-tech skill courts measure passing and ball-handling; and every rep is tracked in the Shoot 360 app. Coaches use the data to guide your training.'),
 (None, 'Who is Shoot 360 for?', 'Players of all ages and skill levels, from youth learning fundamentals to high-school, college and adult athletes. Classes, camps and Little Ballers (ages 6–10) are grouped by age and level. A parent or guardian attends with minors for the first visit.'),
 (None, 'How do I get started?', f'<a href="{BOOK}" target="_blank" rel="noopener">Book an evaluation session online</a> and a coach meets you on the court. Evaluations are for first-time visitors; a parent or guardian attends with minors.'),
 (None, 'What happens at the evaluation?', 'About an hour, coach-led. You shoot on the Splash Meter, work a skill court and leave with a baseline on your shot\'s arc, depth and alignment, all tracked in the app. There is no obligation to join.'),
 (None, 'How do I book?', 'Use the <strong>Book an Evaluation</strong> button on any page, or call <a href="tel:+17202625501">720-262-5501</a>. Members book sessions, classes and personal training in the Shoot 360 app.'),
 ('q-tech', 'What does the Splash Meter measure?', 'Arc, depth and left-right alignment on every shot, in real time. When all three land in the Splash Zone™ the make probability rises to as high as 98%. <a href="technology.html">More on the technology →</a>'),
 (None, 'How many shots do I get in a session?', 'A 30-minute hoop session on a shooting court produces 300 or more measured shots. Automatic rebounding keeps the ball coming back.'),
 (None, 'Is the technology really used by the NBA?', 'NBA organizations run or co-brand Shoot 360 facilities (the Golden State Warriors, Utah Jazz, Brooklyn Nets and LA Clippers), a dozen current and former NBA and WNBA players own or invest in locations, and the shot-tracking behind the Splash Meter is the same kind installed in NBA practice facilities. <a href="publications.html">Read the publications →</a>'),
 (None, 'What is a session, and how long is it?', 'A session is a 30-minute block on one court: a shooting bay (300+ measured shots with automatic rebounding) or a skills court (passing and ball-handling games). Members book them one at a time in the app, so a typical visit is a shooting session, a skills session, and a few minutes with your coach on the numbers.'),
 (None, 'How often should my athlete train?', 'Two or three sessions a week is where players see steady improvement; once a week still shows in the numbers over a season. Varsity (8 sessions a month) fits twice a week, Committed and Ball is Life fit anything more.'),
 (None, 'Can parents watch?', 'Yes. A parent or guardian can stay in the facility and watch from the viewing area during their child\'s session, and every workout\'s numbers are in the app afterwards. Under-18s need a guardian present for their first visit.'),
 (None, 'What should we wear and bring?', 'Athletic clothes, clean court shoes (no black-soled shoes or cleats on the courts) and a water bottle. We supply the basketballs and equipment; outside balls stay in the bag. No food or drinks except water on the courts.'),
 (None, 'How do I cancel or change a membership?', 'Memberships continue month to month after the commitment. Cancel in the Shoot 360 app before the 1st of the month (basketball icon → Contracts → Cancel), or ask the front desk. The contract you signed sets the notice and any early-termination terms. <a href="memberships.html#policies">Membership policies →</a>'),
 (None, 'Are you closed for events?', 'Occasionally. The courts close for a full-facility takeover on select Saturday nights after 6 PM and for camps or tournaments; members see closures in the app schedule ahead of time.'),
 (None, 'Do you photograph or film athletes?', 'Court cameras track the ball, not faces, and your stats are yours in the app. We sometimes photograph or film sessions, classes and events for our website and social media; tell the front desk if you would rather your athlete not appear. First names may show on court leaderboards.'),
 ('q-memberships', 'How do memberships work?', 'Pick a hoop membership by how often you train: <strong>JV</strong> is 4 sessions a month ($149/mo), <strong>Varsity</strong> is 8 ($189/mo), <strong>Committed</strong> is unlimited ($229/mo) and <strong>Ball is Life</strong> is unlimited on a 12-month commitment ($220/mo). In the Shoot 360 app they appear as Rookie, Pro, All-Star and Hall of Fame. Every membership includes a coach during your sessions, the patented NBA technology, your stats in the app and Nike camp discounts. <a href="memberships.html#tiers">Compare tiers →</a>'),
 (None, 'What are Unlimited Classes and Little Ballers?', f'<strong>Unlimited Classes</strong> is a classes-only membership ({TBD("$159")}/mo, 1-month commitment): every coach-led group class on the schedule, all month, with stats in the app, members\' leagues and Nike camp discounts. <strong>Little Ballers</strong> is the same idea for ages 6–10: all classes, built for our youngest players. Hoop members can add unlimited classes for $40 a month. <a href="memberships.html#classes">Details →</a>'),
 (None, 'Can I train without a membership?', f'Yes. A <strong>Drop-In</strong> session is {TBD("$42")} on the technology, booked in the Shoot 360 app up to 3 days ahead when space permits. Drop-ins are technology only; coaching comes with a membership.'),
 (None, 'Is coaching extra?', f'No. Every membership includes a coach on the floor during your sessions at no additional fee. Want dedicated one-on-one time? Personal training add-ons are 4 sessions for {TBD("$120")} or 8 for {TBD("$240")} a month, membership required. <a href="memberships.html#coaching">How coaching works →</a>'),
 (None, 'What is the enrollment fee?', 'A one-time $40 fee creates your athlete profile and connects it to the app. Drop-In and My Spark memberships have no enrollment fee. Aurora sales tax is added to membership dues.'),
 (None, 'How far ahead can I book, and can I book back-to-back sessions?', 'Each membership has a scheduling window: JV books 5 days ahead, Varsity 6, Committed and Ball is Life 7, Drop-In 3; Lock-In Reserved holds a fixed weekly time. Sessions are one at a time, not back to back, so every member gets court time.'),
 (None, 'What happens if I miss a session?', 'Cancel in the app before your session and nothing happens. A no-show with no call counts as a strike: the first strike adds $50 to your membership, the second ends it without refund. The contract you sign at signup has the exact wording. <a href="memberships.html#policies">Membership policies →</a>'),
 ('q-programs', 'Do you run camps, classes and clinics?', 'Yes, for all ages and skill levels, taught by certified Shoot 360 coaches. Official <a href="https://www.ussportscamps.com/basketball/nike/nike-basketball-camp-shoot360-denver-co" target="_blank" rel="noopener">Nike Basketball Camps</a> are hosted here each summer through US Sports Camps, and members get Nike camp discounts.'),
 (None, 'Is there an app?', 'Yes, the Shoot 360 app for <a href="https://apps.apple.com/us/app/shoot-360/id1177068011" target="_blank" rel="noopener">iOS</a> and <a href="https://play.google.com/store/apps/details?id=com.Shoot360.Mobile" target="_blank" rel="noopener">Android</a>. It shows stat summaries of every workout, awards digital trophies, books sessions, classes and personal training, and registers you for leagues. <a href="technology.html#app">Download the app →</a>'),
 ('q-visit', 'Where are you, and when are you open?', f'Inside <a href="{FH}" target="_blank" rel="noopener">FieldhouseUSA</a> at 14200 E Alameda Ave, Aurora, CO 80012. Park in the FieldhouseUSA lot and come through the main entrance. Hours: Monday to Friday 2 to 9 PM, Saturday and Sunday 10 AM to 5 PM. <a href="contact.html">Map and directions →</a>'),
 (None, 'What is My Spark Denver, and can I use it here?', 'My Spark Denver is a DPS Foundation scholarship for Denver Public Schools students in grades 6–8 whose families qualify for free or reduced-price school meals. Each student gets a $1,000 My Spark card to spend on after-school and enrichment programs with approved providers, and Shoot 360 Denver is one of them. Our My Spark membership is 6 months of training, 4 sessions a month, no enrollment fee, paid with the card, and families who spend their full card here can apply for the DPS Foundation\'s $1,000 grant. Aurora Public Schools families: ask us about the same plan. <a href="programs.html#myspark">Details and application link →</a>'),
 ('q-parties', 'Do you host birthday parties and events?', 'Yes. Birthday parties on 2 courts with a coach running the games, full-facility takeovers for bigger groups on select Saturday nights, corporate and team events, bachelor and graduation parties, and date nights. Food and drinks come from the on-site restaurant and bar. <a href="events.html">Events and parties →</a>'),
 (None, 'Do you have homeschool sessions?', 'Yes. Homeschool sessions run Monday to Friday, 2 to 4 PM. Members use their regular sessions; non-members book a Drop-In. <a href="programs.html#homeschool">Homeschool details →</a>'),
 (None, 'Is there a family discount?', 'Yes. Households with more than one athlete get a discount on the second and later memberships. Ask for current family pricing at the front desk or when you book your evaluation.'),
 (None, 'Can I pause my membership?', 'Yes. Memberships can be suspended for injury, travel or a tournament season; ask the front desk for the current terms and notice period. <a href="memberships.html#policies">Membership policies →</a>'),
 (None, 'How do I register for classes, camps and leagues?', 'In the Shoot 360 app, for members and non-members alike. Download it, create your athlete profile, and register from the schedule; drop-in sessions are booked the same way when space permits. <a href="programs.html#app">Get the app →</a>'),
 (None, 'Do you offer private training?', f'Yes. Coaching is already included in every membership; for dedicated one-on-one blocks, personal training add-ons are 4 sessions for {TBD("$120")} or 8 for {TBD("$240")} a month (membership required). Email <a href="mailto:info@shoot360denver.com?subject=Private%20training">info@shoot360denver.com</a> with the athlete\'s age, level and availability.'),
 (None, 'Do I need to sign a waiver?', 'Yes. Every participant, or a parent or guardian for a minor, agrees to the participation disclaimer before training. <a href="legal.html#disclaimer">Read the full text →</a>'),
]
FAQ_CATS = [('q-start', 'Getting started'), ('q-tech', 'The technology'), ('q-memberships', 'Memberships'), ('q-programs', 'Programs & app'), ('q-visit', 'Visit & My Spark'), ('q-parties', 'Events & parties')]

def faq_html():
    out = []
    for cid, q, a in FAQ:
        idattr = f' id="{cid}"' if cid else ''
        out.append(f'      <div class="faq-item"{idattr}><button class="faq-q" type="button">{q}</button><div class="faq-a"><p>{a}</p></div></div>')
    return '\n'.join(out)

def faq_json():
    def plain(a):
        t = re.sub(r'<[^>]+>', '', a)
        return htmlmod.unescape(t).replace('™', '')
    return json.dumps({"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": htmlmod.unescape(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for _, q, a in FAQ]},
        ensure_ascii=False, separators=(',', ':'))

BALL_SVG = ('<svg class="faq-ball" viewBox="0 0 200 200" aria-hidden="true" focusable="false"><circle cx="100" cy="100" r="96" fill="#E0001B"/>'
            '<g fill="none" stroke="#0B0B0B" stroke-width="5"><circle cx="100" cy="100" r="96"/><path d="M4 100h192M100 4v192M30 32c40 30 40 106 0 136M170 32c-40 30-40 106 0 136"/></g></svg>')

# ---------------------------------------------------------------- shared blocks on every page
for f, key in PAGES.items():
    if not Path(f).exists():
        print('skip (not built yet):', f); continue
    s = Path(f).read_text(encoding='utf-8')
    s = rep_re(s, r'<!-- \[NAV\] -->.*?</header>', nav(key), f)
    s = rep_re(s, r'<!-- \[FT\] -->.*?</footer>', FOOTER, f)
    s = s.replace(OLD_VIMEO_Q, VIMEO_Q)
    s = s.replace('"opens":"13:00"', '"opens":"14:00"')
    s = s.replace('"priceRange":"$72–$389"', '"priceRange":"$42–$240"')
    s = s.replace('href="parties.html"', 'href="events.html#parties"')
    Path(f).write_text(s, encoding='utf-8')

# ---------------------------------------------------------------- index.html
f = 'index.html'; s = Path(f).read_text(encoding='utf-8')
s = rep(s, 'Come evaluate. Memberships from $159/mo.', 'Come evaluate. Memberships from $149/mo.', f)
s = rep(s, '<span><strong>Mon–Fri</strong> 1–9 PM</span>', '<span><strong>Mon–Fri</strong> 2–9 PM</span>', f)
s = rep(s, '"geo":{"@type":"GeoCoordinates","latitude":39.7092942,"longitude":-104.822972}', '"geo":{"@type":"GeoCoordinates","latitude":39.7092894,"longitude":-104.8217123}', f)
# 1. partners: logos first, label under, Nuggets 40% larger (30 -> 42 px)
s = rep(s, '''    <p>Our industry partners</p>
    <img src="assets/img/partner-nike.png" alt="Nike" width="360" height="188" loading="lazy">
    <img src="assets/img/partner-wilson.png" alt="Wilson" width="360" height="85" loading="lazy">
    <img src="assets/img/partner-nuggets.png" alt="Denver Nuggets" width="300" height="300" loading="lazy">''',
'''    <div class="logos">
      <img src="assets/img/partner-nike.png" alt="Nike" width="360" height="188" loading="lazy">
      <img src="assets/img/partner-wilson.png" alt="Wilson" width="360" height="85" loading="lazy">
      <img src="assets/img/partner-nuggets.png" alt="Denver Nuggets" width="300" height="300" loading="lazy" class="lg">
    </div>
    <p>Our industry partners</p>''', f)
# 3. how it works: each step links to its page
s = rep(s, '<div class="step reveal"><h3>Come evaluate</h3><p>Book an evaluation online. A coach meets you on the court, you shoot on the Splash Meter, and you leave with a baseline on arc, depth and alignment.</p></div>',
        f'<a class="step reveal" href="{BOOK}" target="_blank" rel="noopener"><h3>Come evaluate</h3><p>Book an evaluation online. A coach meets you on the court, you shoot on the Splash Meter, and you leave with a baseline on arc, depth and alignment.</p><span class="more">Book an evaluation →</span></a>', f)
s = rep(s, '<div class="step reveal"><h3>Train with a coach on the tech</h3><p>Dedicated shooting courts and skill courts turn every session into 300+ measured reps. A coach reads the numbers with you; that coaching is included.</p></div>',
        '<a class="step reveal" href="technology.html"><h3>Train with a coach on the tech</h3><p>Dedicated shooting courts and skill courts turn every session into 300+ measured reps. A coach reads the numbers with you; that coaching is included.</p><span class="more">See the technology →</span></a>', f)
s = rep(s, '<div class="step reveal"><h3>Track and book in the app</h3><p>Every workout lands in the Shoot 360 app: shot charts, streaks, achievements, and the schedule where you register for classes, camps and leagues.</p></div>',
        '<a class="step reveal" href="technology.html#app"><h3>Track and book in the app</h3><p>Every workout lands in the Shoot 360 app: shot charts, streaks, achievements, and the schedule where you register for classes, camps and leagues.</p><span class="more">Download the app →</span></a>', f)
# 4. Vimeo clips replace the HUD still in the technology teaser
s = rep(s, '<img src="assets/img/tech-splash-meter-hud.jpg" alt="Splash Meter display showing arc, depth and left-right alignment for each shot" width="1600" height="900" loading="lazy" class="reveal">',
        f'<div class="vimeo-pair reveal">{vimeo(*VIMEO_SHOOT, cls="")}{vimeo(*VIMEO_PASS, cls="")}</div>', f)
# programs grid card: parties -> events
s = rep(s, '<div class="card-body"><h3>Birthday parties</h3><p>Private court time, a coach running the games, and a Splash Meter leaderboard finish.</p><span class="more">Party packages →</span></div>',
        '<div class="card-body"><h3>Events &amp; parties</h3><p>Birthday parties, team and corporate events, and date nights on the technology, with a coach running the games.</p><span class="more">See events →</span></div>', f)
s = s.replace('<a class="card reveal" href="events.html#parties"><img src="assets/img/coaching-huddle.jpg"', '<a class="card reveal" href="events.html"><img src="assets/img/coaching-huddle.jpg"')
s = rep(s, '<p>4 visits, 8 visits or unlimited. Coaching included, family discounts, join online.</p>', '<p>JV, Varsity, Committed and Ball is Life: 4, 8 or unlimited sessions. Coaching included, join online.</p>', f)
# 6/7/13. pricing teaser with the owner's names
HM06 = f'''<!-- [HM-06] Pricing teaser — owner's tier names (app names in brackets); Join goes straight to each contract's signup -->
<section class="sec sec-light" aria-labelledby="price-h">
  <div class="wrap">
    <p class="eyebrow">Memberships</p>
    <h2 id="price-h">Pick your membership</h2>
    <p class="lead">Every membership is fully integrated: a coach during your sessions, the patented NBA technology, your stats in the Shoot 360 app and Nike camp discounts. Pick by how often you want to train.</p>
    <div class="tiers mt2">
      <div class="tier reveal"><h3>JV</h3><p class="fine">Rookie in the app</p><div class="visits">4<small>sessions / month</small></div><div class="price">$149<small>/mo</small></div><ul><li>Coaching included</li><li>3-month commitment</li><li>Book 5 days ahead · extra session $37</li></ul><a class="btn btn-outline-dark btn-sm" href="https://www.shoot360.com/membership-checkout?locationid=5739019&amp;contractid=151" target="_blank" rel="noopener">Join</a></div>
      <div class="tier reveal"><h3>Varsity</h3><p class="fine">Pro in the app</p><div class="visits">8<small>sessions / month</small></div><div class="price">$189<small>/mo</small></div><ul><li>Coaching included · members' leagues</li><li>3-month commitment</li><li>Book 6 days ahead · extra session $24</li></ul><a class="btn btn-outline-dark btn-sm" href="https://www.shoot360.com/membership-checkout?locationid=5739019&amp;contractid=152" target="_blank" rel="noopener">Join</a></div>
      <div class="tier hot reveal"><span class="tag">Most popular</span><h3>Committed</h3><p class="fine">All-Star in the app</p><div class="visits">∞<small>unlimited sessions</small></div><div class="price">$229<small>/mo</small></div><ul><li>Coaching included · members' leagues</li><li>3-month commitment · day-time court access</li><li>Book 7 days ahead · extra sessions $0</li></ul><a class="btn btn-primary btn-sm" href="https://www.shoot360.com/membership-checkout?locationid=5739019&amp;contractid=154" target="_blank" rel="noopener">Join</a></div>
      <div class="tier reveal"><h3>Ball is Life</h3><p class="fine">Hall of Fame in the app</p><div class="visits">∞<small>unlimited sessions</small></div><div class="price">$220<small>/mo</small></div><ul><li>Coaching included · members' leagues</li><li>12-month commitment · day-time court access</li><li>Book 7 days ahead · extra sessions $0</li></ul><a class="btn btn-outline-dark btn-sm" href="https://www.shoot360.com/membership-checkout?locationid=5739019&amp;contractid=156" target="_blank" rel="noopener">Join</a></div>
    </div>
    <p class="fine mt1">Also: <a href="memberships.html#classes">Unlimited Classes</a> and <a href="memberships.html#classes">Little Ballers</a> (ages 6–10) at {TBD("$159")}/mo, <a href="memberships.html#more">Drop-In</a> sessions, <a href="memberships.html#more">Lock-In Reserved</a> fixed weekly times, and a <a href="memberships.html#more">My Spark / DPS / APS</a> membership. One-time $40 enrollment fee; Aurora sales tax not included. Prices as of Sept 17, 2026; full contract terms are shown at signup.</p>
    <div class="btns mt1"><a class="btn btn-dark" href="memberships.html#compare">Compare every membership</a><a class="btn btn-outline-dark" href="memberships.html#calc">Trainer vs. membership calculator</a></div>
  </div>
</section>
'''
s = rep_re(s, r'<!-- \[HM-06\].*?</section>\n', HM06, f)
# 10/11. visit block: hours, FieldhouseUSA link, directions + map pinned on the FieldhouseUSA listing
s = rep(s, '<tr><td>Monday – Friday</td><td>1:00 – 9:00 PM</td></tr>', '<tr><td>Monday – Friday</td><td>2:00 – 9:00 PM</td></tr>', f)
s = rep(s, '<p class="addr">FieldhouseUSA<br>14200 E Alameda Ave', f'<p class="addr"><a href="{FH}" target="_blank" rel="noopener">FieldhouseUSA</a><br>14200 E Alameda Ave', f)
s = rep(s, 'destination=14200+E+Alameda+Ave,+Aurora,+CO+80012', f'destination={MAP_Q}', f)
s = rep(s, 'maps?q=14200+E+Alameda+Ave,+Aurora,+CO+80012&amp;output=embed', f'maps?q={MAP_Q}&amp;output=embed', f)
# home FAQ answers that named the old tiers
s = rep(s, '<p>No. Every membership includes private training and coaching. A coach works with you during your sessions at no additional fee; Pro, All-Star and Hall of Fame add scheduled one-on-one sessions on top.</p>',
        '<p>No. Every membership includes a coach on the floor during your sessions at no additional fee. Personal training add-ons are available for dedicated one-on-one time.</p>', f)
s = rep(s, '<div class="faq-item"><button class="faq-q" type="button">Can I come once without joining?</button><div class="faq-a"><p>Yes. A guest workout is $72, and a 12-visit pack is $480 with no commitment. Drop-in times are booked in the app when space permits.</p></div></div>',
        f'<div class="faq-item"><button class="faq-q" type="button">Can I come once without joining?</button><div class="faq-a"><p>Yes. A Drop-In session is {TBD("$42")}, booked in the Shoot 360 app up to 3 days ahead when space permits. Drop-ins are technology only; coaching comes with a membership.</p></div></div>', f)
s = rep(s, '<p>We are inside FieldhouseUSA at 14200 E Alameda Ave in Aurora. Park in the FieldhouseUSA lot and come through the main entrance.</p>',
        f'<p>We are inside <a href="{FH}" target="_blank" rel="noopener">FieldhouseUSA</a> at 14200 E Alameda Ave in Aurora. Park in the FieldhouseUSA lot and come through the main entrance.</p>', f)
Path(f).write_text(s, encoding='utf-8')

# ---------------------------------------------------------------- technology.html
f = 'technology.html'; s = Path(f).read_text(encoding='utf-8')
s = rep(s, '<img src="assets/img/tech-skill-court.jpg" alt="Player working through a passing game in a Shoot 360 skill court" width="1200" height="802" loading="lazy" class="reveal">',
        vimeo(*VIMEO_PASS), f)
s = rep(s, '<section class="sec sec-light" aria-labelledby="app-h">', '<section class="sec sec-light" id="app" aria-labelledby="app-h">', f)
s = rep(s, '<h2 id="app-h">Track everything</h2>', '<h2 id="app-h">Download the app</h2>\n      <p class="lead">Members and non-members book sessions, classes, camps and leagues in the Shoot 360 app, and every workout\'s numbers land there too.</p>', f)
PUBS = '''<!-- [TC-PUB] Publications teaser -->
<section class="sec sec-ink" aria-labelledby="pub-h">
  <div class="wrap">
    <div class="callout reveal">
      <div>
        <strong id="pub-h">In the press and on NBA practice courts</strong>
        <p>Articles, broadcasts and partner pages about the Splash Meter, the skill courts and the pros and programs that use them.</p>
      </div>
      <a class="btn btn-primary" href="publications.html">Read the publications</a>
    </div>
  </div>
</section>

'''
s = rep(s, '<!-- [TC-08] CTA -->', PUBS + '<!-- [TC-08] CTA -->', f)
s = rep(s, '<a class="btn btn-ghost" href="programs.html">Programs &amp; Pricing</a>', '<a class="btn btn-ghost" href="memberships.html">Memberships</a>', f)
Path(f).write_text(s, encoding='utf-8')

# ---------------------------------------------------------------- programs.html
f = 'programs.html'; s = Path(f).read_text(encoding='utf-8')
s = rep(s, '<li>Hall of Fame and All-Star members: unlimited classes included</li>', f'<li><strong>Unlimited Classes</strong> ({TBD("$159")}/mo) and <strong>Little Ballers</strong> for ages 6–10: every class on the schedule, all month</li>', f)
s = rep(s, '<li>Rookie, Pro and non-members: register per class in the app at the rate shown there</li>', '<li>JV, Varsity, Committed and Ball is Life members: add unlimited classes for $40/mo, or register per class in the app</li>', f)
s = rep(s, ' Hall of Fame members save 15% on camps, clinics and combines.', ' Members get discounts on Nike Basketball Camps.', f)
PGPT = '''<!-- [PG-PT] Events & parties -->
<section class="sec sec-ink" id="parties" aria-labelledby="pt-h">
  <div class="wrap split rev">
    <img src="assets/img/shooting-kids.jpg" alt="Kids shooting on Splash Meter courts" width="1024" height="681" loading="lazy" class="reveal">
    <div class="reveal">
      <p class="eyebrow">Events &amp; parties</p>
      <h2 id="pt-h">Parties, special events, date nights</h2>
      <p class="lead">Birthday parties on 2 courts with a coach running the games and a Splash Meter leaderboard finish; full-facility takeovers for teams, companies and celebrations on select Saturday nights; and date nights on the technology with food and drinks from the on-site restaurant and bar.</p>
      <div class="btns mt1"><a class="btn btn-primary" href="events.html#parties">Party packages</a><a class="btn btn-ghost" href="events.html#special">Special events</a><a class="btn btn-ghost" href="events.html#date-night">Date nights</a></div>
    </div>
  </div>
</section>
'''
s = rep_re(s, r'<!-- \[PG-PT\].*?</section>\n', PGPT, f)
s = rep(s, '<li>Members use their regular visits; non-members use the guest rate or a 12-visit pack</li>', '<li>Members use their regular sessions; non-members book a Drop-In</li>', f)
s = rep(s, '<p>Spend your full My Spark card at Shoot 360 Denver and apply for the $1,000 grant.</p>',
        '<p>My Spark Denver gives income-qualified Denver Public Schools students in grades 6–8 a $1,000 card for after-school programs, and Shoot 360 Denver is an approved provider. Our My Spark membership is 6 months, 4 sessions a month, no enrollment fee, paid with the card. Spend your full card here and apply for the DPS Foundation\'s $1,000 grant. Aurora Public Schools families: ask us about the same plan.</p>', f)
Path(f).write_text(s, encoding='utf-8')

# ---------------------------------------------------------------- contact.html
f = 'contact.html'; s = Path(f).read_text(encoding='utf-8')
s = rep(s, '<tr><td>Monday – Friday</td><td>1:00 – 9:00 PM</td></tr>', '<tr><td>Monday – Friday</td><td>2:00 – 9:00 PM</td></tr>', f)
s = rep(s, '<p class="addr">Shoot 360 Denver<br>FieldhouseUSA<br>', f'<p class="addr">Shoot 360 Denver<br><a href="{FH}" target="_blank" rel="noopener">FieldhouseUSA</a><br>', f)
s = rep(s, 'destination=14200+E+Alameda+Ave,+Aurora,+CO+80012', f'destination={MAP_Q}', f)
s = rep(s, 'maps?q=14200+E+Alameda+Ave,+Aurora,+CO+80012&amp;output=embed', f'maps?q={MAP_Q}&amp;output=embed', f)
s = rep(s, '<p class="lead">Ten minutes from I-225 and Alameda. Park in the FieldhouseUSA lot and come through the main entrance.</p>',
        f'<p class="lead">Ten minutes from I-225 and Alameda, inside <a href="{FH}" target="_blank" rel="noopener">Aurora FieldhouseUSA</a>. Park in the FieldhouseUSA lot and come through the main entrance.</p>', f)
Path(f).write_text(s, encoding='utf-8')

# ---------------------------------------------------------------- faq.html
f = 'faq.html'; s = Path(f).read_text(encoding='utf-8')
s = rep(s, '<img class="hero-img" src="assets/img/coaching-girls.jpg" alt="" width="1024" height="839">', '<img class="hero-img hero-img-faq" src="assets/img/coaching-girls.jpg" alt="" width="1024" height="839">', f)
FQ02 = f'''<!-- [FQ-02] Questions — generated by scripts/patch_v04.py from its FAQ list, together with the FAQPage JSON-LD -->
<section class="sec faq-sec" aria-label="Frequently asked questions">
  {BALL_SVG}
  <div class="wrap">
    <nav class="faq-cats" aria-label="Question topics">{''.join(f'<a href="#{cid}">{label}</a>' for cid, label in FAQ_CATS)}</nav>
    <div class="faq">
{faq_html()}
    </div>
  </div>
</section>

'''
s = rep_re(s, r'<!-- \[FQ-02\].*?</section>\n\n', FQ02, f)
s = rep_re(s, r'\{"@type":"FAQPage".*?\]\}', faq_json(), f)
s = rep(s, 'Answers about Shoot 360 Denver: the evaluation session, coaching included, who it\'s for, what the Splash Meter measures, membership tiers and pricing, drop-ins, camps, the app, hours, parking and waivers.',
        'Answers about Shoot 360 Denver: the evaluation session, coaching included, who it\'s for, what the Splash Meter measures, JV to Ball is Life memberships, Unlimited Classes, drop-ins, My Spark Denver, camps, the app, hours, parking, events and waivers.', f)
Path(f).write_text(s, encoding='utf-8')

# ---------------------------------------------------------------- legal.html: Vimeo in the third-party services list
f = 'legal.html'; s = Path(f).read_text(encoding='utf-8')
s = rep(s, 'No Instagram login is involved.</p>', 'No Instagram login is involved.</p>\n    <h3>Vimeo video clips</h3>\n    <p>Two short training clips on the home and technology pages stream from Vimeo with Do Not Track enabled (<code>dnt=1</code>), which stops Vimeo from tracking the session or storing analytics cookies. Vimeo still receives standard request data from your browser to deliver the video; see <a href="https://vimeo.com/privacy" target="_blank" rel="noopener">Vimeo’s privacy policy</a>.</p>', f)
Path(f).write_text(s, encoding='utf-8')

# ---------------------------------------------------------------- sitemap
f = 'sitemap.xml'; s = Path(f).read_text(encoding='utf-8')
s = rep(s, '  <url><loc>https://www.shoot360denver.com/parties.html</loc><lastmod>2026-09-16</lastmod></url>\n',
        '  <url><loc>https://www.shoot360denver.com/events.html</loc><lastmod>2026-09-17</lastmod></url>\n  <url><loc>https://www.shoot360denver.com/publications.html</loc><lastmod>2026-09-17</lastmod></url>\n', f)
s = s.replace('<lastmod>2026-09-16</lastmod>', '<lastmod>2026-09-17</lastmod>')
Path(f).write_text(s, encoding='utf-8')

# ---------------------------------------------------------------- main.js
f = 'assets/js/main.js'; s = Path(f).read_text(encoding='utf-8')
s = rep(s, 'var SHARE={weekday:[[13,16,0.35],[16,21,0.85]], weekend:[[10,13,0.55],[13,17,0.70]]};', 'var SHARE={weekday:[[14,16,0.35],[16,21,0.85]], weekend:[[10,13,0.55],[13,17,0.70]]}; // v0.4: weekdays open 2 PM', f)
s = rep(s, "var tiers=[{name:'Pro · 8 visits',price:199,visits:8},{name:'Hall of Fame · unlimited',price:379,visits:null},{name:'All-Star · unlimited',price:389,visits:null}];",
        "var tiers=[{name:'Varsity · 8 sessions',price:189,visits:8},{name:'Committed · unlimited',price:229,visits:null},{name:'Ball is Life · unlimited, 12-month',price:220,visits:null}];", f)
JS4 = r'''
// ===== v0.4 =====================================================================
// Tabs (events page): <div class="tabs" role="tablist"><button role="tab" aria-controls="panelId">…  Panels: <section class="tabpanel" id="panelId">
// The URL hash picks the tab (events.html#parties), including a hash that points inside a panel (#takeover).
(function(){
  var tl=document.querySelector('.tabs[role=tablist]'); if(!tl)return;
  var tabs=[].slice.call(tl.querySelectorAll('[role=tab]'));
  var panels=tabs.map(function(t){return document.getElementById(t.getAttribute('aria-controls'));});
  function show(i,focus){tabs.forEach(function(t,j){var on=i===j;t.setAttribute('aria-selected',String(on));t.tabIndex=on?0:-1;if(panels[j]){panels[j].hidden=!on;if(on)panels[j].querySelectorAll('.reveal').forEach(function(el){el.classList.add('visible');});}});if(focus)tabs[i].focus();}
  tabs.forEach(function(t,i){
    t.addEventListener('click',function(){show(i);if(history.replaceState)history.replaceState(null,'','#'+panels[i].id);});
    t.addEventListener('keydown',function(e){var n=i;if(e.key==='ArrowRight')n=(i+1)%tabs.length;else if(e.key==='ArrowLeft')n=(i-1+tabs.length)%tabs.length;else if(e.key==='Home')n=0;else if(e.key==='End')n=tabs.length-1;else return;e.preventDefault();show(n,true);});
  });
  function fromHash(){
    var h=location.hash.replace('#',''), i=-1;
    if(h){var el=document.getElementById(h); var p=el&&(el.classList.contains('tabpanel')?el:el.closest('.tabpanel')); if(p)i=panels.indexOf(p); if(i>=0&&el!==p){show(i);setTimeout(function(){el.scrollIntoView();},0);return;}}
    show(i>=0?i:0);
  }
  window.addEventListener('hashchange',fromHash); fromHash();
})();
'''
s = s.split('\n// ===== v0.4 =====')[0].rstrip('\n') + '\n' + JS4   # re-runnable: the v0.4 block is always the script's current version
Path(f).write_text(s, encoding='utf-8')

# ---------------------------------------------------------------- styles.css
f = 'assets/css/styles.css'; s = Path(f).read_text(encoding='utf-8')
CSS4 = '''
/* ===== v0.4 additions ======================================================== */
/* 1. Partners: logos in a row, label under them, Nuggets 40% larger */
.trust .wrap{flex-direction:column;gap:16px}
.trust .logos{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:22px 56px}
.trust img.lg{height:42px}
/* 2. shots tracked in Splash Meter green; 8. BOOM letters yellow, value headings green; 9. facility stats red */
.counter .n{color:var(--meter)}
.value b{color:#F5C400}
.value h3{color:var(--meter)}
.stat b{color:var(--red-text)}
/* 3. how-it-works steps are links */
a.step{text-decoration:none;color:inherit;display:block;transition:border-color .18s,transform .18s}
a.step:hover{border-color:var(--grey-700);transform:translateY(-2px)}
.step .more{display:block;margin-top:12px;font-family:var(--display);font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--red-text);font-size:15px}
@media(prefers-reduced-motion:reduce){a.step:hover{transform:none}}
/* 4. Vimeo embeds, borderless */
.vimeo{position:relative;aspect-ratio:16/9;border-radius:var(--radius);overflow:hidden;background:#000;box-shadow:var(--shadow)}
.vimeo iframe{position:absolute;inset:0;width:100%;height:100%;border:0;display:block}
.vimeo .cap{position:absolute;left:14px;bottom:12px;font-family:var(--display);font-weight:600;letter-spacing:.08em;text-transform:uppercase;font-size:13px;color:#fff;background:rgba(0,0,0,.55);padding:4px 10px;border-radius:3px;pointer-events:none}
.vimeo-pair{display:grid;gap:14px}
/* 13. membership comparison table */
.cmp-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;border:1px solid #E2E2E2;border-radius:var(--radius);background:#fff}
.cmp{width:100%;border-collapse:collapse;font-size:14.5px;min-width:980px;color:var(--black)}
.cmp th,.cmp td{padding:10px 12px;border-bottom:1px solid #E6E6E6;text-align:center;vertical-align:middle}
.cmp thead th{font-family:var(--display);text-transform:uppercase;letter-spacing:.06em;font-size:15px;background:var(--black);color:#fff;line-height:1.15;padding:14px 12px}
.cmp thead th small{display:block;font-size:11px;letter-spacing:.08em;color:var(--grey-300);font-weight:600;margin-top:3px;text-transform:none}
.cmp th:first-child,.cmp td:first-child{text-align:left;position:sticky;left:0;background:#fff;font-weight:600;z-index:1;min-width:190px;box-shadow:1px 0 0 #E6E6E6}
.cmp thead th:first-child{background:var(--black)}
.cmp thead th.hot{background:var(--red)}
.cmp td.hot{background:#FFF4F5}
.cmp .y{color:var(--meter);font-weight:700;font-size:20px;line-height:1}
.cmp .n{color:#C4C4C4}
.cmp tr.price td{font-family:var(--display);font-weight:700;font-size:21px}
.cmp tr.price td:first-child{font-family:var(--body);font-size:14.5px}
.cmp tbody tr:last-child td{border-bottom:0}
.cmp td .tbd{font-size:.8em}
.cmp tr.price td small{display:block;font:600 12px/1.3 var(--body);color:var(--grey-700);margin-top:2px}
.bigprice{font-family:var(--display);font-weight:700;font-size:30px;line-height:1;margin:0 0 8px}
.bigprice small{font-size:14px;font-weight:600;color:var(--grey-500);margin-left:2px}
.sec-light .bigprice small{color:var(--grey-700)}
.cmp a{color:var(--red-dark);font-weight:700;text-decoration:none}
.cmp a:hover{text-decoration:underline}
/* 18. publications list */
.pubs{list-style:none;padding:0;margin:0;display:grid;gap:10px}
.pubs li{padding:14px 18px;border:1px solid var(--line);border-radius:var(--radius);background:var(--ink)}
.pubs .src{display:block;font-family:var(--display);font-weight:600;text-transform:uppercase;letter-spacing:.1em;font-size:12px;color:var(--grey-500);margin-bottom:2px}
.pubs a{font-weight:600;color:#fff;text-decoration:none}
.pubs a:hover{text-decoration:underline;color:var(--meter)}
.pubs p{margin:4px 0 0;color:var(--grey-300);font-size:15px}
.sec-light .pubs li{background:#fff;border-color:#E2E2E2}
.sec-light .pubs a{color:var(--black)}
.sec-light .pubs a:hover{color:var(--red-dark)}
.sec-light .pubs p{color:var(--grey-700)}
.review cite a{color:inherit;text-decoration:none}
.review cite a:hover{color:#fff;text-decoration:underline}
.panel p a{color:inherit;font-weight:600}
/* 15. tabs (events page) */
.tabs{display:flex;flex-wrap:wrap;gap:6px;border-bottom:1px solid var(--line);margin-bottom:32px}
.tabs [role=tab]{background:none;border:0;border-bottom:3px solid transparent;color:var(--grey-300);font:700 18px/1.2 var(--display);text-transform:uppercase;letter-spacing:.08em;padding:14px 18px;cursor:pointer;margin-bottom:-1px}
.tabs [role=tab]:hover,.tabs [role=tab][aria-selected=true]{color:#fff}
.tabs [role=tab][aria-selected=true]{border-bottom-color:var(--red)}
.tabpanel[hidden]{display:none}
.dates{display:flex;flex-wrap:wrap;gap:10px;list-style:none;padding:0;margin:14px 0 0}
.dates li{font-family:var(--display);font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:15px;border:1px solid var(--line);border-radius:999px;padding:8px 16px;background:var(--ink-2)}
/* 16. FAQ: hero crop shows heads; section gets a gradient, a basketball and topic chips */
.hero-img-faq{object-position:50% 20%}
.faq-sec{position:relative;overflow:hidden;background:radial-gradient(ellipse at 88% 8%,rgba(224,0,27,.30),transparent 46%),radial-gradient(ellipse at 0% 100%,rgba(34,212,120,.12),transparent 42%),var(--black)}
.faq-ball{position:absolute;right:-130px;top:110px;width:min(46vw,540px);height:auto;opacity:.16;pointer-events:none}
@media(max-width:900px){.faq-ball{right:-170px;top:auto;bottom:-90px;width:380px}}
.faq-sec .wrap{position:relative}
.faq-cats{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin:0 auto 30px;max-width:860px}
.faq-cats a{font-family:var(--display);font-weight:600;text-transform:uppercase;letter-spacing:.08em;font-size:14px;color:#fff;text-decoration:none;border:1px solid rgba(255,255,255,.22);border-radius:999px;padding:8px 16px;background:rgba(255,255,255,.05)}
.faq-cats a:hover{border-color:var(--red);background:rgba(224,0,27,.18)}
.faq-sec .faq-item{border-color:rgba(255,255,255,.14)}
.faq-sec .faq-item:target .faq-q{color:var(--meter)}
.faq-sec .faq-q{scroll-margin-top:90px}
'''
s = s.split('\n/* ===== v0.4 additions')[0].rstrip('\n') + '\n' + CSS4   # re-runnable, same as the JS block
Path(f).write_text(s, encoding='utf-8')

print('v0.4 patch applied to', ', '.join(p for p in PAGES if Path(p).exists()))
