# Create a program to remove a specific element from a set.

str = input(f'Enter a list, separate entries with a space: ')
element = input(f'Enter the element to remove: ')

input_set = set(str.split(" "))
input_set.discard(element)
print(f'{input_set}')