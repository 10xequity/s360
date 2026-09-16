# Changelog — Shoot 360 Denver site

Newest first. Each entry says what changed and why, so the next person does not undo a decision.

## v0.2 — 2026-09-16 — Owner directives, review deployment

**Repo public, Pages on.** Review URL `https://10xequity.github.io/shoot360-denver-site/`. The domain
still points at Wix; DNS moves after the owner signs off on the content.

**Owner directives implemented** (from the review of v0.1):
- **Birthday parties** are sold: new `parties.html` (three packages, how it works, party FAQ, request
  section), plus a card on home, a section on programs, a nav item and a footer link on every page.
  Prices, athlete caps, durations, deposit and lead time are yellow placeholders until supplied.
- **Coaching is included in every membership.** Dedicated section on programs, tier bullets reworded
  ("Coaching included · N one-on-one sessions"), hero and FAQ updated, policies section explains the
  difference between floor coaching (never expires) and bundled one-on-ones (monthly).
- **Homeschool sessions, weekdays 2–4 PM**: section on programs, row in both hours tables, FAQ, home card.
- **Savings calculator** on programs: visitor sets trainer rate and sessions/month; shows monthly
  saving vs Pro, Hall of Fame and All-Star. The trainer rate is the visitor's input, not a claim.
- **Family discounts** callout and FAQ (percentages are placeholders).
- **Membership policies** section: pausing (terms are placeholders), commitments, coaching sessions.
- **Live shots-tracked counter** on home. Same mechanism Huntsville uses: a hand-set number with a
  count-up animation; Shoot 360 exposes no data feed. Number is a placeholder.
- **Google Business Profile connected.** Listing found (4.7 stars, CID 8030805088891520148):
  rating badge, "Read reviews" and "Write a review" links on home, "Reviews on Google" in every
  footer, listing URL in `sameAs` and `hasMap` schema. Review text is not readable without the
  owner's login, so no quotes were added.
- **Instagram**: section on home wired for a Behold feed (`#ig[data-feed]`), the same vendor behind
  coloradoboom.com. Grid hides until a feed id is set.
- **GoHighLevel form slots** on contact (`#ghl-contact`) and parties (`#ghl-party`), hidden until the
  embed code is pasted.
- **Benefits copy**: six-point grid on technology, three-point version on home.

**Quality passes.**
- **Fonts self-hosted** (`assets/fonts/`, Rajdhani 600/700 + one variable Open Sans file, latin subset,
  preloaded). Reason: the performance trace showed CLS 0.34 with every shift caused by Google-hosted
  font swaps; after the change CLS is 0.00 and LCP 326 ms on the home page. Also removes the last
  third-party request on first paint.
- `img,video{height:auto}` added to the base rule: images carry HTML height attributes and CSS set
  only width, which Lighthouse flagged as distorted aspect ratio on two pages.
- Footer headings changed from `h4` to `h3` (Lighthouse heading-order).
- `.tiers.t3` class replaces an inline three-column style that broke the phone layout on parties.
- **Lighthouse (mobile) after fixes**: home, programs, parties each 100 accessibility / 100 best
  practices / 100 SEO. Console clean.
- **`scripts/preflight.py`** added: fails on any missing local link/asset/anchor, image without alt,
  bad JSON-LD, page missing from the sitemap, unreachable outbound link (`--external`), or any
  remaining `class="tbd"` placeholder. Current state: 7 pages, 11 outbound links all reachable,
  23 placeholders, 0 problems. It must exit 0 before go-live.
- Link check note: the MySpark grant page rejects HEAD requests but serves normally; the checker
  falls back to GET for that reason.

## v0.1 — 2026-09-16 — Initial build (private, not live)

**Archive.** Downloaded the entire Wix site (6 rendered pages, all 47 Media Manager uploads at
original resolution including six training clips, the official logo pack, fonts and icon zips) into
`wix-archive/`, with a text inventory of every page, a media manifest and viewport screenshots.
Found and recorded the live defects: template-default `mailto:info@mysite.com` and
`tel:123-456-7890` links on every page, an indexable template-filler `/about`, summer hours shown year-round.

**Research.** Compared 19 own-domain Shoot 360 franchise sites and 22 HQ location pages on 18
marketing features; collected price points from 9 franchises; read Denver's live prices from HQ's
pricing page (`locationId=5739019`). Written up in `docs/`.

**Site.** Six static pages on the coloradoboom.com stack. Decisions worth knowing:
- The one red button everywhere is **Book a Free Workout**, to the same SalonCloud form Wix used.
  Every franchise leads with the free workout; Denver's Wix called it "apply for membership".
- **Prices are shown** (a first for Denver) with "Join" links into HQ's live Denver pricing page so
  contract and payment stay in Shoot 360's system. Fine print names the live page as authoritative.
- **Hours are HQ's** (Mon–Fri 1–9, Sat–Sun 10–5), not Wix's 9–9. Flagged for the owner.
- **Fonts are Rajdhani + Open Sans** (shoot360.com's faces, free). The archived Gotham/Tungsten files
  are licensed and were not shipped.
- **Red tokens split**: `#E0001B` for fills (white text on it measures 5.0:1), `#FF2A3C` for small red
  text on black (5.3:1). The brand `#EF001D` fails AA for both by a hair.
- `/about` was **dropped**, not rebuilt: it was template filler. Returns when real coach bios exist.
- `legal.html` is `noindex`; `wix-archive/` is disallowed in `robots.txt` so old pages are not
  indexed as duplicates.
- Branch is `main` (lowercase) on purpose; the sister repos' capital-M `Main` is a documented trap.
