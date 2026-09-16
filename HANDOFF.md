# HANDOFF — Shoot 360 Denver site

**Version** 0.2 · **Updated** 2026-09-16 · **Status** Public for review at https://10xequity.github.io/shoot360-denver-site/ · The public domain shoot360denver.com is still Wix

## Where things stand

- Repo `10xequity/shoot360-denver-site`, branch `main` (lowercase), **public**, GitHub Pages on.
- Seven pages: `index`, `technology`, `programs`, `parties`, `faq`, `contact`, `legal`.
- Lighthouse mobile: 100 / 100 / 100 (accessibility, best practices, SEO) on home, programs, parties.
  Home CLS 0.00, LCP 326 ms locally. Fonts are self-hosted; no third-party request before first paint.
- `python scripts/preflight.py --external` must exit 0 before DNS moves. Today it reports
  **27 yellow placeholders** (`class="tbd"`) and nothing else.
- Everything from the Wix site is preserved under `wix-archive/` (see its README).
- Analysis: `docs/gap-analysis_v1_2026-09-16.md`, `docs/franchise-research_v1_2026-09-16.md`,
  `docs/site-design-spec_v1_2026-09-16.md`; live ledger artifact "Denver Gap Ledger".

## What the owner still supplies (and exactly where it goes)

Yellow highlights on the review site mark every value below. Search the repo for `class="tbd"`.

| # | Item | Where | Notes |
|---|---|---|---|
| 1 | **Hours** | hero-meta + `[HM-08]` table in `index.html`; `contact.html` table; footer ×7; FAQ "Where are you"; JSON-LD `openingHoursSpecification` ×7 (`13:00`/`21:00`, `10:00`/`17:00`) | Site shows HQ's Mon–Fri 1–9, Sat–Sun 10–5. Owner said hours come next run. |
| 2 | **GoHighLevel embed codes** | `contact.html` → `#ghl-contact`; `parties.html` → `#ghl-party` | Paste the GHL embed (iframe + script) inside the div, delete `hidden`, delete the "Online form coming" callout beneath. |
| 3 | **Party packages** | `parties.html` `[PT-02]` and `[PT-04]` | Price per package, member price, max athletes, duration, extra-athlete fee, deposit %, lead time, final-count deadline. Package names (Rookie / Pro / MVP) and inclusions are proposals; edit freely. |
| 4 | **Family discount** | `programs.html` `#family` callout | Two percentages (second athlete, third+). |
| 5 | **Pause / suspension terms** | `programs.html` `#policies` first panel | Max months per year, monthly fee, notice days. |
| 6 | **Shots tracked total** | `index.html` `[HM-COUNT]` | Put digits in `data-count`, delete the inner yellow span. Refresh monthly; the number only animates, it does not update itself. |
| 7 | **Behold feed id** for @shoot360denver | `index.html` `#ig` `data-feed` | Create the feed in the same Behold account coloradoboom.com uses; allowed domains must include shoot360denver.com and the github.io review URL. |
| 8 | **Coach bios and the Denver story** | new `about.html` (not yet built) | Names, photos, two lines each. The card component exists. |
| 9 | **Google review quotes** (optional) | `index.html` `[HM-REV]` | Only if the Business Profile has good ones; the public listing hides review text. Add a `.reviews` grid of three `.review` cards. |
| 10 | **Class schedule** (only if classes run on fixed times) | `programs.html` `#camps` | Table with `data-show-until` dates so it retires itself. |
| 11 | **Analytics** | `assets/js/main.js` `GA_MEASUREMENT_ID`, or Cloudflare Web Analytics once proxied | Nothing records today. |

Also confirm: the footer's "independently owned and operated Shoot 360 location" wording against the
franchise agreement; the party inclusions (coach for the whole party, table time, "you bring the food").

## How to fill a placeholder safely

1. Open the file, search `class="tbd"`, replace the whole `<span class="tbd">…</span>` with the value.
2. Run `python scripts/preflight.py`. The placeholder count must go down and problems must stay 0.
3. Commit to `main`. Pages redeploys in about a minute.

## Going live (after the placeholders are gone)

`CNAME` with `www.shoot360denver.com` → Settings → Pages → Custom domain → DNS (Cloudflare
recommended, same as the sister sites) → Enforce HTTPS → check every page → unpublish Wix →
cancel Wix Premium at renewal. Full steps: `DEPLOY_GITHUB.md`. Then: Search Console verify and
submit the sitemap; point the Google Business Profile website field at the new domain.

## Facts the build relies on

| Fact | Source |
|---|---|
| Address 14200 E Alameda Ave, Aurora CO 80012, inside FieldhouseUSA; phone 720-262-5501; email info@shoot360denver.com | Wix site + shoot360.com/denver + Google listing |
| HQ location id **5739019** (pricing and trial links) | shoot360.com/denver |
| Prices: Rookie $159 · Pro $199 · Hall of Fame $379 (12-mo) · All-Star $389 · 12-visit pack $480 · guest $72 | shoot360.com/membership-pricing?locationId=5739019, rendered 2026-09-16 |
| Coaching included in every membership; no fee for coaching during sessions | Owner, 2026-09-16 |
| Homeschool sessions weekdays 2–4 PM; parties are sold | Owner, 2026-09-16 |
| Google listing: 4.7 stars, CID 8030805088891520148, place /g/11pd1hmkmh | Google Maps, 2026-09-16 |
| Membership booking URL `shoot360-prod.saloncloudsplus.io/ghl/athlete-info` | Wix site CTAs (same on every franchise) |
| Facility numbers 4 bays / 4 full courts / 2 half courts; 30 + 30 skills games; 300+ shots per 30-min | Wix site copy |

## Known limits

- Party package names, inclusions and structure are proposals modelled on the Kirkland location; the
  owner should edit them, not just fill the numbers.
- The savings calculator's default trainer rate ($75/hr) is a slider default, not a published market figure.
- Wix screenshots in the archive are viewport-only.
- Repo is ~250 MB because the archive keeps originals.

## Trap log

- Long prose or multi-line code through a bash heredoc dies on quoting; write files with the Write
  tool, run them from disk. Bit twice this project.
- Wix Media Manager listing exceeds the 50 KB tool cap; page 12 files at a time with `paging.cursor`.
- Any page with a `<video>` (Wix's or ours) times out headless screenshots; strip the element first.
  Tall viewports time out too; viewport-sized shots only.
- HTML `height` attributes + CSS `width` only = distorted images. Keep `img{height:auto}` in the base rule.
- Google Fonts by `<link>` caused CLS 0.34 on the hero headline. Self-host and preload.
- White on brand red `#EF001D` is 4.49:1. Fills use `#E0001B`; small red text on black uses `#FF2A3C`.
