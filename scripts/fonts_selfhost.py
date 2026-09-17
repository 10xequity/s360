"""Self-host Rajdhani 600/700 and Open Sans 400/600 (latin) and swap the Google Fonts <link>s for preloads.
Removes the third-party font dependency and the layout shift from late font swap."""
import re, os, urllib.request
from pathlib import Path
os.chdir(r"C:\Users\vv58\AppData\Local\Temp\claude\c--\98c1dc28-f52e-48ff-b639-94d5a6d91319\scratchpad\shoot360-denver")
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'
css_url = 'https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700&family=Open+Sans:wght@400;600&display=swap'
css = urllib.request.urlopen(urllib.request.Request(css_url, headers={'User-Agent': UA}), timeout=30).read().decode()
Path('assets/fonts').mkdir(parents=True, exist_ok=True)
faces = []
# Parse each @font-face block; keep only the latin subset (the comment before each block names it)
for m in re.finditer(r'/\* (\w[\w-]*) \*/\s*@font-face \{(.*?)\}', css, re.S):
    subset, block = m.group(1), m.group(2)
    if subset != 'latin':
        continue
    fam = re.search(r"font-family: '([^']+)'", block).group(1)
    wt = re.search(r'font-weight: (\d+)', block).group(1)
    url = re.search(r'url\((https://[^)]+)\)', block).group(1)
    name = f"{fam.replace(' ', '')}-{wt}.woff2"
    data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=30).read()
    Path('assets/fonts', name).write_bytes(data)
    faces.append((fam, wt, name, len(data)))
    print(f'{name:24} {len(data)//1024} KB')
assert len(faces) == 4, faces
ff = '/* Self-hosted fonts (latin subset, from Google Fonts). Preloaded from every page head. */\n' + ''.join(
    f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{wt};font-display:swap;src:url(../fonts/{name}) format('woff2');}}\n"
    for fam, wt, name, _ in faces)
p = Path('assets/css/styles.css'); s = p.read_text(encoding='utf-8')
assert '@font-face' not in s
s = ff + s.replace('.split img,.split video{border-radius:var(--radius);width:100%;box-shadow:var(--shadow)}',
                   '.split img,.split video{border-radius:var(--radius);width:100%;height:auto;box-shadow:var(--shadow)}')
p.write_text(s, encoding='utf-8'); print('styles.css: @font-face added, split img height:auto')
old = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
       '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
       '<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">\n')
new = ''.join(f'<link rel="preload" href="assets/fonts/{name}" as="font" type="font/woff2" crossorigin>\n'
              for fam, wt, name, _ in faces if (fam == 'Rajdhani') or (fam == 'Open Sans' and wt == '400'))
for f in sorted(Path('.').glob('*.html')):
    h = f.read_text(encoding='utf-8'); n = h.count(old); assert n == 1, (f, n)
    f.write_text(h.replace(old, new), encoding='utf-8'); print(f.name, 'fonts preloaded')
print('FONTS OK')
