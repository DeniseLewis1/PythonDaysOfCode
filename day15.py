# Create a program that checks if a year is a leap year.

try:
  year = int(input(f'Enter a year: '))

  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} is a leap year')
  else:
    print(f'{year} is not a leap year')

except ValueError:
  print(f'Invalid input')