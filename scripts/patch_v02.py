"""v0.2 multi-page patch. Exact-anchor replacements; every anchor must match exactly once or the script throws."""
from pathlib import Path
import os
os.chdir(r"C:\Users\vv58\AppData\Local\Temp\claude\c--\98c1dc28-f52e-48ff-b639-94d5a6d91319\scratchpad\shoot360-denver")
GMAPS = 'https://maps.google.com/?cid=8030805088891520148'
WRONG = '8031246155164271764'

def rep(s, a, b, f, expect=1):
    if b in s:  # already applied (script is re-runnable)
        return s
    n = s.count(a)
    assert n == expect, (f, 'expected', expect, 'found', n, a[:80])
    return s.replace(a, b)

# 1. correct the Google listing id in the two pages written with the wrong decimal
for f in ['parties.html', 'programs.html']:
    p = Path(f); s = p.read_text(encoding='utf-8'); n = s.count(WRONG)
    if n: p.write_text(s.replace(WRONG, '8030805088891520148'), encoding='utf-8')
    print(f, 'cid fixed x', n)

# 2. nav + footer + sameAs on the four pages not rewritten
for f in ['technology.html', 'faq.html', 'contact.html', 'legal.html']:
    p = Path(f); s = p.read_text(encoding='utf-8')
    s = rep(s, '<li><a href="programs.html">Programs &amp; Pricing</a></li>\n        <li><a href="faq.html"',
               '<li><a href="programs.html">Programs &amp; Pricing</a></li>\n        <li><a href="parties.html">Parties</a></li>\n        <li><a href="faq.html"', f)
    s = rep(s, '<li><a href="programs.html">Programs &amp; Pricing</a></li><li><a href="faq.html">FAQ</a></li>',
               '<li><a href="programs.html">Programs &amp; Pricing</a></li><li><a href="parties.html">Birthday Parties</a></li><li><a href="faq.html">FAQ</a></li>', f)
    FB = 'Visit Us</a></li><li><a href="https://www.instagram.com/shoot360denver/" target="_blank" rel="noopener">Instagram @shoot360denver</a></li><li><a href="https://www.facebook.com/shoot360denver" target="_blank" rel="noopener">Facebook</a></li></ul></div>'
    s = rep(s, FB, FB.replace('Facebook</a></li></ul></div>', 'Facebook</a></li><li><a href="' + GMAPS + '" target="_blank" rel="noopener">Reviews on Google</a></li></ul></div>'), f)
    if f != 'legal.html':
        s = rep(s, '"https://www.facebook.com/shoot360denver"],"parentOrganization"',
                   '"https://www.facebook.com/shoot360denver","' + GMAPS + '"],"parentOrganization"', f)
    p.write_text(s, encoding='utf-8'); print(f, 'nav/footer patched')

# 3. technology: benefits section before the clips
p = Path('technology.html'); s = p.read_text(encoding='utf-8')
ben = '''<!-- [TC-BEN] Benefits -->
<section class="sec sec-light" aria-labelledby="ben-h">
  <div class="wrap">
    <p class="eyebrow">Why it works</p>
    <h2 id="ben-h">What the technology does for a player</h2>
    <div class="benefits mt2">
      <div class="benefit reveal"><span class="k">Objective</span><h3>Feedback you cannot argue with</h3><p>Arc, depth and alignment are measured, not eyeballed. A player stops guessing why a shot missed and starts fixing the one thing the meter shows.</p></div>
      <div class="benefit reveal"><span class="k">300+</span><h3>More reps, each one corrected</h3><p>Automatic rebounding means 300 or more shots in 30 minutes. Skill is repetition with correction, and this is the most correction per rep a player can get.</p></div>
      <div class="benefit reveal"><span class="k">Faster</span><h3>Muscle memory built on the right motion</h3><p>Real-time feedback lets an athlete adjust mid-session, so the pattern that gets grooved is the correct one, instead of a bad habit reinforced for a season.</p></div>
      <div class="benefit reveal"><span class="k">Both hands</span><h3>Ball skills measured, not assumed</h3><p>The skill courts time reaction, score passing accuracy with each hand and grade body position. Weak-hand work becomes a number that moves.</p></div>
      <div class="benefit reveal"><span class="k">Gamified</span><h3>Kids want to come back</h3><p>Leaderboards, achievements and virtual competition across the network turn drills into games. Consistency is the whole battle in youth development.</p></div>
      <div class="benefit reveal"><span class="k">Coached</span><h3>A coach reads the data with you</h3><p>The technology shows what happened; the coach shows why and what to change. At Shoot 360 Denver that coaching is included in every membership.</p></div>
    </div>
  </div>
</section>

<!-- [TC-06] Clips -->'''
s = rep(s, '<!-- [TC-06] Clips -->', ben, 'technology.html'); p.write_text(s, encoding='utf-8'); print('technology benefits inserted')

# 4. faq: five new questions (html + schema), inserted before the waiver question
p = Path('faq.html'); s = p.read_text(encoding='utf-8')
new_html = '''<div class="faq-item"><button class="faq-q" type="button">Is coaching extra?</button><div class="faq-a"><p>No. Every Shoot 360 Denver membership includes private training and coaching. A coach works with you during your sessions at no additional fee; Pro, All-Star and Hall of Fame add scheduled one-on-one sessions on top. <a href="programs.html#coaching">How coaching works →</a></p></div></div>
      <div class="faq-item"><button class="faq-q" type="button">Do you host birthday parties?</button><div class="faq-a"><p>Yes. Three packages for up to 20 athletes: private time on the shooting and skill courts, a coach running the games, a Splash Meter shooting contest with a leaderboard finish, and table time for food and cake. <a href="parties.html">Party packages →</a></p></div></div>
      <div class="faq-item"><button class="faq-q" type="button">Do you have homeschool sessions?</button><div class="faq-a"><p>Yes. Homeschool sessions run Monday to Friday, 2 to 4 PM. Members use their regular visits; non-members pay the guest rate or use a 12-visit pack. <a href="programs.html#homeschool">Homeschool details →</a></p></div></div>
      <div class="faq-item"><button class="faq-q" type="button">Is there a family discount?</button><div class="faq-a"><p>Yes. Households with more than one athlete get a discount on the second and later memberships. Ask for current family pricing at the front desk or when you book your free evaluation.</p></div></div>
      <div class="faq-item"><button class="faq-q" type="button">Can I pause my membership?</button><div class="faq-a"><p>Yes. Memberships can be suspended for injury, travel or a tournament season; ask the front desk for the current terms and notice period. <a href="programs.html#policies">Membership policies →</a></p></div></div>
      <div class="faq-item"><button class="faq-q" type="button">Do I need to sign a waiver?</button>'''
s = rep(s, '<div class="faq-item"><button class="faq-q" type="button">Do I need to sign a waiver?</button>', new_html, 'faq.html')
new_json = '''{"@type":"Question","name":"Is coaching extra?","acceptedAnswer":{"@type":"Answer","text":"No. Every Shoot 360 Denver membership includes private training and coaching. A coach works with you during your sessions at no additional fee; Pro, All-Star and Hall of Fame add scheduled one-on-one sessions on top."}},
{"@type":"Question","name":"Do you host birthday parties?","acceptedAnswer":{"@type":"Answer","text":"Yes. Three packages for up to 20 athletes: private time on the shooting and skill courts, a coach running the games, a Splash Meter shooting contest with a leaderboard finish, and table time for food and cake."}},
{"@type":"Question","name":"Do you have homeschool sessions?","acceptedAnswer":{"@type":"Answer","text":"Yes. Homeschool sessions run Monday to Friday, 2 to 4 PM. Members use their regular visits; non-members pay the guest rate or use a 12-visit pack."}},
{"@type":"Question","name":"Is there a family discount?","acceptedAnswer":{"@type":"Answer","text":"Yes. Households with more than one athlete get a discount on the second and later memberships. Ask for current family pricing at the front desk or when you book your free evaluation."}},
{"@type":"Question","name":"Can I pause my membership?","acceptedAnswer":{"@type":"Answer","text":"Yes. Memberships can be suspended for injury, travel or a tournament season; ask the front desk for the current terms and notice period."}},
{"@type":"Question","name":"Do I need to sign a waiver?"'''
s = rep(s, '{"@type":"Question","name":"Do I need to sign a waiver?"', new_json, 'faq.html')
s = rep(s, '<title>FAQ — Free Workout, Memberships, Hours | Shoot 360 Denver</title>', '<title>FAQ — Free Workout, Memberships, Parties, Hours | Shoot 360 Denver</title>', 'faq.html')
p.write_text(s, encoding='utf-8'); print('faq: 5 questions added')

# 5. contact: GoHighLevel inquiry-form slot
p = Path('contact.html'); s = p.read_text(encoding='utf-8')
form = '''<!-- [CT-FORM] General inquiry form — GoHighLevel embed. Paste the GHL embed code inside #ghl-contact and remove the hidden attribute. -->
<section class="sec sec-ink" id="inquiry" aria-labelledby="inq-h">
  <div class="wrap">
    <p class="eyebrow">Send a message</p>
    <h2 id="inq-h">Questions? Ask here</h2>
    <div id="ghl-contact" class="mt2" hidden><!-- GoHighLevel form embed goes here --></div>
    <div class="callout mt2">
      <div><strong>Online form coming</strong><p>Until it is live, email <a href="mailto:info@shoot360denver.com">info@shoot360denver.com</a> or call <a href="tel:+17202625501">720-262-5501</a>. Membership questions are fastest answered at a free evaluation.</p></div>
      <a class="btn btn-primary" href="mailto:info@shoot360denver.com">Email us</a>
    </div>
  </div>
</section>

<!-- [CT-03] Social + app -->'''
s = rep(s, '<!-- [CT-03] Social + app -->', form, 'contact.html'); p.write_text(s, encoding='utf-8'); print('contact form slot inserted')

# 6. sitemap
p = Path('sitemap.xml'); s = p.read_text(encoding='utf-8')
s = rep(s, '  <url><loc>https://www.shoot360denver.com/faq.html</loc>',
           '  <url><loc>https://www.shoot360denver.com/parties.html</loc><lastmod>2026-09-16</lastmod></url>\n  <url><loc>https://www.shoot360denver.com/faq.html</loc>', 'sitemap')
p.write_text(s, encoding='utf-8'); print('sitemap: parties added')
# 7. footer headings h4 -> h3 (Lighthouse heading-order); the footer is the only place h4 is used
import glob
for f in sorted(glob.glob('*.html')):
    p = Path(f); s = p.read_text(encoding='utf-8'); n = s.count('<h4>')
    if n: p.write_text(s.replace('<h4>', '<h3>').replace('</h4>', '</h3>'), encoding='utf-8')
    print(f, 'footer headings fixed x', n)
p = Path('assets/css/styles.css'); s = p.read_text(encoding='utf-8')
s = rep(s, '.ft h4{', '.ft h3{', 'styles.css'); p.write_text(s, encoding='utf-8'); print('css .ft h3')
print('PATCH OK')
