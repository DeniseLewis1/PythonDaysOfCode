# Write a function to check if a given list is sorted

def is_sorted(lst):
    if lst == sorted(lst):
        return True
    else:
        return False

input_list = input(f'Enter a list, separate entries with a space: ')
print(f'Sorted: {is_sorted(input_list.split(" "))}')