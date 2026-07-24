import { ensureBaronSsoAuth } from "../baron-sso-auth.js?v=20260721-worker2";

const pathSegments = location.pathname.split('/').filter(Boolean);
const rootMarkerSegments = ['ko', 'en', 'callback', 'assets', 'protected', 'public', 'recruit'];
const rootPrefix = pathSegments.length && !rootMarkerSegments.includes(pathSegments[0]) ? `/${pathSegments[0]}` : '';
const normalizePath = (path) => {
  const normalizedPath = (path || '/').replace(/\/index\.html$/i, '/');
  if (normalizedPath.length > 1 && normalizedPath.endsWith('/')) {
    return normalizedPath.slice(0, -1);
  }
  return normalizedPath;
};
const currentPath = normalizePath(location.pathname);
const landingPagePaths = [
  `${rootPrefix}/ko`,
  `${rootPrefix}/ko/`,
  `${rootPrefix}/ko/index.html`,
  `${rootPrefix}/en`,
  `${rootPrefix}/en/`,
  `${rootPrefix}/en/index.html`,
];
const publicPagePaths = [
  ...landingPagePaths,
  `${rootPrefix}/ko/sv_sw_kngil.html`,
  `${rootPrefix}/en/sv_sw_kngil.html`,
  `${rootPrefix}/ko/pr_`,
  `${rootPrefix}/en/pr_`,
  `${rootPrefix}/ko/gaia`,
  `${rootPrefix}/en/gaia`,
];
const normalizedLandingPagePaths = landingPagePaths.map(normalizePath);
const isLandingPage = normalizedLandingPagePaths.includes(currentPath);
const isPublicInfoPage = publicPagePaths.some((entry) => {
  const normalizedEntry = normalizePath(entry);
  if (normalizedEntry.endsWith('/pr_')) {
    return currentPath.startsWith(normalizedEntry);
  }

  return currentPath === normalizedEntry || currentPath.startsWith(`${normalizedEntry}/`);
});
const loginRequested = isPublicInfoPage && new URL(window.location.href).searchParams.get('login') === '1';

if (isLandingPage) {
  document.documentElement.dataset.baronPageMode = 'landing';
} else if (isPublicInfoPage) {
  document.documentElement.dataset.baronPageMode = 'public-info';
}

const authResult = await ensureBaronSsoAuth(
  isPublicInfoPage
    ? {
        publicPaths: publicPagePaths,
        forceAuth: loginRequested,
      }
    : {}
);

const isAuthenticated = Boolean(authResult?.session);
const isAnonymousPublicPage = Boolean(isPublicInfoPage && !isAuthenticated);

document.documentElement.dataset.baronAuthState = isAuthenticated ? 'authenticated' : 'anonymous';

// ?�� AJAX 관??SCRIPT
$(function () {
  const includeVersion = '20260623-4';
  const navIncludeFile = isAnonymousPublicPage ? 'nav-public.html' : 'nav.html';
  const includeBase = `${rootPrefix}/_include/eng`;

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
        console.error(`Failed to load ${url}:`, error || status);
        if (typeof callback === "function") callback();
      },
    });
  }

  function normalizeSiteLinks(root) {
    if (!root) {
      return;
    }

    root.querySelectorAll('a[href], img[src], source[src]').forEach((node) => {
      const attributeName = node.hasAttribute('href') ? 'href' : 'src';
      const rawValue = node.getAttribute(attributeName);

      if (!rawValue || /^(?:https?:|mailto:|tel:|javascript:|#)/i.test(rawValue)) {
        return;
      }

      const normalizedValue = rawValue
        .replace(/^\.\.\/(ko|en|recruit)\//, `${rootPrefix}/$1/`)
        .replace(/^\/(ko|en|recruit)\//, `${rootPrefix}/$1/`)
        .replace(/^\.\.\/callback\.html$/, `${rootPrefix}/callback.html`)
        .replace(/^\/callback\.html$/, `${rootPrefix}/callback.html`);

      if (normalizedValue !== rawValue) {
        node.setAttribute(attributeName, normalizedValue);
      }
    });
  }

  // nav 연결 (depth3 지원)
  function connectNavToMapList() {
    const currentPathname = location.pathname; // 전체 경로로 비교
    const navLinks = document.querySelectorAll(
      "header .corp nav ol li.depth1 ul.depth2 li a"
    );

    let matchedLink = null;

    navLinks.forEach((link) => {
      const href = link.getAttribute("href"); // 절대경로 그대로
      if (href === currentPathname || currentPathname.endsWith(href)) {
        if (matchedLink && matchedLink.closest('.depth3')) {
          return;
        }
        if (!matchedLink || link.closest('.depth3')) {
          matchedLink = link;
        }
      }
    });

    if (matchedLink) {
      const mapList = document.querySelector(".map_list");
      if (mapList) {
        mapList.innerHTML = "";
        matchedLink.closest(".depth1").classList.add("active");

        const hasDepth3 = matchedLink.closest("li.has_depth3");
        if (hasDepth3) {
          matchedLink.closest(".depth1").querySelectorAll("li.has_depth3").forEach(el => {
            el.classList.remove("active");
          });
          hasDepth3.classList.add("active");
        }

        const liHome = document.createElement("li");
        liHome.innerHTML = '<i class="home"></i>';
        mapList.appendChild(liHome);

        const categoryTitle = matchedLink
          .closest(".depth1")
          ?.querySelector("span")
          ?.textContent.trim();
        const subTitle = matchedLink
          .closest(".depth1")
          ?.querySelector("em")
          ?.textContent.trim();
        const mainTitle = categoryTitle.replace(subTitle, "").trim();

        const liCategory = document.createElement("li");
        liCategory.textContent = mainTitle || "";
        mapList.appendChild(liCategory);

        const depth3El = matchedLink.closest('.depth3');
        if (depth3El) {
          const depth2Link = matchedLink.closest('.has_depth3')?.querySelector('a');
          const depth2Title = depth2Link ? depth2Link.textContent.trim() : "";
          const liDepth2 = document.createElement("li");
          liDepth2.textContent = depth2Title;
          mapList.appendChild(liDepth2);

          const targetTitle = matchedLink.textContent.trim();
          const liOn = document.createElement("li");
          liOn.classList.add("on");
          liOn.textContent = targetTitle || "";
          mapList.appendChild(liOn);
        } else {
          const targetTitle = matchedLink.textContent.trim();
          const liOn = document.createElement("li");
          liOn.classList.add("on");
          liOn.textContent = targetTitle || "";
          mapList.appendChild(liOn);
        }
      }
    }
  }

  // PC GNB 패키지 S/W 3depth 탭 전환 기능
  function initPackageSWTab() {
    const $dropdown = $('.package_sw_dropdown');
    if (!$dropdown.length) return;

    const $menuItems = $dropdown.find('> li.has_depth3');

    // 패키지 S/W 1depth 메뉴 호버 시 드롭다운이 열리면 첫 번째 항목 기본 활성화
    $dropdown.closest('.depth1').on('mouseenter', function () {
      if (!$menuItems.filter('.active').length) {
        $menuItems.removeClass('active');
        $menuItems.first().addClass('active');
      }
    });

    // 2depth 메뉴 호버 시 active 클래스 전환
    $menuItems.on('mouseenter', function () {
      $menuItems.removeClass('active');
      $(this).addClass('active');
    });
  }

  function trimPopupDepth3Nav() {
    const popupNav = document.querySelector(".popup_wrap.sitemap .popup_contents_wrap nav");

    if (!popupNav) {
      return;
    }

    popupNav.querySelectorAll("li.has_depth3 > .depth3").forEach((depth3) => {
      depth3.remove();
    });
  }

  function trimPublicNav(root) {
    if (!isAnonymousPublicPage || !root) {
      return;
    }

    const allowedLabels = ['Package S/W', 'Service S/W', 'Big Room', 'PR Center'];
    const topLevels = root.querySelectorAll('ol > li.depth1');
    topLevels.forEach((item) => {
      const label = item.querySelector('span')?.textContent.replace(/\s+/g, ' ').trim() || '';
      const shouldKeep = allowedLabels.some((allowedLabel) => label.includes(allowedLabel));

      if (!shouldKeep) {
        // li는 유지하고 링크만 비워 sitemap 팝업의 :nth-child 기반 3depth 스타일 위치를 보존한다.
        item.classList.add('menu_hidden');
        const depth2 = item.querySelector(':scope > ul.depth2');
        if (depth2) {
          depth2.innerHTML = '';
        }
      }
    });
  }

  function configureHeaderActions(root) {
    if (!root) {
      return;
    }

    const loginWrap = root.querySelector('.header_login');
    const loginLink = root.querySelector('.header_login_link');
    if (!loginWrap || !loginLink) {
      return;
    }

    if (isAuthenticated) {
      loginWrap.hidden = false;
      loginLink.textContent = 'LOGOUT';
      loginLink.href = '#';
      loginLink.onclick = (event) => {
        event.preventDefault();
        window.baronSsoLogout?.();
      };
      return;
    }

    if (!isPublicInfoPage) {
      loginWrap.hidden = true;
      return;
    }

    loginWrap.hidden = false;
    loginLink.textContent = 'LOGIN';
    loginLink.href = `${location.pathname}?login=1`;
    loginLink.onclick = null;
  }

  function loadSitemapNav() {
    if (!$('.container').hasClass('recruit')) {
      loadHTML(`${includeBase}/${navIncludeFile}?v=${includeVersion}`, '.popup_wrap.sitemap .popup_contents_wrap nav', function () {
        normalizeSiteLinks(document.querySelector('.popup_wrap.sitemap .popup_contents_wrap nav'));
        trimPublicNav(document.querySelector('.popup_wrap.sitemap .popup_contents_wrap nav'));
        mobileMenu();
      });
    } else {
      loadHTML(`${includeBase}/nav_recruit.html?v=${includeVersion}`, '.popup_wrap.sitemap .popup_contents_wrap nav', function () {
        mobileMenu();
      });
    }
  }

  if (!$('.container').hasClass('recruit')) {
    loadHTML(`${includeBase}/header.html?v=${includeVersion}`, '#header', function () {
      normalizeSiteLinks(document.querySelector('#header'));
      loadHTML(`${includeBase}/${navIncludeFile}?v=${includeVersion}`, '#header .corp .nav', function () {
        normalizeSiteLinks(document.querySelector('#header .corp .nav'));
        connectNavToMapList();
        initPackageSWTab();
        trimPublicNav(document.querySelector('#header .corp .nav'));
      });
      configureHeaderActions(document.querySelector('#header'));
      loadSitemapNav();
    });
  } else {
    loadHTML(`${includeBase}/header_recruit.html?v=${includeVersion}`, '#header_recruit', function () {
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

  loadHTML(`${includeBase}/footer.html?v=${includeVersion}`, '#footer', function () {
    normalizeSiteLinks(document.querySelector('#footer'));
    loadHTML(`${includeBase}/${navIncludeFile}?v=${includeVersion}`, '#footer .nav', function () {
      normalizeSiteLinks(document.querySelector('#footer .nav'));
      trimPublicNav(document.querySelector('#footer .nav'));
    });
  });
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

  let showMapList = null;
  const headerNavMM = gsap.matchMedia();
  headerNavMM.add("(max-width: 1400px)", () => {
    showMapList = gsap
      .from(".map_list", {
        y: -40,
        autoAlpha: 0,
        paused: true,
        duration: 0.2,
      })
      .progress(1);
    return () => {
      showMapList = null;
    };
  });

  ScrollTrigger.create({
    start: "top top",
    end: 99999,
    onUpdate: (self) => {
      if (lenis.isStopped) return;
      if (self.direction === -1) {
        showNav.play();
        showMapList && showMapList.play();
      } else {
        showNav.reverse();
        showMapList && showMapList.reverse();
      }
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

      const isActive = item.classList.contains("active");

      // 다른 모든 활성화된 메뉴 닫기 (아코디언 동작)
      mNav.forEach((otherItem) => {
        if (otherItem !== item) {
          otherItem.classList.remove("active");
          const otherDepth2 = otherItem.querySelector(":scope > .depth2");
          if (otherDepth2) {
            otherDepth2.style.maxHeight = null;
          }
        }
      });

      if (!isActive) {
        item.classList.add("active");
        depth2.style.maxHeight = depth2.scrollHeight + "px";
      } else {
        item.classList.remove("active");
        depth2.style.maxHeight = null;
      }
    });
  });
}
