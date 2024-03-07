# Create a function that returns the key with the maximum value in a dictionary

def find_max_key(dict):
    return max(dict, key=lambda x:dict[x])

dict = {'a': 10, 'b': 2, 'c': 15, 'd': 4, 'e': 5}
print(f'Dictionary: {dict} \nKey of maximum value: {find_max_key(dict)}')