# Create a function that takes a string and returns the reverse of each word

def reverse_words(str):
    reversed_words = [word[::-1] for word in str.split(" ")]
    return " ".join(reversed_words)

str = input("Enter a string: ")
print(reverse_words(str))