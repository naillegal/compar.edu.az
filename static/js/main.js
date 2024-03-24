// responsive-openmenu
$(document).ready(function () {
  $(".inside-ul").hide();
  $(".responsive-openmenu").hide();

  function hideResponsiveMenu() {
    $(".fa-bars")
      .removeClass("fa-x")
      .addClass("fa-bars")
      .css("transform", "rotate(0deg)");
    $("body").removeClass("overflow-hidden");
    $(".fa-x").removeClass("fa-x").addClass("fa-bars");
    $(".responsive-openmenu").hide();
  }

  if ($(window).width() >= 992) {
    hideResponsiveMenu();
  }

  $(".isopenmenu").click(function () {
    var $chevronIcon = $(this).find(".fa-chevron-down");
    $(this).siblings(".inside-ul").slideToggle();
    $(this)
      .siblings(".isopenmenu")
      .find(".fa-chevron-down")
      .removeClass("rotate")
      .css("transform", "rotate(0deg)");
    $chevronIcon.toggleClass("rotate");

    if ($chevronIcon.hasClass("rotate")) {
      $chevronIcon.css("transform", "rotate(180deg)");
    } else {
      $chevronIcon.css("transform", "rotate(0deg)");
    }
  });

  $(".fa-bars").click(function () {
    $(this).toggleClass("fa-bars fa-x");

    if ($(this).hasClass("fa-x")) {
      $(this).css("transform", "rotate(180deg)");
      $("body").addClass("overflow-hidden");
      $(".responsive-openmenu")
        .css("overflow", "auto")
        .show()
        .animate({ left: "0" }, 400);
    } else {
      $(".responsive-openmenu").animate({ left: "-100%" }, 400, function () {
        $(this).hide();
        $(this).css("left", "-100%");
      });
      $("body").removeClass("overflow-hidden");
      $(this)
        .removeClass("fa-x")
        .addClass("fa-bars")
        .css("transform", "rotate(0deg)");
    }
  });

  $(window).on("resize", function () {
    if ($(window).width() >= 992) {
      hideResponsiveMenu();
    }
  });
});

// home-education-slider
$(document).ready(function () {
  var swiper2 = new Swiper("#education .mySwiper2", {
    slidesPerView: 1,
    loop: true,
    breakpoints: {
      768: {
        slidesPerView: 2,
      },
      1200: {
        slidesPerView: 4,
      },
    },
  });

  $("#education .button-prev").click(function () {
    swiper2.slidePrev();
  });

  $("#education .button-next").click(function () {
    swiper2.slideNext();
  });
});

// slider-student-review
$(document).ready(function () {
  var swiper1 = new Swiper("#slider-student-review .mySwiper1", {
    slidesPerView: 1,
    effect: "coverflow",
    coverflowEffect: {
      rotate: 0,
      stretch: 0,
      depth: 80,
      modifier: 2,
      slideShadows: false,
    },
    loop: true,
    scrollbar: {
      el: ".swiper-scrollbar",
      hide: false,
    },
    breakpoints: {
      992: {
        slidesPerView: 3,
      },
    },
  });

  $("#slider-student-review .button-prev").click(function () {
    swiper1.slidePrev();
  });

  $("#slider-student-review .button-next").click(function () {
    swiper1.slideNext();
  });
});

// portfolio
document.addEventListener("DOMContentLoaded", function () {
  const boxes = document.querySelectorAll(".portfolio-box");
  const parent = boxes[0].parentNode;
  let firstBox = boxes[0];
  firstBox.classList.add("active");

  boxes.forEach((box) => {
    box.addEventListener("mouseover", function () {
      boxes.forEach((b) => b.classList.remove("active"));
      this.classList.add("active");
    });
  });

  parent.addEventListener("mouseout", function (event) {
    if (!parent.contains(event.relatedTarget)) {
      boxes.forEach((b) => b.classList.remove("active"));
      firstBox.classList.add("active");
    }
  });
});

// portfolio-slider
var swiper3 = new Swiper(".mySwiper3", {
  loop: true,
  scrollbar: {
    el: ".swiper-scrollbar",
    hide: false,
  },
});

// home-main-slider
let items = document.querySelectorAll(".slider .list .item");
let next = document.getElementById("next");
let prev = document.getElementById("prev");
let thumbnails = document.querySelectorAll(".thumbnail .item");

let countItem = items.length;
let itemActive = 0;
next.onclick = function () {
  itemActive = itemActive + 1;
  if (itemActive >= countItem) {
    itemActive = 0;
  }
  showSlider();
};
prev.onclick = function () {
  itemActive = itemActive - 1;
  if (itemActive < 0) {
    itemActive = countItem - 1;
  }
  showSlider();
};
let refreshInterval = setInterval(() => {
  next.click();
}, 5000);
function showSlider() {
  let itemActiveOld = document.querySelector(".slider .list .item.active");
  let thumbnailActiveOld = document.querySelector(".thumbnail .item.active");
  itemActiveOld.classList.remove("active");
  thumbnailActiveOld.classList.remove("active");

  items[itemActive].classList.add("active");
  thumbnails[itemActive].classList.add("active");

  clearInterval(refreshInterval);
  refreshInterval = setInterval(() => {
    next.click();
  }, 5000);
}

thumbnails.forEach((thumbnail, index) => {
  thumbnail.addEventListener("click", () => {
    itemActive = index;
    showSlider();
  });
});

// copyright year
var date = new Date();
var year = date.getFullYear();
var copyrightcontent = "© " + year + " Compar Academy. Bütün hüquqlar qorunur";
document.getElementById("copyright").innerHTML = copyrightcontent;
