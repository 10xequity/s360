"""Set every <lastmod> in sitemap.xml to the date of the last commit that touched that page.

Run from the repo root after committing page changes:  python scripts/sitemap_lastmod.py
Then commit sitemap.xml. Pages with uncommitted changes keep their committed date, so commit first.
"""
import re, subprocess
from pathlib import Path

f = Path('sitemap.xml')
s = f.read_bytes().decode('utf-8')

def lastmod(m):
    page = m.group(1) or 'index.html'
    date = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', page], capture_output=True, text=True, check=True).stdout.strip()
    assert date, f'no commit touches {page}'
    return f'<loc>https://www.shoot360denver.com/{m.group(1) or ""}</loc><lastmod>{date}</lastmod>'

s2, n = re.subn(r'<loc>https://www\.shoot360denver\.com/([\w\-]+\.html)?</loc><lastmod>[\d\-]+</lastmod>', lastmod, s)
assert n == s.count('<url>'), ('every <url> must match', n, s.count('<url>'))
f.write_bytes(s2.encode('utf-8'))
print(f'{n} lastmod dates set from git')
