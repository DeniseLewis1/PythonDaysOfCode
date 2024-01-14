# Write a program to find the sum of all elements in a list.

str = input(f'Enter a list of numbers separated by a comma (,): ')
num_list = str.split(",")

sum = 0

for num in num_list:
  sum += float(num)

print(f'Sum: {sum}')