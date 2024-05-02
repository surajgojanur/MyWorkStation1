// Array to store all collected phone numbers
let allPhoneNumbers = [];

// Function to collect phone numbers from divs
function collectPhoneNumbers() {
    // Select all divs with the specified class name
    let divs = document.querySelectorAll('.Io6YTe.fontBodyMedium.kR99db');

    // Regular expression to match phone numbers in the desired format
    let phoneNumberRegex = /\+\d{2}\s\d{4}\s\d{5}/g;

    // Iterate over each selected div
    divs.forEach(div => {
        // Extract text content from each div
        let text = div.textContent.trim();

        // Extract phone numbers from the text using the regular expression
        let extractedPhoneNumbers = text.match(phoneNumberRegex);
        
        // Add extracted phone numbers to the array
        if (extractedPhoneNumbers) {
            allPhoneNumbers = allPhoneNumbers.concat(extractedPhoneNumbers);
        }
    });
}

// Function to click on each link recursively
function clickNextLink(links, index) {
    // Base case: If all links have been clicked
    if (index >= links.length) {
        // Output all collected phone numbers after all links have been clicked
        console.log(allPhoneNumbers);
        return;
    }

    // Click on the current lin
    links[index].click();

    // Wait for a short delay to ensure content loads after the click
    setTimeout(() => {
        // Collect phone numbers after the click
        collectPhoneNumbers();

        // Click on the next link recursively
        clickNextLink(links, index + 1);
    }, 2000); // Adjust the delay as needed based on the time it takes for the content to load after the click
}

// Select all links with the specified class name
let links = document.querySelectorAll('a.hfpxzc');

// Start clicking on each link recursively
clickNextLink(links, 0);
