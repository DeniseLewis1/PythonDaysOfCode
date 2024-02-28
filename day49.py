# Create a program that implements the bubble sort algorithm

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst

try:
    input_list = input(f'Enter a list of numbers, separate entries with a space: ')
    num_list = [eval(num) for num in input_list.split(" ")]
    print(bubble_sort(num_list))

except:
    print(f'Invalid input')