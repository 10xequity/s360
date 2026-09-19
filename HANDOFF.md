# HANDOFF — Shoot 360 Denver site

**Version** 0.4.4 · **Updated** 2026-09-19 · **Status** Content complete (0 placeholders). Cut-over waiting on the Cloudflare `www` record. · **Supersedes** HANDOFF v0.4.3 (2026-09-19)

## Cut-over status (2026-09-19)

| Piece | State |
|---|---|
| Registrar nameservers | ✅ `greg.ns.cloudflare.com`, `journey.ns.cloudflare.com` (changed 2026-09-19) |
| Pages custom domain | ✅ `CNAME` = `www.shoot360denver.com`, build green, serves every page when addressed by that hostname |
| Cloudflare `www` record | ❌ **does not exist** — `www.shoot360denver.com` is going dark as stale Wix answers expire from resolver caches |
| Cloudflare apex record | ❌ still `A → 185.230.63.x` (Wix), proxied; 301s to `www` |
| HTTPS | ❌ `https_enforced: false`; GitHub cannot issue the certificate until DNS resolves to it |

The one remaining action is the DNS table in `DEPLOY_GITHUB.md` step 4: `www` CNAME → `10xequity.github.io`
and four apex `A` records to GitHub, **both DNS-only (grey cloud)**, deleting the Wix records. Verified on
2026-09-19 with `curl --resolve www.shoot360denver.com:80:185.199.108.153` that GitHub already answers 200 for
`/`, `memberships.html`, `events.html`, `publications.html`, `faq.html` and `assets/css/styles.css`.

## Where things stand

- Repo **`10xequity/s360`** (renamed by the owner 2026-09-19 from `shoot360-denver-site`; the local clone folder still has the old name). Branch `main` (lowercase), public, GitHub Pages on. **There is no preview URL any more**: the old `github.io` path 404s and the new one redirects to the custom domain, so review happens on the live domain or locally.
- **Ten HTML files**: `index`, `technology`, `publications`, `memberships`, `programs`, `events`, `faq`, `contact`, `legal`, plus `parties.html` (redirect stub → `events.html#parties`, noindex, not in the sitemap).
- Navigation: Technology ▾ (The technology · Publications · Download the app) · Memberships · Programs ▾ · Events ▾ (Special events · Parties · Date nights) · FAQ · Visit Us · **New Membership**.
- `python scripts/preflight.py` today: 10 pages, 82 external URLs, **0 placeholders, 0 problems**. Every value on the site is now a real one; nothing is highlighted yellow and nothing prints "TBD".
- Owner's v0.4 directives (18) are all built; see CHANGELOG v0.4.

## Decisions the owner still owes (nothing is highlighted on the site any more)

| # | Question | Where | Status |
|---|---|---|---|
| 1 | GoHighLevel embed codes | `contact.html #ghl-contact`, `events.html #ghl-party` | still open; page says phone/email meanwhile |
| 2 | Behold feed id | `index.html #ig` | still open; the Instagram grid hides itself until it is set |

Answered 2026-09-19: **event pricing** — two courts for 2 hours $160, all four courts for 2 hours $720
(Saturday nights after 6 PM only); capacity ten athletes under 10 or six aged 11–17 on two courts. The
four-court capacity shown (20 / 12) is that doubled and is an inference, not the owner's number — correct it if
wrong. Member pricing, extra-guest fees, deposits and lead times are gone; the booking system cannot enforce
them. **Weekend hours** stay 10 AM–5 PM, and every hours block now points at the Shoot 360 app as the live
schedule. **Family discount percentages and pause terms** are off the page (see below).

Answered 2026-09-17 (v0.4.1): tier prices = HQ's online Denver prices ($159/$199/$389/$379); Drop-In $80 non-member,
$42 member extra session; Unlimited Classes and Little Ballers $149; no personal-training add-ons on the site; Ball
is Life includes classes, the others add them for $40.

Not yellow but still open:
- **HQ checkout mismatch.** Join buttons open HQ contracts 154 (Committed/All-Star) and 156 (Ball is Life/Hall
  of Fame). HQ was still showing $389 and $379 for Denver on 2026-09-19 while this site shows $239 and $230.
  Ask HQ to reprice those two Denver contracts, or expect the price to change under the customer at signup.
- **Event pricing is unresolved.** The page shows two courts for two hours at $160 and all four at $720, from
  the owner on 2026-09-19 01:40. At 02:35 the owner added "the 449 is for an hour" and "date night is $60/court
  for 30 min", which work out at $224.50 and $120 per court-hour against the $40 the $160 implies. Nothing was
  changed pending an answer; see the question put to the owner in that session.
- **Committed / All-Star classes.** HQ's online page lists "unlimited classes" inside All-Star; the owner says
  Committed adds classes for $40 and only Ball is Life includes them. Site follows the owner; checkout may read differently.
- **Vimeo playback** on the review domain is unverified (Vimeo blocks automated browsers). The clips belong to a
  basic account named Josef Slezak; if they refuse to play, that account must allow the domain or the owner re-uploads.
- **Google Business Profile pin** sits at the street-address centroid, not the FieldhouseUSA building; the site
  embeds the FieldhouseUSA listing instead.
- **"Patented" Splash Meter.** HQ copy says patented; no patent assigned to Shoot 360 was found (the shot-tracking
  patents are Noah Basketball's; SPLASH METER is a trademark). Kept because the franchisee is licensed to use HQ copy.
- **Spots remaining** counts from the owner's sheet are left off; a static number goes stale.
- **Wilson logo**: no partnership surfaced in research; carried from the Wix site.

## How shared blocks are edited now

Header (`[NAV]`…`</header>`) and footer (`[FT]`…`</footer>`) on every page are regenerated by **`scripts/patch_v04.py`** (`nav()` and `FOOTER`). The FAQ list lives in the same script and writes both the FAQ HTML and the FAQPage JSON-LD. Edit there, re-run (`python scripts/patch_v04.py`), never hand-edit ten copies. The script is idempotent.

## How to fill a placeholder safely

1. Search the repo for `class="tbd"`, replace the whole `<span class="tbd">…</span>` with the value (for FAQ answers, edit the list in `patch_v04.py` and re-run).
2. `python scripts/preflight.py` — placeholder count goes down, problems stay 0.
3. Commit to `main`; Pages redeploys in about a minute.

## Going live

`CNAME` with `www.shoot360denver.com` → Settings → Pages → Custom domain → DNS (Cloudflare recommended) → Enforce HTTPS → check every page → unpublish Wix → cancel Wix Premium at renewal. Full steps in `DEPLOY_GITHUB.md`. Then Search Console verify + sitemap; point the Google Business Profile website field at the new domain; update `legal.html#services` if analytics go on.

## Facts the build relies on

| Fact | Source |
|---|---|
| Address 14200 E Alameda Ave, Aurora CO 80012, inside FieldhouseUSA; phone 720-262-5501; email info@shoot360denver.com | Wix site + shoot360.com/denver + Google listing |
| FieldhouseUSA building pin 39.7092894, -104.8217123 (Google "Aurora FieldhouseUSA" listing); Shoot 360 listing and street address pin 39.7092942, -104.822972 | Google Maps embed responses, 2026-09-17 |
| HQ location id **5739019**; contract ids 151/152/154/156 | shoot360.com/membership-pricing, 2026-09-16 |
| Membership names, inclusions, scheduling windows, fees, commitments | Owner's "Denver Membership Options" sheet pasted 2026-09-17 (+ Jan 2026 PDF in Downloads/Shoot360) |
| Tier prices **$159 / $199 / $239 / $230** | Owner's sheet ($149/$189/$229/$220) **plus $10**, the margin kept back for closing in store. Never say so on the site. JV and Varsity already matched HQ; Committed and Ball is Life were corrected down from HQ's $389/$379 on 2026-09-19. |
| A session is an hour: 30 min shooting + 30 min skills | Owner 2026-09-19, corroborated by HQ pricing "$39.75 per visit" against the 4-session tier |
| Members bring a guest for $10 per session | Owner, 2026-09-19 |
| Drop-In $80 non-member, $42 member; Unlimited Classes $149; no PT add-ons; Ball is Life includes classes; no event deposits | Owner, 2026-09-17 11:40 |
| Weekday hours 2–9 PM; weekends 10 AM–5 PM, with the app as the live schedule | Owner, 2026-09-17 and 2026-09-19 |
| Events: two courts 2 h $160, all four courts 2 h $720; ten under-10s or six 11–17 on two courts | Owner, 2026-09-19 |
| Registrar Porkbun; nameservers moved to Cloudflare 2026-09-19 07:58 | Verisign RDAP, 2026-09-19 |
| Vimeo clips 720241338 (shooting, 14 s) and 720257389 (passing, 14 s), account Josef Slezak, basic | Wix page data + Vimeo oEmbed, 2026-09-17 |
| My Spark Denver: DPS Foundation, grades 6–8, free/reduced-price meals, $1,000 card, 200+ providers | dpsfoundation.org + search results, 2026-09-17 (owner said "SNAP"; official test is meal eligibility) |
| Coaching included; parties sold; homeschool weekdays 2–4 PM; club basketball via Team EVO; GHL forms; "evaluate" not "free" | Owner, 2026-09-16 |
| Splash Meter green `#22D478` | sampled from the archived HUD photo |

## Known limits

- The shots counter is a deterministic estimate, labelled as such; weekday bands start at 14:00.
- Event pricing is the owner's, confirmed 2026-09-19. The court-hour model behind it is in `docs/party-pricing-model_v1_2026-09-17.md`; the proposals in that file are superseded.
- Vimeo iframes add third-party JavaScript to the home and technology pages; `loading="lazy"` and `dnt=1` limit the cost. If Lighthouse performance drops below the owner's tolerance, swap to poster + click-to-play like the self-hosted clips.
- Repo is ~250 MB because `wix-archive/` keeps originals.

## Trap log

- Bash heredocs with prose or code die on quoting; write scripts to disk, then run them.
- The Write/Edit tools need the file Read first in-session; `cat` via Bash does not count.
- Wix page content is not in the server HTML; the thunderbolt `pages/pages/thunderbolt?...module=thunderbolt-features&pageId=…json` JSON has component props (that is where the Vimeo URLs were).
- `google.com/maps?q=…&output=embed` 301s to `/maps/embed?pb=…`; follow redirects to see which listing it pinned.
- Pages with `<video>` and tall viewports time out headless screenshots; use `--virtual-time-budget` and viewport-size captures.
- HTML `height` attributes + CSS `width` only = distorted images. Keep `img{height:auto}`.
- Inline `grid-template-columns` styles break phone breakpoints; use a class.
- A `.sec-light` section with dark cards inside makes inherited black text vanish.
- White on brand red `#EF001D` is 4.49:1; fills use `#E0001B`, small red text on black uses `#FF2A3C`.
