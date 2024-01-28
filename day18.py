# Create a program to find the largest among three numbers.

try:
    str = input(f'Enter a list of numbers, separate entries with a space: ')
    num_list = str.split(" ")
    num_list = [eval(num) for num in num_list]
    print(f'Largest number: {max(num_list)}')

except Exception:
  print(f'Invalid input')