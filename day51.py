# Create a program that counts the occurrences of each word in a text file

import re

def count_words(text_file):
    text = re.sub(r'[^\w\s]', '', text_file.lower()).split(" ")
    words_dict = {}

    for word in text:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    
    return words_dict

with open("text.txt", "r") as file:
    text_file = file.read()

words = count_words(text_file)

for key, value in words.items():
    print(f'{key}: {value}')