# Write a program to shuffle the elements of a list randomly.

import random

str = input(f'Enter a list, separate entries with a comma (,): ')
input_list = str.split(",")
random.shuffle(input_list)
print(f'Shuffled list: {input_list}')