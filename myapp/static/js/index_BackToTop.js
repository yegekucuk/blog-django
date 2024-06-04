// Function to return the page to the beginning
function scrollToTop() {
    window.scrollTo({
        top: 0,  // Scroll to the top of the page
        behavior: "smooth"  // Smooth scroll animation
    });
}

// Show or hide the back button based on page position
window.onscroll = function() {
    scrollFunction();  // Call scrollFunction when the user scrolls
};

function scrollFunction() {
    // Check if the scroll position is greater than a certain number of pixels (e.g., 20 pixels)
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("backToTopButton").style.display = "block";  // Show the button
    } else {
        document.getElementById("backToTopButton").style.display = "none";  // Hide the button
    }
}
