# HANDOFF — Shoot 360 Denver site

**Version** 0.1 · **Updated** 2026-09-16 · **Status** Built, private, not live. The public site is still Wix.

## Where things stand

- Repo `10xequity/shoot360-denver-site`, branch `main` (lowercase). Private. GitHub Pages **off**.
- Six pages built from the Wix content, HQ's Denver data, and the franchise research:
  `index`, `technology`, `programs`, `faq`, `contact`, `legal`.
- Everything from the Wix site is preserved under `wix-archive/` (HTML, all 47 media uploads at
  original size, logo pack, fonts, text inventory, screenshots). See `wix-archive/README.md`.
- Analysis: `docs/gap-analysis_v1_2026-09-16.md` (what to do and why),
  `docs/franchise-research_v1_2026-09-16.md` (the evidence), `docs/site-design-spec_v1_2026-09-16.md` (what was built).

## Decisions needed from the owner

1. **Hours.** The site shows HQ's listing for Denver: Mon–Fri 1–9 PM, Sat–Sun 10 AM–5 PM. The Wix
   site said 9 AM–9 PM daily ("summer hours"). Pick one; it appears in the hero, visit block, footer,
   FAQ and schema on every page (search `1:00 – 9:00 PM` and `13:00`).
2. **Inquiry form backend.** Options in order of preference: a Google Form on the business account
   (free, same as coloradoboom.com; paste the `forms.gle` link, never the `/edit` URL) · a
   GoHighLevel form embed if Denver has GHL access · Formspree (free tier, 50/mo). Until then the
   contact page offers phone, email and the free-workout booking.
3. **Coaches and story for `about.html`.** Names, photos, two lines each, plus who owns Denver and
   why. Card component exists; page does not.
4. **Testimonials.** Three real quotes with permission and, ideally, a number in each. Plus the
   Google Business Profile URL so reviews can be linked and added to schema `sameAs`.
5. **Offerings to add or not.** Birthday parties (15 of 19 sister sites), court rentals (8), team
   training (many), homeschool daytime block (2), family tier (2). Nothing is published until you say it exists.
6. **Analytics.** Cloudflare Web Analytics (no code, once the domain is proxied) and/or Google
   Analytics (paste the `G-` id in `assets/js/main.js`). Nothing records today.
7. **Legal wording.** Footer says "An independently owned and operated Shoot 360 location" — confirm
   with the franchise agreement. Privacy and disclaimer text is verbatim from Wix; counsel has not reviewed it.

## Facts the build relies on (verify if anything looks off)

| Fact | Source |
|---|---|
| Address 14200 E Alameda Ave, Aurora CO 80012, inside FieldhouseUSA; phone 720-262-5501; email info@shoot360denver.com | Wix site + shoot360.com/denver |
| HQ location id **5739019** (pricing and trial links) | shoot360.com/denver |
| Prices: Rookie $159 · Pro $199 · Hall of Fame $379 (12-mo) · All-Star $389 · 12-visit pack $480 · guest $72 | shoot360.com/membership-pricing?locationId=5739019, rendered 2026-09-16 |
| Membership booking URL `shoot360-prod.saloncloudsplus.io/ghl/athlete-info` | Wix site CTAs (same on every franchise) |
| Nike camp URL, MySpark grant URL, app store ids | Wix site |
| Facility numbers 4 bays / 4 full courts / 2 half courts; 30 + 30 skills games; 300+ shots per 30-min | Wix site copy (Wix said 323 shots) |
| Partner logos Nike, Wilson, Denver Nuggets | Wix "Our Industry Partners" |

## Going live (summary; full steps in `DEPLOY_GITHUB.md`)

Make the repo public (Pages on a private repo needs GitHub Pro) → Settings → Pages → `main` /(root)
→ add `CNAME` with `www.shoot360denver.com` → DNS at the registrar (or move DNS to Cloudflare like
the sister sites) → Enforce HTTPS → check every page → unpublish Wix → cancel Wix Premium at renewal.

## Known limits of v0.1

- Screenshots of the old Wix pages are viewport-only (full-page capture timed out on Wix's renderer).
- Hero video is the 720p transcode of the "around the facility" clip (2.7 MB); reduced-motion users
  get the poster.
- No Instagram feed. Wix's app does not port; a Cloudflare Worker + Behold (as on coloradoboom.com) would.
- Repo is ~245 MB because the archive keeps originals. Fine for GitHub; do not add more originals
  without a reason.

## Trap log

- Long prose through a bash heredoc died on a quote; write docs with the Write tool (already a memory rule).
- Wix Media Manager listing exceeds the tool output cap at 50 KB; page it 12 files at a time with the cursor.
- White on brand red `#EF001D` is 4.49:1. Fills use `#E0001B` (5.0:1); small red text on black uses `#FF2A3C` (5.3:1).
