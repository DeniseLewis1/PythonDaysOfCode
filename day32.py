# Create a function that calculates the average of a list of numbers

def get_average(num_list): 
    num_list = [float(num) for num in num_list]
    return sum(num_list) / len(num_list)

try:
    str = input(f'Enter a list of numbers, separate entries with a space: ')
    print(f'Average: {get_average(str.split(" "))}')

except Exception:
   print(f'Invalid input')