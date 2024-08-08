from itertools import product

def generate_email_permutations(first_name, last_name, domain):
    formats = [
        "{first}.{last}@{domain}",
        "{first}_{last}@{domain}",
        "{first}{last}@{domain}",
        "{f}.{last}@{domain}",
        "{f}_{last}@{domain}",
        "{last}.{first}@{domain}",
        "{last}_{first}@{domain}",
        "{last}{first}@{domain}",
        "{first}.{l}@{domain}",
        "{first}_{l}@{domain}",
        "{first}{l}@{domain}",
        "{f}{last}@{domain}",
        "{f}.{l}@{domain}",
        "{f}_{l}@{domain}",
        "{f}{l}@{domain}",
        "{l}.{first}@{domain}",
        "{l}_{first}@{domain}",
        "{l}{first}@{domain}",
        "{last}.{f}@{domain}",
        "{last}_{f}@{domain}",
        "{last}{f}@{domain}",
        "{l}.{f}@{domain}",
        "{l}_{f}@{domain}",
        "{l}{f}@{domain}",
        "{first}-{last}@{domain}",
        "{f}-{last}@{domain}",
        "{first}-{l}@{domain}",
        "{f}-{l}@{domain}",
        "{l}-{first}@{domain}",
        "{last}-{first}@{domain}",
        "{l}-{f}@{domain}",
        "{last}-{f}@{domain}",
        "{first}@{domain}",
        "{last}@{domain}"
    ]

    f = first_name[0].lower()
    l = last_name[0].lower()
    first = first_name.lower()
    last = last_name.lower()

    emails = [fmt.format(first=first, last=last, f=f, l=l, domain=domain) for fmt in formats]

    return emails

# Example usage
first_name = "Nikhil"  
last_name = "Talawar"
domain = "accenture.com"
email_permutations = generate_email_permutations(first_name, last_name, domain)

for email in email_permutations:
    print(email)
