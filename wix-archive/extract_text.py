import re, html, sys, json
from html.parser import HTMLParser
from pathlib import Path

class P(HTMLParser):
    SKIP={'script','style','noscript','svg','template','head'}
    def __init__(s):
        super().__init__(); s.skip=0; s.out=[]; s.tag=None; s.meta={}; s.links=[]; s.imgs=[]
    def handle_starttag(s,t,a):
        a=dict(a)
        if t in s.SKIP: s.skip+=1
        if t=='meta' and a.get('name') in ('description','keywords') or a.get('property','').startswith('og:'):
            s.meta[a.get('name') or a.get('property')]=a.get('content','')
        if t=='title': s.tag='title'
        if t in ('h1','h2','h3','h4','h5','h6','p','li','a','button','span','div','label','address','figcaption'): s.tag=t
        if t=='a' and a.get('href'): s.links.append((a['href'],''))
        if t=='img': s.imgs.append((a.get('src',''),a.get('alt','')))
    def handle_endtag(s,t):
        if t in s.SKIP and s.skip: s.skip-=1
    def handle_data(s,d):
        if s.skip: return
        d=' '.join(d.split())
        if not d: return
        if s.tag=='a' and s.links and not s.links[-1][1]: s.links[-1]=(s.links[-1][0],d)
        s.out.append((s.tag,d))

def run(f):
    p=P(); p.feed(Path(f).read_text(encoding='utf-8',errors='ignore'))
    seen=set(); lines=[]
    for t,d in p.out:
        k=(t,d)
        if k in seen: continue
        seen.add(k)
        if t in ('h1','h2','h3','h4'): lines.append(f"\n{'#'*(int(t[1])+1)} {d}")
        elif t=='title': lines.append(f"# {d}")
        else: lines.append(d)
    return p, lines

out=["# Shoot 360 Denver — Wix site content inventory (archived 2026-09-16)\n",
     "Source: https://www.shoot360denver.com (Wix Studio). Text extracted from the server-rendered HTML; order follows the DOM.\n"]
for name in ['index','about','technology','contact','privacy-policy','terms-and-coniditions']:
    p,lines=run(f'pages/{name}.html')
    out.append(f"\n\n---\n\n## PAGE: /{'' if name=='index' else name}\n")
    for k,v in p.meta.items(): out.append(f"- meta {k}: {v}")
    out.append("")
    out.extend(lines)
    out.append("\n**Links on this page:**")
    seen=set()
    for h,t in p.links:
        if h.startswith('#') or h in seen: continue
        seen.add(h); out.append(f"- [{t or '(image/icon)'}]({h})")
    out.append("\n**Images with alt text:**")
    for src,alt in p.imgs:
        if alt: out.append(f"- {alt}  ←  {src[:90]}")
Path('content-inventory.md').write_text('\n'.join(out),encoding='utf-8')
print(Path('content-inventory.md').stat().st_size,"bytes")
