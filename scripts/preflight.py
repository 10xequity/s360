"""Pre-flight check for the Shoot 360 Denver site.

Run from the repo root:  python scripts/preflight.py [--external]

Fails (exit 1) if any local link/asset is missing, any <img> lacks alt, any page lacks exactly one <h1>/<main>,
any JSON-LD does not parse, a page is missing from the sitemap, or any review placeholder (class="tbd") remains.
--external also checks every clickable outbound URL (HEAD, falling back to GET). Canonical self-links to the
future domain and font preconnect hints are not clickable links and are skipped.
Positive control: the anchor detector is tested against a planted bad fragment before it is trusted.
"""
import re, json, os, sys, urllib.request, urllib.error
from pathlib import Path

EXT = '--external' in sys.argv
pages = sorted(f for f in os.listdir('.') if f.endswith('.html'))
assert pages, 'run from the repo root'
problems, tbd, external = [], 0, set()

# positive control: the detector must catch a known-bad fragment
assert re.search(r'href="([a-z\-]+\.html)#([\w\-]+)"', 'x href="faq.html#nope" y'), 'anchor detector broken'

SKIP_TAG = re.compile(r'<(?:link[^>]*rel="(?:canonical|preconnect)"[^>]*|meta[^>]*)>', re.I)

for f in pages:
    h = Path(f).read_text(encoding='utf-8')
    body = SKIP_TAG.sub('', h)  # drop canonical/preconnect/meta tags before harvesting URLs
    for m in re.finditer(r'(?:href|src|poster|data-src)="([^"#][^"]*)"', body):
        u = m.group(1)
        if u.startswith(('http://', 'https://')):
            if 'shoot360denver.com' not in u:
                external.add(u.replace('&amp;', '&'))
            continue
        if u.startswith(('mailto:', 'tel:', 'javascript:')):
            continue
        if not Path(u.split('#')[0].split('?')[0]).exists():
            problems.append(f'{f}: missing {u}')
    for m in re.finditer(r'href="([a-z\-]+\.html)#([\w\-]+)"', h):
        if f'id="{m.group(2)}"' not in Path(m.group(1)).read_text(encoding='utf-8'):
            problems.append(f'{f}: bad anchor {m.group(0)}')
    for m in re.finditer(r'href="#([\w\-]+)"', h):
        if f'id="{m.group(1)}"' not in h:
            problems.append(f'{f}: bad local anchor #{m.group(1)}')
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try:
            json.loads(m.group(1))
        except Exception as e:
            problems.append(f'{f}: JSON-LD {e}')
    if len(re.findall(r'<h1[\s>]', h)) != 1 or len(re.findall(r'<main[\s>]', h)) != 1:
        problems.append(f'{f}: h1/main count')
    for im in re.findall(r'<img[^>]*>', h):
        if 'alt=' not in im:
            problems.append(f'{f}: img without alt: {im[:70]}')
    n = len(re.findall(r'class="tbd', re.sub(r'<!--.*?-->', '', h, flags=re.S))); tbd += n  # ignore mentions inside comments
    if n:
        print(f'  {f}: {n} review placeholder(s) (class="tbd")')

sm = Path('sitemap.xml').read_text(encoding='utf-8')
for f in pages:
    if 'http-equiv="refresh"' in Path(f).read_text(encoding='utf-8'):
        continue  # redirect stubs (parties.html -> events.html) are noindex and stay out of the sitemap on purpose
    if f != 'legal.html' and (f if f != 'index.html' else 'shoot360denver.com/</loc>') not in sm:
        problems.append(f'sitemap missing {f}')

def fetch(u, method):
    req = urllib.request.Request(u, method=method, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0',
                                                            'Referer': 'https://www.shoot360denver.com/'})  # embed players (Vimeo) answer 401 without a page referer
    return urllib.request.urlopen(req, timeout=20).getcode()

if EXT:
    for u in sorted(external):
        try:
            code = fetch(u, 'HEAD')
        except urllib.error.HTTPError as e:
            code = e.code
            if code in (403, 404, 405, 429):
                try: code = fetch(u, 'GET')
                except urllib.error.HTTPError as e2: code = e2.code
                except Exception as e2: code = str(e2)
        except Exception as e:
            code = str(e)
        ok = isinstance(code, int) and code < 400
        print(f'  {"ok " if ok else "BAD"} {code} {u}')
        if not ok:
            problems.append(f'external {code}: {u}')

for p in problems:
    print('PROBLEM', p)
print(f'{len(pages)} pages - {len(external)} external URLs{" checked" if EXT else ""} - {tbd} placeholders - {len(problems)} problems')
sys.exit(1 if problems or tbd else 0)
