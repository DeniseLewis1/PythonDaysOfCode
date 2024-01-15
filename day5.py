# Write a program to find the maximum and minimum values in a list.

str = input(f'Enter a list of numbers separated by a comma (,): ')
num_list = str.split(",")

max = float(num_list[0])
min = float(num_list[0])

for num in num_list:
  if float(num) > max:
    max = float(num)
  if float(num) < min:
    min = float(num)

print(f'Max: {max}')
print(f'Min: {min}')