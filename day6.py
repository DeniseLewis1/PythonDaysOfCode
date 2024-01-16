# Write a program to count the occurrences of a specific character in a string.

str = input(f'Enter a string: ')
char = input(f'Enter a character: ')

count = 0

for i in str:
  if i == char:
    count += 1

print(f'{char} occurs {count} times in {str}')