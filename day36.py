# Write a Python program to check if two strings are anagrams

def is_anagram(str1, str2):
    if sorted(str1.lower()) == sorted(str2.lower()):
        print(f'{str1} and {str2} are anagrams')
    else:
        print(f'{str1} and {str2} are not anagrams')

str1 = input(f'Enter the first string: ')
str2 = input(f'Enter the second string: ')
is_anagram(str1, str2)