# Editing Guide — Shoot 360 Denver site

**Version** 1.2 · **Updated** 2026-09-16 · **Status** Active · **Supersedes** 1.1 (seven pages, hand-edited header/footer)

Static site — plain HTML/CSS/JS, no build step. Every page opens with a comment listing its section
codes, so "change `[MB-TIERS]`" is findable by search. Run `python scripts/preflight.py` after any edit.

## Pages & codes

| File | Code | Purpose |
|---|---|---|
| `index.html` | **HM** | Hero, `HM-SPARK` MySpark banner, partners, `HM-COUNT` live shots, how it works, tech teaser, `HM-BEN`, programs grid, `HM-06` pricing teaser, values + numbers, `HM-REV` Google, visit, app, `HM-IG`, FAQ, CTA |
| `technology.html` | **TC** | Splash Meter, Splash Zone, skill courts, sensors, `TC-BEN` benefits (green, `.meter`), clips, app |
| `memberships.html` | **MB** | `MB-COACH`, `MB-TIERS` (direct contract links), `MB-FAM`, `MB-PACKS`, `MB-CALC`, `MB-POL`, `MB-APP` |
| `programs.html` | **PG** | Evaluation, `PG-APP`, `PG-CLASSES`, `PG-CAMPS`, `PG-LEAGUES`, `PG-CLUB` (Team EVO), `PG-PRIVATE`, `PG-HS`, `PG-PT`, MySpark, teams |
| `parties.html` | **PT** | Packages, how it works, party FAQ, `PT-05` request with GHL slot |
| `faq.html` | **FQ** | 22 questions; FAQPage JSON-LD mirrors them — **update both** |
| `contact.html` | **CT** | Address, hours, map, `CT-FORM` GHL slot + data note, social, app |
| `legal.html` | **LG** | `#privacy`, `#services` (data & third parties), `#disclaimer`, `#accessibility`; `noindex` |

## Header and footer are generated — do not hand-edit

`[NAV]…</header>` and `[FT]…</footer>` on all eight pages come from the `nav()` and `FOOTER`
templates in the v0.3 patch script (`scripts/patch_v03.py`). Edit the template, run the script, commit. The script is idempotent and sets
`aria-current` per page. Nav order: Technology · Memberships · Programs ▾ · Parties · FAQ · Visit Us ·
New Membership. Dropdown items: All programs, Classes, Camps, Leagues, Basketball Club (teamevo.org),
Private Training (mailto).

## Placeholders

`<span class="tbd">…</span>` renders as a yellow chip for a value the owner has not supplied.
Replace the whole span. Pre-flight fails while any remain. Mentions inside HTML comments do not count.

## Global content — change everywhere

| Item | Value | Where |
|---|---|---|
| Phone | 720-262-5501 | hero-meta, visit, contact, footer template, FAQ, party FAQ, schema |
| Email | info@shoot360denver.com | contact, footer template, private training, teams, legal |
| Hours | Mon–Fri 1–9 PM · Sat–Sun 10 AM–5 PM · Homeschool Mon–Fri 2–4 PM | hero-meta, `[HM-08]`, `contact.html`, footer template, FAQ, JSON-LD ×7, **and the `SHARE` bands in `main.js` for the counter** |
| Prices | $159 / $199 / $379 / $389 / $480 / $72 | `[HM-06]`, `[MB-TIERS]`, `[MB-PACKS]`, FAQ text + JSON-LD, `makesOffer` in memberships schema, `priceRange`, calculator `tiers` in `main.js` |
| Contract links | `https://www.shoot360.com/membership-checkout?locationid=5739019&contractid=151/152/154/156`, `packageid=158/157` | every Join / Buy button, memberships `makesOffer` |
| Evaluation URL | `https://shoot360-prod.saloncloudsplus.io/ghl/athlete-info` | every "Book an Evaluation" |
| Google listing | `https://maps.google.com/?cid=8030805088891520148` | `[HM-REV]`, footer template, schema |
| Team EVO | `https://www.teamevo.org/` | nav dropdown, footer template, `[PG-CLUB]` |

## Components

- **Live counter**: `#shots` in `[HM-COUNT]`; model constants at the top of the v0.3 block in `main.js`
  (`BASE`, `EPOCH`, `BAYS`, `PER_BAY_HOUR`, `SHARE`). Reduced-motion users get a once-a-minute update.
- **Savings calculator**: markup in `[MB-CALC]`; tier prices in `main.js` `tiers`. Change both when prices move.
- **Register-in-the-app strip**: `.appnote` with text + `.badges`. Use it wherever a class, camp, league,
  drop-in or homeschool session is mentioned.
- **App badges**: `.badge-app` images (`badge-appstore.svg`, `badge-googleplay.png`). Google's badge
  carries transparent padding, hence the taller height and negative margin in CSS.
- **MySpark banner**: `.spark` / `.spark-cta` on home; logo `myspark-logo.png` (navy) and
  `myspark-logo-white.png` (stacked, for dark grounds).
- **Dropdown**: `.has-sub > .sub-toggle[aria-expanded] + .sub`. Hover/focus-within opens on desktop,
  click toggles everywhere, Escape closes, outside click closes.
- **GHL slots**: `#ghl-contact`, `#ghl-party` (`hidden`); paste embed, remove `hidden`, delete the callout.
- **Instagram**: `#ig[data-feed="BEHOLD_ID"]`; empty stays hidden.
- **Party packages** reuse `.tier` inside `.tiers.t3`. Never inline `grid-template-columns`.

## Multi-page changes: the method that works

1. Write a throwaway script to disk (Write tool, not a shell heredoc), exact-string anchors, throw if
   an anchor is missing or appears more than once, skip if the replacement is already present.
2. `scripts/preflight.py` afterwards; `--external` when links changed.
3. Preview locally at desktop and 390 px; check `document.documentElement.scrollWidth <= innerWidth`.

## Dated content that retires itself

`data-show-until="YYYY-MM-DD"` hides the element the day after; `data-show-from="YYYY-MM-DD"`
reveals it on that day (author it `hidden style="display:none"`). Judged in America/Denver by `main.js`.

## Design conventions

- **Fonts**: self-hosted Rajdhani 600/700 (display) and Open Sans 400–600 (body). No Google Fonts `<link>`.
- **Tokens**: `--red #E0001B` (fills), `--red-text #FF2A3C` (small red text on black), `--red-dark #C20101`,
  `--meter #22D478` (Splash Meter green; dark grounds only, it fails contrast on light), blacks and greys in `:root`.
- **Contrast measured**: white on `#E0001B` 5.0:1 · `#FF2A3C` on black 5.3:1 · `#22D478` on `#141414` 9.4:1 ·
  `#C20101` on `#F3F3F3` 5.7:1 · `#9A9A9A` on `#141414` 6.5:1 · `#4A4A4A` on `#F3F3F3` 8:1.
- **Text sizes** for facts people act on: hero meta 18 px, hours table 18 px, address 19 px, footer 17 px.
- **Never put dark cards inside `.sec-light`** without overriding their text colour; `.sec-light .benefit`
  is overridden as a safety net.
- **Images**: keep `img{height:auto}`; every `<img>` has `alt`; decorative hero backgrounds use `alt=""`.
- **Headings**: one `h1` per page; footer headings are `h3`.
- **Sections alternate** black → ink → light grey; never two light sections in a row.
- **Words**: "evaluation", not "free". "Register in the Shoot 360 app" wherever a bookable thing is named.
