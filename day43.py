# Write a program that removes all whitespaces from a given string

import re

def remove_whitespace(str):
    return re.sub(r'\s+', '', str)

str = input("Enter a string: ")
print(remove_whitespace(str))