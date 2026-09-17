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

// ===== v0.2 =====================================================================
// Count-up counters: <span class="count" data-count="9440096">  (leave data-count off to show as-is)
(function(){
  var els=document.querySelectorAll('[data-count]'); if(!els.length)return;
  var rm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  function run(el){
    var target=parseInt(String(el.getAttribute('data-count')).replace(/[^0-9]/g,''),10); if(!target){return;}
    var fmt=function(n){return n.toLocaleString('en-US');};
    if(rm){el.textContent=fmt(target);return;}
    var start=null, dur=1800;
    function step(ts){ if(!start)start=ts; var p=Math.min((ts-start)/dur,1); var e=1-Math.pow(1-p,3); el.textContent=fmt(Math.round(target*e)); if(p<1)requestAnimationFrame(step); }
    requestAnimationFrame(step);
  }
  if(!('IntersectionObserver' in window)){els.forEach(run);return;}
  var io=new IntersectionObserver(function(en){en.forEach(function(e){if(e.isIntersecting){run(e.target);io.unobserve(e.target);}});},{threshold:.3});
  els.forEach(function(el){io.observe(el);});
})();

// Savings calculator (#calc): private-trainer spend vs membership. Trainer rate is the visitor's own input.
(function(){
  var c=document.getElementById('calc'); if(!c)return;
  var rate=c.querySelector('#c-rate'), sess=c.querySelector('#c-sess');
  var tiers=[{name:'Varsity · 8 sessions',price:199,visits:8},{name:'Ball is Life · unlimited, 12-month',price:379,visits:null},{name:'Committed · unlimited',price:389,visits:null}];
  var money=function(n){return '$'+Math.round(n).toLocaleString('en-US');};
  function calc(){
    var r=+rate.value, s=+sess.value, trainer=r*s;
    c.querySelector('#c-rate-out').textContent=money(r)+'/hr';
    c.querySelector('#c-sess-out').textContent=s+' / month';
    c.querySelector('#c-trainer').textContent=money(trainer);
    var rows=tiers.map(function(t){
      var ok=t.visits===null||s<=t.visits, diff=trainer-t.price;
      return '<tr><td>'+t.name+(ok?'':' <span class="cost">(covers '+t.visits+' visits)</span>')+'<br><span class="cost">'+money(t.price)+'/mo, coaching included</span></td><td>'+
        (diff>0?'<span class="save">save '+money(diff)+'</span>':'<span class="cost">'+money(-diff)+' more</span>')+'</td></tr>';
    }).join('');
    c.querySelector('#c-rows').innerHTML=rows;
  }
  rate.addEventListener('input',calc); sess.addEventListener('input',calc); calc();
})();

// Instagram feed via Behold (same vendor as coloradoboom.com). Set data-feed on #ig to the Behold feed id.
(function(){
  var ig=document.getElementById('ig'); if(!ig)return;
  var id=ig.getAttribute('data-feed'); if(!id)return;
  var s=document.createElement('script'); s.type='module'; s.src='https://w.behold.so/widget.js'; document.head.appendChild(s);
  var w=document.createElement('behold-widget'); w.setAttribute('feed-id',id); ig.innerHTML=''; ig.appendChild(w);
})();

// ===== v0.3 =====================================================================
// Programs dropdown: click toggles (touch + keyboard); CSS handles hover on desktop.
(function(){
  var items=document.querySelectorAll('.has-sub'); if(!items.length)return;
  items.forEach(function(li){
    var b=li.querySelector('.sub-toggle'); if(!b)return;
    b.addEventListener('click',function(e){e.stopPropagation();var o=b.getAttribute('aria-expanded')==='true';b.setAttribute('aria-expanded',String(!o));});
    li.addEventListener('keydown',function(e){if(e.key==='Escape'){b.setAttribute('aria-expanded','false');b.focus();}});
  });
  document.addEventListener('click',function(){items.forEach(function(li){var b=li.querySelector('.sub-toggle');if(b)b.setAttribute('aria-expanded','false');});});
})();

// Live shots estimate (#shots). Baseline count at a fixed moment, plus a model of shots taken since,
// during opening hours only. Every visitor sees the same number at the same instant.
//   4 shooting bays x 300 shots per 30-minute session = 600 shots per bay-hour when a bay is busy.
//   Utilisation shares below are the tuning knobs (prime time evenings and weekends are busier).
(function(){
  var el=document.getElementById('shots'); if(!el)return;
  var BASE=375000, EPOCH=Date.UTC(2026,8,16,6,0,0); // 375,000 shots as of 2026-09-16 00:00 America/Denver (UTC-6)
  var BAYS=4, PER_BAY_HOUR=600;
  var SHARE={weekday:[[14,16,0.35],[16,21,0.85]], weekend:[[10,13,0.55],[13,17,0.70]]}; // v0.4: weekdays open 2 PM // [open hour, close hour, share of bays busy]
  var fmt=new Intl.DateTimeFormat('en-US',{timeZone:'America/Denver',hour12:false,weekday:'short',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',second:'2-digit'});
  function parts(ms){var o={};fmt.formatToParts(new Date(ms)).forEach(function(x){o[x.type]=x.value});o.h=(+o.hour%24)+(+o.minute)/60+(+o.second)/3600;o.we=(o.weekday==='Sat'||o.weekday==='Sun');return o;}
  function rateAt(p){var bands=p.we?SHARE.weekend:SHARE.weekday;for(var i=0;i<bands.length;i++){if(p.h>=bands[i][0]&&p.h<bands[i][1])return bands[i][2]*BAYS*PER_BAY_HOUR;}return 0;}
  function dayTotal(we,upToHour){var bands=we?SHARE.weekend:SHARE.weekday,t=0;bands.forEach(function(b){var end=Math.min(b[1],upToHour);if(end>b[0])t+=(end-b[0])*b[2]*BAYS*PER_BAY_HOUR;});return t;}
  function estimate(now){
    var total=0, dayMs=86400000, t=EPOCH;
    // full days from the epoch up to yesterday (Denver), then today's partial
    var today=parts(now), key=function(p){return p.year+p.month+p.day;};
    while(key(parts(t))!==key(today)){total+=dayTotal(parts(t+12*3600000).we,24);t+=dayMs;}
    total+=dayTotal(today.we,today.h);
    return BASE+total;
  }
  var rm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  function render(){var now=Date.now();el.textContent=Math.floor(estimate(now)).toLocaleString('en-US');var live=rateAt(parts(now))>0;el.setAttribute('data-live',live?'1':'0');}
  render(); if(!rm) setInterval(render,1000); else setInterval(render,60000);
})();

// ===== v0.4 =====================================================================
// Tabs (events page): <div class="tabs" role="tablist"><button role="tab" aria-controls="panelId">…  Panels: <section class="tabpanel" id="panelId">
// The URL hash picks the tab (events.html#parties), including a hash that points inside a panel (#takeover).
(function(){
  var tl=document.querySelector('.tabs[role=tablist]'); if(!tl)return;
  var tabs=[].slice.call(tl.querySelectorAll('[role=tab]'));
  var panels=tabs.map(function(t){return document.getElementById(t.getAttribute('aria-controls'));});
  function show(i,focus){tabs.forEach(function(t,j){var on=i===j;t.setAttribute('aria-selected',String(on));t.tabIndex=on?0:-1;if(panels[j]){panels[j].hidden=!on;if(on)panels[j].querySelectorAll('.reveal').forEach(function(el){el.classList.add('visible');});}});if(focus)tabs[i].focus();}
  tabs.forEach(function(t,i){
    t.addEventListener('click',function(){show(i);if(history.replaceState)history.replaceState(null,'','#'+panels[i].id);});
    t.addEventListener('keydown',function(e){var n=i;if(e.key==='ArrowRight')n=(i+1)%tabs.length;else if(e.key==='ArrowLeft')n=(i-1+tabs.length)%tabs.length;else if(e.key==='Home')n=0;else if(e.key==='End')n=tabs.length-1;else return;e.preventDefault();show(n,true);});
  });
  function fromHash(){
    var h=location.hash.replace('#',''), i=-1;
    if(h){var el=document.getElementById(h); var p=el&&(el.classList.contains('tabpanel')?el:el.closest('.tabpanel')); if(p)i=panels.indexOf(p); if(i>=0&&el!==p){show(i);setTimeout(function(){el.scrollIntoView();},0);return;}}
    show(i>=0?i:0);
  }
  window.addEventListener('hashchange',fromHash); fromHash();
})();
