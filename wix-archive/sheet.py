from PIL import Image, ImageDraw, ImageFont, ImageOps
import os, json, math
from pathlib import Path
names={}
for r in json.loads(Path('media-manager-list.json').read_text(encoding='utf-8')):
    if r['url']: names[r['url'].rsplit('/',1)[-1]]=r['name']
files=[f for f in sorted(os.listdir('media')) if f.lower().endswith(('.jpg','.jpeg','.png','.gif','.webp'))]
cell=(300,230); cols=6; rows=math.ceil(len(files)/cols)
sheet=Image.new('RGB',(cols*cell[0],rows*cell[1]),(40,40,40)); d=ImageDraw.Draw(sheet)
try: font=ImageFont.truetype('arial.ttf',12)
except: font=ImageFont.load_default()
Image.MAX_IMAGE_PIXELS=None
for i,f in enumerate(files):
    x=(i%cols)*cell[0]; y=(i//cols)*cell[1]
    try:
        im=Image.open('media/'+f); im.draft('RGB',(600,600)); w,h=im.size
        im=im.convert('RGBA'); bg=Image.new('RGBA',im.size,(90,90,90,255)); im=Image.alpha_composite(bg,im).convert('RGB')
        im.thumbnail((cell[0]-8,cell[1]-44)); sheet.paste(im,(x+4,y+4))
        d.text((x+4,y+cell[1]-38),f"{i:02d} {names.get(f,'')[:34]}",fill=(255,255,255),font=font)
        d.text((x+4,y+cell[1]-24),f"{w}x{h}  {os.path.getsize('media/'+f)//1024}KB",fill=(200,200,200),font=font)
        d.text((x+4,y+cell[1]-12),f[:44],fill=(150,150,150),font=font)
    except Exception as e: d.text((x+4,y+4),f"ERR {f[:30]} {e}",fill=(255,80,80),font=font)
sheet.save('contact-sheet.jpg',quality=82); print('sheet',sheet.size,len(files),'images')
