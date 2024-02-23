# Write a program that reads an integer from the user and handles invalid inputs

try:
    num = int(input("Enter an integer: "))
    print(num)

except ValueError:
    print("Invalid input, please enter an integer")