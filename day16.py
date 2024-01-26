# Write a function that counts the frequency of each word in a sentence.
import re

def count_frequency(str):
    str = str.lower()
    str = re.sub(r'[^\w\s]', '', str)

    str_list = str.split(" ")
    str_dict = {}

    for word in str_list:
        if word not in str_dict:
            str_dict[word] = 1
        else:
            str_dict[word] += 1
    
    return str_dict

str_dict = count_frequency(input(f'Enter a sentence: '))

for key, value in str_dict.items():
    print(f'{key}: {value}')