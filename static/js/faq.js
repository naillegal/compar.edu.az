// questions open
$(document).ready(function () {
  $(".faq-open").click(function () {
    $(this).next("p").slideToggle();

    var $chevronIcon = $(this).find(".fa-chevron-down");
    $chevronIcon.toggleClass("rotate");

    if ($chevronIcon.hasClass("rotate")) {
      $chevronIcon.css("transform", "rotate(180deg)");
    } else {
      $chevronIcon.css("transform", "rotate(0deg)");
    }
  });
});
