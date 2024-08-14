# Job Opportunities Tapping Guide Using Email Permutations

This guide provides detailed steps to effectively reach out to potential employers and increase your chances of securing an internship by generating and validating email addresses using permutations.

## Steps to Follow

### 1. Identify Target Companies
- List out companies you're interested in.
- Visit each company's website to find their domain name (e.g., `data.com`).

### 2. Gather Employee Information from LinkedIn
- Search for the company on LinkedIn.
- Find employees working at the company.
- Note down the first and last names of these employees.

### 3. Prepare Your Excel Sheet
- Create a new Excel or Google Sheets document.
- Split the first names and last names into separate columns.
- List down the domain name in another column.

### 4. Generate Email Permutations
- Create a list of common email formats. For example:
  - `firstname.lastname@domain.com`
  - `firstname_lastname@domain.com`
  - `f.lastname@domain.com`
  - `firstnamelastname@domain.com`
  - `f_lastname@domain.com`
  - (Repeat for other common formats up to 35 permutations)
- Use Excel formulas to generate these permutations:
  - If `A2` is the first name, `B2` is the last name, and `C2` is the domain, an example formula for `firstname.lastname` could be `=A2 & "." & B2 & "@" & C2`.
  - Repeat for all other formats to get different permutations.

### 5. Validate Email Addresses Using Google Sheets
- Copy the generated email addresses.
- Paste them back into Google Sheets.
- Use the "People Chips" feature in Google Sheets:
  - Select the cells with email addresses.
  - Go to `Insert > People Chips`.
  - Valid email addresses will convert into chips.

### 6. Filter Valid Email Addresses
- Filter out the cells that didn't convert into chips, as those are likely invalid email addresses.

### 7. Prepare Your Email
- Draft a professional email template.
- Personalize it for the specific company and role you are applying for.
- Mention how you found their email and your interest in the company.
- Attach your resume and other relevant documents.

### 8. Send Emails
- Use an email client to send emails to the valid email addresses.
- Keep track of the responses in your Excel or Google Sheets document.

### 9. Follow-Up
- If you don't receive a response within a week or two, consider sending a polite follow-up email.

By following these steps, you can effectively reach out to potential employers and increase your chances of securing an internship.

## License
This project is licensed under the MIT License.
