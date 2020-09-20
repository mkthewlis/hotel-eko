// Shows toast alerts following user actions
$('.toast').toast('show');

// Adds spinner overlay when page loads
function customSpinner() {
    $('.spinner-overlay').fadeOut(2000);
}

$(document).ready(function(){
    // Adds border bottom navbar on scroll down past 30px, inspired by source code found on here: https://stackoverflow.com/questions/23706003/changing-nav-bar-color-after-scrolling
    $(function () {
        $(document).scroll(function () {
        var $nav = $(".sticky-top");
        $nav.toggleClass('scrolled', $(this).scrollTop() > 50);
        });
    });

    // Smooth scroll to top function courtesy of: https://codepen.io/deveb22/pen/QxPmGz
    var scrollBtn = $('#scroll-top-button');

    $(window).scroll(function() {
        if ($(window).scrollTop() > 120) {
            scrollBtn.addClass('show');
        } else {
            scrollBtn.removeClass('show');
        }
    });

    scrollBtn.on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({scrollTop:0}, '80');
    });
        // To allow AOS scroll effects
        AOS.init();
});