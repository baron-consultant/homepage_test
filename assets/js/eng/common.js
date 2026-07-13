// ?�� AJAX 관??SCRIPT
$(function () {
  $.ajaxSetup({ cache: false });

  function loadHTML(url, target, callback) {
    $.ajax({
      url: url,
      async: true,
      success: function (data) {
        $(target).html(data);
        if (typeof callback === "function") callback();
      },
      error: function (xhr, status, error) {
        console.error(`??Failed to load ${url}:`, error);
      },
    });
  }

  // ?��nav ?�결
  function connectNavToMapList() {
    const currentPath = location.pathname.split("/").pop();
    const navLinks = document.querySelectorAll(
      "header .corp nav ol li.depth1 ul.depth2 li a"
    );

    navLinks.forEach((link) => {
      const href = link.getAttribute("href").split("/").pop();
      if (href === currentPath) {
        const mapList = document.querySelector(".map_list");
        if (mapList) {
          const targetTitle = link.textContent.trim();
          const categoryTitle = link
            .closest(".depth1")
            ?.querySelector("span")
            ?.textContent.trim();
          const subTitle = link
            .closest(".depth1")
            ?.querySelector("em")
            ?.textContent.trim();
          const mainTitle = categoryTitle.replace(subTitle, "");
          mapList.innerHTML = "";
          link.closest(".depth1").classList.add("active");
          const liHome = document.createElement("li");
          liHome.innerHTML = '<i class="home"></i>';

          const liCategory = document.createElement("li");
          liCategory.textContent = mainTitle || "";

          const liOn = document.createElement("li");
          liOn.classList.add("on");
          liOn.textContent = targetTitle || "";

          mapList.appendChild(liHome);
          mapList.appendChild(liCategory);
          mapList.appendChild(liOn);
        }
      }
    });
  }

  function loadSitemapNav() {
    if (!$('.container').hasClass('recruit')) {
      loadHTML(
        "../_include/eng/nav.html",
        ".popup_wrap.sitemap .popup_contents_wrap nav",
        mobileMenu
      );
    } else {
      loadHTML(
        "../_include/eng/nav_recruit.html",
        ".popup_wrap.sitemap .popup_contents_wrap nav",
        mobileMenu
      );
    }
  }

  // ?��header ??nav.html ?�결
  if (!$(".container").hasClass("recruit")) {
    loadHTML("../_include/eng/header.html", "#header", function () {
      loadHTML("../_include/eng/nav.html", "#header .corp .nav", function () {
        connectNavToMapList();
      });
      loadSitemapNav();
    });
  } else {
    loadHTML("../_include/eng/header_recruit.html", "#header_recruit", function () {
      loadSitemapNav();
      if (!$(".container").hasClass("recruit")) {
      } else {
        const currentPath = location.pathname.split("/").pop();
        const navLinks = document.querySelectorAll(
          "header .recruit nav ol li.depth1 a"
        );
        navLinks.forEach((link) => {
          const href = link.getAttribute("href").split("/").pop();
          if (href === currentPath) {
            link.closest(".depth1").classList.add("active");
          }
        });
      }
    });
  }

  // ?��footer ??nav.html ?�결
  loadHTML("../_include/eng/footer.html", "#footer", function () {
    loadHTML("../_include/eng/nav.html", "#footer .nav", function () {
      $("#footer .nav ol li.has_depth3 > .depth3").hide();
    });
  });
  mobileMenu();
});

// ?�� TITLE 관??SCRIPT
// ?��  S: title ?�일?�기

$(function () {
  const currentPath = location.pathname;
  if (currentPath.indexOf("/recruit/") > 0) {
    document.querySelector("head title").textContent =
      "?�재채용 | (�?바론컨설?�트";
  } else {
    document.querySelector("head title").textContent = "BaronConsultant";
  }
});

// E : title ?�일?�기

// ?�� S : header ?�기�?
$(function () {
  const showNav = gsap
    .from("#header, #header_recruit", {
      yPercent: -200,
      paused: true,
      duration: 0.2,
      onStart: () => {
        const stHeader = document.querySelector("header");
        if (window.scrollY > 100) {
          stHeader.classList.add("open");
        }
      },
      onReverseComplete: () => {
        const stHeader = document.querySelector("header");
        stHeader.classList.remove("open");
      },
    })
    .progress(1);

  ScrollTrigger.create({
    start: "top top",
    end: 99999,
    onUpdate: (self) => {
      if (lenis.isStopped) return;
      self.direction === -1 ? showNav.play() : showNav.reverse();
    },
  });
});
// E : header ?�기�?

// ?�� POPUP SCRIPT
// ?��S : ?�업 ?�기
// ?��S : ?�업 ?�기
$(function () {
  $(document).on("click", "button", function () {
    const button = this;
    const value = button.getAttribute("data-value");
    const popup = document.querySelector(`.popup_wrap.${value}`);

    if (popup) {
      // ?�재 ?�크�??�치 ?�??
      const scrollY = window.scrollY;
      document.body.setAttribute('data-scroll-lock', scrollY);
      
      // body 고정
      document.body.style.position = 'fixed';
      document.body.style.top = `-${scrollY}px`;
      document.body.style.left = '0';
      document.body.style.right = '0';
      
      // Lenis ?�전 중�?
      if (lenis) {
        lenis.destroy();
      }
      
      // ?�업 ?�시
      popup.style.display = 'block';
      
      // ?�업 ?��? ?�치 ?�크�?강제 ?�성??
      const popupContents = popup.querySelector('.popup_contents_wrap');
      if (popupContents) {
        popupContents.removeAttribute('data-lenis-prevent-wheel');
        popupContents.removeAttribute('data-lenis-prevent');
        popupContents.style.cssText = `
          overflow-y: auto !important;
          -webkit-overflow-scrolling: touch !important;
          overscroll-behavior: contain !important;
          height: 100vh !important;
          touch-action: pan-y !important;
        `;
        
        // ?�치 ?�벤??강제 ?�용
        popupContents.addEventListener('touchstart', function(e) {
          e.stopPropagation();
        }, { passive: true });
        
        popupContents.addEventListener('touchmove', function(e) {
          e.stopPropagation();
        }, { passive: true });
      }
    }
  });
});
// E : ?�업 ?�기

// ?��S : ?�업 ?�기
$(function () {
  $(document).on("click", function (e) {
    const $target = $(e.target);

    // ?��?�기 버튼 ?�릭 ??
    if ($target.closest(".btn_close").length) {
      const $popupWrap = $target.closest(".popup_wrap");
      if ($popupWrap.length) {
        $popupWrap.hide();
        enableBodyScroll();
      }
      return;
    }

    // ?��popup_contents_wrap ?�릭 ?�도 ?�함?�서 ?�기
    const $popupContents = $target.closest(".popup_contents_wrap");
    if ($popupContents.length && $target.is(".popup_contents_wrap")) {
      const $popupWrap = $target.closest(".popup_wrap");
      if ($popupWrap.length) {
        $popupWrap.hide();
        enableBodyScroll();
      }
    }
  });

  // ?��?�업 ?�힐 ??body ?�크�??�성??
  function enableBodyScroll() {
    // body ?�크�??�치 복원
    const scrollY = document.body.style.top;
    document.body.style.position = '';
    document.body.style.top = '';
    document.body.style.width = '';
    window.scrollTo(0, parseInt(scrollY || '0') * -1);
    
    // Lenis ?�시??
    lenis.start();
  }
});
// E : ?�업 ?�기

// ?��S : map list ?�직이�? /* 250604추�??�� */
let lastScrollY = window.scrollY;
const stickyBox = document.querySelector(".map_list");

window.addEventListener("scroll", () => {
  const currentScrollY = window.scrollY;
  const width = window.innerWidth;
  if (width > 1440) {
    //250604 추�?
    if (stickyBox != null) {
      if (currentScrollY > lastScrollY) {
        // ?�래�??�크롤할 ??
        stickyBox.style.top = "24px";
      } else {
        // ?�로 ?�크롤할 ??
        stickyBox.style.top = "124px";
      }
    }
  } else {
    if (stickyBox != null) {
      if (currentScrollY > lastScrollY) {
        // ?�래�??�크롤할 ??
        stickyBox.style.top = "24px";
      } else {
        // ?�로 ?�크롤할 ??
        stickyBox.style.top = "74px";
      }
    }
  }

  lastScrollY = currentScrollY;
});
// E : map list ?�직이�?

// ?�� SCROLL SCRIPT
// ?��AOS
AOS.init();

// ?��Lenis

let lenis;

function handleStartLenis() {
  lenis = new Lenis({
    lerp: 0.1, // ?�크롤의 부?�러???�도
    smoothWheel: true,
    smoothTouch: false,
  });
  gsap.ticker.add((time) => {
    lenis.raf(time * 1000);
  });
  gsap.ticker.lagSmoothing(0);
}
handleStartLenis();

export default lenis;

function mobileMenu() {
  const mNav = document.querySelectorAll(".sitemap ol > li.depth1");

  mNav.forEach((item) => {
    const trigger = item.querySelector(":scope > span");
    const depth2 = item.querySelector(":scope > .depth2");

    if (!trigger || !depth2 || trigger.dataset.mobileMenuBound === "true") {
      return;
    }

    trigger.dataset.mobileMenuBound = "true";
    trigger.addEventListener("click", function () {
      if (window.innerWidth > 1440) {
        return;
      }

      if (!item.classList.contains("active")) {
        item.classList.add("active");
        depth2.style.maxHeight = depth2.scrollHeight + "px";
      } else {
        item.classList.remove("active");
        depth2.style.maxHeight = null;
      }
    });
  });
}
