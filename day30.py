# Create a function that finds the second smallest element in a list.

def second_smallest(num_list):
   num_list = [eval(num) for num in num_list]
   num_list.sort()
   return num_list[1]

try:
   str = input(f'Enter a list of numbers, separate entries with a space: ')
   print(f'Second smallest element: {second_smallest(str.split(" "))}')

except Exception:
   print(f'Invalid input')