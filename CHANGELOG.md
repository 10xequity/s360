# Changelog — Shoot 360 Denver site

Newest first. Each entry says what changed and why, so the next person does not undo a decision.

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
