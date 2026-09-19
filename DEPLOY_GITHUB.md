# Deploying Shoot 360 Denver on GitHub Pages

**Version** 1.1 · **Updated** 2026-09-19 · **Status** Mid cut-over. GitHub side done; DNS not yet pointed at GitHub. · **Supersedes** v1.0 (2026-09-16)

**Where the cut-over actually stands (2026-09-19):** the registrar now points at Cloudflare
(`greg.ns.cloudflare.com`, `journey.ns.cloudflare.com`, changed 2026-09-19). Pages has the custom domain
(`CNAME` file = `www.shoot360denver.com`, build green) and GitHub already serves every page under that
hostname. **The Cloudflare zone has no `www` record at all**, so `www.shoot360denver.com` is going dark as
the old Wix answers expire from resolver caches, and the apex still proxies to Wix. Step 4 below is the
only thing left.

Plain static site, no build step. Same hosting pattern as coloradoboom.com.

## Cut-over checklist

1. **Repo visibility.** GitHub Pages on a free plan needs a **public** repo. Either make
   `10xequity/shoot360-denver-site` public (Settings → General → Danger Zone → Change visibility) or
   keep it private on GitHub Pro. Public is fine: the `wix-archive/` folder contains only assets that
   were already on the public Wix site plus the logo pack.
2. **Enable Pages.** Settings → Pages → Source: *Deploy from a branch* → `main` → `/ (root)` → Save.
   Wait for the green check; the site appears at `https://10xequity.github.io/shoot360-denver-site/`.
   Check every page there first. Note the `og:url`/canonical tags point at the custom domain, which is expected.
3. **Custom domain.** ✅ Done 2026-09-19. A file named `CNAME` at the repo root contains exactly
   `www.shoot360denver.com`. Settings → Pages shows the same. Do not delete it: Pages drops the custom
   domain the moment that file goes.
4. **DNS in Cloudflare.** ⬅ *the remaining step.* In the `shoot360denver.com` zone → DNS → Records:

   | Type | Name | Target | Proxy |
   |---|---|---|---|
   | CNAME | `www` | `10xequity.github.io` | **DNS only (grey cloud)** |
   | A | `@` | `185.199.108.153` | **DNS only** |
   | A | `@` | `185.199.109.153` | **DNS only** |
   | A | `@` | `185.199.110.153` | **DNS only** |
   | A | `@` | `185.199.111.153` | **DNS only** |

   Delete the existing apex `A` records that point at Wix (`185.230.63.x`) and any leftover `www`
   record pointing at `cdn3.wixdns.net`. GitHub redirects the apex to `www` on its own, because the
   `CNAME` file names `www`.

   **Grey cloud, not orange.** With the Cloudflare proxy on, Cloudflare answers the
   `/.well-known/acme-challenge/` request that GitHub uses to issue its certificate, so the certificate
   never issues and **Enforce HTTPS** stays greyed out; if Cloudflare's SSL/TLS mode is also *Flexible*
   you get an infinite redirect loop. Leave both records DNS-only until step 5 is green. Turning the
   proxy on afterwards is optional and only safe with SSL/TLS mode **Full (strict)**; GitHub's own CDN
   already handles caching, so there is little to gain.
5. **HTTPS.** Settings → Pages: wait for "certificate issued" (minutes to a few hours after DNS
   resolves), then tick **Enforce HTTPS**. Until then `https_enforced` is false and the site answers on
   http only.
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
- **"Enforce HTTPS" stays greyed out** — the record is proxied (orange cloud). Set it to DNS only.
- **Redirect loop / ERR_TOO_MANY_REDIRECTS** — proxied record plus SSL/TLS mode *Flexible*. Grey-cloud it.
- **`www` does not resolve** — no `www` record in the Cloudflare zone. That is the failure seen on
  2026-09-19: the zone was created with the apex only, so `www` answered from stale Wix cache until it expired.
- **Apex shows the old Wix site** — the apex `A` records still hold Wix's `185.230.63.x`.
- **Fonts missing** — Google Fonts blocked on the network; the system fallbacks are intentional.
