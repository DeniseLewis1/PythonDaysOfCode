# Write a function to check if a number is a prime number

def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False
        return True
    return False

try:
    num = int(input("Enter an number: "))
    print(is_prime(num))

except:
    print(f'Invalid input')