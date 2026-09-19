# Changelog — Shoot 360 Denver site

Newest first. Each entry says what changed and why, so the next person does not undo a decision.

## v0.4.4 — 2026-09-19 — Unlimited tiers repriced; booking windows removed

**Committed and Ball is Life come off HQ's numbers and onto the owner's sheet.** HQ's checkout shows $389 and
$379 for Denver's All-Star and Hall of Fame; the owner's own pricing sheet says $229 and $220. The site now
shows **$239** and **$230**, which is the sheet plus the $10 the owner keeps back so staff have something to
give away when closing in person. That is the same rule the other two tiers already followed — the sheet's
$149 and $189 are the $159 and $199 HQ publishes — so all four are finally consistent. The in-store discount
is deliberately not mentioned anywhere on the site. Changed in the tier cards, the comparison table, the home
teaser, the FAQ, the savings calculator, the `Offer` schema and the meta description; `priceRange` drops to
`$42–$240`, Lock-In Reserved now being the dearest monthly.

**Booking windows are gone**, at the owner's request: the "book 5 / 6 / 7 days ahead" lines on every tier card
and the home teaser, the whole **Scheduling window** row in the comparison table, "up to 3 days ahead" on the
drop-in card and in two FAQ answers, and the policies line about a tier's scheduling window. The FAQ question
"How far ahead can I book, and can I book back-to-back sessions?" becomes "Can I book back-to-back sessions?",
keeping the one-at-a-time rule and the Lock-In Reserved exception.

**Fine print corrected.** It claimed prices matched HQ's online checkout, which is no longer true for the two
unlimited tiers; it now just dates them.

**Open risk:** the Join buttons still point at HQ contracts 154 and 156, and HQ's checkout was showing $379 for
Hall of Fame when this was written. Until HQ's Denver contracts carry $239 and $230, a member will see one
price here and another at signup.

## v0.4.3 — 2026-09-19 — Owner's event prices; hours point at the app; zero placeholders

**Event pricing is the owner's now**, and the whole page is simpler for it. One court rate does all the work:
**two courts for two hours, $160**, and **all four courts for two hours, $720** on Saturday nights after 6 PM.
That replaces the proposed $449 / $1,295 tiers, the member prices, the extra-guest fee and the guest caps.
Capacity is expressed as what it really is, stations rather than floor space: ten athletes under 10, or six
aged 11 to 17, on two courts. The four-court numbers (20 / 12) are that doubled and are flagged in `HANDOFF.md`
as an inference. Date nights fold into the same $160 booking instead of a separate hourly rate, with the
takeover offered for bigger groups. The three invented "open Saturday" chips are gone, replaced by an ask.

**Weekend hours** stay 10 AM–5 PM, with a line under every hours block, in the footer and in the FAQ saying the
Shoot 360 app has the live schedule, because that is the thing that is actually kept up to date.

**Placeholders: 19 → 0.** `python scripts/preflight.py` now exits clean, which was the condition set in the
README for pointing the real domain at this site.

`docs/party-pricing-model_v1_2026-09-17.md` keeps the court-hour method but leads with the decision and shows
the owner's prices against modelled cost: the two-court booking runs at about 25% margin once a coach is paid,
so the money on it is the restaurant spend; the takeover carries the margin at about 67%.

## v0.4.2 — 2026-09-19 — Cut-over day: domain checks, TBD text removed

**Cut-over state found this morning.** The registrar moved to Cloudflare today
(`greg.ns.cloudflare.com`, `journey.ns.cloudflare.com`) and the owner added the `CNAME` file through
GitHub's UI, so Pages now holds the custom domain and the build is green. Two things were not done:
the Cloudflare zone has **no `www` record at all**, and the apex still carries Wix's `185.230.63.x`
proxied through Cloudflare, which is why `shoot360denver.com` still 301s to a `www` that answers only
from expiring Wix cache. Proved GitHub is otherwise ready with
`curl --resolve www.shoot360denver.com:80:185.199.108.153`: 200 on the home page, memberships, events,
publications, FAQ and the stylesheet.

**Docs.** `DEPLOY_GITHUB.md` v1.1: real cut-over status at the top; step 4 replaced with the exact
record table and the reason both records must be **DNS-only (grey cloud)** — with the Cloudflare proxy
on, Cloudflare answers the `/.well-known/acme-challenge/` request GitHub uses to issue its certificate,
so "Enforce HTTPS" never becomes available, and with SSL/TLS mode *Flexible* you also get a redirect
loop. Four new troubleshooting entries. `HANDOFF.md` v0.4.2 leads with a cut-over status table.

**Live-site copy.** The five remaining `class="tbd"` spans on `memberships.html` printed the literal
word TBD ("gets TBD% off their membership", "suspend for up to TBD months for $TBD a month"). With the
domain about to resolve, those were rewritten to say what is true without inventing numbers: ask the
front desk for today's family pricing, and memberships can be suspended with terms and notice period
from the desk. Placeholders 24 → 19, all remaining ones on `events.html`.

**Note.** The old Pages build marked "errored" on 17 Sept was a superseded duplicate, not a failure:
duration 0, and the live bytes match the latest commit once CRLF is normalised.

## v0.4.1 — 2026-09-17 — Owner's answers to the v0.4 questions

- **Tier prices follow Shoot 360's online checkout for Denver** (owner: "use the online prices as the website
  price"): JV/Rookie **$159**, Varsity/Pro **$199**, Committed/All-Star **$389**, Ball is Life/Hall of Fame **$379**
  (12-month). Read from `shoot360.com/membership-pricing?locationId=5739019` rendered in a browser on 2026-09-17.
  Names stay the owner's. "Most popular" moves to Ball is Life, as online. Calculator tiers, JSON-LD offers, FAQ,
  home teaser and meta descriptions updated. Ball is Life card and table say classes are included.
- **Drop-In**: $80 a session for non-members; members add a session beyond their plan for **$42** (owner). The
  sheet's per-tier extra-session prices ($37/$24/$30) are replaced by the flat $42; unlimited tiers stay $0.
- **Unlimited Classes and Little Ballers: $149** (owner). Not a product on HQ's online page, so unconfirmed there.
- **Personal training add-ons removed** everywhere (owner: assigned privately). Private training is "arranged
  individually with a coach"; the email route stays.
- **Ball is Life includes classes**; JV, Varsity and Committed add them for $40 (owner). The $149 cell was a typo.
- **Event booking rules removed**: no deposit, lead time, headcount cut-off or reschedule window (owner: the
  booking system cannot enforce them). Event prices remain proposals in yellow.
- **Fix**: the two insert steps in `patch_v04.py` (Vimeo privacy note on legal, publications teaser on technology) re-inserted on every run; v0.4 shipped three copies of each and v0.4.1 seven. Guarded, files deduplicated to one copy.
- Placeholders left: 24 (event prices and guest caps, open Saturday dates, family %, pause terms, weekend hours
  unconfirmed but not flagged).

## v0.4 — 2026-09-17 — Owner's third review (18 directives)

**Structure.**
- **Events page** (`events.html`) replaces `parties.html` (a redirect stub stays so the shared review link lands).
  Three hash-selected tabs: **Special events** (corporate, partnership meetings, bachelor/graduation, team nights,
  takeovers), **Parties** (birthdays) and **Date nights**. Two formats everywhere: **2-Court** (a shooting bay + a
  skills court, 2 h, up to 12) and **Full Facility Takeover** (all 8 courts, 2 coaches, Saturday nights after 6 PM
  on select weekends), plus Date Night / Double Date. Food and drink come from the on-site restaurant and bar (owner
  rule). "Next open Saturday nights" chips retire themselves with `data-show-until`. Prices are proposals from
  `docs/party-pricing-model_v1_2026-09-17.md` and are yellow placeholders until the owner confirms.
- **Publications page** (`publications.html`) under Technology: about 60 sources, every one fetched and read
  (`docs/publications-research_v1_2026-09-17.md`). Team sources (Warriors, Jazz, Nets/Liberty, Clippers, Squadron),
  player-owners, national press, partners (Nike/US Sports Camps, Noah, Microsoft, LA Fitness), podcasts and video.
  The page states the NBA link carefully: the shot-tracking engine is licensed from Noah Basketball, whose install
  base is what "28 of 30 NBA teams" counts.
- **Navigation regenerated on every page** by `scripts/patch_v04.py`: Technology ▾ (The technology · Publications ·
  Download the app → `technology.html#app`) · Memberships · Programs ▾ · Events ▾ (Special events · Parties · Date
  nights) · FAQ · Visit Us · New Membership. Footer: hours 2–9 PM, FieldhouseUSA linked, Publications and Events links.

**Memberships** (owner's "Denver Membership Options" sheet; HQ's page is not the source).
- Hoop tiers renamed with app names shown: **JV** (Rookie) 4 sessions $149 · **Varsity** (Pro) 8 sessions $189 ·
  **Committed** (All-Star) unlimited $229 · **Ball is Life** (Hall of Fame) unlimited, 12-month, $220. Contract links
  unchanged (151/152/154/156). Per tier: scheduling window, extra-session price, day-time court access, leagues.
- New: **Unlimited Classes** and **Little Ballers** (ages 6–10) classes-only memberships; **Drop-In**; **Lock-In
  Reserved** $240 (fixed weekly time); **My Spark / DPS / APS** $1,000 for 6 months, $0 enrollment. Full comparison
  table; the Jr Nuggets jersey row is omitted for now (owner). Add-ons: personal training 4/$120 and 8/$240,
  unlimited classes +$40. Policies: $40 one-time enrollment, Aurora tax not included, one-month deposit applied to
  month 4, no back-to-back sessions, two-strike no-show policy. "15% off camps and clinics" removed site-wide.
- Calculator tiers in `main.js` now Varsity / Committed / Ball is Life.

**Home.** Partner logos in a row with the label underneath, Nuggets 30→42 px (+40%). Shots counter in Splash Meter
green. How-it-works steps are links (evaluation form, technology, app). Two **Vimeo** clips carried over from the
Wix site (720241338 shooting, 720257389 passing) replace the HUD still: borderless, background mode, `dnt=1`.
BOOM letters yellow `#F5C400`, value headings green, facility stats red. Pricing teaser rebuilt with the new names.
**Hours** Mon–Fri **2–9 PM** everywhere (hero, tables, footer, FAQ, JSON-LD `opens`, counter model).
**FieldhouseUSA** linked to aurorafieldhouseusa.com; map embed and directions pinned on the FieldhouseUSA listing
(39.7092894, -104.8217123), which is the building; the bare street address and the Shoot 360 Google listing both
pin the mall centroid 100 m west. JSON-LD geo updated.

**Technology.** Skill-court still replaced by the passing Vimeo clip; `#app` anchor and "Download the app"
heading; publications teaser before the CTA.

**FAQ.** Hero crop `object-position:50% 20%` so heads show. Section gets a red/green gradient, an inline SVG
basketball and topic chips (Getting started · Technology · Memberships · Programs & app · Visit & My Spark ·
Events). Questions are generated from one list in `patch_v04.py` into both the HTML and the FAQPage JSON-LD: 35
questions, including My Spark (DPS grades 6–8, free or reduced-price meals, $1,000 card), Unlimited Classes / Little
Ballers, what a session is, how often to train, parents watching, what to wear, cancelling, closures, photography.

**Legal.** Vimeo added to the third-party services list.
**Preflight.** Redirect stubs are exempt from the sitemap check. Sitemap: events + publications added, parties removed.

**Checks.** `preflight`: 10 pages, 82 external URLs, 49 placeholders (proposals and open owner decisions), 0 problems.

## v0.3 — 2026-09-16 (late) — Owner's second review

**Structure.**
- **Memberships is its own page** (`memberships.html`): coaching-included section, four tiers, family
  discounts, packs and guest workout, savings calculator, policies, app download. Programs page now
  holds evaluation, classes, camps, leagues, Basketball Club (Team EVO), private training, homeschool,
  parties, MySpark, teams.
- **Navigation regenerated on every page**: Technology · Memberships · Programs ▾ (All programs, Classes,
  Camps, Leagues, Basketball Club → teamevo.org, Private Training → mailto) · Parties · FAQ · Visit Us ·
  **New Membership** CTA (→ memberships) with more spacing. Dropdown is a real button with
  `aria-expanded`; hover opens it on desktop, tap on mobile, Escape closes. Mobile breakpoint moved to
  1024 px because the bar is wider.
- **Direct contract links.** Every Join button goes straight to that tier's signup in Shoot 360's
  system, bypassing HQ's pricing page whose copy the owner says is wrong: Rookie 151 · Pro 152 ·
  All-Star 154 · Hall of Fame 156 · 12-visit pack 158 · guest 157 (`membership-checkout?locationid=5739019&…`).
  Mapping read off the HQ page's own buttons in a browser; all six URLs return 200.

**Wording.** "Free" is gone from the site (the only remaining instance is "of my own free will" in the
waiver). Primary CTA is **Book an Evaluation**; copy says "come evaluate". Every class, camp, league,
drop-in and homeschool mention now says **Register in the Shoot 360 app** with badges.

**Home.** MySpark Denver CTA banner directly under the hero in the program's navy with its logo.
**Live shots counter**: 375,000 baseline at 2026-09-16 00:00, plus a model of shots since (4 bays ×
600 shots per busy bay-hour × utilisation: weekdays 35% 1–4 PM, 85% 4–9 PM; weekends 55% 10–1,
70% 1–5). Deterministic, ticks once a second while open, label says "live estimate". Programs grid
now Memberships / Classes & camps / Leagues & club / Parties.

**Brand and type.** Header and footer use the red-and-white Shoot 360 Basketball lockup
(`basketball (3).png` from the logo pack). Official Apple App Store (SVG) and Google Play badges
replace the text badges. Hours, phone and address text sizes increased (hero meta 14→18 px, hours
16→18, address 17→19, footer 15→17). Technology benefits grid moved to a dark section with headings in
Splash Meter green `#22D478` (sampled from the HUD photo) — it had been black text on dark cards.

**Privacy.** `legal.html#services` "Data and third-party services": what each integration collects
(Shoot 360 membership system, GoHighLevel forms, the app, Google Maps and reviews, Behold/Instagram,
calculator and counter, GitHub Pages hosting, analytics status, children, your choices). Footer links
to it; contact form slot carries a one-line data note.

**Checks.** Lighthouse mobile 100 / 100 / 100 on home, memberships, programs. Pre-flight: 8 pages,
23 outbound links reachable, 22 placeholders, 0 problems.

## v0.2 — 2026-09-16 — Owner directives, review deployment

**Repo public, Pages on.** Review URL `https://10xequity.github.io/shoot360-denver-site/`. The domain
still points at Wix; DNS moves after the owner signs off on the content.

**Owner directives implemented** (from the review of v0.1):
- **Birthday parties** are sold: new `parties.html` (three packages, how it works, party FAQ, request
  section), plus a card on home, a section on programs, a nav item and a footer link on every page.
  Prices, athlete caps, durations, deposit and lead time are yellow placeholders until supplied.
- **Coaching is included in every membership.** Dedicated section, tier bullets reworded, hero and FAQ
  updated, policies section explains floor coaching (never expires) vs bundled one-on-ones (monthly).
- **Homeschool sessions, weekdays 2–4 PM**: section, hours tables, FAQ, home card.
- **Savings calculator**: visitor sets trainer rate and sessions/month; shows monthly saving vs Pro,
  Hall of Fame and All-Star. The trainer rate is the visitor's input, not a claim.
- **Family discounts** callout and FAQ (percentages are placeholders).
- **Membership policies** section: pausing (terms are placeholders), commitments, coaching sessions.
- **Google Business Profile connected.** Listing found (4.7 stars, CID 8030805088891520148): rating
  badge, review links, "Reviews on Google" in every footer, listing in `sameAs`/`hasMap` schema.
- **Instagram**: home section wired for a Behold feed (`#ig[data-feed]`); grid hides until a feed id is set.
- **GoHighLevel form slots** on contact (`#ghl-contact`) and parties (`#ghl-party`), hidden until pasted.
- **Benefits copy**: six-point grid on technology, three-point version on home.

**Quality passes.** Fonts self-hosted and preloaded (CLS 0.34 → 0.00). `img{height:auto}` (distorted
aspect flags). Footer headings `h4`→`h3`. `.tiers.t3` replaces an inline grid style that broke the
phone layout. `scripts/preflight.py` added (links, anchors, alt, schema, sitemap, placeholders,
`--external`). MySpark grant link rejects HEAD but serves GET; checker falls back.

## v0.1 — 2026-09-16 — Initial build (private, not live)

**Archive.** Downloaded the entire Wix site (6 rendered pages, all 47 Media Manager uploads at
original resolution including six training clips, the official logo pack, fonts and icon zips) into
`wix-archive/`, with a text inventory of every page, a media manifest and viewport screenshots.
Found and recorded the live defects: template-default `mailto:info@mysite.com` and
`tel:123-456-7890` links on every page, an indexable template-filler `/about`, summer hours shown year-round.

**Research.** Compared 19 own-domain Shoot 360 franchise sites and 22 HQ location pages on 18
marketing features; collected price points from 9 franchises; read Denver's live prices from HQ's
pricing page (`locationId=5739019`). Written up in `docs/`.

**Site.** Six static pages on the coloradoboom.com stack: one red button everywhere (booking form
every franchise uses), prices shown with links into HQ's system, HQ's hours (flagged), Rajdhani +
Open Sans (shoot360.com's faces), contrast-safe red tokens (`#E0001B` fills, `#FF2A3C` small text),
`/about` dropped as template filler, `legal.html` noindex, `wix-archive/` disallowed in robots,
branch `main` lowercase on purpose.
