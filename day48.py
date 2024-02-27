# Create a program that replaces specific words in a text with their synonyms

import nltk
from nltk.corpus import wordnet
import random

def replace_synonym(text, word):
   synonyms = []
   
   for syn in wordnet.synsets(word):
      for l in syn.lemmas():
            synonyms.append(l.name())
   
   new_text = text.replace(word, random.choice(list(set(synonyms))))
   return new_text

text = input("Enter text: ")
word = input("Enter word to replace: ")
print(replace_synonym(text, word))