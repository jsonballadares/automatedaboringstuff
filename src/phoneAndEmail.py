#! python3

import re
import pyperclip

# Create a regex for phone numbers
phone_regex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))? # area code (optional)
(\s|-)                     # first separator
\d\d\d                     # first 3 digits
-                          # separator
\d\d\d\d                   # last 4 digits
(((ext(\.)?\s)|x)           # extension word part (optional)
(\d{2,5}))?                 # extension number part (p[tional])
)
''', re.VERBOSE)

# TODO: Create a regex for email addresses
email_regex = re.compile(r'''
# (some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+    # name part
@                  # @ symbol
[a-zA-Z0-9_.+]+    # domain name part

''', re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from this text
extracted_phone_numbers = phone_regex.findall(text)
extracted_emails = email_regex.findall(text)

phone_numbers = []
for phone_number in extracted_phone_numbers:
    phone_numbers.append(phone_number[0])

# TODO: Copy the extracted email/phone to the clipboard
numbers = '\n'.join(phone_numbers)
emails = '\n'.join(extracted_emails)
print(numbers)
print(emails)
