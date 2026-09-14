/* SETL content pages. Small, dependency-free, and nothing here is scroll-linked:
   every effect is triggered once by IntersectionObserver and animated with CSS. */
(function(){
  "use strict";
  var doc=document.documentElement;
  doc.classList.remove('no-js');
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches;
  var hasIO='IntersectionObserver' in window;

  /* reveal on arrival; a timed fallback guarantees nothing can stay hidden */
  var rv=[].slice.call(document.querySelectorAll('.rv'));
  var showAll=function(){ rv.forEach(function(el){ el.classList.add('in'); }); };
  if(reduce||!hasIO){ showAll(); }
  else{
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    },{rootMargin:'0px 0px -8% 0px',threshold:0});
    rv.forEach(function(el){ io.observe(el); });
    setTimeout(showAll,2500);
  }

  /* footer year */
  [].forEach.call(document.querySelectorAll('[data-year]'),function(el){ el.textContent=new Date().getFullYear(); });

  /* ABOUT: the night advances as each chapter arrives */
  var chapters=[].slice.call(document.querySelectorAll('.chapter[data-hour]'));
  if(chapters.length){
    var marks=[].slice.call(document.querySelectorAll('.clock li'));
    var chip=document.querySelector('.timechip span');
    var setHour=function(ch){
      var h=ch.getAttribute('data-hour');
      document.body.setAttribute('data-hour',h);
      marks.forEach(function(m){ m.classList.toggle('on', m.getAttribute('data-hour')===h); });
      if(chip) chip.textContent=ch.getAttribute('data-time');
    };
    setHour(chapters[0]);
    if(hasIO){
      var cio=new IntersectionObserver(function(es){
        es.forEach(function(e){ if(e.isIntersecting) setHour(e.target); });
      },{rootMargin:'-45% 0px -50% 0px',threshold:0});
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
      var step=function(ts){
        if(t0===null) t0=ts;
        var p=Math.min(1,(ts-t0)/dur), e=1-Math.pow(1-p,4);
        goal.textContent=fmt(target*e);
        if(p<1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };
    if(hasIO&&!reduce){
      var gio=new IntersectionObserver(function(es){
        if(es[0].isIntersecting){ run(); gio.disconnect(); }
      },{threshold:.4});
      gio.observe(goal);
    }else{ run(); }
  }
})();
