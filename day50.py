# Create a program that finds the intersection and union of two sets

set1 = input(f'Enter the first set, separate entries with a space: ')
set2 = input(f'Enter the second set, separate entries with a space: ')
set1 = set(set1.split(" "))
set2 = set(set2.split(" "))

print(f'Intersection: {set1.intersection(set2)}')
print(f'Union: {set1.union(set2)}')