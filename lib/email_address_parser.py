import re

class EmailAddressParser:
    def __init__(self, string):
        self.string = string

    def parse(self):
        # Regex to match email addresses
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        # Find all matches
        emails = re.findall(email_regex, self.string)
        # Remove duplicates and sort
        unique_emails = sorted(set(emails))
        return unique_emails
