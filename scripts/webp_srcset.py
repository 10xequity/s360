"""WebP + srcset for every content JPEG; partner logos shrunk to 2x their 30/42px display height.

Run:  python scripts/webp_srcset.py   (needs Pillow)
Idempotent: <img> tags that already have a srcset are left alone. After replacing a photo, delete its
assets/img/<name>-NNN.webp files and the srcset/sizes on its <img> tags, then re-run.
Writes assets/img/<name>-640.webp plus <name>-<width, max 1600>.webp (one file if the JPEG is 900px or less).
"""
import os, re
from pathlib import Path
from PIL import Image
os.chdir(Path(__file__).resolve().parent.parent)

PAGES = ['index.html', 'technology.html', 'publications.html', 'memberships.html', 'programs.html',
         'events.html', 'faq.html', 'contact.html', 'legal.html']
HERO_SIZES = '100vw'
BODY_SIZES = '(max-width: 900px) calc(100vw - 40px), 560px'  # split/grid columns top out near 560px at 1440

def widths(w):
    return [640, min(w, 1600)] if w > 900 else [w]

made = {}
def webp(name):
    if name in made:
        return made[name]
    src = Path('assets/img') / f'{name}.jpg'
    im = Image.open(src).convert('RGB')
    out = []
    for w in widths(im.width):
        h = round(im.height * w / im.width)
        p = Path('assets/img') / f'{name}-{w}.webp'
        (im if w == im.width else im.resize((w, h), Image.LANCZOS)).save(p, 'WEBP', quality=80, method=6)
        out.append((p.as_posix(), w))
    made[name] = out
    return out

IMG = re.compile(r'<img\b[^>]*>')
for f in PAGES:
    s = open(f, encoding='utf-8', newline='').read()
    def fix(m):
        tag = m.group(0)
        sm = re.search(r'src="assets/img/([\w-]+)\.jpg"', tag)
        if not sm or 'srcset=' in tag:
            return tag
        set_ = ', '.join(f'{p} {w}w' for p, w in webp(sm.group(1)))
        sizes = HERO_SIZES if 'hero-img' in tag else BODY_SIZES
        return tag.replace(sm.group(0), f'{sm.group(0)} srcset="{set_}" sizes="{sizes}"', 1)
    s2 = IMG.sub(fix, s)
    if s2 != s:
        open(f, 'w', encoding='utf-8', newline='').write(s2)

# partner logos: CSS shows them 30px tall (.lg 42px); keep 2x
LOGOS = {'partner-nike.png': 60, 'partner-wilson.png': 60, 'partner-nuggets.png': 84}
s = open('index.html', encoding='utf-8', newline='').read()
for name, h in LOGOS.items():
    p = Path('assets/img') / name
    im = Image.open(p)
    if im.height > h:
        w = round(im.width * h / im.height)
        m = re.search(rf'src="assets/img/{re.escape(name)}" alt="([^"]*)" width="{im.width}" height="{im.height}"', s)
        assert m, name
        im.resize((w, h), Image.LANCZOS).save(p, optimize=True)
        s = s.replace(m.group(0), f'src="assets/img/{name}" alt="{m.group(1)}" width="{w}" height="{h}"')
open('index.html', 'w', encoding='utf-8', newline='').write(s)

for n, outs in sorted(made.items()):
    print(n, (Path('assets/img') / f'{n}.jpg').stat().st_size // 1024, 'KB ->', ', '.join(f'{w}w {Path(p).stat().st_size // 1024}KB' for p, w in outs))
print(len(made), 'photos converted')
