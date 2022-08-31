// Gets full year and display on the footer
$("#year").text(new Date().getFullYear());


// Back to the top button
$('.btt-link').click(function (e) {
    window.scrollTo(0, 0)
})


//Navbar background and color changes on scrooll
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
})

