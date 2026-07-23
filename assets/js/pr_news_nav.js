// PR 뉴스 상세페이지 이전글/다음글 자동 연결
// 파일명 규칙: pr_news_view_YYMMDD.html
// 뉴스를 추가/삭제할 때는 아래 NEWS_DATES 배열만 수정하면 됩니다.
(function () {
  const NEWS_DATES = ["251127", "260121", "260519", "260527"];

  function clearLink(el) {
    el.classList.add("no_content");
    const a = el.querySelector("a");
    const tit = el.querySelector(".tit");
    if (a) a.setAttribute("href", "");
    if (tit) tit.textContent = "";
  }

  function setLink(el, targetFile) {
    el.classList.remove("no_content");
    const a = el.querySelector("a");
    const tit = el.querySelector(".tit");
    if (a) a.setAttribute("href", targetFile);

    fetch(targetFile)
      .then(function (res) {
        return res.text();
      })
      .then(function (html) {
        const doc = new DOMParser().parseFromString(html, "text/html");
        const titleEl = doc.querySelector(".news_view_wrap .top .tit b");
        if (tit) tit.textContent = titleEl ? titleEl.textContent.trim() : "";
      })
      .catch(function () {
        // 제목을 가져오지 못해도 링크(href)는 이미 정상 연결된 상태로 둡니다.
      });
  }

  document.addEventListener("DOMContentLoaded", function () {
    const match = location.pathname.match(/pr_news_view_(\d{6})\.html$/);
    if (!match) return;

    const idx = NEWS_DATES.indexOf(match[1]);
    if (idx === -1) return;

    const prevFile = idx > 0 ? "pr_news_view_" + NEWS_DATES[idx - 1] + ".html" : null;
    const nextFile = idx < NEWS_DATES.length - 1 ? "pr_news_view_" + NEWS_DATES[idx + 1] + ".html" : null;

    const prevEl = document.querySelector(".news_list .prev");
    const nextEl = document.querySelector(".news_list .next");

    if (prevEl) prevFile ? setLink(prevEl, prevFile) : clearLink(prevEl);
    if (nextEl) nextFile ? setLink(nextEl, nextFile) : clearLink(nextEl);
  });
})();
