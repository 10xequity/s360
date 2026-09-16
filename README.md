# Shoot 360 Denver — Website

**Version** 0.2 · **Updated** 2026-09-16 · **Status** Public for review at https://10xequity.github.io/shoot360-denver-site/ · shoot360denver.com is still served by Wix until DNS moves

Static site — plain HTML/CSS/JS, no build step — on **GitHub Pages**, the same stack as
coloradoboom.com and boomtownathletics.com. This repo also holds a complete archive of the Wix site
it replaces.

Change history: `CHANGELOG.md`. How to edit safely: `EDITING_GUIDE.md`. What the owner still owes and
how to go live: `HANDOFF.md`. Why it is built this way: `docs/`.

---

## Read this first

**The branch is `main`, lowercase.** The sister repos use `Main` with a capital M and that has cost
real time. This repo does not.

**Yellow highlights are placeholders.** Anything wrapped in `<span class="tbd">` is a value the owner
has not supplied (party prices, family discount, pause terms, shots total). `python scripts/preflight.py`
counts them and refuses to pass while any remain. Do not ship to the real domain until it exits 0.

**Prices and hours come from Shoot 360 HQ's Denver page**, not from Wix. Denver's HQ location id is
`5739019`; "Join" buttons send people to `https://www.shoot360.com/membership-pricing?locationId=5739019`,
where the contract and payment live. If HQ changes a price, `programs.html`, `index.html` and
`faq.html` need a hand edit.

**Fonts are self-hosted** in `assets/fonts/` and preloaded from every page head. Do not reintroduce a
Google Fonts `<link>`: it caused a 0.34 layout-shift score before removal.

**`wix-archive/` is 237 MB of originals.** Disallowed in `robots.txt`, not linked from any page. Do not
delete it; it is the only copy of the logo pack and the training clips at full size.

---

## Files

**7 pages** — `index.html`, `technology.html`, `programs.html`, `parties.html`, `faq.html`,
`contact.html`, `legal.html`

| Path | What it is |
|---|---|
| `assets/css/styles.css` | All styling. Brand tokens are `:root` variables at the top; `@font-face` above them. |
| `assets/js/main.js` | Date-gated visibility, nav toggle, scroll reveal, FAQ accordion, video facade, back-to-top, count-up counter, savings calculator, Behold loader, analytics hook. |
| `assets/img/` | 42 web-sized images derived from the archive by `wix-archive/optimize.py`. |
| `assets/video/` | Four 720p clips. Hero uses `facility-tour-720p.mp4`. |
| `assets/fonts/` | Rajdhani 600/700, Open Sans variable (latin). |
| `scripts/preflight.py` | Link, asset, anchor, alt, schema, sitemap and placeholder check. `--external` also checks outbound URLs. |
| `robots.txt`, `sitemap.xml`, `.nojekyll` | SEO and Pages plumbing. **Keep `.nojekyll`.** |
| `wix-archive/` | The old site: HTML, media, logo pack, fonts, text inventory, screenshots. Read its README. |
| `docs/` | Gap analysis, franchise research, design spec. |

No `CNAME` yet — added at cut-over.

---

## Update the site

Edit a file, run the pre-flight, commit to `main`. Pages redeploys in about a minute.

```bash
python scripts/preflight.py
git add -A && git commit -m "what changed" && git push origin main
```

Anything touching the header, footer or hours is a **seven-file edit** because shared blocks are
copy-pasted (see `EDITING_GUIDE.md`). Preview locally with `python -m http.server 8765` from the
repo root and open `http://127.0.0.1:8765/`.

---

## Content state (2026-09-16, v0.2)

- Primary CTA everywhere: **Book a Free Workout** → SalonCloud Plus form.
- Coaching is stated as included in every membership (owner directive).
- Pricing shown: Rookie $159 · Pro $199 · Hall of Fame $379 (12-mo) · All-Star $389 · 12-visit pack
  $480 · guest workout $72. Family discount and pause policy present with placeholder numbers.
- Programs: free evaluation, memberships, packs/drop-in, savings calculator, camps-classes-clinics,
  homeschool (weekdays 2–4 PM), Nike Basketball Camps, leagues, birthday parties (own page, prices
  pending), MySpark grant, policies, team inquiry.
- Google Business listing linked (4.7 stars). Instagram section wired for a Behold feed id.
  GoHighLevel form slots on contact and parties await the embed code.
- Not on the site: coach bios (needs content), review quotes (needs the owner's Business Profile access).
