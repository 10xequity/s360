"""v0.3 cross-cutting patch: navigation with Programs dropdown, red/white logo, New Membership CTA,
evaluation wording, bigger hours/phone text, image app badges, Splash Meter green, live shots model,
privacy/data section, sitemap. Exact anchors; re-runnable (skips replacements already present)."""
import re, os, glob
from pathlib import Path
os.chdir(r"C:\Users\vv58\AppData\Local\Temp\claude\c--\98c1dc28-f52e-48ff-b639-94d5a6d91319\scratchpad\shoot360-denver")

def rep(s, a, b, f, expect=1, atleast=False):
    if b in s and a not in s:
        return s
    n = s.count(a)
    ok = (n >= 1) if atleast else (n == expect)
    assert ok, (f, 'expected', 'at least 1' if atleast else expect, 'found', n, a[:90])
    return s.replace(a, b)

PAGES = ['index.html', 'technology.html', 'memberships.html', 'programs.html', 'parties.html', 'faq.html', 'contact.html', 'legal.html']
for f in PAGES:
    assert Path(f).exists(), f + ' must exist before the patch runs'

BADGES = ('<a class="badge-app" href="https://apps.apple.com/us/app/shoot-360/id1177068011" target="_blank" rel="noopener"><img src="assets/img/badge-appstore.svg" alt="Download on the App Store" width="120" height="40" loading="lazy"></a>'
          '<a class="badge-app" href="https://play.google.com/store/apps/details?id=com.Shoot360.Mobile" target="_blank" rel="noopener"><img src="assets/img/badge-googleplay.png" alt="Get it on Google Play" width="646" height="250" loading="lazy"></a>')
OLD_BADGE_A = '<a href="https://apps.apple.com/us/app/shoot-360/id1177068011" target="_blank" rel="noopener"><span>Download on the<b>App Store</b></span></a>'
OLD_BADGE_G = '<a href="https://play.google.com/store/apps/details?id=com.Shoot360.Mobile" target="_blank" rel="noopener"><span>Get it on<b>Google Play</b></span></a>'
GMAPS = 'https://maps.google.com/?cid=8030805088891520148'

def nav(cur):
    def a(href, label, key):
        ac = ' aria-current="page"' if key == cur else ''
        return f'<li><a href="{href}"{ac}>{label}</a></li>'
    sub_open = ' class="has-sub open-parent"' if cur == 'programs' else ' class="has-sub"'
    return f'''<!-- [NAV] -->
<header class="nav">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Shoot 360 Denver — home"><img src="assets/img/logo-red-white.png" alt="Shoot 360 Basketball" width="720" height="245"></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Open menu"><span></span>Menu</button>
    <nav aria-label="Primary">
      <ul id="primary-nav" class="nav-links">
        {a("technology.html", "Technology", "technology")}
        {a("memberships.html", "Memberships", "memberships")}
        <li{sub_open}>
          <button type="button" class="sub-toggle" aria-expanded="false" aria-controls="sub-programs">Programs</button>
          <ul id="sub-programs" class="sub">
            <li><a href="programs.html">All programs</a></li>
            <li><a href="programs.html#classes">Classes</a></li>
            <li><a href="programs.html#camps">Camps</a></li>
            <li><a href="programs.html#leagues">Leagues</a></li>
            <li><a href="https://www.teamevo.org/" target="_blank" rel="noopener">Basketball Club</a></li>
            <li><a href="mailto:info@shoot360denver.com?subject=Private%20training">Private Training</a></li>
          </ul>
        </li>
        {a("parties.html", "Parties", "parties")}
        {a("faq.html", "FAQ", "faq")}
        {a("contact.html", "Visit Us", "contact")}
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
      <div><h3>Visit</h3><ul><li>FieldhouseUSA<br>14200 E Alameda Ave<br>Aurora, CO 80012</li><li><a href="tel:+17202625501">720-262-5501</a></li><li><a href="mailto:info@shoot360denver.com">info@shoot360denver.com</a></li></ul></div>
      <div><h3>Hours</h3><ul><li>Mon – Fri: 1 – 9 PM</li><li>Sat – Sun: 10 AM – 5 PM</li><li>Homeschool: Mon – Fri 2 – 4 PM</li></ul></div>
      <div><h3>Explore</h3><ul><li><a href="technology.html">Technology</a></li><li><a href="memberships.html">Memberships</a></li><li><a href="programs.html">Programs</a></li><li><a href="parties.html">Birthday Parties</a></li><li><a href="faq.html">FAQ</a></li><li><a href="contact.html">Visit Us</a></li><li><a href="https://www.teamevo.org/" target="_blank" rel="noopener">Basketball Club — Team EVO</a></li><li><a href="https://www.instagram.com/shoot360denver/" target="_blank" rel="noopener">Instagram @shoot360denver</a></li><li><a href="https://www.facebook.com/shoot360denver" target="_blank" rel="noopener">Facebook</a></li><li><a href="{GMAPS}" target="_blank" rel="noopener">Reviews on Google</a></li></ul></div>
    </div>
    <div class="legal">
      <span>© 2026 Shoot 360 Denver. An independently owned and operated Shoot 360 location.</span>
      <span><a href="legal.html#privacy">Privacy</a> · <a href="legal.html#services">Data &amp; third-party services</a> · <a href="legal.html#disclaimer">Disclaimer</a> · <a href="legal.html#accessibility">Accessibility</a></span>
    </div>
  </div>
</footer>'''

KEY = {'index.html': 'home', 'technology.html': 'technology', 'memberships.html': 'memberships', 'programs.html': 'programs',
       'parties.html': 'parties', 'faq.html': 'faq', 'contact.html': 'contact', 'legal.html': 'legal'}

# ---------------------------------------------------------------- pages
for f in PAGES:
    p = Path(f); s = p.read_text(encoding='utf-8')
    s, n = re.subn(r'<!-- \[NAV\] -->.*?</header>', lambda m: nav(KEY[f]), s, count=1, flags=re.S); assert n == 1, (f, 'nav')
    s, n = re.subn(r'<!-- \[FT\] -->.*?</footer>', lambda m: FOOTER, s, count=1, flags=re.S); assert n == 1, (f, 'footer')
    s = s.replace(OLD_BADGE_A + '\n          ' + OLD_BADGE_G, BADGES).replace(OLD_BADGE_A + '\n        ' + OLD_BADGE_G, BADGES)
    s = s.replace(OLD_BADGE_A + OLD_BADGE_G, BADGES).replace(OLD_BADGE_A, BADGES.split('</a>')[0] + '</a>').replace(OLD_BADGE_G, BADGES.split('</a>')[1] + '</a>')
    s = s.replace('>Book a Free Workout</a>', '>Book an Evaluation</a>')
    s = s.replace('src="assets/img/logo-white.png"', 'src="assets/img/logo-red-white.png"')
    p.write_text(s, encoding='utf-8'); print(f, 'nav/footer/badges/cta regenerated')

# ---------------------------------------------------------------- wording: technology, contact, faq
p = Path('technology.html'); s = p.read_text(encoding='utf-8')
s = rep(s, '<h2 id="cta-h">Shoot on it for free</h2>', '<h2 id="cta-h">Shoot on it first</h2>', 'technology')
s = rep(s, 'Book a free evaluation workout and see your arc, depth and alignment on your first ten shots.', 'Book an evaluation workout and see your arc, depth and alignment on your first ten shots.', 'technology')
s = rep(s, '<section class="sec sec-light" aria-labelledby="ben-h">', '<section class="sec meter" aria-labelledby="ben-h">', 'technology')
p.write_text(s, encoding='utf-8'); print('technology wording + meter section')

p = Path('contact.html'); s = p.read_text(encoding='utf-8')
s = rep(s, 'For membership questions, the fastest route is the free evaluation: you meet a coach and see the technology in person.', 'For membership questions, the fastest route is an evaluation session: you meet a coach and see the technology in person.', 'contact')
s = rep(s, 'Membership questions are fastest answered at a free evaluation.', 'Membership questions are fastest answered at an evaluation.', 'contact')
s = rep(s, 'The free evaluation workout takes about an hour and costs nothing.', 'The evaluation workout takes about an hour.', 'contact')
s = rep(s, '<div id="ghl-contact" class="mt2" hidden><!-- GoHighLevel form embed goes here --></div>',
           '<div id="ghl-contact" class="mt2" hidden><!-- GoHighLevel form embed goes here --></div>\n    <p class="fine">Messages sent through this form are stored in Shoot 360 Denver\u2019s GoHighLevel account and used only to reply to you. <a href="legal.html#services">How we handle your data \u2192</a></p>', 'contact')
p.write_text(s, encoding='utf-8'); print('contact wording + data note')

p = Path('faq.html'); s = p.read_text(encoding='utf-8')
pairs = [
 ('Is the first workout really free?', 'How do I get started?'),
 ('Yes. The free workout is open to first-time visitors and local residents, valid at participating facilities; conditions apply. <a href="https://shoot360-prod.saloncloudsplus.io/ghl/athlete-info" target="_blank" rel="noopener">Book it online</a> and a coach meets you on the court.',
  '<a href="https://shoot360-prod.saloncloudsplus.io/ghl/athlete-info" target="_blank" rel="noopener">Book an evaluation session online</a> and a coach meets you on the court. Evaluations are for first-time visitors; a parent or guardian attends with minors.'),
 ('Yes. The free workout is open to first-time visitors and local residents, valid at participating facilities; conditions apply. Book it online and a coach meets you on the court.',
  'Book an evaluation session online and a coach meets you on the court. Evaluations are for first-time visitors; a parent or guardian attends with minors.'),
 ('What happens at the free evaluation?', 'What happens at the evaluation?'),
 ('Use the <strong>Book a Free Workout</strong> button on any page', 'Use the <strong>Book an Evaluation</strong> button on any page'),
 ('Use the Book a Free Workout button on any page', 'Use the Book an Evaluation button on any page'),
 ('when you book your free evaluation', 'when you book your evaluation'),
 ('The free evaluation answers most questions in the first ten minutes.', 'An evaluation session answers most questions in the first ten minutes.'),
 ('<a href="programs.html#memberships">Compare tiers \u2192</a>', '<a href="memberships.html#tiers">Compare tiers \u2192</a>'),
 ('<a href="programs.html#policies">Membership policies \u2192</a>', '<a href="memberships.html#policies">Membership policies \u2192</a>'),
 ('<a href="programs.html#coaching">How coaching works \u2192</a>', '<a href="memberships.html#coaching">How coaching works \u2192</a>'),
]
for a, b in pairs:
    s = rep(s, a, b, 'faq', atleast=True)
new_html = '''<div class="faq-item"><button class="faq-q" type="button">How do I register for classes, camps and leagues?</button><div class="faq-a"><p>In the Shoot 360 app, for members and non-members alike. Download it, create your athlete profile, and register from the schedule; drop-in sessions are booked the same way when space permits. <a href="programs.html#app">Get the app \u2192</a></p></div></div>
      <div class="faq-item"><button class="faq-q" type="button">Do you offer private training?</button><div class="faq-a"><p>Yes. Coaching is already included in every membership; for dedicated one-on-one blocks beyond that, email <a href="mailto:info@shoot360denver.com?subject=Private%20training">info@shoot360denver.com</a> with the athlete\u2019s age, level and availability.</p></div></div>
      <div class="faq-item"><button class="faq-q" type="button">Do I need to sign a waiver?</button>'''
s = rep(s, '<div class="faq-item"><button class="faq-q" type="button">Do I need to sign a waiver?</button>', new_html, 'faq')
new_json = '''{"@type":"Question","name":"How do I register for classes, camps and leagues?","acceptedAnswer":{"@type":"Answer","text":"In the Shoot 360 app, for members and non-members alike. Download it, create your athlete profile, and register from the schedule; drop-in sessions are booked the same way when space permits."}},
{"@type":"Question","name":"Do you offer private training?","acceptedAnswer":{"@type":"Answer","text":"Yes. Coaching is already included in every membership; for dedicated one-on-one blocks beyond that, email info@shoot360denver.com with the athlete's age, level and availability."}},
{"@type":"Question","name":"Do I need to sign a waiver?"'''
s = rep(s, '{"@type":"Question","name":"Do I need to sign a waiver?"', new_json, 'faq')
p.write_text(s, encoding='utf-8'); print('faq wording + 2 questions')

# ---------------------------------------------------------------- legal: data & services section
p = Path('legal.html'); s = p.read_text(encoding='utf-8')
services = '''<!-- [LG-05] Data & third-party services -->
<section class="sec" id="services" aria-labelledby="sv-h">
  <div class="wrap prose">
    <h2 id="sv-h">Data and third-party services</h2>
    <p><em>Added September 16, 2026.</em> This is a static website: it sets no cookies of its own, runs no advertising trackers, and hosts its own fonts, images and videos. The services below are the only places your information can go from this site, and each is used only for the purpose stated.</p>
    <h3>Booking an evaluation or joining</h3>
    <p>The <strong>Book an Evaluation</strong> buttons and every membership <strong>Join</strong> button take you to Shoot 360\u2019s membership system (shoot360.com and its SalonCloud Plus scheduler), operated by Shoot 360 LLC. Name, contact details, athlete details and payment information are collected there under <a href="https://www.shoot360.com/privacy-policy" target="_blank" rel="noopener">Shoot 360\u2019s privacy policy</a>. This website never sees your payment details.</p>
    <h3>Contact and party request forms</h3>
    <p>Forms on the Visit Us and Parties pages are provided by GoHighLevel (LeadConnector). What you type, typically name, email, phone and your message, is stored in Shoot 360 Denver\u2019s GoHighLevel account and used to reply to you and, if you opt in, to send you updates. See <a href="https://www.gohighlevel.com/privacy-policy" target="_blank" rel="noopener">GoHighLevel\u2019s privacy policy</a>. Reply STOP to any text or use the unsubscribe link in any email to opt out.</p>
    <h3>The Shoot 360 app</h3>
    <p>Class, camp, league and drop-in registration happens in the Shoot 360 app, published by Shoot 360 LLC. Its data practices are described in the App Store and Google Play listings and in Shoot 360\u2019s privacy policy.</p>
    <h3>Google Maps and Google reviews</h3>
    <p>The map on the home and Visit Us pages is an embedded Google Map. When it loads, Google receives your IP address and may set cookies under <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google\u2019s privacy policy</a>. \u201cRead reviews\u201d and \u201cWrite a review\u201d links open Google Maps in a new tab.</p>
    <h3>Instagram feed</h3>
    <p>When the Instagram section is active it is rendered by Behold, which fetches public posts from @shoot360denver. Behold receives standard request data from your browser; see <a href="https://behold.so/privacy" target="_blank" rel="noopener">Behold\u2019s privacy policy</a>. No Instagram login is involved.</p>
    <h3>Calculator and counter</h3>
    <p>The savings calculator runs entirely in your browser; nothing you enter is sent anywhere. The shots counter on the home page is an estimate computed from the facility\u2019s court count and opening hours, not a feed of any athlete\u2019s data.</p>
    <h3>Hosting and analytics</h3>
    <p>The site is served by GitHub Pages, which keeps standard server logs (IP address, pages requested) under <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">GitHub\u2019s privacy statement</a>. No analytics are active today. If Google Analytics or Cloudflare Web Analytics is switched on, this section will say so and, for Google Analytics, a cookie notice will be added.</p>
    <h3>Children</h3>
    <p>Many of our athletes are minors, but this website is written for parents and guardians. Forms and registrations should be completed by an adult, and a parent or guardian signs the participation disclaimer for every minor.</p>
    <h3>Your choices and questions</h3>
    <p>To see, correct or delete information you gave us through a form, or to opt out of messages, email <a href="mailto:info@shoot360denver.com">info@shoot360denver.com</a> or call <a href="tel:+17202625501">720-262-5501</a>. Requests about membership or app data go to Shoot 360 LLC via <a href="https://www.shoot360.com/contact" target="_blank" rel="noopener">shoot360.com/contact</a>.</p>
  </div>
</section>

<!-- [LG-03] Disclaimer -->'''
s = rep(s, '<!-- [LG-03] Disclaimer -->', services, 'legal')
s = rep(s, '<section class="sec" id="disclaimer" aria-labelledby="dc-h">', '<section class="sec sec-ink" id="disclaimer" aria-labelledby="dc-h">', 'legal')
s = rep(s, '<section class="sec sec-ink" id="accessibility" aria-labelledby="ac-h">', '<section class="sec" id="accessibility" aria-labelledby="ac-h">', 'legal')
s = rep(s, '<a href="#privacy">Privacy policy</a> \u00b7 <a href="#disclaimer">Participation disclaimer</a>', '<a href="#privacy">Privacy policy</a> \u00b7 <a href="#services">Data &amp; third-party services</a> \u00b7 <a href="#disclaimer">Participation disclaimer</a>', 'legal')
s = rep(s, '<p><em>Last updated: April 17, 2024</em></p>', '<p><em>Policy text adopted from Shoot 360\u2019s network policy, last updated April 17, 2024. The <a href="#services">Data and third-party services</a> section below describes this website specifically.</em></p>', 'legal')
s = rep(s, '<meta name="description" content="Shoot 360 Denver privacy policy, participation disclaimer for adults and minors, and accessibility statement.">',
           '<meta name="description" content="Shoot 360 Denver privacy policy, what data each third-party service on this site collects, participation disclaimer for adults and minors, and accessibility statement.">', 'legal')
p.write_text(s, encoding='utf-8'); print('legal: services section')

# ---------------------------------------------------------------- CSS
p = Path('assets/css/styles.css'); s = p.read_text(encoding='utf-8')
s = rep(s, '@media(max-width:900px){\n  .nav-toggle{display:block}', '@media(max-width:1024px){\n  .nav-toggle{display:block}', 'css')
s = rep(s, 'text-transform:uppercase;font-size:14px;color:var(--grey-300)}\n.hero-meta strong{color:#fff}', 'text-transform:uppercase;font-size:18px;color:var(--grey-300)}\n.hero-meta strong{color:#fff}', 'css')
s = rep(s, '.hours{width:100%;border-collapse:collapse;font-size:16px}', '.hours{width:100%;border-collapse:collapse;font-size:18px}', 'css')
s = rep(s, '.addr{font-size:17px;line-height:1.5}', '.addr{font-size:19px;line-height:1.5}', 'css')
s = rep(s, '.ft{background:#050505;border-top:1px solid var(--line);padding:56px 0 28px;font-size:15px;color:var(--grey-300)}', '.ft{background:#050505;border-top:1px solid var(--line);padding:56px 0 28px;font-size:17px;color:var(--grey-300)}', 'css')
s = rep(s, '.ft li{margin:0 0 8px}', '.ft li{margin:0 0 10px}', 'css')
s = rep(s, '.ft h3{font-size:15px;letter-spacing:.14em;color:var(--grey-500);margin:0 0 12px}', '.ft h3{font-size:16px;letter-spacing:.14em;color:var(--grey-500);margin:0 0 12px}', 'css')
s = rep(s, '  --red:#E0001B; --red-text:#FF2A3C; --red-dark:#C20101; --red-brand:#EF001D;', '  --red:#E0001B; --red-text:#FF2A3C; --red-dark:#C20101; --red-brand:#EF001D; --meter:#22D478;', 'css')
s += '''
/* ===== v0.3 additions ======================================================== */
/* Programs dropdown */
.has-sub{position:relative}
.sub-toggle{background:none;border:0;color:var(--grey-300);font:600 16px/1.6 var(--display);text-transform:uppercase;letter-spacing:.08em;padding:10px 12px;cursor:pointer;border-radius:4px;display:inline-flex;align-items:center;gap:7px}
.sub-toggle::after{content:"";width:7px;height:7px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(45deg) translateY(-3px)}
.sub-toggle:hover,.sub-toggle[aria-expanded="true"],.open-parent .sub-toggle{color:#fff}
.open-parent .sub-toggle{box-shadow:inset 0 -3px 0 var(--red)}
.sub{list-style:none;margin:0;padding:8px 0;position:absolute;top:100%;left:0;min-width:230px;background:var(--ink);border:1px solid var(--line);border-radius:6px;box-shadow:var(--shadow);display:none;z-index:120}
.has-sub:hover .sub,.has-sub:focus-within .sub,.has-sub .sub-toggle[aria-expanded="true"]+.sub{display:block}
.sub li a{padding:10px 16px;font-size:15px;letter-spacing:.06em;white-space:nowrap}
.nav-links .nav-cta{margin-left:26px}
.nav-links .nav-cta .btn{margin-left:0}
@media(max-width:1024px){
  .has-sub .sub,.has-sub:hover .sub,.has-sub:focus-within .sub{position:static;display:none;border:0;box-shadow:none;background:transparent;padding:0 0 6px 14px;min-width:0}
  .has-sub .sub-toggle[aria-expanded="true"]+.sub{display:block}
  .sub-toggle{width:100%;justify-content:space-between;padding:14px 8px;font-size:18px}
  .nav-links .nav-cta{margin:10px 0 0}
}
/* Image app badges */
.badges .badge-app{background:none;border:0;padding:0;display:inline-flex;align-items:center}
.badges .badge-app img{height:44px;width:auto;display:block}
.badges .badge-app img[src$="badge-googleplay.png"]{height:66px;margin:-11px -8px}
.ft-app{font-size:15px;color:var(--grey-500)}
/* Register-in-the-app strip */
.appnote{display:flex;flex-wrap:wrap;align-items:center;gap:14px 22px;background:var(--ink);border:1px solid var(--line);border-radius:var(--radius);padding:16px 20px;margin-top:18px}
.appnote p{margin:0;color:var(--grey-300);font-size:15.5px}
.appnote strong{color:#fff;font-family:var(--display);text-transform:uppercase;letter-spacing:.04em}
.sec-light .appnote{background:#fff;border-color:#E2E2E2}
.sec-light .appnote p{color:var(--grey-700)}
.sec-light .appnote strong{color:var(--black)}
/* Splash Meter green for the technology benefits */
.meter .benefit .k,.meter .benefit h3{color:var(--meter)}
.sec-light .benefit{background:#fff;border-color:#E2E2E2}
.sec-light .benefit h3{color:var(--black)}
.sec-light .benefit p{color:var(--grey-700)}
/* MySpark banner */
.spark{background:#143E7B;color:#fff;border-bottom:1px solid rgba(255,255,255,.15)}
.spark-cta{display:flex;flex-wrap:wrap;align-items:center;gap:18px 28px;padding:16px 0;text-decoration:none;color:inherit}
.spark-cta img{height:64px;width:auto;border-radius:4px}
.spark-cta .t{flex:1;min-width:240px}
.spark-cta strong{display:block;font-family:var(--display);font-weight:700;text-transform:uppercase;letter-spacing:.03em;font-size:22px;line-height:1.1}
.spark-cta span.s{color:rgba(255,255,255,.85);font-size:16px}
.spark-cta .btn-ghost{border-color:#fff}
.spark-cta:hover .btn-ghost{background:#fff;color:#143E7B}
/* Live counter label */
.counter .l small{display:block;margin-top:6px;letter-spacing:.08em;font-size:12px;color:var(--grey-500);text-transform:none;font-family:var(--body);font-weight:400}
'''
p.write_text(s, encoding='utf-8'); print('css: dropdown, sizes, badges, meter, spark, counter')

# ---------------------------------------------------------------- JS
p = Path('assets/js/main.js'); s = p.read_text(encoding='utf-8')
if 'Programs dropdown' not in s:
    s += '''
// ===== v0.3 =====================================================================
// Programs dropdown: click toggles (touch + keyboard); CSS handles hover on desktop.
(function(){
  var items=document.querySelectorAll('.has-sub'); if(!items.length)return;
  items.forEach(function(li){
    var b=li.querySelector('.sub-toggle'); if(!b)return;
    b.addEventListener('click',function(e){e.stopPropagation();var o=b.getAttribute('aria-expanded')==='true';b.setAttribute('aria-expanded',String(!o));});
    li.addEventListener('keydown',function(e){if(e.key==='Escape'){b.setAttribute('aria-expanded','false');b.focus();}});
  });
  document.addEventListener('click',function(){items.forEach(function(li){var b=li.querySelector('.sub-toggle');if(b)b.setAttribute('aria-expanded','false');});});
})();

// Live shots estimate (#shots). Baseline count at a fixed moment, plus a model of shots taken since,
// during opening hours only. Every visitor sees the same number at the same instant.
//   4 shooting bays x 300 shots per 30-minute session = 600 shots per bay-hour when a bay is busy.
//   Utilisation shares below are the tuning knobs (prime time evenings and weekends are busier).
(function(){
  var el=document.getElementById('shots'); if(!el)return;
  var BASE=375000, EPOCH=Date.UTC(2026,8,16,6,0,0); // 375,000 shots as of 2026-09-16 00:00 America/Denver (UTC-6)
  var BAYS=4, PER_BAY_HOUR=600;
  var SHARE={weekday:[[13,16,0.35],[16,21,0.85]], weekend:[[10,13,0.55],[13,17,0.70]]}; // [open hour, close hour, share of bays busy]
  var fmt=new Intl.DateTimeFormat('en-US',{timeZone:'America/Denver',hour12:false,weekday:'short',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',second:'2-digit'});
  function parts(ms){var o={};fmt.formatToParts(new Date(ms)).forEach(function(x){o[x.type]=x.value});o.h=(+o.hour%24)+(+o.minute)/60+(+o.second)/3600;o.we=(o.weekday==='Sat'||o.weekday==='Sun');return o;}
  function rateAt(p){var bands=p.we?SHARE.weekend:SHARE.weekday;for(var i=0;i<bands.length;i++){if(p.h>=bands[i][0]&&p.h<bands[i][1])return bands[i][2]*BAYS*PER_BAY_HOUR;}return 0;}
  function dayTotal(we,upToHour){var bands=we?SHARE.weekend:SHARE.weekday,t=0;bands.forEach(function(b){var end=Math.min(b[1],upToHour);if(end>b[0])t+=(end-b[0])*b[2]*BAYS*PER_BAY_HOUR;});return t;}
  function estimate(now){
    var total=0, dayMs=86400000, t=EPOCH;
    // full days from the epoch up to yesterday (Denver), then today's partial
    var today=parts(now), key=function(p){return p.year+p.month+p.day;};
    while(key(parts(t))!==key(today)){total+=dayTotal(parts(t+12*3600000).we,24);t+=dayMs;}
    total+=dayTotal(today.we,today.h);
    return BASE+total;
  }
  var rm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  function render(){var now=Date.now();el.textContent=Math.floor(estimate(now)).toLocaleString('en-US');var live=rateAt(parts(now))>0;el.setAttribute('data-live',live?'1':'0');}
  render(); if(!rm) setInterval(render,1000); else setInterval(render,60000);
})();
'''
    p.write_text(s, encoding='utf-8'); print('js: dropdown + live shots model')

# ---------------------------------------------------------------- sitemap
p = Path('sitemap.xml'); s = p.read_text(encoding='utf-8')
s = rep(s, '  <url><loc>https://www.shoot360denver.com/programs.html</loc>', '  <url><loc>https://www.shoot360denver.com/memberships.html</loc><lastmod>2026-09-16</lastmod></url>\n  <url><loc>https://www.shoot360denver.com/programs.html</loc>', 'sitemap')
p.write_text(s, encoding='utf-8'); print('sitemap: memberships added')

# ---------------------------------------------------------------- report leftover "free" wording
for f in PAGES:
    h = re.sub(r'<!--.*?-->', '', Path(f).read_text(encoding='utf-8'), flags=re.S)
    hits = [m.group(0) for m in re.finditer(r'.{40}\bfree\b.{40}', h, re.I)]
    if hits: print('  FREE in', f, len(hits)); [print('     …' + x + '…') for x in hits[:6]]
print('PATCH v0.3 OK')
