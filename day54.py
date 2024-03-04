# Create a function to find all words in a sentence that start with a vowel

def find_vowel_words(sentence):
    words = sentence.lower().split(" ")
    vowel_words = []
    for word in words:
        if word[0] in "aeiou":
            vowel_words.append(word)
    return vowel_words

sentence = input("Enter a sentence: ")
print(find_vowel_words(sentence))