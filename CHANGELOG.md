# Changelog — Shoot 360 Denver site

Newest first. Each entry says what changed and why, so the next person does not undo a decision.

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
- No inquiry form: a static site needs a form backend; owner decision.
- `legal.html` is `noindex`; `wix-archive/` is disallowed in `robots.txt` so old pages are not
  indexed as duplicates.
- Branch is `main` (lowercase) on purpose; the sister repos' capital-M `Main` is a documented trap.

**Verification.** Automated check over all six pages: every local link, anchor, image, poster and
video path resolves; every `<img>` has `alt`; one `<h1>` and one `<main>` per page; all JSON-LD
parses. Home first view (HTML + CSS + JS + above-fold images) ≈ 0.5 MB before the hero video, which
streams at 2.7 MB. Rendered locally in Chrome at 1440 px and 390 px.
