<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
?>
<!DOCTYPE html>
<html lang="ko">
  <head>
    <?php include __DIR__ . "/_head.php"; ?>
  </head>
  <body>
    <div class="wrap"> 
      <?php include __DIR__ . "/_header.php"; ?>
      <!-- container -->
      <div class="container buy">
        <section class="sub-header">
          <div class="page-title">
            <h2 data-aos="fade-down" data-aos-duration="1000">구매하기</h2>
            <p class="sub-txt">KNGIL 구매문의 및 제품 안내</p>
          </div>
        </section>
        <section class="contents-wrap full">
          <div class="inner">
            <h3 class="cont-tit"><span class="logo-c">KNGIL</span>로 <strong>기초조사 업무의 효율성</strong>을 높여보세요</h3>
            <div class="cont-wrapper">
              <div class="cont-left">
                
                <ul class="cont-list feature-list">
                  <li class="feature-item">
                    <div class="feature-item-inner">
                      <div class="feature-icon">
                        <i class="ico-natural"></i>
                      </div>
                      <div class="feature-decoration"></div>
                    </div>
                    <dl>
                      <dt class="feature-title">
                        자연조건 <br class="mo-only">사회특성
                      </dt>
                      <dd class="feature-desc">항목별 현황 분석<br class="pc-only"> 프로그램</dd>
                    </dl>
                  </li>
                  <li class="feature-item">
                    <div class="feature-item-inner">
                      <div class="feature-icon">
                        <i class="ico-gis"></i>
                      </div>
                      <div class="feature-decoration"></div>
                    </div>

                    <dl>
                      <dt class="feature-title">GIS 기반</dt>
                      <dd class="feature-desc">지형/공간 정보<br class="pc-only"> 분석 환경</dd>
                    </dl>
                  </li>
                  <li class="feature-item">
                    <div class="feature-item-inner">
                      <div class="feature-icon">
                        <i class="ico-data"></i>
                      </div>
                      <div class="feature-decoration"></div>
                    </div>

                    <dl>
                      <dt class="feature-title">데이터 <br class="mo-only">항목 다량</dt>
                      <dd class="feature-desc">도시계획, 상하수도 분야<br> 설계 기초자료 제공</dd>
                    </dl>
                  </li>
                  <li class="feature-item">
                    <div class="feature-item-inner">
                      <div class="feature-icon">
                        <i class="ico-coordinate"></i>
                      </div>
                      <div class="feature-decoration"></div>
                    </div>
                    <dl>
                      <dt class="feature-title">다양한 <br class="mo-only">좌표계 지원</dt>
                      <dd class="feature-desc">좌표(Bessel, GRS80)<br> 시각화 및 손쉬운 전환</dd>
                    </dl>
                  </li>
                  <li class="feature-item">
                    <div class="feature-item-inner">
                      <div class="feature-icon">
                        <i class="ico-standard"></i>
                      </div>
                      <div class="feature-decoration"></div>
                    </div>
                    <dl>
                      <dt class="feature-title">최신 기준 <br class="mo-only">설정</dt>
                      <dd class="feature-desc">추정사업비, 비작업일수<br> 관련 기준/지침 업데이트</dd>
                    </dl>
                  </li>
                </ul>
              </div>
              
              <div class="cont-right">
                <div class="contact-area">
                  <div class="tit-box">
                    <h4 class="tit">구매 상담</h4>
                    <p class="sub-text">KNGIL 담당자에게 직접 문의하기</p>
                  </div>
                  <ul class="contact-info">
                    <li class="tel">
                      <i></i>
                      <strong>02-6285-7755</strong>
                    </li>
                    <li class="mail">
                      <i></i>
                      <strong>baroncs@baroncs.co.kr</strong>
                    </li>
                  </ul>
                  <dl class="cs-info">
                    <dt>고객지원 운영 시간</dt>
                    <dd>
                      <p>평일 09:00 ~ 18:00</p> 
                      <span>※ 주말 및 공휴일 휴무 </span>      
                      <span>※ 기타 사항은 Q&A로 문의하세요.</span>
                    </dd>
                  </dl>

                </div>
                <div class="btn-wrap">
                  <a href="/kngil/bbs/qa_list.php" class="btn-contact">
                    <i class="ico-contact"></i>
                    KNGIL 구매문의
                  </a>
                  <a href="/kngil/download/KNGIL_leaflet.pdf" download class="btn-brochure">
                    <i class="ico-brochure"></i>
                    브로슈어
                  </a>
                </div>
                <p class="info-msg" style="display:none;">
                  <i class="ico-alert"></i>
                  <span>라이선스 중복 시 <strong>이용이 제한</strong>될 수 있습니다.</span>
                </p>
              </div>
            </div>
          </div>
        </section>
      </div>
      <!-- // container -->
      <?php include __DIR__ . "/_footer.php"; ?>
    </div>
    <?php
      include __DIR__ . "/pop_login.php";
      include __DIR__ . "/pop_join.php";
      include __DIR__ . "/pop_agreement.php";
      include __DIR__ . "/pop_mypage01.php";
      include __DIR__ . "/pop_mypage02.php";
      include __DIR__ . "/pop_mypage03.php";
      include __DIR__ . "/pop_password.php";
      include __DIR__ . "/pop_privacy.php";
      include __DIR__ . "/pop_search.php";
      include __DIR__ . "/pop_guide.php";
      include __DIR__ . "/_nav.php";
    ?>
    <script>
      window.IS_LOGIN = <?= isset($_SESSION['login']) ? 'true' : 'false' ?>;
    </script>
    <script src="/kngil/js/index.js"></script>
    <script src="/kngil/js/mypage.js"></script>
    <script src="/kngil/js/join.js"></script>
    <script type="module" src="/kngil/js/login.js"></script>
    <script src="/kngil/js/login_sms.js"></script>
    <script src="/kngil/js/value.js"></script>
  </body>
</html>