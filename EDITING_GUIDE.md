# Editing Guide — Shoot 360 Denver site

**Version** 1.1 · **Updated** 2026-09-16 · **Status** Active · **Supersedes** 1.0 (six pages, Google Fonts)

Static site — plain HTML/CSS/JS, no build step. Every page opens with a comment listing its section
codes, so "change `[PG-CALC]`" is findable by search. Run `python scripts/preflight.py` after any edit.

## Pages & codes

| File | Code | Purpose |
|---|---|---|
| `index.html` | **HM** | Hero, partners, `HM-COUNT` shots counter, how it works, tech teaser, `HM-BEN` benefits, programs, pricing teaser, values + numbers, `HM-REV` Google rating, visit, app, `HM-IG` Instagram, top FAQ, CTA |
| `technology.html` | **TC** | Splash Meter, Splash Zone, skill courts, sensors, `TC-BEN` benefits, clips, app |
| `programs.html` | **PG** | Free evaluation, `PG-COACH` coaching included, memberships + `PG-FAM` family, packs, `PG-CALC` calculator, camps, `PG-HS` homeschool, Nike, leagues, `PG-PT` parties, MySpark, `PG-POL` policies, teams |
| `parties.html` | **PT** | Packages, how it works, party FAQ, `PT-05` request section with GHL slot |
| `faq.html` | **FQ** | 20 questions; the FAQPage JSON-LD in `<head>` mirrors them — **update both** |
| `contact.html` | **CT** | Address, hours, map, `CT-FORM` GHL slot, social, app |
| `legal.html` | — | `#privacy`, `#disclaimer`, `#accessibility`; `noindex` |

## Placeholders

`<span class="tbd">…</span>` renders as a yellow chip. It marks a value the owner has not supplied.
Replace the whole span with the value. The pre-flight fails while any remain, on purpose.

## Shared blocks are copy-pasted, not included

| Code | What | Lives in |
|---|---|---|
| `[NAV]` | Header + nav (Technology · Programs & Pricing · Parties · FAQ · Visit Us) + red CTA | all 7 pages |
| `[ANN]` | Optional announcement bar (commented out in `index.html`) | any page |
| `[FT]` | Footer: address, hours (incl. homeschool line on home), app badges, Explore links incl. Parties and Reviews on Google, legal links | all 7 pages |
| JSON-LD `SportsActivityLocation` | Hours, address, phone, `sameAs` (Instagram, Facebook, Google listing) | all pages except legal |

Centralised: `assets/css/styles.css` (tokens in `:root`, `@font-face` above) and `assets/js/main.js`.

## Global content — change everywhere

| Item | Value | Where |
|---|---|---|
| Phone | 720-262-5501 (`tel:+17202625501`) | hero-meta, visit, contact, footers, FAQ, party FAQ, schema |
| Email | info@shoot360denver.com | contact, footers, teams, legal, party request |
| Hours | Mon–Fri 1–9 PM · Sat–Sun 10 AM–5 PM · Homeschool Mon–Fri 2–4 PM | hero-meta, `[HM-08]`, `contact.html`, footers ×7, FAQ text + schema, JSON-LD `openingHoursSpecification` ×6 |
| Address | FieldhouseUSA, 14200 E Alameda Ave, Aurora, CO 80012 | visit, contact, footers, schema, map `src` |
| Prices | $159 / $199 / $379 / $389 / $480 / $72 | `[HM-06]`, `[PG-03]`, `[PG-04]`, FAQ text + JSON-LD, `makesOffer` in programs schema, `priceRange`, calculator tiers in `main.js` |
| Booking URL | `https://shoot360-prod.saloncloudsplus.io/ghl/athlete-info` | every "Book a Free Workout" |
| Pricing URL | `https://www.shoot360.com/membership-pricing?locationId=5739019` | every "Join", fine print |
| Google listing | `https://maps.google.com/?cid=8030805088891520148` | `[HM-REV]`, footers, schema `sameAs`/`hasMap` |
| Social | instagram.com/shoot360denver · facebook.com/shoot360denver | footers, contact, schema |

## Components added in v0.2

- **Counter**: `<span class="n" data-count="9440096">` counts up on scroll. Empty `data-count` = no animation.
- **Savings calculator**: markup in `[PG-CALC]`; tier prices live in `main.js` (`tiers` array). Change both places when prices move.
- **Instagram**: `#ig[data-feed="BEHOLD_ID"]` loads `https://w.behold.so/widget.js` and renders `<behold-widget>`. Empty = hidden.
- **GHL slots**: `#ghl-contact`, `#ghl-party` are `hidden` divs; paste the embed, remove `hidden`, delete the fallback callout.
- **Party packages** reuse `.tier` inside `.tiers.t3` (three columns, one on phones). Never use an inline `grid-template-columns` style; it breaks the phone breakpoint.
- **Reviews grid** (`.reviews > .review`) is styled but not yet used; add three cards under `[HM-REV]` when quotes exist.

## Multi-page changes: the method that works

1. Write a throwaway script (file on disk, not a shell heredoc) that does exact-string replacement
   and **throws if an anchor is missing or appears more than once**. Make it re-runnable: skip if the
   replacement text is already present.
2. Assert across all seven pages afterwards; `scripts/preflight.py` covers links, anchors, alt, schema, sitemap.
3. Match the shortest distinctive fragment, and check it is unique per file first (the contact page has
   two Facebook links; the footer one needed a longer anchor).
4. Preview locally at desktop and 390 px wide; check `document.documentElement.scrollWidth <= innerWidth`.

## Dated content that retires itself

`data-show-until="YYYY-MM-DD"` hides the element the day after; `data-show-from="YYYY-MM-DD"`
reveals it on that day (author it `hidden style="display:none"`). Judged in America/Denver by `main.js`.

## Design conventions

- **Fonts**: self-hosted Rajdhani 600/700 (display) and Open Sans 400–600 (body) in `assets/fonts/`,
  preloaded from each `<head>`. No Google Fonts `<link>`. Gotham/Tungsten in the archive are licensed; do not ship.
- **Tokens**: `--red #E0001B` (fills), `--red-text #FF2A3C` (small red text on black), `--red-dark
  #C20101` (hover; red text on light), `--red-brand #EF001D` (reference only), blacks and greys as listed in `:root`.
- **Contrast measured**: white on `#E0001B` 5.0:1 · `#FF2A3C` on black 5.3:1 · `#C20101` on `#F3F3F3`
  5.7:1 · `#9A9A9A` on `#141414` 6.5:1 · `#4A4A4A` on `#F3F3F3` 8:1. `#EF001D` fails AA in both roles.
- **Images**: keep `img{height:auto}` in the base rule; every `<img>` has `alt`; decorative hero
  backgrounds use `alt=""`. Regenerate sizes with `wix-archive/optimize.py`.
- **Headings**: one `h1` per page; footer headings are `h3` (Lighthouse heading-order).
- **Sections alternate** black → ink → light grey; never two light sections in a row.
