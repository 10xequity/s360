# Shoot 360 Denver — Website

**Version** 0.4 · **Updated** 2026-09-17 · **Status** Public for review at https://10xequity.github.io/shoot360-denver-site/ · shoot360denver.com is still served by Wix until DNS moves

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
has not supplied (party prices, family discount, pause terms). `python scripts/preflight.py`
counts them and refuses to pass while any remain. Do not ship to the real domain until it exits 0.

**Join buttons go straight to Shoot 360's contract signup**, not to HQ's pricing page. Denver's HQ
location id is `5739019`; contract ids are JV/Rookie 151, Varsity/Pro 152, Committed/All-Star 154,
Ball is Life/Hall of Fame 156. Tier names, prices and inclusions come from the owner's "Denver Membership
Options" sheet, not HQ. If a price changes, `memberships.html`, `index.html`, the FAQ list in
`scripts/patch_v04.py` and the calculator tiers in `main.js` need a hand edit.

**Header, footer and the FAQ list are generated.** Do not hand-edit them on ten pages; edit `nav()`,
`FOOTER` and `FAQ` in `scripts/patch_v04.py` and re-run it (see `EDITING_GUIDE.md`).

**The word "free" is banned from marketing copy** by the owner; say "evaluation" or "come evaluate".
Every class, camp, league or drop-in mention must say registration is in the Shoot 360 app.

**Fonts are self-hosted** in `assets/fonts/` and preloaded. No Google Fonts `<link>`.

**`wix-archive/` is 237 MB of originals.** Disallowed in `robots.txt`, not linked. Do not delete it.

---

## Files

**9 pages** — `index.html`, `technology.html`, `publications.html`, `memberships.html`, `programs.html`,
`events.html`, `faq.html`, `contact.html`, `legal.html` — plus `parties.html`, a noindex redirect stub to
`events.html#parties` kept for the review link already shared.

| Path | What it is |
|---|---|
| `assets/css/styles.css` | All styling. `@font-face`, then brand tokens in `:root` (`--red`, `--red-text`, `--meter` green…). |
| `assets/js/main.js` | Date-gated visibility, nav toggle + dropdowns, scroll reveal, FAQ accordion, video facade, back-to-top, live shots model, savings calculator, Behold loader, analytics hook, hash-selected tabs (events). |
| `assets/img/` | Web-sized images from the archive, official logo lockups, app badges, MySpark logo. |
| `assets/video/` | Four 720p clips. |
| `assets/fonts/` | Rajdhani 600/700, Open Sans variable. |
| `scripts/preflight.py` | Link, asset, anchor, alt, schema, sitemap and placeholder check. `--external` checks outbound URLs. |
| `robots.txt`, `sitemap.xml`, `.nojekyll` | SEO and Pages plumbing. **Keep `.nojekyll`.** |
| `wix-archive/` | The old site: HTML, media, logo pack, fonts, text inventory, screenshots. |
| `docs/` | Gap analysis, franchise research, design spec, party pricing model, publications research log. |

No `CNAME` yet — added at cut-over.

---

## Update the site

```bash
python scripts/preflight.py
git add -A && git commit -m "what changed" && git push origin main
```

Preview locally with `python -m http.server 8765` from the repo root.

---

## Content state (2026-09-16, v0.3)

- Primary CTA: **Book an Evaluation** → SalonCloud Plus form. Nav CTA: **New Membership** → memberships.
- Memberships: Rookie $159 · Pro $199 · Hall of Fame $379 (12-mo) · All-Star $389; 12-visit pack $480;
  guest $72. Coaching stated as included in every tier. Family discount and pause policy have placeholder numbers.
- Programs: evaluation, classes, camps (Shoot 360 + Nike), leagues, Basketball Club (Team EVO),
  private training (email), homeschool weekdays 2–4 PM, parties, MySpark grant, teams. All app-registered.
- Home: MySpark banner, live shots estimate (375,000 baseline), Google 4.7 badge, Instagram slot.
- Not yet: coach bios/About, review quotes, GHL embeds, Behold feed id, analytics. See `HANDOFF.md`.
