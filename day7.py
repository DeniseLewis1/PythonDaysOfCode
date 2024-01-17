# Write a program to check if a number is positive, negative, or zero.

num = input(f'Enter a number: ')

try:
  if float(num) > 0:
    print(f'{num} is a positive number')
  elif float(num) < 0:
    print(f'{num} is a negative number')
  elif float(num) == 0:
    print(f'{num} is zero')
except ValueError:
  print(f'Invalid input')