To create a README file for your GitHub repository explaining the JavaScript code to collect email addresses from a webpage using Chrome developer tools, you can follow these steps:

1. **Create a new file**: Open a text editor or an integrated development environment (IDE) and create a new file named `README.md`. The `.md` extension stands for Markdown, which is a lightweight markup language widely used for formatting text.

2. **Write the title**: Start by giving your README file a title, usually at the top and prefixed with a `#`. For example:

   ```markdown
   # JavaScript Code to Collect Email Addresses from a Webpage
   ```

3. **Introduction**: Briefly introduce the purpose of the script and how it can be used. Mention that the script is intended to be run in the Chrome developer tools console.

   ```markdown
   ## Introduction

   This JavaScript script allows you to collect all email addresses present on a webpage directly from the console in Chrome developer tools. By executing the script in the browser's console, you can quickly gather email addresses for various purposes.
   ```

4. **Instructions**: Provide clear instructions on how to use the script. Include steps for opening the developer tools console and running the script.

   ```markdown
   ## Instructions

   1. Open the webpage from which you want to collect email addresses in Google Chrome.
   2. Right-click on the page and select "Inspect" from the context menu, or press `Ctrl+Shift+I`.
   3. Navigate to the "Console" tab in the Developer Tools window.
   4. Copy the JavaScript code provided below and paste it into the console.
   5. Press `Enter` to execute the script. The script will then collect and log all unique email addresses found on the webpage.
   ```

5. **JavaScript Code**: Include the JavaScript code in a code block format within your README file. This allows users to easily copy the code.

   ```markdown
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
   ```

6. **Usage Notes**: Optionally, you can include any additional information or usage notes for the script.

   ```markdown
   ## Usage Notes

   - This script may not capture all email addresses on a webpage, especially if they are obfuscated or hidden behind JavaScript.
   - It's recommended to review the collected email addresses for accuracy and legitimacy before using them.
   ```

7. **License**: If applicable, include a section for licensing information or any other relevant legal notices.

8. **Contributing**: Optionally, include instructions for contributing to the project or guidelines for submitting issues and pull requests.

9. **Save and Upload**: Save the README.md file in your project directory. You can then upload it to your GitHub repository along with your JavaScript file.

Once you've created the README file, commit it to your GitHub repository along with your JavaScript code file. This README will help users understand how to use your script effectively.