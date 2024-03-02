# Create a program that checks if a string is a palindrome

def is_palindrome(str):
    str = str.lower()
    return str == str[::-1]

str = input(f'Enter a string: ')
print(f'Palindrome: {is_palindrome(str)}')