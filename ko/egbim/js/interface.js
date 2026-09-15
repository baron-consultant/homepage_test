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
    var target = document.getElementById("myimg");
    if (!target || !document.getElementById("dualm")) return;

    // Keep the optimized HTML poster until a requested frame is decoded.
    var firstSrc = target.getAttribute("src");
    var ready = {0: firstSrc};
    var pending = {};
    var failed = {};
    var queue = [];
    var active = 0;
    var near = false;
    var desired = 0;
    var direction = 1;
    var obj = {curImg: 0};

    function render() {
        if (ready[desired] && target.getAttribute("src") !== ready[desired]) {
            target.setAttribute("src", ready[desired]);
        }
    }

    function pump() {
        while (near && active < 4 && queue.length) {
            load(queue.shift());
        }
    }

    function load(index) {
        if (ready[index] || pending[index] || failed[index]) return;
        pending[index] = true;
        active++;
        var img = new Image();
        var src = "img/com_img/comp_" + (index + 1) + ".png";
        function finish(ok) {
            if (ok) ready[index] = src;
            else failed[index] = true;
            delete pending[index];
            active--;
            render();
            pump();
        }
        img.onload = function () {
            if (img.decode) img.decode().then(function () { finish(true); }, function () { finish(false); });
            else finish(img.naturalWidth > 0);
        };
        img.onerror = function () { finish(false); };
        img.src = src;
    }

    function schedule() {
        // Rebuild only a small window; fast scrolling discards stale queued work.
        queue = [];
        if (!near) return;
        [0, direction, 2 * direction, 3 * direction, -direction].forEach(function (offset) {
            var index = desired + offset;
            if (index >= 0 && index < 104 && !ready[index] && !pending[index] && !failed[index]) queue.push(index);
        });
        pump();
    }

    var sequence = gsap.to(obj, {
        curImg: 103,
        roundProps: "curImg",
        immediateRender: true,
        ease: "none",
        onUpdate: function () {
            var next = Math.max(0, Math.min(103, Math.round(obj.curImg)));
            if (next !== desired) direction = next > desired ? 1 : -1;
            desired = next;
            render();
            schedule();
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
    function updateProximity(self) {
        var next = self.isActive && window.scrollY > 0;
        if (next !== near) { near = next; schedule(); }
    }

    // Prepare frames only after scrolling toward this section.
    ScrollTrigger.create({
        trigger: "#dualm",
        start: "top bottom+=600",
        end: function () { return sequence.scrollTrigger.end + window.innerHeight + 600; },
        onToggle: updateProximity,
        onUpdate: updateProximity,
        onRefresh: updateProximity
    });
});
