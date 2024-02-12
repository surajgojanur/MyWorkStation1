// Find all text on the webpage
const allText = document.body.innerText;

// Regular expression to find email addresses
const emailRegex = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g;

// Extract email addresses using the regex
const emails = allText.match(emailRegex);

// Remove duplicate emails
const uniqueEmails = [...new Set(emails)];

// Print out the unique emails found
console.log(uniqueEmails);