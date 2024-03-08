# Create a function that converts a string to an integer and handles ValueError

def string_to_integer(str):
    try:
        return int(str)
        
    except ValueError:
        return "Invalid input, please enter an integer"

str = input("Enter an integer: ")
print(string_to_integer(str))