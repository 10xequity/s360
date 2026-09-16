# Throwaway: derive web-sized assets from the archived originals. Re-run any time.
from PIL import Image, ImageOps
from pathlib import Path
Image.MAX_IMAGE_PIXELS=None
M=Path('wix-archive/media'); Z=M/'_zips'; OUT=Path('assets/img'); OUT.mkdir(parents=True,exist_ok=True)
def save(src,name,width,fmt='JPEG',q=82,height=None,crop=None):
    im=Image.open(src); im=ImageOps.exif_transpose(im)
    if crop: im=im.crop(crop)
    if height:  # cover-crop to aspect
        im=ImageOps.fit(im,(width,height),Image.LANCZOS,centering=(0.5,0.45))
    elif im.width>width: im=im.resize((width,round(im.height*width/im.width)),Image.LANCZOS)
    p=OUT/name
    if fmt=='JPEG': im.convert('RGB').save(p,'JPEG',quality=q,optimize=True,progressive=True)
    else: im.save(p,'PNG',optimize=True)
    print(f"{name:34} {im.width}x{im.height} {p.stat().st_size//1024} KB")
# photos
save(M/'3bffc9_a71d22605cbc4b6f97c5cce7f3451669~mv2.jpg','hero-shooter.jpg',1920,height=1080)
save(M/'3bffc9_a71d22605cbc4b6f97c5cce7f3451669~mv2.jpg','og-image.jpg',1200,height=630)
save(M/'3bffc9_1d867d217e294f33af00f73ccb6e2a8b~mv2.png','tech-splash-courts.jpg',1920)
save(M/'3bffc9_274290caa48c40f79ad3cd2ce885d604~mv2.png','tech-splash-meter-hud.jpg',1600)
save(M/'3bffc9_09bd2bb30eeb4618a378487afcd68a56~mv2.jpg','tech-shooting-kid.jpg',1200)
save(M/'3bffc9_db524abb548a4e4ba269e69521391128~mv2.jpg','tech-skill-court.jpg',1200)
save(M/'3bffc9_8bd27ce8b69948bc968b97e18d876faa~mv2.jpg','tech-skill-court-2.jpg',1200)
save(M/'3bffc9_39c586044d5c467da661b2332efc7ea9~mv2.jpg','tech-shooting-bay.jpg',1600)
save(M/'3bffc9_b619c36558224abd9afa33869cddc318~mv2.jpg','tech-video-wall.jpg',1200)
save(M/'3bffc9_7af1b6c180314785acf27d58405e77f0~mv2.jpg','tech-screens.jpg',1200)
save(M/'3bffc9_f84c9150eaeb4383aca968d45734ab99~mv2.jpg','app-screens.jpg',900)
save(M/'3bffc9_958bff59ae2b4234ad481034dda4c6d0~mv2.png','app-phone.jpg',1000)
save(M/'3bffc9_0c9b438495504d7a8f745cd7fb1ecc05~mv2.png','coaching-lineup.jpg',1600)
save(M/'3bffc9_83437d199be2412b96352978bb6bdc8f~mv2.png','coaching-girls.jpg',1024)
save(M/'3bffc9_4dacb38a213740d0b7a54b89c1754748~mv2.jpg','coaching-huddle.jpg',1200)
save(M/'3bffc9_0ecc87b9287642a7923d60f9ae063c8f~mv2.jpeg','coaching-clinic.jpg',1200)
save(M/'3bffc9_b4f7543ee89a42b98463fad3200fc862~mv2.jpg','coaching-drills.jpg',1200)
save(M/'3bffc9_af075fb4d9e449638d7d716bd1fd3d09~mv2.png','coaching-group.jpg',1200)
save(M/'3bffc9_aed488b108c340d2b45214c427957167~mv2.jpeg','coaching-dribble.jpg',1200)
save(M/'3bffc9_ad418384f7924200a581dd637b233621~mv2.jpg','facility-courts.jpg',1600)
save(M/'3bffc9_d275bb03db5a420799d4c62d119d44fa~mv2.jpg','facility-skill-court-tall.jpg',900)
save(M/'3bffc9_679b0b1e08194c449c4d1c56d5146e87~mv2.jpg','facility-shooting-bays.jpg',1200)
save(M/'3bffc9_6c0a5520444847ebaae1bf0b8dc2f265~mv2.jpg','player-portrait.jpg',1200)
save(M/'3bffc9_bcd9ab602a0d46cba9dcb8c07e9d17a2~mv2.png','shooting-kids.jpg',1024)
save(M/'3bffc9_2aeafc41fcb146ea82b01ae829cec9b7~mv2.jpg','unlock.jpg',1200)
# video posters
for vid,name in [('3bffc9_9a84a4fc16d04bf6b59a7d9b901be818','poster-facility.jpg'),('3bffc9_d335148a1cc9428daa6f26cc41665de1','poster-splash-overlay.jpg'),('3bffc9_45b036af019e450cb540434b459f869d','poster-splash-arc.jpg'),('3bffc9_bf7179f2e35e494fbecce87830948a2b','poster-splash-depth.jpg'),('3bffc9_1a4029584ad141c5aeba94070a27d5a1','poster-splash-freeze.jpg'),('3bffc9_d3c4b4c40bd14a7e9da88f9b17b3b54b','poster-shooting-tech.jpg')]:
    save(M/f'{vid}f000.jpg',name,1280)
# logos (PNG, keep alpha)
L=Z/'Shoot-360-Basketball-Logos'
save(L/'Shoot 360 Basketball (2)/shoot360_basketball_all_White.png','logo-white.png',720,'PNG')
save(L/'Shoot 360 Basketball (2)/shoot360_basketball.png','logo-red-black.png',720,'PNG')
save(L/'Stacked S360 Basketball/Stacked_Baksetball_Logo_Red_White.png','logo-stacked-white.png',600,'PNG')
save(M/'3bffc9_ae4c9645e91c498d928909f1fb74a00b~mv2.png','logo-denver.png',800,'PNG')
save(Z/'Icon/icon_red.png','icon-red.png',512,'PNG'); save(Z/'Icon/icon_white.png','icon-white.png',256,'PNG')
for n,s in [('favicon-32.png',32),('apple-touch-icon.png',180)]:
    Image.open(Z/'Icon/icon_red.png').convert('RGBA').resize((s,s),Image.LANCZOS).save(OUT/n,'PNG',optimize=True)
# partner logos: black on transparent -> keep; CSS inverts on dark
def trim(src,name,width):
    im=Image.open(src).convert('RGBA'); bbox=im.getbbox(); im=im.crop(bbox); im.thumbnail((width,width)); im.save(OUT/name,'PNG',optimize=True); print(f"{name:34} {im.width}x{im.height} {(OUT/name).stat().st_size//1024} KB")
trim(M/'3bffc9_4dc58c8368ee4848a30e6ac71a2d6e1f~mv2.png','partner-nike.png',360)
trim(M/'3bffc9_85f3d536dc484741946e30013108d088~mv2.png','partner-wilson.png',360)
trim(M/'3bffc9_b1b3df59568f423a932e2cbe66f89c10~mv2.png','partner-nuggets.png',300)
tot=sum(p.stat().st_size for p in OUT.iterdir()); print(f"\n{len(list(OUT.iterdir()))} files, {tot/1024/1024:.1f} MB in assets/img")
