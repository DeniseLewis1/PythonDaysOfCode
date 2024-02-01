# Create a program to find the second-largest element in a list.

try:
  str = input(f'Enter a list of numbers, separate entries with a space: ')
  num_list = str.split(" ")
  num_list = [eval(num) for num in num_list]
  num_list.sort()
  print(f'Second largest element: {num_list[-2]}')

except Exception:
  print(f'Invalid input')