# Write a program that uses recursion to generate all permutations of a list

def permutations(lst, end=[]):
    if len(lst) == 0:
        print(end)
    else:
        for i in range(len(lst)):
            permutations(lst[:i] + lst[i+1:], end + lst[i:i+1])

input_list = input(f'Enter a list, separate entries with a space: ')
permutations(input_list.split(" "))