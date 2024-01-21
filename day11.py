# Write a program to print the multiplication table of a given number.

try:
  num = int(input(f'Enter a number: '))
  print(f'Multiplication table of {num}:')
  
  for i in range(1, 13):
    print(f'{num} x {i} = {num * i}')
except ValueError:
  print(f'Invalid input')