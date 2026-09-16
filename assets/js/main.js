// Shoot 360 Denver — shared behaviour. Loaded on every page. Ported from colorado-boom-site so
// one person can maintain all three sites with the same conventions.

// ===== Date-based visibility — dated content retires itself ======================
// Tag any element:  data-show-until="YYYY-MM-DD"  hides it the day AFTER that date
//                   data-show-from="YYYY-MM-DD"   reveals it on that date (author it with
//                                                 hidden style="display:none")
// Judged in America/Denver. Fail-safe: a bad/missing date is left as authored.
(function(){
  var valid=/^\d{4}-\d{2}-\d{2}$/, today;
  try{ today=new Intl.DateTimeFormat('en-CA',{timeZone:'America/Denver'}).format(new Date()); }
  catch(e){ today=new Date().toISOString().slice(0,10); }
  document.querySelectorAll('[data-show-until]').forEach(function(el){
    var d=el.getAttribute('data-show-until');
    if(valid.test(d)&&today>d){ el.setAttribute('hidden',''); el.style.display='none'; }
  });
  document.querySelectorAll('[data-show-from]').forEach(function(el){
    var d=el.getAttribute('data-show-from'); if(!valid.test(d)) return;
    if(today>=d){ el.removeAttribute('hidden'); el.style.display=''; }
    else { el.setAttribute('hidden',''); el.style.display='none'; }
  });
})();

// ===== Mobile nav toggle ==========================================================
(function(){
  var t=document.querySelector('.nav-toggle'),n=document.getElementById('primary-nav');
  if(!t||!n)return;
  t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',String(o));t.setAttribute('aria-label',o?'Close menu':'Open menu');});
  n.addEventListener('click',function(e){if(e.target.tagName==='A'&&n.classList.contains('open')){n.classList.remove('open');t.setAttribute('aria-expanded','false');}});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&n.classList.contains('open')){n.classList.remove('open');t.setAttribute('aria-expanded','false');t.focus();}});
})();

// ===== Scroll reveal ==============================================================
(function(){
  var items=document.querySelectorAll('.reveal');
  var rm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  if(!items.length||rm||!('IntersectionObserver' in window)){items.forEach(function(el){el.classList.add('visible');});return;}
  var io=new IntersectionObserver(function(entries){entries.forEach(function(en,i){if(en.isIntersecting){setTimeout(function(){en.target.classList.add('visible');},Math.min(i*60,240));io.unobserve(en.target);}});},{threshold:0.12,rootMargin:'0px 0px -40px 0px'});
  items.forEach(function(el){io.observe(el);});
})();

// ===== FAQ accordion ==============================================================
(function(){
  document.querySelectorAll('.faq-q').forEach(function(b){
    b.setAttribute('aria-expanded','false');
    b.addEventListener('click',function(){
      var open=b.parentElement.classList.toggle('open');
      b.setAttribute('aria-expanded',String(open));
    });
  });
})();

// ===== Video facade (self-hosted mp4) ============================================
// <div class="vid" data-src="assets/video/x.mp4"><img ...><button class="play" aria-label="Play …"></button></div>
(function(){
  function play(el){
    var src=el.getAttribute('data-src'); if(!src)return;
    var v=document.createElement('video');
    v.src=src; v.controls=true; v.autoplay=true; v.playsInline=true; v.setAttribute('aria-label',el.getAttribute('data-label')||'Video');
    var poster=el.querySelector('img'); if(poster) v.poster=poster.getAttribute('src');
    el.innerHTML=''; el.appendChild(v); el.style.cursor='default';
  }
  document.querySelectorAll('.vid[data-src]').forEach(function(el){
    el.addEventListener('click',function(){play(el);});
    var btn=el.querySelector('.play');
    if(btn) btn.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();play(el);}});
  });
})();

// ===== Hero video: honour reduced motion, never block paint =====================
(function(){
  var v=document.querySelector('.hero video'); if(!v)return;
  var rm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  if(rm){ v.removeAttribute('autoplay'); v.pause(); return; }
  var p=v.play(); if(p&&p.catch) p.catch(function(){});
})();

// ===== Back-to-top button ========================================================
(function(){
  if(document.querySelector('.to-top'))return;
  var css='.to-top{position:fixed;right:18px;bottom:18px;z-index:200;width:46px;height:46px;'+
    'border-radius:50%;background:var(--red,#EF001D);color:#fff;font-size:22px;line-height:1;border:0;cursor:pointer;'+
    'box-shadow:0 6px 18px rgba(0,0,0,.35);opacity:0;visibility:hidden;transform:translateY(8px);'+
    'transition:opacity .2s ease,transform .2s ease,background .2s ease;}'+
    '.to-top.show{opacity:1;visibility:visible;transform:translateY(0);}'+
    '.to-top:hover{background:var(--red-dark,#C20101);}'+
    '.to-top:focus-visible{outline:3px solid #fff;outline-offset:3px;}'+
    '@media(prefers-reduced-motion:reduce){.to-top{transition:none;}}';
  var s=document.createElement('style');s.textContent=css;document.head.appendChild(s);
  var btn=document.createElement('button');
  btn.type='button';btn.className='to-top';btn.setAttribute('aria-label','Back to top');btn.innerHTML='↑';
  document.body.appendChild(btn);
  var toggle=function(){btn.classList.toggle('show',window.scrollY>600);};
  window.addEventListener('scroll',toggle,{passive:true}); toggle();
  btn.addEventListener('click',function(){
    var rm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion:reduce)').matches;
    window.scrollTo({top:0,behavior:rm?'auto':'smooth'});
  });
})();

// ===== Analytics hook (inert until an ID is pasted) ==============================
// Google Analytics: paste the Measurement ID ("G-XXXXXXXXXX") between the quotes. Leave empty
// to keep it off. Cloudflare Web Analytics needs nothing here once the domain is proxied.
(function(){
  var GA_MEASUREMENT_ID = '';
  if(!GA_MEASUREMENT_ID) return;
  var s=document.createElement('script');
  s.async=true; s.src='https://www.googletagmanager.com/gtag/js?id='+GA_MEASUREMENT_ID;
  document.head.appendChild(s);
  window.dataLayer=window.dataLayer||[];
  function gtag(){window.dataLayer.push(arguments);}
  gtag('js',new Date()); gtag('config',GA_MEASUREMENT_ID);
})();
