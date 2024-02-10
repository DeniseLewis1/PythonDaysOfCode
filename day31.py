# Create a program that checks if a given string is a valid email address.

import re

email = input(f'Enter an email address: ')

if re.match(r'[^@]+@[^@]+\.[^@]+', email):
    print(f'{email} is a valid email address')
else:
    print(f'{email} is not a valid email address')