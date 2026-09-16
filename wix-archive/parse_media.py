import json, re, sys, os, urllib.request
from pathlib import Path
raw=Path(sys.argv[1]).read_text(encoding='utf-8',errors='ignore')
j=json.loads(raw[raw.index('{'):raw.rindex('}')+1])
files=j.get('files',[]); nc=j.get('nextCursor',{})
print("files in root:",len(files),"| total per cursor:",nc.get('total'),"| hasNext:",bool((nc.get('cursors') or {}).get('next')))
rows=[]
for f in files:
    url=f.get('url',''); name=f.get('displayName',''); mt=f.get('mediaType'); size=f.get('sizeInBytes')
    img=(f.get('media') or {}).get('image',{}).get('image',{}) if isinstance(f.get('media'),dict) else {}
    w=img.get('width'); h=img.get('height')
    vid=(f.get('media') or {}).get('video',{}) if isinstance(f.get('media'),dict) else {}
    rows.append(dict(id=f.get('id'),name=name,type=mt,size=int(size or 0),w=w,h=h,url=url,folder=f.get('parentFolderId'),created=f.get('createdDate','')[:10],
                     vres=[r.get('url') for r in (vid.get('resolutions') or [])] if vid else []))
rows.sort(key=lambda r:-r['size'])
Path('media-manager-list.json').write_text(json.dumps(rows,indent=1),encoding='utf-8')
have=set(os.listdir('media'))
print(f"{'type':6} {'size':>10} {'dims':>11}  name  (id)  [already?]")
for r in rows:
    fid=r['url'].rsplit('/',1)[-1] if r['url'] else ''
    print(f"{str(r['type']):6} {r['size']:>10} {str(r['w'])+'x'+str(r['h']):>11}  {r['name'][:45]:45} {fid[:50]} {'HAVE' if fid in have else 'NEW'}")
# download NEW ones
n=0
for r in rows:
    if not r['url']: continue
    fid=r['url'].rsplit('/',1)[-1]
    if fid in have: continue
    try:
        req=urllib.request.Request(r['url'],headers={'User-Agent':'Mozilla/5.0'})
        data=urllib.request.urlopen(req,timeout=120).read()
        Path('media',fid).write_bytes(data); n+=1
    except Exception as e: print("FAIL",r['name'],e)
    for vr in r['vres'] or []:
        if vr:
            try:
                data=urllib.request.urlopen(urllib.request.Request(vr,headers={'User-Agent':'Mozilla/5.0'}),timeout=300).read()
                Path('media',fid+'.'+vr.rsplit('/',1)[-1]).write_bytes(data); n+=1
            except Exception as e: print("FAIL video",vr,e)
print("downloaded new:",n)
