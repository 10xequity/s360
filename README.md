# Shoot 360 Denver — Website

**Version** 0.1 · **Updated** 2026-09-16 · **Status** Built for owner review; private; the live shoot360denver.com is still on Wix

Static site — plain HTML/CSS/JS, no build step — intended for **GitHub Pages**, the same stack as
coloradoboom.com and boomtownathletics.com. This repo also holds a complete archive of the Wix site
it replaces.

Change history: `CHANGELOG.md`. How to edit safely: `EDITING_GUIDE.md`. Open decisions: `HANDOFF.md`.
Why it is built this way: `docs/gap-analysis_v1_2026-09-16.md` and `docs/site-design-spec_v1_2026-09-16.md`.

---

## Read this first

**The branch is `main`, lowercase.** The sister repos use `Main` with a capital M and that has cost
real time. This repo does not.

**Nothing here is public yet.** The repo is private and Pages is off. The domain still points at Wix.
Cut-over steps are in `DEPLOY_GITHUB.md`; the owner decides when.

**Prices and hours come from Shoot 360 HQ's Denver page**, not from Wix. Denver's HQ location id is
`5739019`; the "Join" buttons send people to
`https://www.shoot360.com/membership-pricing?locationId=5739019`, which is where the contract and
payment live. If HQ changes a price, the numbers on `programs.html`, `index.html` and `faq.html`
need a hand edit (the live HQ page is stated as authoritative on those pages).

**The hours on the site are HQ's** (Mon–Fri 1–9 PM, Sat–Sun 10–5). Wix said 9–9 daily. Unconfirmed.

**`wix-archive/` is 237 MB of originals.** It is disallowed in `robots.txt` and not linked from any
page. Do not delete it; it is the only copy of the logo pack and the training clips at full size.

---

## Files

**6 pages** — `index.html`, `technology.html`, `programs.html`, `faq.html`, `contact.html`, `legal.html`

| Path | What it is |
|---|---|
| `assets/css/styles.css` | All styling. Brand tokens are `:root` variables at the top. |
| `assets/js/main.js` | Date-gated visibility, nav toggle, scroll reveal, FAQ accordion, video facade, back-to-top, analytics hook. |
| `assets/img/` | 42 web-sized images derived from the archive by `wix-archive/optimize.py`. Re-run it to regenerate. |
| `assets/video/` | Four 720p clips (Wix transcodes). Hero uses `facility-tour-720p.mp4`. |
| `robots.txt`, `sitemap.xml`, `.nojekyll` | SEO and Pages plumbing. **Keep `.nojekyll`.** |
| `wix-archive/` | The old site: HTML, media, logo pack, fonts, text inventory, screenshots. Read its README. |
| `docs/` | Gap analysis, franchise research, design spec. |

No `CNAME` yet — added at cut-over.

---

## Update the site

Edit a file, commit to `main`. Once Pages is on, it redeploys in about a minute.

```bash
git add -A && git commit -m "what changed" && git push origin main
```

Anything touching the header, footer or hours is a **six-file edit** because shared blocks are
copy-pasted (see `EDITING_GUIDE.md`). Preview locally with `python -m http.server 8765` from the
repo root and open `http://127.0.0.1:8765/`.

---

## Content state (2026-09-16)

- Primary CTA everywhere: **Book a Free Workout** → SalonCloud Plus form (same as Wix and every franchise).
- Pricing shown: Rookie $159 · Pro $199 · Hall of Fame $379 (12-mo, "most popular") · All-Star $389 ·
  12-visit pack $480 · guest workout $72. Coaching sessions included in tiers are non-recurring.
- Programs: free evaluation, memberships, packs/drop-in, camps-classes-clinics, Nike Basketball
  Camps (link), leagues (via app), MySpark Denver $1,000 grant (link), team inquiry (phone/email).
- Not on the site because the owner has not supplied it: coaches, testimonials, Google reviews link,
  inquiry form, any new offerings (parties, rentals). See `HANDOFF.md`.
