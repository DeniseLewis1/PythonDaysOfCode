# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.
import re

def count_case(str):
  upper_count = len(re.findall('[A-Z]', str))
  lower_count = len(re.findall('[a-z]', str))

  print(f'{str} has {upper_count} uppercase letters and {lower_count} lowercase letters')

count_case(input("Enter a string: "))