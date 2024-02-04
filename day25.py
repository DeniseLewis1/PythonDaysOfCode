# Create a program to concatenate two lists.

list_one = input(f'Enter the first list, separate entries with a comma: ')
list_two = input(f'Enter the second list, separate entries with a comma: ')
concatenated_list = list_one.split(",") + list_two.split(",")
print(f'Concatenated list: {concatenated_list}')