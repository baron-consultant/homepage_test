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
        start: "center top",
    //    markers: true,
        onEnter: () => updateElements(0),
        onLeaveBack: () => updateElements(0)
    });
    
    ScrollTrigger.create({
        trigger: sections[1],
        start: "center center",
        //markers: true,
        onEnter: () => updateElements(1),
        onLeaveBack: () => updateElements(1)
    });

    ScrollTrigger.create({
        trigger: sections[2],
        start: "center bottom",
       // markers: true,
        onEnter: () => updateElements(2),
        onLeaveBack: () => updateElements(2)
    });

});

// 고정 슬라이드 (GSAP ScrollTrigger 마이그레이션 및 Pin 고정 추가)
$(function() {
    gsap.registerPlugin(ScrollTrigger);

    const route = document.querySelector('.route');
    if (!route) return;

    const fixElement = route.querySelector('.fix');
    const sections = route.querySelectorAll('#sec1, #sec2, #sec3');
    const subs = route.querySelectorAll('.subs li');
    const imgs = route.querySelectorAll('.imgs li');

    // 1. .fix 요소를 .route 스크롤 트랙 동안 화면 상단에 단단히 고정 (Pin)
    ScrollTrigger.create({
        trigger: route,
        start: "top top",
        end: "bottom bottom",
        pin: fixElement,
        pinSpacing: false, // 겹치며 스크롤되도록 설정
        invalidateOnRefresh: true,
        anticipatePin: 1 // 빠르게 스크롤할 때 핀 시작 지점에서 튕기는 현상 방지
    });

    function activateSlide(index) {
        [subs, imgs].forEach(group => {
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


// 듀얼모니터 시퀀스 애니메이션 (GSAP v3 ScrollTrigger 마이그레이션)
$(function(){
    gsap.registerPlugin(ScrollTrigger);

    var images = Array();
    for (let i = 1; i < 105; i++) {
        images.push(`img/com_img/comp_${i}.png`);
    }

    // 프레임을 미리 로드해 캐시에 채워둔다. 스크롤로 해당 구간에 도달하기 전
    // 백그라운드에서 로드가 끝나야, 스크럽 시 아직 받아오지 못한 프레임 때문에
    // 이미지가 깨지거나 빈 화면으로 보이는 현상을 막을 수 있다.
    var loadedImages = images.map(function (src) {
        var img = new Image();
        img.src = src;
        return img;
    });

    var obj = {curImg: 0};
    var lastLoadedSrc = images[0];

    gsap.to(obj, {
        curImg: images.length - 1,
        roundProps: "curImg",
        immediateRender: true,
        ease: "none",
        onUpdate: function () {
            var idx = obj.curImg;
            var img = loadedImages[idx];
            // 아직 로드가 끝나지 않은 프레임은 건너뛰고, 직전까지 정상적으로
            // 로드된 프레임을 계속 보여준다.
            if (img.complete && img.naturalWidth > 0) {
                lastLoadedSrc = images[idx];
            }
            $("#myimg").attr("src", lastLoadedSrc);
        },
        scrollTrigger: {
            trigger: "#dualm",
            start: "top top",
            end: "+=2500",
            pin: true,
            scrub: true,
            invalidateOnRefresh: true
        }
    });
});

