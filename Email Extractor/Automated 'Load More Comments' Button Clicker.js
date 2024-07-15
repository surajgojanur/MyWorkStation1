// Replace '.comments-comments-list__load-more-comments-button' with the actual class name of your button
var buttonClass = '.comments-comments-list__load-more-comments-button';

// Replace 'numberOfClicks' with the number of times you want to click the button
var numberOfClicks = 5; // For example, to click the button 5 times

// Function to click the button with random delay
function clickButton() {
    var button = document.querySelector(buttonClass);
    if (button) {
        var randomDelay = Math.floor(Math.random() * 3000) + 1000; // Generate random delay between 1 to 4 seconds
        setTimeout(function() {
            button.click();
        }, randomDelay);
    } else {
        console.log("Button not found. Waiting to retry...");
        setTimeout(clickButton, 1000); // Retry after 1 second
    }
}

// Click the button multiple times with a 3-second delay after each click
function clickMultipleTimesWithDelay() {
    var counter = 0;
    var interval = setInterval(function() {
        clickButton();
        counter++;
        if (counter === numberOfClicks) {
            clearInterval(interval); // Stop the interval after clicking the button the specified number of times
        }
    }, 3000); // Delay of 3 seconds (3000 milliseconds)
}

// Start clicking the button multiple times with a delay
clickMultipleTimesWithDelay();
