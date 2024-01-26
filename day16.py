# Write a function that counts the frequency of each word in a sentence.
import re

str = input(f'Enter a sentence: ')
str = str.lower()
str = re.sub(r'[^\w\s]', '', str)

str_list = str.split(" ")
str_dict = {}

for word in str_list:
    if word not in str_dict:
        str_dict[word] = 1
    else:
        str_dict[word] += 1

for key, value in str_dict.items():
    print(f'{key}: {value}')