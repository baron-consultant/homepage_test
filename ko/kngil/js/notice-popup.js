(function () {
  var STORAGE_KEY = 'kngil_notice_popup_hide_date';
  // 공지 팝업 종료 시각 이후에는 자동으로 팝업을 노출하지 않음
  var EXPIRE_AT = new Date('2026-08-18T13:00:00+09:00').getTime();

  function getLocalDateString() {
    var d = new Date();
    var m = String(d.getMonth() + 1).padStart(2, '0');
    var day = String(d.getDate()).padStart(2, '0');
    return d.getFullYear() + '-' + m + '-' + day;
  }

  function isExpired() {
    return Date.now() >= EXPIRE_AT;
  }

  function isHiddenToday() {
    try {
      return window.localStorage.getItem(STORAGE_KEY) === getLocalDateString();
    } catch (err) {
      return false;
    }
  }

  function hideToday() {
    try {
      window.localStorage.setItem(STORAGE_KEY, getLocalDateString());
    } catch (err) {
      /* ignore */
    }
  }

  function initSwiper(wrap) {
    var el = wrap.querySelector('.notice-pop-swiper');
    if (!el || typeof window.Swiper === 'undefined') return;
    new window.Swiper(el, {
      slidesPerView: 1,
      spaceBetween: 0,
      loop: false,
      pagination: {
        el: el.querySelector('.notice-pop-swiper__pagination'),
        clickable: true,
      },
    });
  }

  function isOpen(wrap) {
    return wrap.classList.contains('is-open');
  }

  function openPopup(wrap) {
    wrap.classList.add('is-open');
  }

  function closePopup(wrap) {
    if (!isOpen(wrap)) return;
    wrap.classList.remove('is-open');
  }

  function init() {
    var wrap = document.getElementById('pop_notice');
    if (!wrap) return;

    initSwiper(wrap);

    if (!isExpired() && !isHiddenToday()) {
      openPopup(wrap);
    }

    // 종료 시각이 되면 열려 있어도 자동으로 닫고, 이후에는 다시 열리지 않음
    var remaining = EXPIRE_AT - Date.now();
    if (remaining > 0) {
      window.setTimeout(function () {
        closePopup(wrap);
      }, remaining);
    }

    var noShowBtn = document.getElementById('pop-no-show-btn');
    if (noShowBtn) {
      noShowBtn.addEventListener('click', function () {
        hideToday();
        closePopup(wrap);
      });
    }

    var closeBtn = wrap.querySelector('.pop-close-btn');
    if (closeBtn) {
      closeBtn.addEventListener('click', function () {
        closePopup(wrap);
      });
    }

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen(wrap)) {
        closePopup(wrap);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
