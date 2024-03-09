# Create a function that checks if a number is a perfect square

import math

def is_perfect_square(num):
    return math.sqrt(num).is_integer()

try:
    num = int(input("Enter a number: "))
    print(f"Perfect square: {is_perfect_square(num)}")

except:
    print("Invalid input")