// Gets full year and display on the footer
$("#year").text(new Date().getFullYear());

 // Smooth scroll on click
 $("a").on('click', function (e) {
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      e.preventDefault();
      // Store hash
      var hash = this.hash;
      // Using jQuery's animate() method to add smooth page scroll
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 1000);
    }
    // End if
  });

// Navbar position changes on scrooll
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(document).scrollTop() > 25) {
            $(".btt-button").addClass("back-top-active");
            $(".topnav").addClass("topnav-active");
        } else {
            $(".btt-button").removeClass("back-top-active");
            $(".topnav").removeClass("topnav-active");
        }
    });
});

// OWL Carousel
$('.owl-carousel').owlCarousel({
    loop: true,

    nav: true,
    autoplay: true,
    autoPlaySpeed: 5000,
    autoPlayTimeout: 5000,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 3
        }
    }
});

