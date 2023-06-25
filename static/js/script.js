// Alert messages fade out animation
$(document).ready(function() {
    setTimeout(function() {
      $('.alert').fadeOut('slow');
    }, 3000);
  });

// Scroll animaton to about section
$(document).ready(function() {
  // Smooth scroll to the About section on clicking the "About" link
  $(".about-link").click(function(event) {
    event.preventDefault(); // Prevent the default link behavior

    var aboutSection = $("#about-container");
    var targetUrl = $(this).data("target-url"); // Retrieve the target URL from data attribute

    // Check if the current page is the home page
    if (window.location.pathname === targetUrl) {
      // Scroll to the About section
      $('html, body').animate({
        scrollTop: aboutSection.offset().top - 100
      }, 800);
    } else {
      // Redirect to the target URL and append the hash fragment
      window.location.href = targetUrl + "#about-container";
    }
  });
});