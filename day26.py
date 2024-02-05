# Create a program that uses a lambda function to square each element of a list.

try:
  str = input(f'Enter a list of numbers, separate entries with a space: ')
  num_list = map(eval, str.split(" "))
  square_list = list(map(lambda num: num ** 2, num_list))

  print(square_list)

except Exception:
  print(f'Invalid input')