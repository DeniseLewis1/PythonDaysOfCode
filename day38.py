# Write a program to flatten a nested list

def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        flat_list += element
    return flat_list

nested_list = [[9, 3, 8, 3], [4, 5, 2, 8], [6, 4, 3, 1], [1, 0, 4, 5]]
print(flatten_list(nested_list))