async function openKngilMapApp(userId) {
    if (!userId || userId === "") {
        console.error("사용자 ID가 없습니다.");
        login();
        return;
    }

    try {
        const logRes = await fetch('/kngil/bbs/log_service_access.php');
        const logData = await logRes.json();
        console.log("서버 응답:", logData);
    } catch (e) {
        console.warn("로그 기록 실패(무시하고 진행):", e);
    }

    var appUrl = (userId === "dev01")
        ? '/kngil_app_khg/sys/controller/location/Location_controller.php'
        : '/kngil_app/sys/controller/location/Location_controller.php';

    const popupName = 'kngilAppPopup';
    const width = 1400;
    const height = 900;
    const left = (window.screen.width / 2) - (width / 2);
    const top = (window.screen.height / 2) - (height / 2);

    const win = window.open('', popupName, `width=${width},height=${height},left=${left},top=${top},resizable=yes,scrollbars=yes`);

    if (!win) {
        alert("팝업 차단 설정이 되어 있습니다. 팝업을 허용해 주세요.");
        return;
    }

    const form = document.createElement('form');
    form.method = 'POST';
    form.action = appUrl;
    form.target = popupName;

    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'ActionMode';
    input.value = 'SCREEN_01';
    form.appendChild(input);

    document.body.appendChild(form);
    form.submit();
    document.body.removeChild(form);
}

// 스크롤 최상단 여부에 따라 우측 플로팅 메뉴 <-> 상단 가로형 버튼 전환
(function () {
    function initFloatingScrollToggle() {
        const floatingMenu = document.querySelector('.floating-menu');
        const floatingTopBtn = document.querySelector('.floating-top-btn');
        if (!floatingMenu || !floatingTopBtn) return;

        // Lenis 관성 스크롤 특성상 scrollY가 0에 서서히 수렴하므로,
        // 임계값을 살짝 두어 최상단 복귀 시 체감 반응 속도를 높인다.
        const TOP_THRESHOLD = 10;

        function update() {
            const isTop = window.scrollY <= TOP_THRESHOLD;
            floatingMenu.classList.toggle('is-visible', !isTop);
            floatingTopBtn.classList.toggle('is-visible', isTop);
        }

        update();
        window.addEventListener('scroll', update, { passive: true });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initFloatingScrollToggle);
    } else {
        initFloatingScrollToggle();
    }
})();

// 사용가이드 레이어팝업 (영상/문서 탭 전환)
(function () {
    function initGuideModal() {
        const modal = document.getElementById('guideModal');
        if (!modal) return;

        const PDF_SRC = './img/guide/kngil_guide_v1.0.pdf';

        const tabs = modal.querySelectorAll('.guide-tab');
        const panels = modal.querySelectorAll('.guide-panel');
        const video = modal.querySelector('.guide-video');
        const pdfFrame = modal.querySelector('.guide-pdf');
        const videoPanel = modal.querySelector('.guide-panel-video');

        function setTab(name) {
            tabs.forEach(function (tab) {
                tab.classList.toggle('active', tab.dataset.guideTab === name);
            });
            panels.forEach(function (panel) {
                panel.classList.toggle('active', panel.dataset.guidePanel === name);
            });

            if (name === 'pdf' && pdfFrame && !pdfFrame.getAttribute('src')) {
                pdfFrame.setAttribute('src', PDF_SRC);
            }
            if (name !== 'video' && video) {
                video.pause();
            }
        }

        function openModal() {
            modal.classList.add('is-open');
            modal.setAttribute('aria-hidden', 'false');
            document.body.classList.add('guide-modal-open');
        }

        function closeModal() {
            modal.classList.remove('is-open');
            modal.setAttribute('aria-hidden', 'true');
            document.body.classList.remove('guide-modal-open');
            if (video) video.pause();
        }

        // 커스텀 비디오 컨트롤 (사이트 전역 CSS가 네이티브 컨트롤을 강제로 숨기기 때문에 자체 구현)
        if (video && videoPanel) {
            const centerPlayBtn = videoPanel.querySelector('.video-center-play');
            const playToggleBtn = videoPanel.querySelector('.video-play-toggle');
            const muteToggleBtn = videoPanel.querySelector('.video-mute-toggle');
            const fullscreenBtn = videoPanel.querySelector('.video-fullscreen-toggle');
            const seekInput = videoPanel.querySelector('.video-seek');
            const currentTimeEl = videoPanel.querySelector('.video-time-current');
            const durationEl = videoPanel.querySelector('.video-time-duration');
            let isSeeking = false;

            function formatTime(sec) {
                if (!isFinite(sec) || sec < 0) return '0:00';
                const m = Math.floor(sec / 60);
                const s = Math.floor(sec % 60);
                return m + ':' + (s < 10 ? '0' : '') + s;
            }

            function togglePlay() {
                if (video.paused || video.ended) {
                    video.play();
                } else {
                    video.pause();
                }
            }

            video.addEventListener('play', function () {
                videoPanel.classList.add('is-playing');
            });
            video.addEventListener('pause', function () {
                videoPanel.classList.remove('is-playing');
            });
            video.addEventListener('ended', function () {
                videoPanel.classList.remove('is-playing');
            });
            video.addEventListener('loadedmetadata', function () {
                if (durationEl) durationEl.textContent = formatTime(video.duration);
            });
            video.addEventListener('timeupdate', function () {
                if (currentTimeEl) currentTimeEl.textContent = formatTime(video.currentTime);
                if (seekInput && !isSeeking && video.duration) {
                    seekInput.value = (video.currentTime / video.duration) * 100;
                }
            });
            video.addEventListener('click', togglePlay);

            if (centerPlayBtn) centerPlayBtn.addEventListener('click', togglePlay);
            if (playToggleBtn) playToggleBtn.addEventListener('click', togglePlay);

            if (seekInput) {
                seekInput.addEventListener('input', function () {
                    isSeeking = true;
                    if (video.duration) {
                        video.currentTime = (seekInput.value / 100) * video.duration;
                    }
                });
                seekInput.addEventListener('change', function () {
                    isSeeking = false;
                });
            }

            if (muteToggleBtn) {
                muteToggleBtn.addEventListener('click', function () {
                    video.muted = !video.muted;
                    videoPanel.classList.toggle('is-muted', video.muted);
                });
            }

            if (fullscreenBtn) {
                fullscreenBtn.addEventListener('click', function () {
                    const requestFs = videoPanel.requestFullscreen || videoPanel.webkitRequestFullscreen;
                    if (requestFs) requestFs.call(videoPanel);
                });
            }
        }

        document.querySelectorAll('[data-guide-open]').forEach(function (btn) {
            btn.addEventListener('click', function (e) {
                e.preventDefault();
                openModal();
            });
        });

        tabs.forEach(function (tab) {
            tab.addEventListener('click', function () {
                setTab(tab.dataset.guideTab);
            });
        });

        modal.querySelectorAll('[data-guide-close]').forEach(function (btn) {
            btn.addEventListener('click', closeModal);
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && modal.classList.contains('is-open')) {
                closeModal();
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initGuideModal);
    } else {
        initGuideModal();
    }
})();
