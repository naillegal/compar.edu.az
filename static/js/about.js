// about-counter
function animateCounters() {
  let valueDisplays = document.querySelectorAll(".count");
  let interval = 1500;

  valueDisplays.forEach((valueDisplay) => {
    let startValue = 0;
    let endValue = parseInt(valueDisplay.getAttribute("data-val"));
    let duration = Math.floor(interval / endValue);
    let counter = setInterval(function () {
      startValue += 1;
      valueDisplay.textContent = startValue;
      if (startValue == endValue) {
        clearInterval(counter);
      }
    }, duration);
  });
}

function isCountersInViewport() {
  let valueDisplays = document.querySelectorAll(".count");
  for (let valueDisplay of valueDisplays) {
    let rect = valueDisplay.getBoundingClientRect();
    if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
      return true;
    }
  }
  return false;
}

window.addEventListener("load", function () {
  if (isCountersInViewport()) {
    animateCounters();
  }
});

let animationStarted = false;

window.addEventListener("scroll", function () {
  let currentScrollPos =
    window.pageYOffset || document.documentElement.scrollTop;
  if (
    !animationStarted &&
    isCountersInViewport() &&
    currentScrollPos > lastScrollTop
  ) {
    animateCounters();
    animationStarted = true;
  }
  lastScrollTop = currentScrollPos <= 0 ? 0 : currentScrollPos;
});

window.addEventListener("DOMContentLoaded", function (event) {
  animateCounters();
});

// about-teachers-slider
var swiper = new Swiper("#our-teachers .swiper-container", {
  slidesPerView: 5,
  loop: true,
  spaceBetween: 30,
  scrollbar: {
    el: ".swiper-scrollbar",
    hide: false,
  },
  breakpoints: {
    1100: {
      slidesPerView: 5,
    },
    576: {
      slidesPerView: 3,
    },
    0: {
      slidesPerView: 2,
    },
  },
});
