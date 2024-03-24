// courses-design
document.addEventListener("DOMContentLoaded", function () {
  const headings = document.querySelectorAll(".switch-tabs .switcher h5");
  const switchTabs = document.querySelectorAll(".switch-tabs");

  headings.forEach(function (heading) {
    heading.addEventListener("click", function () {
      headings.forEach(function (h) {
        h.classList.remove("active");
      });
      this.classList.add("active");

      switchTabs.forEach(function (tab) {
        tab.classList.add("loading");

        setTimeout(() => {
          tab.classList.remove("loading");
        }, 1000);
      });
    });
  });

  const graphicToggle = document.querySelector(".graphic-toggle");
  const uixToggle = document.querySelector(".uix-toggle");
  const graphicTab = document.querySelector(".graphic-tab");
  const uixTab = document.querySelector(".uix-tab");

  graphicToggle.addEventListener("click", function () {
    graphicTab.style.display = "block";
    uixTab.style.display = "none";
  });

  uixToggle.addEventListener("click", function () {
    graphicTab.style.display = "none";
    uixTab.style.display = "block";
  });
});

// courses-programming
document.addEventListener("DOMContentLoaded", function () {
  const headings = document.querySelectorAll(".switch-tabs .switcher h5");
  const switchTabs = document.querySelectorAll(".switch-tabs");

  headings.forEach(function (heading) {
    heading.addEventListener("click", function () {
      headings.forEach(function (h) {
        h.classList.remove("active");
      });
      this.classList.add("active");

      switchTabs.forEach(function (tab) {
        tab.classList.add("loading");

        setTimeout(() => {
          tab.classList.remove("loading");
        }, 1000);
      });
    });
  });

  const frontendToggle = document.querySelector(".frontend-toggle");
  const csharpToggle = document.querySelector(".csharp-toggle");
  const pythonToggle = document.querySelector(".python-toggle");
  const javaToggle = document.querySelector(".java-toggle");
  const mernstackToggle = document.querySelector(".mernstack-toggle");
  const flutterToggle = document.querySelector(".flutter-toggle");

  const frontendTab = document.querySelector(".frontend-tab");
  const csharpTab = document.querySelector(".csharp-tab");
  const pythonTab = document.querySelector(".python-tab");
  const javaTab = document.querySelector(".java-tab");
  const mernstackTab = document.querySelector(".mernstack-tab");
  const flutterTab = document.querySelector(".flutter-tab");

  frontendToggle.addEventListener("click", function () {
    frontendTab.style.display = "block";
    csharpTab.style.display = "none";
    pythonTab.style.display = "none";
    javaTab.style.display = "none";
    mernstackTab.style.display = "none";
    flutterTab.style.display = "none";
  });

  csharpToggle.addEventListener("click", function () {
    frontendTab.style.display = "none";
    csharpTab.style.display = "block";
    pythonTab.style.display = "none";
    javaTab.style.display = "none";
    mernstackTab.style.display = "none";
    flutterTab.style.display = "none";
  });

  pythonToggle.addEventListener("click", function () {
    frontendTab.style.display = "none";
    csharpTab.style.display = "none";
    pythonTab.style.display = "block";
    javaTab.style.display = "none";
    mernstackTab.style.display = "none";
    flutterTab.style.display = "none";
  });

  javaToggle.addEventListener("click", function () {
    frontendTab.style.display = "none";
    csharpTab.style.display = "none";
    pythonTab.style.display = "none";
    javaTab.style.display = "block";
    mernstackTab.style.display = "none";
    flutterTab.style.display = "none";
  });

  mernstackToggle.addEventListener("click", function () {
    frontendTab.style.display = "none";
    csharpTab.style.display = "none";
    pythonTab.style.display = "none";
    javaTab.style.display = "none";
    mernstackTab.style.display = "block";
    flutterTab.style.display = "none";
  });

  flutterToggle.addEventListener("click", function () {
    frontendTab.style.display = "none";
    csharpTab.style.display = "none";
    pythonTab.style.display = "none";
    javaTab.style.display = "none";
    mernstackTab.style.display = "none";
    flutterTab.style.display = "block";
  });
});
