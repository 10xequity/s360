# Shoot 360 Denver website — design spec

**Version** 1.0 · **Date** 2026-09-16 · **Status** Built as v0.1 for owner review · **Supersedes** none
**Repo** github.com/10xequity/shoot360-denver-site (private until the owner flips it) · **Live today** shoot360denver.com on Wix

## 1. Goal

Replace the 4-page Wix brochure with a marketing site that turns local search traffic and ad clicks
into booked free workouts, on the same zero-cost, no-build static stack already running
coloradoboom.com and boomtownathletics.com (plain HTML/CSS/JS on GitHub Pages behind Cloudflare).

Success looks like: a parent in Aurora searching "basketball training near me" lands, understands
what Shoot 360 is in ten seconds, sees hours, price and location without hunting, and books a free
workout in two clicks.

## 2. Audience and jobs

| Who | What they need from the site |
|---|---|
| Parents of players roughly 7–18 (primary) | Is this legit, what does it cost, where is it, when is it open, can we try it free |
| High-school, college and adult players | What the tech measures, how sessions work, the app, drop-in |
| Coaches and teams | Team training, court time, camps — a contact path |
| Existing members | Hours, app download, phone |

## 3. Information architecture (6 pages)

| File | Purpose | Key sections |
|---|---|---|
| `index.html` | Convert | Hero (video, "Get Better Faster", free-workout CTA) · trust strip (Nike, Wilson, Denver Nuggets partner logos) · how it works (3 steps) · technology teaser · programs grid · membership tiers teaser with live-pricing link · facility numbers · hours + map + address · Nike camps · app download · top FAQ · footer |
| `technology.html` | Explain | Splash Meter (arc, depth, alignment) · Splash Zone · shooting courts · skill courts (passing, ball-handling, virtual trainer) · the app · short clips from the archive |
| `programs.html` | Choose | Free evaluation workout · Memberships (Rookie 4 / Pro 8 / All-Star unlimited / Hall of Fame unlimited 12-month) with live-pricing link · Drop-in · Camps, classes and clinics · Nike Basketball Camps · Leagues via the app · MySpark grant callout |
| `faq.html` | Reassure | 14 questions, FAQPage schema |
| `contact.html` | Reach | Phone, email, address inside FieldhouseUSA, hours, embedded map, free-workout CTA, social |
| `legal.html` | Comply | Privacy (from archive) · participation disclaimer for adults and minors (from archive) · accessibility statement |

Dropped from the old site: `/about` (template filler). Rebuild only when the owner supplies real
team bios and the Denver story.

## 4. Calls to action and integrations (no new vendors)

| Action | Destination | Notes |
|---|---|---|
| Book a free workout (primary) | `https://shoot360-prod.saloncloudsplus.io/ghl/athlete-info` | Same SalonCloud Plus / GoHighLevel form the Wix site and every franchise uses. |
| See current pricing | `https://www.shoot360.com/membership-pricing?locationId=5739019` | HQ page injects Denver's live prices by script. Denver's HQ location id is **5739019** (from shoot360.com/denver). |
| HQ free-trial page | `https://www.shoot360.com/trial?locationId=5739019` | Secondary; the free-workout fine print lives here. |
| Nike Basketball Camps | `https://www.ussportscamps.com/basketball/nike/nike-basketball-camp-shoot360-denver-co` | Existing. |
| MySpark grant | `https://www.grantinterface.com/Opportunity/Catalog?urlkey=dpsf` | Existing. |
| App | App Store `id1177068011`, Google Play `com.Shoot360.Mobile` | Existing. |
| Call / email | `tel:+17202625501`, `mailto:info@shoot360denver.com` | Fixes the template-default links. |
| Map | Google Maps embed by address query, no API key | |
| Instagram / Facebook | `@shoot360denver` | Links only; no feed widget in v1 (Wix's Instagram app does not port). |

General-inquiry form: **not in v1.** A static site needs a form backend (Google Form, Formspree,
or a GoHighLevel form embed). Owner decision, listed in HANDOFF.

## 5. Brand

- **Logos**: official pack recovered from Wix (`wix-archive/media/_zips/Shoot-360-Basketball-Logos/`).
  Header uses the all-white horizontal lockup on black; the red/black "SHOOT 360 DENVER" stacked
  mark is the location mark on light grounds; the red ball icon is the favicon.
- **Colour tokens**: red `#EF001D` (HQ), red-dark `#C20101`, black `#0B0B0B`, ink `#141414`,
  grey-100 `#F3F3F3`, grey-500 `#6E6E6E`, white. Dark-first: black grounds, white type, red for
  the primary action and accents only. Every pairing checked at 4.5:1 or better; white on the red
  is reserved for large bold button text, never body copy.
- **Type**: Rajdhani 600/700 for display (what shoot360.com uses) and Open Sans 400/600 for body,
  both from Google Fonts with system fallbacks. Gotham and Tungsten from the Wix Fonts.zip are
  licensed faces and are **not** shipped.
- **Voice**: HQ taglines verbatim where they exist ("GET BETTER FASTER.", "TRY IT FOR FREE"),
  Denver's own "BOOM" values kept, no invented statistics. Every number on the page traces to the
  archive or to shoot360.com.

## 6. Components (shared by copy-paste, as on the sister sites)

`[NAV]` header with logo, five links, red CTA button, mobile toggle · `[ANN]` optional announcement
bar with `data-show-from` / `data-show-until` date gating · `[FT]` footer with address, hours, app
badges, social, legal links · cards, stat tiles, FAQ accordion with `aria-expanded`, lazy video
facade, back-to-top.

`assets/js/main.js` is ported from colorado-boom-site: date-gated visibility in America/Denver,
nav toggle, scroll reveal, FAQ accordion, back-to-top, inert Google Analytics hook. Same
conventions so one person can maintain all three sites.

## 7. SEO and structured data

- Titles follow `Shoot 360 Denver | Basketball Training in Aurora, CO`, unique per page.
- Meta descriptions on every page; canonical tags; Open Graph image (facility shot).
- JSON-LD: `SportsActivityLocation` (name, address, phone, `openingHoursSpecification`, `sameAs`
  social, `parentOrganization` Shoot 360) on every page; `FAQPage` on faq.html; `BreadcrumbList`
  on inner pages.
- `sitemap.xml`, `robots.txt`, `.nojekyll`. Search Console verification tag slot left commented.

## 8. Accessibility and performance

Semantic landmarks, one `h1` per page, visible focus rings, skip link, keyboard-operable nav and
accordion, `prefers-reduced-motion` respected (video paused, reveals disabled), alt text on every
content image, 4.5:1 contrast. Images resized to 1920px wide or less with `loading="lazy"` below
the fold; hero video is the 720p transcode with a poster and `preload="metadata"`.
Target: under 1.5 MB first view on the home page, Lighthouse 90 or better on all four scores.

## 9. Hosting

GitHub Pages from `main` (lowercase; the sister repos use `Main`, a documented trap this repo
avoids). Custom domain `shoot360denver.com` via `CNAME` plus Cloudflare DNS when the owner is
ready to cut over. Until then the repo stays private and Pages is off. Cut-over checklist in
`DEPLOY_GITHUB.md`.

## 10. Out of scope for v1 (recommended; see the gap analysis)

Coach bios page · testimonials or Google reviews embed · birthday-party and court-rental pages ·
blog · Spanish · general contact form backend · online store · live "shots tracked" counter.
Each needs owner content or a vendor decision.
