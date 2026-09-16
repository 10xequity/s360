# Editing Guide — Shoot 360 Denver site

**Version** 1.0 · **Updated** 2026-09-16 · **Status** Active

Static site — plain HTML/CSS/JS, no build step. Every page opens with a comment listing its section
codes, so "change `[HM-06]`" is findable by search.

## Pages & codes

| File | Code | Purpose |
|---|---|---|
| `index.html` | **HM** | Home: hero, partners, how it works, tech teaser, programs, pricing teaser, values + numbers, visit, app, top FAQ, CTA |
| `technology.html` | **TC** | Splash Meter, Splash Zone, skill courts, sensors, clips, app |
| `programs.html` | **PG** | Free evaluation, memberships, packs, camps, Nike, leagues, MySpark, teams |
| `faq.html` | **FQ** | 15 questions; the FAQPage JSON-LD in `<head>` mirrors them — **update both** |
| `contact.html` | **CT** | Address, hours, map, phone, email, social, app |
| `legal.html` | — | `#privacy`, `#disclaimer`, `#accessibility`; `noindex` |

## Shared blocks are copy-pasted, not included

| Code | What | Lives in |
|---|---|---|
| `[NAV]` | Header + nav + red CTA button | all 6 pages |
| `[ANN]` | Optional announcement bar (commented out in `index.html`) | any page that needs it |
| `[FT]` | Footer with address, hours, app badges, social, legal links | all 6 pages |
| JSON-LD `SportsActivityLocation` | Hours, address, phone in schema | all 6 pages' `<head>` |

Truly centralised: `assets/css/styles.css` (all styling; tokens in `:root`) and `assets/js/main.js` (all behaviour).

## Global content — change everywhere

| Item | Value | Where |
|---|---|---|
| Phone | 720-262-5501 (`tel:+17202625501`) | header CTA fallbacks, hero-meta, visit, contact, footer, FAQ, schema |
| Email | info@shoot360denver.com | contact, footer, teams sections, legal |
| Hours | Mon–Fri 1–9 PM · Sat–Sun 10 AM–5 PM | hero-meta, `[HM-08]`, `contact.html`, footer ×6, FAQ text + schema, JSON-LD `openingHoursSpecification` ×6 (`13:00`/`21:00`, `10:00`/`17:00`) |
| Address | FieldhouseUSA, 14200 E Alameda Ave, Aurora, CO 80012 | visit, contact, footer, schema, map `src` |
| Prices | $159 / $199 / $379 / $389 / $480 / $72 | `[HM-06]`, `[PG-03]`, `[PG-04]`, FAQ "How do memberships work" + "without a membership" (text and JSON-LD), `priceRange` in schema |
| Booking URL | `https://shoot360-prod.saloncloudsplus.io/ghl/athlete-info` | every "Book a Free Workout" button |
| Pricing URL | `https://www.shoot360.com/membership-pricing?locationId=5739019` | every "Join" button, fine print |
| Social | instagram.com/shoot360denver · facebook.com/shoot360denver | footer ×6, contact, schema `sameAs` |

## Multi-page changes: the method that works

1. Write a throwaway script that does exact-string replacement and **throws if an anchor is missing
   or appears more than once**. Silent skips are the failure you cannot see.
2. Assert across all six pages afterwards: count the footers, confirm the old string is gone,
   confirm the strings that should survive did.
3. Add a positive control: feed the search a known-bad string and confirm it matches.
4. Grep for the shortest distinctive fragment, not the whole sentence.
5. Preview locally, click every nav link, open the FAQ accordion, and check the map loads.

## Dated content that retires itself

Tag an element with `data-show-until="YYYY-MM-DD"` (hidden the day after) or
`data-show-from="YYYY-MM-DD"` (revealed on that day; author it `hidden style="display:none"`).
Evaluated on load in America/Denver by `main.js`. Wrap only the expiring words so what remains still
reads. Use it for camp dates, seasonal hours notices, promotions. A malformed date is left as authored.

## Design conventions

- **Fonts**: Rajdhani 600/700 (display, buttons, nav) and Open Sans 400/600 (body), from Google
  Fonts. These are what shoot360.com uses. The Gotham/Tungsten files in the archive are licensed; do not ship them.
- **Tokens** in `:root`: `--red #E0001B` (fills: buttons, band, tags), `--red-text #FF2A3C` (small red
  text on black), `--red-dark #C20101` (hover; red text on light), `--red-brand #EF001D` (reference
  only), `--black #0B0B0B`, `--ink #141414`, `--grey-100 #F3F3F3`, `--grey-300 #C9C9C9`,
  `--grey-500 #9A9A9A`, `--grey-700 #4A4A4A`.
- **Contrast measured**: white on `#E0001B` 5.0:1 · white on `#EF001D` 4.49:1 (fails, hence the
  fill token) · `#FF2A3C` on black 5.3:1 · `#EF001D` on black 4.4:1 (fails for small text) ·
  `#C20101` on `#F3F3F3` 5.7:1 · `#9A9A9A` on `#141414` 6.5:1 · `#4A4A4A` on `#F3F3F3` 8:1.
- **Button hierarchy**: red primary is the free workout, always. White outline is secondary on dark;
  black solid / black outline on light. `.btn-sm` in the header and tier cards.
- **Sections alternate** black → ink → light grey; never two light sections in a row.
- **Images**: keep filenames in `assets/img/`; regenerate with `wix-archive/optimize.py` from the
  originals. Every `<img>` has `alt`; decorative hero backgrounds use `alt=""`.
- **Videos**: click-to-play facades (`.vid[data-src]`) with a poster, never autoplay except the hero.
