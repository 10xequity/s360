import json, re, sys, os, urllib.request
from pathlib import Path
raw=Path(sys.argv[1]).read_text(encoding='utf-8',errors='ignore')
start=raw.index('{')
try:
    j,_=json.JSONDecoder().raw_decode(raw[start:]); files=j.get('files',[]); print("parsed cleanly; files:",len(files),"nextCursor:",j.get('nextCursor'))
except Exception as e:
    print("truncated JSON ->", e); files=[]
    # regex fallback: split on file objects by "id"
    for m in re.finditer(r'\{"id":"([^"]+)","displayName":"([^"]*)","url":"([^"]+)"[^{}]*?"sizeInBytes":"?(\d+)"?[^{}]*?"mediaType":"([A-Z]+)"', raw):
        files.append(dict(id=m.group(1),displayName=m.group(2),url=m.group(3),sizeInBytes=m.group(4),mediaType=m.group(5)))
    print("regex recovered files:",len(files))
rows=[]
for f in files:
    url=f.get('url',''); name=f.get('displayName',''); mt=f.get('mediaType'); size=int(f.get('sizeInBytes') or 0)
    med=f.get('media') or {}
    img=(med.get('image') or {}).get('image') or {}
    vid=med.get('video') or {}
    rows.append(dict(id=f.get('id'),name=name,type=mt,size=size,w=img.get('width'),h=img.get('height'),url=url,
                     folder=f.get('parentFolderId'),created=(f.get('createdDate') or '')[:10],
                     vres=[r.get('url') for r in (vid.get('resolutions') or []) if r.get('url')]))
rows.sort(key=lambda r:-r['size'])
Path('media-manager-list.json').write_text(json.dumps(rows,indent=1),encoding='utf-8')
have=set(os.listdir('media'))
print(f"\n{'type':6} {'size':>10} {'dims':>11}  {'name':45} {'file id':50} status")
for r in rows:
    fid=r['url'].rsplit('/',1)[-1] if r['url'] else ''
    print(f"{str(r['type']):6} {r['size']:>10} {str(r['w'])+'x'+str(r['h']):>11}  {r['name'][:45]:45} {fid[:50]:50} {'HAVE' if fid in have else 'NEW'}")
n=0
for r in rows:
    if not r['url']: continue
    fid=r['url'].rsplit('/',1)[-1]
    if fid in have: continue
    try:
        data=urllib.request.urlopen(urllib.request.Request(r['url'],headers={'User-Agent':'Mozilla/5.0'}),timeout=180).read()
        Path('media',fid).write_bytes(data); n+=1
    except Exception as e: print("FAIL",r['name'],e)
    for vr in r['vres']:
        try:
            data=urllib.request.urlopen(urllib.request.Request(vr,headers={'User-Agent':'Mozilla/5.0'}),timeout=600).read()
            Path('media',fid+'__'+vr.rsplit('/',1)[-1]).write_bytes(data); n+=1
        except Exception as e: print("FAIL video",vr,e)
print("\ndownloaded new:",n, "| media dir now:", len(os.listdir('media')), "files")
