/* SETL site behaviour, shared by every page. Small and dependency free.
   Nothing here blocks rendering, and every effect has a static fallback. */
(function(){
  "use strict";
  var doc=document.documentElement;
  doc.classList.remove('no-js');
  var mq=window.matchMedia?function(q){return matchMedia(q).matches;}:function(){return false;};
  var reduce=mq('(prefers-reduced-motion:reduce)');
  var hasIO='IntersectionObserver' in window;
  var $$=function(s,r){return [].slice.call((r||document).querySelectorAll(s));};

  /* reveal on arrival; a timed fallback guarantees nothing can stay hidden */
  var rv=$$('.rv');
  var showAll=function(){ rv.forEach(function(el){ el.classList.add('in'); }); };
  if(reduce||!hasIO){ showAll(); }
  else{
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    },{rootMargin:'0px 0px -7% 0px',threshold:0});
    rv.forEach(function(el){ io.observe(el); });
    setTimeout(showAll,3200);
  }

  /* nav: denser glass once the page moves; menu closes on outside click, Escape or a link */
  var nav=document.querySelector('.nav');
  if(nav){
    var onScroll=function(){ nav.classList.toggle('scrolled',window.scrollY>24); };
    addEventListener('scroll',onScroll,{passive:true}); onScroll();
    var m=nav.querySelector('details.nmenu');
    if(m){
      document.addEventListener('click',function(e){ if(m.open&&!m.contains(e.target)) m.open=false; });
      document.addEventListener('keydown',function(e){ if(e.key==='Escape'&&m.open){ m.open=false; m.querySelector('summary').focus(); } });
      m.addEventListener('click',function(e){ if(e.target.closest('a')) m.open=false; });
    }
  }

  /* footer year */
  $$('[data-year]').forEach(function(el){ el.textContent=new Date().getFullYear(); });

  /* glass cards: a soft light follows the pointer (desktop pointers only) */
  if(!reduce&&mq('(hover:hover) and (pointer:fine)')){
    document.addEventListener('pointermove',function(e){
      var c=e.target.closest&&e.target.closest('.card,.plan,.post-card,.stat,.faq details,.bento');
      if(!c) return;
      var r=c.getBoundingClientRect();
      c.style.setProperty('--mx',(e.clientX-r.left)+'px');
      c.style.setProperty('--my',(e.clientY-r.top)+'px');
    },{passive:true});
  }

  /* lazy video: sources load only when a clip nears the screen, and clips pause off screen */
  var vids=$$('video[data-lazy]');
  if(vids.length){
    var load=function(v){
      if(v.__loaded) return; v.__loaded=true;
      $$('source[data-src]',v).forEach(function(s){ s.src=s.getAttribute('data-src'); });
      v.load();
    };
    if(hasIO){
      var vio=new IntersectionObserver(function(es){
        es.forEach(function(e){
          var v=e.target;
          if(e.isIntersecting){ load(v); if(!reduce){ var p=v.play(); if(p&&p.catch) p.catch(function(){}); } }
          else if(v.__loaded){ v.pause(); }
        });
      },{rootMargin:'300px 0px'});
      vids.forEach(function(v){ vio.observe(v); });
    }else{ vids.forEach(load); }
  }

  /* reading progress fallback for browsers without scroll timelines */
  var bar=document.querySelector('.progress');
  if(bar&&!(window.CSS&&CSS.supports&&CSS.supports('animation-timeline','scroll()'))){
    var tick=false;
    var upd=function(){ tick=false; var h=doc.scrollHeight-innerHeight; bar.style.transform='scaleX('+(h>0?Math.min(1,scrollY/h):0)+')'; };
    addEventListener('scroll',function(){ if(!tick){ tick=true; requestAnimationFrame(upd); } },{passive:true}); upd();
  }

  /* table of contents: highlight the section being read */
  var toc=$$('.toc a');
  if(toc.length&&hasIO){
    var map={}; toc.forEach(function(a){ map[a.getAttribute('href').slice(1)]=a; });
    var tio=new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(e.isIntersecting){ toc.forEach(function(a){ a.classList.remove('on'); }); var a=map[e.target.id]; if(a) a.classList.add('on'); }
      });
    },{rootMargin:'-20% 0px -70% 0px'});
    Object.keys(map).forEach(function(id){ var h=document.getElementById(id); if(h) tio.observe(h); });
  }

  /* ABOUT: the night advances as each chapter arrives */
  var chapters=$$('.chapter[data-hour]');
  if(chapters.length){
    var marks=$$('.clock li'), chip=document.querySelector('.timechip span');
    var setHour=function(ch){
      var h=ch.getAttribute('data-hour');
      document.body.setAttribute('data-hour',h);
      marks.forEach(function(mk){ mk.classList.toggle('on', mk.getAttribute('data-hour')===h); });
      if(chip) chip.textContent=ch.getAttribute('data-time');
    };
    setHour(chapters[0]);
    if(hasIO){
      var cio=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting) setHour(e.target); }); },{rootMargin:'-45% 0px -50% 0px'});
      chapters.forEach(function(c){ cio.observe(c); });
    }
  }

  /* MISSION: count up to the goal once, when it is first seen */
  var goal=document.querySelector('[data-countto]');
  if(goal){
    var target=parseInt(goal.getAttribute('data-countto'),10);
    var fmt=function(n){ return Math.round(n).toLocaleString('en-GB'); };
    var run=function(){
      if(reduce){ goal.textContent=fmt(target); return; }
      var t0=null, dur=2600;
      var step=function(ts){ if(t0===null) t0=ts; var p=Math.min(1,(ts-t0)/dur); goal.textContent=fmt(target*(1-Math.pow(1-p,4))); if(p<1) requestAnimationFrame(step); };
      requestAnimationFrame(step);
    };
    if(hasIO&&!reduce){ var gio=new IntersectionObserver(function(es){ if(es[0].isIntersecting){ run(); gio.disconnect(); } },{threshold:.4}); gio.observe(goal); }
    else run();
  }
})();
