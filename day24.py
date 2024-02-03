# Write a program to remove vowels from a given string.

import re

str = input(f'Enter a string: ')
print(re.sub('[aeiouAEIOU]', '', str))