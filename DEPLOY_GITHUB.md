# Deploying Shoot 360 Denver on GitHub Pages

**Version** 1.0 · **Updated** 2026-09-16 · **Status** Not yet deployed. Live site is still Wix.

Plain static site, no build step. Same hosting pattern as coloradoboom.com.

## Cut-over checklist

1. **Repo visibility.** GitHub Pages on a free plan needs a **public** repo. Either make
   `10xequity/shoot360-denver-site` public (Settings → General → Danger Zone → Change visibility) or
   keep it private on GitHub Pro. Public is fine: the `wix-archive/` folder contains only assets that
   were already on the public Wix site plus the logo pack.
2. **Enable Pages.** Settings → Pages → Source: *Deploy from a branch* → `main` → `/ (root)` → Save.
   Wait for the green check; the site appears at `https://10xequity.github.io/shoot360-denver-site/`.
   Check every page there first. Note the `og:url`/canonical tags point at the custom domain, which is expected.
3. **Custom domain.** Create a file named `CNAME` at the repo root containing exactly
   `www.shoot360denver.com`, commit it. In Settings → Pages → Custom domain, enter the same and Save.
4. **DNS.** Where the domain's DNS lives today (probably Wix, since the site is Wix Premium with a
   custom domain; check Wix → Domains). Two routes:
   - **Recommended: move DNS to Cloudflare** like the sister sites (free). Add the zone, copy the
     nameservers to the registrar, then in Cloudflare: `www` CNAME → `10xequity.github.io` (proxied);
     apex `shoot360denver.com` → A records `185.199.108.153`, `185.199.109.153`,
     `185.199.110.153`, `185.199.111.153` (proxied). Cloudflare then gives caching (~10 min),
     Web Analytics with no code, and a managed robots rule.
   - **Simplest: keep DNS where it is.** Same records, unproxied.
5. **HTTPS.** Back in Settings → Pages, wait for the certificate, tick **Enforce HTTPS**.
6. **Verify.** `curl -I https://www.shoot360denver.com/` returns 200 from GitHub; open all six pages;
   the map iframe loads; the Book a Free Workout links open the SalonCloud form.
7. **Search.** Google Search Console: verify the domain (paste the token into the commented
   `<meta>` in `index.html`), submit `https://www.shoot360denver.com/sitemap.xml`. Update the
   Google Business Profile website field if it points at a Wix URL.
8. **Wix.** Unpublish the Wix site (reversible). After a week with no issues, downgrade/cancel Wix
   Premium at renewal. Keep the Wix account: the domain may be registered there.
9. **Cache.** If Cloudflare is in front, edits show within ~10 minutes; hard-refresh to check sooner.

## Quick troubleshooting

- **404 at the URL** — `index.html` not at repo root, or Pages source misset.
- **Page loads, no CSS/images** — `assets/` path broke, or `.nojekyll` missing (dotfiles vanish on some uploads).
- **Old version showing** — hard refresh; GitHub's CDN caches briefly, Cloudflare ~10 min.
- **HTTPS warning** — certificate still issuing; wait, then tick Enforce HTTPS.
- **Fonts missing** — Google Fonts blocked on the network; the system fallbacks are intentional.
