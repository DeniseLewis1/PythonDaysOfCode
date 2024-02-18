# Write a program to find the most common words in a text file

import re

def common_words(text_file):
    text = re.sub(r'[^\w\s]', '', text_file.lower()).split(" ")
    words_dict = {}

    for word in text:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    
    words_dict = sorted(words_dict.items(), key=lambda x:x[1], reverse=True)

    return dict(words_dict[:5])

with open("text.txt", "r") as file:
    text_file = file.read()

words = common_words(text_file)

for key in words:
    print(key)