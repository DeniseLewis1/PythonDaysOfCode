# Write a function to calculate the factorial of a number.

def factorial(num):
  if num == 0 or num == 1:
    return 1
  else:
    return num * factorial(num - 1)

try:
  num = int(input(f'Enter a number: '))
  print(f'Factorial of {num} is {factorial(num)}')

except Exception:
  print(f'Invalid input')