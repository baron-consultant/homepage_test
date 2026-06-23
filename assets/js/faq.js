document.addEventListener("DOMContentLoaded", () => {
  const isEnglish = location.pathname.includes("/en/");

  const pageContent = isEnglish
    ? {
        title: "FAQ | Baron Consultants",
        breadcrumbSection: "Customer Support",
        breadcrumbCurrent: "FAQ",
        pageLabel: "Go to page",
        sampleQuestion: "Add your sample question here to display it as an FAQ item.",
        sampleAnswer:
          "This is a sample answer area. Keep adding objects in the same format to the array below and the page will paginate automatically in groups of 10. Click a question to expand the answer and click again or open another item to close it.",
      }
    : {
        title: "FAQ | (주)바론컨설턴트",
        breadcrumbSection: "고객지원",
        breadcrumbCurrent: "FAQ",
        pageLabel: "페이지로 이동",
        sampleQuestion: "예시 질문을 이 위치에 추가하면 FAQ 항목으로 표시됩니다.",
        sampleAnswer:
          "이 영역은 답변 예시입니다. 동일한 형식의 객체를 아래 배열에 계속 추가하면 10개 단위로 자동 페이징되고, 질문을 클릭하면 답변이 열리고 다시 클릭하면 닫힙니다.",
      };

  document.title = pageContent.title;

  if (typeof AOS !== "undefined") {
    AOS.init({ once: true });
  }

  const faqItems = [
    {
      question: pageContent.sampleQuestion,
      answer: pageContent.sampleAnswer,
    },
  ];

  const itemsPerPage = 10;
  let currentPage = 1;

  const faqList = document.getElementById("faqList");
  const pagination = document.getElementById("faqPagination");
  const breadcrumb = document.querySelector(".map_list");

  if (breadcrumb) {
    breadcrumb.innerHTML = `
      <li><i class="home"></i></li>
      <li>${pageContent.breadcrumbSection}</li>
      <li class="on">${pageContent.breadcrumbCurrent}</li>
    `;
  }

  function createFaqItem(item, index) {
    const li = document.createElement("li");
    li.className = "faq-item";

    const questionId = `faq-question-${currentPage}-${index}`;
    const answerId = `faq-answer-${currentPage}-${index}`;

    li.innerHTML = `
      <button
        type="button"
        class="faq-question"
        id="${questionId}"
        aria-expanded="false"
        aria-controls="${answerId}"
      >
        ${item.question}
      </button>
      <div class="faq-answer" id="${answerId}" role="region" aria-labelledby="${questionId}">
        <div class="faq-answer__inner">
          <p>${item.answer}</p>
        </div>
      </div>
    `;

    const button = li.querySelector(".faq-question");
    const answer = li.querySelector(".faq-answer");

    button.addEventListener("click", () => {
      const isOpen = li.classList.contains("is-open");

      faqList.querySelectorAll(".faq-item").forEach((otherItem) => {
        otherItem.classList.remove("is-open");
        const otherButton = otherItem.querySelector(".faq-question");
        const otherAnswer = otherItem.querySelector(".faq-answer");
        otherButton.setAttribute("aria-expanded", "false");
        otherAnswer.style.maxHeight = null;
      });

      if (!isOpen) {
        li.classList.add("is-open");
        button.setAttribute("aria-expanded", "true");
        answer.style.maxHeight = `${answer.scrollHeight}px`;
      }
    });

    return li;
  }

  function renderPagination(totalPages) {
    pagination.innerHTML = "";

    if (totalPages <= 1) {
      pagination.hidden = true;
      return;
    }

    pagination.hidden = false;

    for (let page = 1; page <= totalPages; page += 1) {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "faq-page-btn";
      button.textContent = String(page);
      button.setAttribute("aria-label", `${pageContent.pageLabel} ${page}`);

      if (page === currentPage) {
        button.classList.add("is-active");
        button.setAttribute("aria-current", "page");
      }

      button.addEventListener("click", () => {
        if (page === currentPage) {
          return;
        }

        currentPage = page;
        renderFaqPage();
        window.scrollTo({
          top: document.querySelector(".faq-board").offsetTop - 120,
          behavior: "smooth",
        });
      });

      pagination.appendChild(button);
    }
  }

  function renderFaqPage() {
    const startIndex = (currentPage - 1) * itemsPerPage;
    const visibleItems = faqItems.slice(startIndex, startIndex + itemsPerPage);
    const totalPages = Math.ceil(faqItems.length / itemsPerPage) || 1;

    faqList.innerHTML = "";
    visibleItems.forEach((item, index) => {
      faqList.appendChild(createFaqItem(item, index));
    });

    renderPagination(totalPages);
  }

  renderFaqPage();
});