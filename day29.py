# Create a function that generates a random number between a given range.

import random

def random_number(start, end):
    return random.randint(start, end)

try:
    start = int(input(f'Enter start of range: '))
    end = int(input(f'Enter end of range: '))
    
    if end <= start:
        print(f'Invalid range')
    else:
        print(f'Random number: {random_number(start, end)}')

except Exception:
    print(f'Invalid input')