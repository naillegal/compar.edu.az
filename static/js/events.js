// news and events switcher 
document.addEventListener("DOMContentLoaded", function () {
  const headings = document.querySelectorAll(
    "#news-events-switch .switcher h5"
  );
  headings.forEach(function (heading) {
    heading.addEventListener("click", function () {
      headings.forEach(function (h) {
        h.classList.remove("active");
      });
      this.classList.add("active");
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const newsToggle = document.querySelector(".newstoggle");
  const eventsToggle = document.querySelector(".eventstoggle");
  const newsSection = document.querySelector(".news");
  const eventsSection = document.querySelector(".events");

  newsToggle.addEventListener("click", function () {
    newsSection.style.display = "block";
    eventsSection.style.display = "none";
    toggleLoading(newsSection);
  });

  eventsToggle.addEventListener("click", function () {
    newsSection.style.display = "none";
    eventsSection.style.display = "block";
    toggleLoading(eventsSection);
  });

  function toggleLoading(section) {
    const mainBoxes = section.querySelectorAll(".main-box");
    mainBoxes.forEach(function (box) {
      box.classList.add("loading");
    });

    setTimeout(function () {
      mainBoxes.forEach(function (box) {
        box.classList.remove("loading");
      });
    }, 1000); 
  }
});
