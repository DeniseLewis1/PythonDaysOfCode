# Write a program that uses a try-except block to handle division by zero

try:
    dividend = float(input("Enter a dividend: "))
    divisor = float(input("Enter a divisor: "))
    print(dividend / divisor)

except ZeroDivisionError:
    print("Cannot divide by zero")

except:
    print("Invalid input")