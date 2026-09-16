# Shoot 360 Denver — website gap analysis and recommendations

**Version** 1.0 · **Date** 2026-09-16 · **Status** Delivered with site v0.1 · **Supersedes** none
**Benchmark set** 19 own-domain Shoot 360 franchise sites + 22 HQ location pages on shoot360.com, fetched 2026-09-16 (full notes: `franchise-research_v1_2026-09-16.md`)

## 1. Bottom line

The Wix site had one job, "apply for membership", and did it behind a wall: no price, no hours that
matched HQ, no free-workout offer in the words every other franchise uses, and broken template
links in the footer. Against 19 sister sites, Denver was last or tied-last on nine of fifteen
marketing features. Site v0.1 in this repo closes the eleven gaps that needed no owner input; the
remaining five (coach bios, testimonials, a working inquiry form, a class schedule if one exists,
and any added offerings such as parties or rentals) need content or a vendor decision from the owner.

## 2. What the Wix site actually had (audit, 2026-09-16)

| Item | Finding |
|---|---|
| Pages | 6 published: home, technology, contact, privacy, disclaimer, and an `/about` that is untouched template filler (robots, fake founders, "Volaso in the News") sitting in the sitemap |
| Primary CTA | "Get recruited: apply for membership" → SalonCloud Plus form. Same form every franchise uses for the **free workout**; Denver labels it as an application |
| Free workout | Mentioned once, small, as "Try it for free — schedule a free membership evaluation session" |
| Pricing | None. HQ's Denver pricing page (`locationId=5739019`) has been live the whole time |
| Hours | "Summer Hours 9 AM–9 PM daily", year-round. HQ lists Denver as Mon–Fri 1–9 PM, Sat–Sun 10–5 |
| Contact links | Email link → `info@mysite.com`; phone link → `tel:123-456-7890`; visible number links to a Google search URL. Template defaults never replaced, on every page |
| SEO | Title "Home \| Shoot 360 Denver", no meta description, `WebSite` schema only |
| Media | 13–25 MB originals behind Wix's resizer; five short training clips and a facility clip uploaded but only two used |
| Trust | Partner logos (Nike, Wilson, Denver Nuggets); no reviews, no coaches, no testimonials |
| Stale | "11 Membership Capacity Left" scarcity counter; "Nike Basketball Camps in July" with no date logic |

## 3. Feature gap table

Prevalence counts the 19 live own-domain franchise sites unless noted. Priority: **P1** conversion-critical,
**P2** trust and discoverability, **P3** nice to have.

| # | Feature | Network prevalence | Denver on Wix | Recommendation | Priority | v0.1 status | Needs from owner |
|---|---|---|---|---|---|---|---|
| 1 | Free first workout as the primary CTA with a direct booking path | 19/19 sites + 22/22 HQ pages | Buried; CTA says "apply" | Make "Book a Free Workout" the one red button on every page, header and footer, linking to the same SalonCloud form | P1 | **Built** | — |
| 2 | Public pricing | 9 full + 8 partial | None | Show all six Denver price points; link "Join" to HQ's live Denver pricing page so payment and contract stay in Shoot 360's system | P1 | **Built** (prices as of 2026-09-16) | Re-check quarterly or when HQ changes prices |
| 3 | Hours and street address on the home page, with map | 16/19 + 22/22; map on 9 | Hours only, wrong season; no map | Hours block, address, directions link and embedded Google Map on home and contact; `OpeningHoursSpecification` schema | P1 | **Built** with HQ's hours | **Confirm which hours are right** (HQ vs Wix) |
| 4 | Full programs menu on its own page | 17/17 | Scattered across home and technology | `programs.html`: free evaluation, four membership tiers, 12-visit pack, guest workout, camps/classes/clinics, Nike camps, leagues, MySpark grant, team inquiry | P1 | **Built** | Decide whether to add birthday parties, court rentals, team training as offerings (15 sites sell parties) |
| 5 | Mobile app promotion with store badges | 22/22 HQ + ~10 sites | Present on technology page only | App section on home, programs, technology, contact and footer | P2 | **Built** | — |
| 6 | Nike Basketball Camps section | ~12 | One tile, "in July" | Callout on programs and a home tile linking to the US Sports Camps page, wording that does not go stale | P2 | **Built** | — |
| 7 | Video: facility tour and technology demo | 9 | One Vimeo embed | Six archived clips served self-hosted at 720p behind click-to-play posters; facility clip as hero background | P2 | **Built** | — |
| 8 | FAQ with FAQPage schema | 6 (Frederick's 16 questions is the model) | None | 15 questions on `faq.html`, five repeated on home, all in schema for rich results | P2 | **Built** | — |
| 9 | Local-SEO titles, meta descriptions, LocalBusiness-type schema | Titles on 7; schema on 6 | None | City + keyword titles, descriptions, `SportsActivityLocation` with hours and `sameAs` on every page, sitemap, robots | P2 | **Built** | Paste Search Console token; submit sitemap |
| 10 | Correct `tel:` and `mailto:` links | All | Broken | Fixed everywhere | P1 | **Built** | — |
| 11 | Fast, lightweight pages | Varies (Wix/Squarespace heavy) | 1.4 MB HTML per page + multi-MB images | Static HTML, images resized to web sizes (5.5 MB total for 42 files), lazy loading, no framework | P2 | **Built** | — |
| 12 | Lead-capture form beyond the membership application | 12/19 | Wix contact form (destination unknown) | Add a short inquiry form. Static hosting needs a backend: Google Form (free, like the Colorado Boom site), Formspree, or a GoHighLevel form embed if Denver has GHL access | P2 | Not built | **Pick a form backend** |
| 13 | Coach bios with photos | 6 sites (12 bios at Lincoln, Charlotte, KC); HQ has 17 | None (template fakes on `/about`) | `about.html` with the Denver story and coach cards; the CSS card component already exists | P2 | Not built | **Names, photos, 2-line bios** |
| 14 | Testimonials with outcomes, or Google rating | 8 sites; no one embeds live Google reviews | None | Three parent/player quotes with a result ("+8% from three"), plus a link to the Google Business Profile. A live-rating embed would be a network first | P2 | Not built | **Real quotes with permission; Google Business Profile URL** |
| 15 | Age-banded youth classes with a schedule | 8 | None | Only if Denver runs scheduled classes: a schedule table with `data-show-until` dates so it retires itself | P3 | Not built | Class list and times, if any |
| 16 | Blog or news | 2 live | None | Skip. Low prevalence, high upkeep | P3 | Skipped | — |
| 17 | Spanish content | 0/19 | None | Skip for now; Aurora's demographics make it a real differentiator later | P3 | Skipped | — |
| 18 | Instagram feed on page | 0 confirmed (Wix app on Denver) | Wix Instagram app | Links only. A feed needs a Worker + Behold like coloradoboom.com; reuse that pattern if wanted | P3 | Links built | — |

## 4. Pricing benchmark

Denver prices from HQ's live Denver page on 2026-09-16; network figures from nine franchises that publish prices.

| Tier | Denver | Network range (9 sites) | Denver vs. network |
|---|---|---|---|
| Rookie, 4 visits/mo | $159 (3-mo) | $89–$159 | At the top of the range |
| Pro, 8 visits/mo | $199 (3-mo), 1 coaching session | $119–$199 | At the top |
| All-Star, unlimited | $389 (3-mo), 2 coaching sessions | $149–$239 | **~60% above the highest peer** |
| Hall of Fame, unlimited 12-mo | $379, 2 sessions, 15% off programs | $119–$209 | **~80% above the highest peer** |
| 12-visit pack | $480 ($40/visit) | $500 (Frederick) | In line |
| Guest workout | $72 | $45 (Frederick), $50 (Walnut Creek) | Highest seen |
| Enrollment fee | not shown | $25–$199 | Unknown |

[INFERENCE] Denver is positioned as premium ("exclusive, world-class sanctuary … luxury training
experience" is the Wix vision statement). That is a defensible position only if the site earns it:
the unlimited tiers cost more than a Frederick unlimited plus a private coach. v0.1 leans into the
premium framing (dark palette, technology-first, coaching included in tiers) and leads with the free
workout so price is discovered after value. If conversion is weak, the first lever is a Rookie tier
closer to $129, not a redesign.

## 5. Technical and SEO gap table

| Area | Wix today | v0.1 | Still open |
|---|---|---|---|
| Hosting | Wix Studio Premium (recurring fee) | GitHub Pages, free, same stack as coloradoboom.com | DNS cut-over; decide Cloudflare in front (recommended, same as sister sites) |
| Page weight | ~1.4 MB HTML + images up to 25 MB | Home first view ≈ 0.5 MB before the hero video, which streams | Lighthouse run after deploy |
| Structured data | `WebSite` | `SportsActivityLocation`, `FAQPage`, `BreadcrumbList` | Google Business Profile link in `sameAs` |
| Indexing | `/about` template page indexable | `/about` gone; archive folder disallowed in robots; `legal.html` noindex | Search Console verify + sitemap submit |
| Analytics | Unknown (Wix) | Inert GA hook in `main.js`; Cloudflare Web Analytics needs no code | Owner: pick one |
| Accessibility | Not audited | Skip link, landmarks, keyboard nav and accordion, 4.5:1 contrast checked, reduced-motion honoured, alt text on all content images | Screen-reader pass after owner content lands |
| Fonts | Gotham (licensed, uploaded to Wix), DIN | Rajdhani + Open Sans (HQ's faces, free) | — |
| Forms | Wix Forms | None | Form backend decision |

## 6. Ideas worth borrowing from the network

- **Savings calculator** (Memphis): "one private trainer session vs. one month unlimited" slider. Strong fit for Denver's premium price.
- **Live shots-tracked counter** (Huntsville): a number that only goes up is a cheap trust signal, if HQ exposes it.
- **Homeschool daytime program** (Vero Beach, Oakville): Denver is closed weekday mornings per HQ hours; a 10 AM–1 PM homeschool block would monetise dead court time.
- **Family membership** (El Dorado Hills $240, Lincoln): siblings are the norm in youth basketball.
- **Published suspension/cancellation policy** (Huntsville, San Mateo): reduces sign-up anxiety on a 12-month contract.
- **Party pricing table + party FAQ** (Kirkland): if Denver ever sells parties, copy the structure.

## 7. Roadmap

| Version | Scope | Blocked on |
|---|---|---|
| **v0.1** (this repo) | Six pages, brand assets, pricing, hours, map, FAQ, schema, videos, archive of Wix | — |
| v0.2 | `about.html` with coaches; testimonials block on home; inquiry form; Google Business Profile link; analytics on | Owner content + two decisions |
| v0.3 | Any new offerings (parties, rentals, team training, homeschool block, family tier) with their own sections and FAQ entries | Owner decides what to sell |
| Go-live | Make repo public (or GitHub Pro), enable Pages, `CNAME`, DNS, HTTPS, unpublish Wix, cancel Wix Premium | Owner go-ahead; see `DEPLOY_GITHUB.md` |
| Later | Spanish, blog, live counter, Instagram feed via Worker | Demand |

## 8. Sources

Live Wix site and Media Manager (archived in `wix-archive/`); shoot360.com/denver and
shoot360.com/membership-pricing?locationId=5739019 (rendered in a browser, 2026-09-16); 19 franchise
sites and 22 HQ location pages listed with URLs in `franchise-research_v1_2026-09-16.md`; Shoot 360
2025 year-end press release (PR Newswire, network size). Anything marked unverified there stays unverified here.
