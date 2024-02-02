# Write a program that checks if a key exists in a dictionary.

def check_key(dict, key):
    if key in dict.keys():
        print(f'{key} exists')
    else:
        print(f'{key} does not exist')

fruits = {"banana": "yellow", "strawberry": "red", "grapes": "purple"}

check_key(fruits, "strawberry")
check_key(fruits, "pineapple")