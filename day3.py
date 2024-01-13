# Write a function to count the number of vowels in a given string

def count_vowels(str):
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  count = 0
  
  for letter in str:
    if letter in vowels:
      count += 1
  
  print(f'{str} has {count} vowels')

count_vowels(input("Enter a string: "))