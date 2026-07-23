<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

$login = $_SESSION['login'] ?? [];
$isLogin = isset($_SESSION['login']);
$auth    = $_SESSION['login']['auth_bc'] ?? '';
$coBc    = $_SESSION['login']['co_bc'] ?? '';
// 권한 그룹 (개인회원 SA150200 은 관리자 버튼 비노출)
$isSuperAdmin   = ($coBc !== 'SA150200') && in_array($auth, ['BS100100', 'BS100200']); 
$isCompanyAdmin = ($coBc !== 'SA150200') && in_array($auth, ['BS100100', 'BS100200', 'BS100300', 'BS100400']);

// 큰길(서비스) 페이지에서만 하단 플로팅 메뉴(서비스 바로가기) 노출
$floatingMenuPages = ['analysis.php', 'primary.php', 'provided.php', 'results.php', 'value.php', 'buy.php'];
$currentPage       = basename($_SERVER['SCRIPT_NAME'] ?? $_SERVER['PHP_SELF'] ?? '');
$showFloatingMenu  = in_array($currentPage, $floatingMenuPages, true);
?>
<head>
  <style>
    .icon-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      margin-right: 6px;
    }

    .icon-btn img {
      width: 28px;
      height: 28px;
      /* filter: invert(1); 흰색 아이콘 */
      opacity: 0.8;
      transition: 0.2s;
    }

    .icon-btn:hover img {
      opacity: 1;
    }
    /* 툴팁 래퍼 */
    .tooltip {
      position: relative;
    }

    /* 툴팁 박스 */
    .tooltip-text {
      position: absolute;
      bottom: 120%;
      left: 50%;
      transform: translateX(-50%);
      white-space: nowrap;

      background: rgba(20, 20, 20, 0.95);
      color: #fff;
      font-size: 12px;
      padding: 6px 10px;
      border-radius: 4px;

      opacity: 0;
      visibility: hidden;
      transition: opacity 0.2s ease, transform 0.2s ease;
      pointer-events: none;
      z-index: 1000;
    }

    /* 말풍선 화살표 */
    .tooltip-text::after {
      content: '';
      position: absolute;
      top: 100%;
      left: 50%;
      transform: translateX(-50%);
      border-width: 6px;
      border-style: solid;
      border-color: rgba(20, 20, 20, 0.95) transparent transparent transparent;
    }

    /* hover 시 노출 */
    .tooltip:hover .tooltip-text {
      opacity: 1;
      visibility: visible;
      transform: translateX(-50%) translateY(-4px);
    }

  </style>
  <script>
    window.IS_LOGIN = <?= isset($_SESSION['login']) ? 'true' : 'false' ?>;
    
    // SSO 토큰 만료 시간 전역 변수 세팅
    <?php if (isset($_SESSION['access_token']) && isset($_SESSION['access_expires_at'])): ?>
        window.SSO_EXPIRES_AT = <?= json_encode($_SESSION['access_expires_at']) ?>;
    <?php else: ?>
        window.SSO_EXPIRES_AT = false; 
    <?php endif; ?>

    let isSsoRefreshing = false;

    // SSO 기반 세션 연장
    function startSessionKeeper() {
        if (!window.SSO_EXPIRES_AT) {
            //console.log("비로그인 상태이므로 SSO 세션 연장 타이머를 실행하지 않습니다.");
            return;
        }

        if (window.ssoTimer) {
            clearTimeout(window.ssoTimer);
        }

        //  남은 시간 계산
        const currentUnixTime = Math.floor(Date.now() / 1000);
        const timeLeft = window.SSO_EXPIRES_AT - currentUnixTime;

        // 이미 만료되었다면 즉시 로그아웃 처리
        if (timeLeft <= 0) {
            //console.log("토큰이 이미 만료되었습니다.");
            location.href = "../bbs/logout.php";
            return;
        }

        // 남은 시간의 80% 시점을 타이머 대기 시간으로 설정
        const refreshDelay = timeLeft * 0.8 * 1000;
        //console.log("SSO 토큰 연장 대기: " + (refreshDelay / 1000).toFixed(1) + "초 뒤에 갱신 시도");

        window.ssoTimer = setTimeout(function () {
            
            if (isSsoRefreshing) {
                //console.log("이미 갱신 통신이 진행 중입니다. 중복 요청을 방지합니다.");
                return;
            }
            
            isSsoRefreshing = true;

            $.ajax({
                url: "../bbs/sso_token_refresh.php",
                type: "POST",
                dataType: "json",
                xhrFields: {
                    withCredentials: true
                },
                success: function (res) {
                    isSsoRefreshing = false;

                    if (res.success) {
                        //console.log("SSO 토큰 갱신 완료");
                        if (res.expires_at) {
                            window.SSO_EXPIRES_AT = res.expires_at;
                        }
                        startSessionKeeper();
                    } else {
                        location.href = "../bbs/logout.php";
                    }
                },
                error: function (xhr) {
                    isSsoRefreshing = false;
                    if (xhr.status === 403 || xhr.status === 401) {
                        location.href = "../bbs/logout.php";
                    }
                }
            });
        }, refreshDelay);
    }

    // 타이머 가동
    startSessionKeeper();

    function openAdminPopup(url, title = 'adminPopup') {
      const w = 1500;
      const h = 900;
      const left = (window.screen.width / 2) - (w / 2);
      const top = (window.screen.height / 2) - (h / 2);
      
      window.open(url, title, `width=${w},height=${h},top=${top},left=${left},scrollbars=yes,resizable=yes`);
    }
  </script>
</head>

<!-- header -->
<div class="header-wrap">
  <header class="header">
    <h1>
      <a href="/kngil/skin/index.php">KNGIL</a>
    </h1>

    <div class="header-right">

      <?php if ($isLogin): ?>

        <!-- 통합 관리자 (관리자/개발자만) -->
        <?php if ($isSuperAdmin): ?>
          <a href="javascript:openAdminPopup('/kngil/skin/adm.php', 'superAdmin')"
            class="icon-btn tooltip">
            <img src="/kngil/img/ico/ico_super_admin.svg" class="header-icon" alt="통합 관리자">
            <span class="tooltip-text">통합 관리자</span>
          </a>
        <?php endif; ?>

        <!-- 기업 관리자 (관리자/개발자/메인/서브) -->
        <?php if ($isCompanyAdmin): ?>
          <a href="javascript:openAdminPopup('/kngil/skin/adm_comp.php', 'companyAdmin')"
            class="icon-btn tooltip">
            <img src="/kngil/img/ico/ico_company_admin.svg" class="header-icon" alt="기업 관리자">
            <span class="tooltip-text">기업 관리자</span>
          </a>
        <?php endif; ?>
      <?php endif; ?>

      <!-- 기존 사용자 메뉴 -->
      <div class="menu-box">
        <button class="menu-user">
          <img src="/kngil/img/ico/ico_user.svg" alt="user">
        </button>

        <ul class="menu-list">
          <!-- 비로그인 -->
          <!-- <li class="<?= $isLogin ? 'd-none' : '' ?>">
            <a class="my-join" href="javascript:agreement();">회원가입</a>
          </li> -->
          <li class="<?= $isLogin ? 'd-none' : '' ?>">
            <a class="my-login" href="javascript:login();">로그인</a>
          </li>

          <!-- 로그인 -->
          <li class="<?= $isLogin ? '' : 'd-none' ?>">
            <a class="my-join" href="javascript:mypage02()">마이페이지</a>
          </li>
          <li class="<?= $isLogin ? '' : 'd-none' ?>">
            <a class="my-login" href="/kngil/bbs/logout.php">로그아웃</a>
          </li>
        </ul>
      </div>

      <div>
        <button class="menu-all">
          <span></span>
          <span></span>
          <span></span>
        </button>
        <?php include __DIR__ . "/_nav.php";?>
      </div>
    </div>
  </header>
</div>
<!--// header -->


<?php if ($showFloatingMenu): ?>
<!-- floating_menu -->
<div class="floating-menu">    
        <div class="floating-kngil">
            <a href="javascript:void(0);" onclick="openKngilMapApp('<?= $isLogin ? $login['user_id']: '' ?>');">
                <i class="ico-logo">
                    <img src="/kngil/img/logo_kngil.svg" alt="KNGIL">
                </i>
                <span>서비스 <br>바로 <br>가기</span>
            </a>
        </div>    
</div>
<!-- //floating_menu -->
<?php endif; ?>
<script>
/* 수정된 스크립트 부분 */
async function openKngilMapApp(userId) {
    // 1. 함수 진입 확인용 (가장 먼저 실행되어야 함)
    console.log("함수 호출 시작 - 전달된 ID:", userId);
    // alert("함수 호출됨: " + userId); // 브라우저에서 알림이 뜨는지 확인하세요.

    if (!userId || userId === "") {
        console.error("사용자 ID가 없습니다.");
		login();
        //alert("로그인 정보가 없습니다. 다시 로그인해주세요.");
        return;
    }

    // 2. 로그 기록 API 호출
    try {
        console.log("로그 기록 시도 중...");
        const logRes = await fetch('/kngil/bbs/log_service_access.php');
        const logData = await logRes.json();
        console.log("서버 응답:", logData);
    } catch (e) {
        console.warn("로그 기록 실패(무시하고 진행):", e);
    }

    // 3. 앱 오픈 로직
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
    console.log("폼 전송 완료");
}
</script>