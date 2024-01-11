# Create a program that swaps the values of two variables.

var1 = input("Enter first value: ")
var2 = input("Enter second value: ")

print(f'Before: var1 = {var1}, var2 = {var2}')

temp = var1
var1 = var2
var2 = temp

print(f'After: var1 = {var1}, var2 = {var2}')