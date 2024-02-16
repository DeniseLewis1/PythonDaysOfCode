# Write a program to iterate through a dictionary and print its keys and values

def print_dict(dict):
    for key, value in dict.items():
        print(f'{key}: {value}')

fruits = {"strawberry": "red", "mango": "orange", "banana": "yellow", "kiwi": "green", "blueberry": "blue", "grape": "purple"}
print_dict(fruits)