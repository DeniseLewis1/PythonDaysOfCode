# Create a program that sorts a list of strings alphabetically.

str = input(f'Enter a list, separate entries with a comma: ')
print(sorted(str.split(","), key=lambda x: x.lower()))