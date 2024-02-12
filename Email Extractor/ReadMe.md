# Email Address Collector

## Introduction

This JavaScript script allows you to collect all email addresses present on a webpage directly from the console in Chrome developer tools.

## Instructions

1. Open the webpage from which you want to collect email addresses in Google Chrome.
2. Right-click on the page and select "Inspect" from the context menu, or press `Ctrl+Shift+I`.
3. Go to the "Console" tab in the Developer Tools window.
4. Copy the JavaScript code provided below and paste it into the console.
5. Press `Enter` to execute the script. The script will then collect and log all unique email addresses found on the webpage.

## JavaScript Code

```javascript
// JavaScript code to collect all email addresses present on a webpage
// Copy and paste this script into the console of Chrome developer tools

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


#Usage Notes
This script may not capture all email addresses on a webpage, especially if they are obfuscated or hidden behind JavaScript.
It's recommended to review the collected email addresses for accuracy and legitimacy before using them.