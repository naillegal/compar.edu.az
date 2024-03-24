// blog first clickable tags
const buttons = document.querySelectorAll(".blog-first-tags button");
const sections = {
  Hamısı: document.querySelector(".blog-all"),
  "UX/UI": document.querySelector(".blog-uix"),
  Qrafik: document.querySelector(".blog-graphic"),
  JAVA: document.querySelector(".blog-java"),
  "C#": document.querySelector(".blog-csharp"),
  Python: document.querySelector(".blog-python"),
  İngilis: document.querySelector(".blog-english"),
  SMM: document.querySelector(".blog-smm"),
};

// loading effect function
function toggleLoading() {
  const blogMainElements = document.querySelectorAll(".blog-main");

  blogMainElements.forEach((element) => {
    element.classList.add("loading");
  });

  setTimeout(() => {
    blogMainElements.forEach((element) => {
      element.classList.remove("loading");
    });
  }, 1000);
}

buttons.forEach((button) => {
  button.addEventListener("click", function () {
    buttons.forEach((btn) => btn.classList.remove("active"));
    this.classList.add("active");

    Object.values(sections).forEach(
      (section) => (section.style.display = "none")
    );

    const section = sections[this.textContent];
    if (section) {
      section.style.display = "block";
      toggleLoading();
    }
  });
});
