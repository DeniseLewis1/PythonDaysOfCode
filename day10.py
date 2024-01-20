# Write a program to remove duplicates from a list.

str = input(f'Enter a list, separate entries with a comma (,): ')
input_list = str.split(",")
output_list = []

for item in input_list:
    if item not in output_list:
        output_list.append(item)

print(f'{output_list}')