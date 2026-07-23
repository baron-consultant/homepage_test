document.addEventListener("DOMContentLoaded", (event) => {
  // ---------------------------------------------
  // js__fixLeft 오른쪽에 따라 왼쪽 내용 변하기
  // 사용 클래스 : js__fixLeft_tit, js__fixLeft_bg, js__fixLeft_sec
  // ---------------------------------------------
  gsap.registerPlugin(ScrollTrigger);

  const tits = document.querySelectorAll(".js__fixLeft_tit");
  const bgs = document.querySelectorAll(".js__fixLeft_bg");
  const sections = document.querySelectorAll(".js__fixLeft_secs > div");


  function bgOnEnter(element) {
      gsap.to(element, {
          transform: "scale(1.05)",
          duration: 0.5
      });
  }

  function bgOnLeave(element) {
      gsap.to(element, {
          transform: "scale(1)",
          duration: 0.5
      });
  }
  
  function titOnEnter(element) {
      gsap.to(element, {
          opacity: 1,
          transform: "scale(1) translate(0%, 0%)",
          duration: 0.5
      });
  }
  
  function titOnLeave(element) {
      gsap.to(element, {
          opacity: 0.5,
          transform: "scale(0.7) translate(-47%, 0%)",
          duration: 0.5
      });
  }

  function updateElements(index) {
      bgs.forEach((bg, i) => {
          if (i === index) {
              bg.classList.add("on");
              bgOnEnter(bg);
          } else {
              bg.classList.remove("on");
              bgOnLeave(bg);
          }
      });
      
      tits.forEach((tit, i) => {
          if (i === index) {
              tit.classList.add("on");
              titOnEnter(tit);
          } else {
              tit.classList.remove("on");
              titOnLeave(tit);
          }
      });
  }
 
  ScrollTrigger.create({
      trigger: sections[0],
      start: "top top",
      // markers: true,
      onEnter: () => updateElements(0),
      onLeaveBack: () => updateElements(0)
  });
  
  ScrollTrigger.create({
      trigger: sections[1],
      start: "top center",
      // markers: true,
      onEnter: () => updateElements(1),
      onLeaveBack: () => updateElements(1)
  });

  ScrollTrigger.create({
      trigger: sections[2],
      start: "top center",
     // markers: true,
      onEnter: () => updateElements(2),
      onLeaveBack: () => updateElements(2)
  });
// ++++++++++++++++++ S: TODO 진슬 추가_ 클릭시에도 메뉴 불 나오게
$(tits).each(function(index, val){
  val.addEventListener("click", () => {
    gsap.to(window, {
      duration: 0, 
      scrollTo: {y:"#content" + (index + 1), offsetY:390 }
    }).play(),
    gsap.to(val, {
      onComplete: function(){
        // $('.js__fixLeft_tit > li > a').removeClass('on'),
        // $(val).addClass('on')
        // ~ S: 기존 함수 활용
        if(index === 0) {
          updateElements(0)
        } else if(index === 1) {
          updateElements(1)
        } else if(index === 2) {
          updateElements(2)
        } 
        // ~ E: 기존 함수 활용 
      }
    }).play();
  });
})
 // ++++++++++++++++++ E: TODO 진슬 추가_ 클릭시에도 메뉴 불 나오게
});
// 고정 슬라이드 (GSAP ScrollTrigger 마이그레이션 및 Pin 고정 추가)
$(function() {
    gsap.registerPlugin(ScrollTrigger);

    const route = document.querySelector('.route');
    if (!route) return;

    const fixElement = route.querySelector('.fix');
    const sections = route.querySelectorAll('#sec1, #sec2, #sec3');
    const tabs = route.querySelectorAll('.tabs .tabs_li');
    const subs = route.querySelectorAll('.subs li');
    const imgs = route.querySelectorAll('.imgs li');

    // 1. .fix 요소를 .route 스크롤 트랙 동안 화면 상단에 단단히 고정 (Pin)
    ScrollTrigger.create({
        trigger: route,
        start: "top top",
        end: "bottom bottom",
        pin: fixElement,
        pinSpacing: false,
        invalidateOnRefresh: true
    });

    function activateSlide(index) {
        [tabs, subs, imgs].forEach(group => {
            group.forEach((el, i) => {
                el.classList.toggle('on', i === index);
            });
        });
    }

    sections.forEach((section, index) => {
        ScrollTrigger.create({
            trigger: section,
            start: "top 50%",
            end: "bottom 50%",
            onEnter: () => activateSlide(index),
            onEnterBack: () => activateSlide(index)
        });
    });
});


