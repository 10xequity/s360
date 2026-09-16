# Wix archive — shoot360denver.com as of 2026-09-16

**Status** Frozen snapshot. Nothing in this folder is served by the new site; it exists so the old
build can be consulted or restored.

Source: Wix Studio site "Shoot 360 Denver" (site id `c1fb6280-139d-42e0-a311-cc402abef750`,
Premium plan, created 2026-01-19, last edited 2026-06-22). Apps installed on it: Instagram Feed,
Promote SEO, Wix Forms, Wix Hotels (unused), Wix Invoices (unused).

| Path | What it is |
|---|---|
| `pages/*.html` | Server-rendered HTML of all 6 published pages (home, about, technology, contact, privacy-policy, terms-and-coniditions — the typo is Wix's URL). Fetched with a browser user-agent. |
| `content-inventory.md` | Every visible string, link and image alt on each page, in DOM order. Start here to see what the old site said. |
| `media/` | All 47 Media Manager uploads at original resolution + the 2 Wix stock assets the pages used, keyed by Wix file id. Videos are Wix's 1080p transcode (raw upload not exposed). |
| `media/_zips/` | The three archive uploads, unzipped alongside: **official Shoot 360 logo pack** (.ai + .png in red/black/white, flat, stacked, icon), **Fonts.zip** (Gotham, Tungsten, Campton — licensed faces, do NOT publish on the web without a licence), Icon.zip. |
| `media/_wix-template-placeholders/` | 11 stock images from the never-finished `/about` template page (robots, fake founders, fake press logos). Not brand assets. |
| `MEDIA_MANIFEST.md` | File id → display name → dimensions → which page used it. |
| `media-manager-list.json`, `videos.txt`, `extra-names.txt`, `media-ids.txt` | Raw listings the manifest was built from. |
| `contact-sheet.jpg`, `logo-sheet.jpg` | One-glance thumbnails of everything above. |
| `screenshots/` | Viewport captures of the live Wix pages at 1440px wide. Full-page capture timed out on Wix's renderer, so these show the top of each page only. |
| `*.py` | The throwaway scripts that produced this folder and the web-sized assets in `/assets/img`. |

## Defects found in the live Wix site

Worth knowing even if the Wix site is never touched again.

- Footer email link points to `mailto:info@mysite.com` and the phone link to `tel:123-456-7890` — Wix
  template defaults never replaced. The visible text is right; the links are wrong, on every page.
- The visible phone number is a link to a Google search results URL, not `tel:`.
- `/about` is untouched template filler ("Improving Everyday Life With Robotics", founders "Sarah
  Suarez / Mike Deng / Reay Finigan", "Volaso in the News"). It is in the sitemap and indexable.
- `/contact` form posts to Wix; there is no confirmation of where submissions land.
- Hours say "Summer Hours … 9 AM – 9 PM" year-round; HQ's Denver page (shoot360.com/denver) lists
  Mon–Fri 1–9 PM, Sat–Sun 10 AM–5 PM.
- The privacy page's "Contact Form" link goes to shoot360.com (HQ), not this site.
- Only `WebSite` schema; `<title>` is "Home | Shoot 360 Denver" with no city or keyword; no meta description.
- Hero and section images ship as 13–25 MB originals behind Wix's resizer.
