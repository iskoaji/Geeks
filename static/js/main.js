(function ($) {
    "use strict";

    jQuery(document).ready(function ($) {

        /*--------------------------
            SCROLLSPY ACTIVE
        ---------------------------*/
        $('body').scrollspy({
            target: '.bs-example-js-navbar-scrollspy',
            offset: 25
        });


        /*---------------------------
                TOOLTIP
        -----------------------------*/
        $('[data-toggle="tooltip"]').tooltip();


        /*----------------------------
        FIXED NAV AND SCROLL TO TOP
        ------------------------------*/
        $(window).scroll(function () {
            var totalHeight = $(window).scrollTop();
            if (totalHeight > 200) {
                $('.mainmenu-area').addClass('fixed');
            } else {
                $('.mainmenu-area').removeClass('fixed');
            }
            if (totalHeight > 300) {
                $(".scrolltotop").fadeIn();
            } else {
                $(".scrolltotop").fadeOut();
            }
        });


        /*---------------------------
            SMOOTH SCROLL
        -----------------------------*/
        $(function () {
            $('ul#nav li a[href^="#"],a.navbar-brand,a.scrolltotop').on('click',function (event) {
                var id = $(this).attr("href");
                var offset = 20;
                var target = $(id).offset().top - offset;
                $('html, body').animate({
                    scrollTop: target
                }, 1000, "easeOutExpo");
                event.preventDefault();
            });
        });


        /*-------------------------
            VENOBOX LIGHTBOX
        ---------------------------*/
        $('.venobox').venobox();


        /*--------------------------
            TESTMONIAL SLIDER
        ---------------------------*/
        $('.testmonial-list').owlCarousel({
            loop: true,
            margin: 10,
            animateIn: 'zoomIn',
            animateOut: 'fadeOutDown',
            nav: true,
            navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 1
                },
                1000: {
                    items: 1
                }
            }
        });


        /*---------------------------
            CLIENT SLIDER
        -----------------------------*/
        $('.client-list').owlCarousel({
            loop: true,
            margin: 10,
            responsiveClass: true,
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 4
                },
                1000: {
                    items: 6
                }
            }
        });

    });


    jQuery(window).load(function () {
        /*--------------------------
            PRE LOADER
        ----------------------------*/
        $(".preloader-text").addClass('pre-animate');
        // will first fade out the loading animation
        $(".status").delay(3000).fadeOut();
        // will fade out the whole DIV that covers the website.
        $(".preloader").delay(3500).fadeOut("slow");

    });

}(jQuery));