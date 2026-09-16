import json, os, re, subprocess
from pathlib import Path
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
names={}
for r in json.loads(Path('media-manager-list.json').read_text(encoding='utf-8')):
    if r['url']: names[r['url'].rsplit('/',1)[-1]]=r['name']
for line in Path('videos.txt').read_text().splitlines():
    vid,name=line.split(' ',1); names[vid]=name
# alt text + page usage from HTML
usage={}; alts={}
for p in Path('pages').glob('*.html'):
    h=p.read_text(encoding='utf-8',errors='ignore')
    for m in re.finditer(r'static\.wixstatic\.com/media/([A-Za-z0-9_~%\-]+\.(?:jpg|jpeg|png|gif|webp|svg))',h):
        usage.setdefault(m.group(1),set()).add(p.stem)
    for m in re.finditer(r'<img[^>]+>',h):
        src=re.search(r'src="[^"]*?/media/([^/"]+)',m.group(0)); alt=re.search(r'alt="([^"]*)"',m.group(0))
        if src and alt and alt.group(1): alts[src.group(1)]=alt.group(1)
rows=[]
for f in sorted(os.listdir('media')):
    if f.startswith('_'): continue
    p=Path('media',f); size=p.stat().st_size; dims=''
    if f.lower().endswith(('.jpg','.jpeg','.png','.gif','.webp')):
        try:
            with Image.open(p) as im: dims=f"{im.width}x{im.height}"
        except: dims='?'
    base=re.sub(r'__.*$','',f); base=re.sub(r'f00\d\.jpg$','',base)
    name=names.get(f) or names.get(base) or alts.get(f) or ''
    if f.endswith('f000.jpg') and not name: name=f"(video poster of {names.get(base,'?')})"
    if f.startswith('11062b_'): name=name or '(Wix stock hero background video)'
    used=', '.join(sorted(usage.get(f,set()))) or ('(video/bg)' if f.endswith('.mp4') else '—')
    rows.append((f,name,dims,size,used))
out=["# Media manifest — Shoot 360 Denver Wix archive","",
     "Archived 2026-09-16 from Wix Media Manager + page-embedded images, at original resolution.",
     "Files keep their Wix IDs so any page reference in `pages/*.html` can be traced. Videos are the 1080p transcode (Wix does not expose the raw upload).",
     "`_wix-template-placeholders/` holds stock images from the unfinished `/about` template page (robots, fake founders, fake press logos) — not brand assets.","",
     "| File | Wix display name | Dimensions | Size | Used on page(s) |","|---|---|---|---|---|"]
for f,name,dims,size,used in rows:
    out.append(f"| `{f}` | {name} | {dims} | {size/1024/1024:.1f} MB | {used} |")
tot=sum(r[3] for r in rows)
out+=["",f"**{len(rows)} files, {tot/1024/1024:.0f} MB.** Placeholders: {len(os.listdir('media/_wix-template-placeholders'))} files."]
Path('MEDIA_MANIFEST.md').write_text('\n'.join(out),encoding='utf-8')
print('\n'.join(out[7:]))
