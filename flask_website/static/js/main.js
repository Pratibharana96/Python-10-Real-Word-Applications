function myFunction(e){e.classList.toggle("change")}jQuery(document).ready(function(){jQuery(".owl-carousel2").owlCarousel({loop:!0,center:!1,margin:20,responsiveClass:!0,nav:!0,responsive:{0:{items:2,nav:!1},600:{items:2,nav:!1},1e3:{items:4,nav:!0,loop:!0}}}),jQuery(".owl-carousel3").owlCarousel({loop:!0,center:!1,margin:20,responsiveClass:!0,nav:!0,responsive:{0:{items:1,nav:!1},600:{items:2,nav:!1},1e3:{items:3,nav:!0,loop:!0}}}),jQuery(".owl-carousel4").owlCarousel({loop:!0,center:!1,margin:20,responsiveClass:!0,nav:!0,responsive:{0:{items:1,nav:!1},600:{items:2,nav:!1},1e3:{items:2,nav:!0,loop:!0}}})});