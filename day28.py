# Create a program that removes the nth element from a list.

try:
    str = input(f'Enter a list, separate entries with a comma: ')
    n = int(input(f'Enter the position of the element to remove: '))
    str_list = str.split(",")
    str_list.pop(n-1)
    print(str_list)

except Exception:
    print(f'Invalid input')