"""Update the Denver Gap Ledger artifact for site v0.2: statuses, new rows, tiles, headline."""
from pathlib import Path
p = Path(r"C:\Users\vv58\AppData\Local\Temp\claude\c--\98c1dc28-f52e-48ff-b639-94d5a6d91319\scratchpad\shoot360-gap-report.html")
s = p.read_text(encoding='utf-8')

def rep(a, b, expect=1):
    global s
    n = s.count(a); assert n == expect, (expect, n, a[:90]); s = s.replace(a, b)

# Rows whose status changed in v0.2
rep("""v01:'Phone, email and the booking button. A static site needs a form backend: Google Form, GoHighLevel embed or Formspree',note:'Owner picks the backend.'},""",
    """v01:'GoHighLevel chosen. Embed slots are in place on the contact page and the party page; the owner pastes the GHL embed code and removes one hidden attribute',note:'Waiting on the GHL embed code from the owner.'},""")
rep("""cat:'Trust',built:0,flag:1,alt:0,st:'Needs owner',
  wix:'None',v01:'Not built. Three real quotes with a number in each, plus the Google Business Profile link. No franchise embeds a live rating; doing so would be a first',note:'Owner supplies quotes and the Google profile link.'},""",
    """cat:'Trust',built:1,flag:0,alt:0,st:'Built',
  wix:'None',v01:'Google Business listing connected: 4.7-star badge, "Read reviews" and "Write a review" links, listing added to the site\\u2019s search data. Quotes stay off the page unless Google has good ones to feature',note:'Review text needs the owner\\u2019s Business Profile login; the public listing hides it.'},""")
rep("""cat:'Programs',built:0,flag:1,alt:0,st:'Needs owner',
  wix:'None',v01:'Not published. Only a "bringing a team?" phone prompt. Parties are sold on 15 of 19 sites and rentals on 8',note:'Owner decides what Denver actually sells.'},""",
    """cat:'Programs',built:1,flag:1,alt:0,st:'Built',
  wix:'None',v01:'Owner confirmed parties. New parties page: three packages, how it works, party FAQ, request-a-date section with a GHL slot. Home and programs link to it',note:'Prices, athlete caps and durations are yellow placeholders until the owner supplies them.'},""")
rep("""cat:'Trust',built:0,flag:0,alt:1,st:'Skipped',
  wix:'Wix Instagram app',v01:'Links only. A feed needs the same edge worker used on coloradoboom.com; reuse it if wanted'}""",
    """cat:'Trust',built:1,flag:1,alt:0,st:'Built',
  wix:'Wix Instagram app',v01:'Instagram section on home wired for a Behold feed (the vendor coloradoboom.com already uses). Grid stays hidden until the feed id is set; follow button shows meanwhile',note:'Needs a Behold feed id for @shoot360denver from the owner\\u2019s Behold account.'}""")

# New rows for v0.2 additions, appended before the closing bracket of DATA
new_rows = """,
 {t:'Coaching included in every membership, stated plainly',sc:0,p:1,cat:'Conversion',built:1,flag:0,alt:0,st:'Built',
  wix:'Not mentioned',v01:'Owner directive. Dedicated section on programs, tier bullets reworded, hero and FAQ updated: a coach is on the floor every session at no extra fee; upper tiers add scheduled one-on-ones'},
 {t:'Savings calculator: private trainer vs membership',sc:1,p:2,cat:'Conversion',built:1,flag:0,alt:0,st:'Built',
  wix:'None',v01:'Interactive calculator on programs. Visitor sets trainer rate and sessions per month; it shows the monthly saving against Pro, Hall of Fame and All-Star'},
 {t:'Live shots-tracked counter',sc:1,p:3,cat:'Trust',built:1,flag:1,alt:0,st:'Built',
  wix:'None',v01:'Count-up counter on home, same mechanism Huntsville uses (a hand-set number, no data feed exists)',note:'Owner supplies the current total from the Shoot 360 dashboard.'},
 {t:'Homeschool daytime sessions',sc:2,p:2,cat:'Programs',built:1,flag:0,alt:0,st:'Built',
  wix:'None',v01:'Owner directive: weekdays 2\\u20134 PM. Section on programs, line in the hours tables, FAQ entry, home card'},
 {t:'Family discounts',sc:2,p:2,cat:'Conversion',built:1,flag:1,alt:0,st:'Built',
  wix:'None',v01:'Family callout under the tiers, FAQ entry, mention on home and homeschool sections',note:'Discount percentages are placeholders until the owner supplies them.'},
 {t:'Published membership pause / suspension policy',sc:2,p:2,cat:'Trust',built:1,flag:1,alt:0,st:'Built',
  wix:'None',v01:'Policies section on programs: pausing, commitments, coaching sessions, in plain words. FAQ entry',note:'Months, monthly fee and notice period are placeholders until the owner supplies them.'},
 {t:'Benefits copy: what the technology does for a player',sc:0,p:2,cat:'Conversion',built:1,flag:0,alt:0,st:'Built',
  wix:'Feature descriptions only',v01:'Six-point benefits grid on the technology page and a three-point version on home: objective feedback, volume with correction, faster muscle memory, both-hand skills, gamification, coaching'}
];"""
rep("""  wix:'Wix Instagram app',v01:'Instagram section on home wired for a Behold feed (the vendor coloradoboom.com already uses). Grid stays hidden until the feed id is set; follow button shows meanwhile',note:'Needs a Behold feed id for @shoot360denver from the owner\\u2019s Behold account.'}
];""", """  wix:'Wix Instagram app',v01:'Instagram section on home wired for a Behold feed (the vendor coloradoboom.com already uses). Grid stays hidden until the feed id is set; follow button shows meanwhile',note:'Needs a Behold feed id for @shoot360denver from the owner\\u2019s Behold account.'}""" + new_rows)

# Tiles + headline + eyebrow + controls label
rep("{n:'19', l:'Features scored', s:'conversion, trust, search, reach'}", "{n:'26', l:'Features scored', s:'conversion, trust, search, reach'}")
rep("{n:'11', l:'Closed in v0.1', s:'no owner input needed', hero:true}", "{n:'22', l:'Built by v0.2', s:'7 of them still carry yellow placeholders', hero:true}")
rep("{n:'5',  l:'Need the owner', s:'content or a vendor decision'}", "{n:'7',  l:'Values pending', s:'party prices, family %, pause terms, shots total, GHL embed, Behold id, hours'}")
rep("Website gap analysis &middot; Shoot 360 Denver &middot; 16 Sep 2026", "Website gap analysis &middot; Shoot 360 Denver &middot; 16 Sep 2026 &middot; updated for site v0.2")
rep("Against 19 sister franchises, Denver's Wix site was last on nine of fifteen features. Eleven gaps are closed in the new build; five wait on the owner.",
    "Against 19 sister franchises, Denver's Wix site was last on nine of fifteen features. After the owner's v0.2 directives, 22 of 26 features are built; seven wait only on numbers the owner holds.")
rep("were checked for 19 marketing, trust and search features.", "were checked for 19 marketing, trust and search features, and seven more were added at the owner's direction in v0.2.")
rep('>Built in v0.1 <span class="c"></span>', '>Built <span class="c"></span>')
rep('>Needs the owner <span class="c"></span>', '>Waiting on owner values <span class="c"></span>')
rep("Skipped on purpose: low prevalence, high upkeep'}", "Skipped on purpose: low prevalence, high upkeep'}")  # sanity: still present
p.write_text(s, encoding='utf-8')
import re
rows = re.findall(r"\{t:'", s); print('rows', len(rows), '| built', s.count('built:1'), '| flagged', s.count('flag:1'), '| skipped', s.count('alt:1'))
