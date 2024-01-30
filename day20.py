# Write a function that takes a list of numbers and returns a new list containing only the even numbers.

def even(num_list):
  even_numbers = []
  
  for num in num_list:
    if num % 2 == 0:
      even_numbers.append(num)

  return even_numbers

try:
  str = input(f'Enter a list of numbers, separate entries with a space: ')
  num_list = str.split(" ")
  num_list = [eval(num) for num in num_list]
  print(f'Even numbers: {even(num_list)}')

except Exception:
  print(f'Invalid input')