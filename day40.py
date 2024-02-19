# Write a function to find the largest common divisor of two numbers using a function

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

try:
    a = int(input(f'Enter first number: '))
    b = int(input(f'Enter second number: '))
    print(f'Largest common divisor: {find_gcd(a, b)}')

except Exception:
   print(f'Invalid input')