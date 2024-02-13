# Write a Python program to merge two dictionaries

def merge_dict(dict_a, dict_b):
    dict_a.update(dict_b)
    return dict_a

fruits = {"banana": "yellow", "strawberry": "red", "grapes": "purple"}
vegetables = {"corn": "yellow", "tomato": "red", "spinach": "green"}

print(merge_dict(fruits, vegetables))