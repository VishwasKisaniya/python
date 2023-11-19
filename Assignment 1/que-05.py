# Get a string of numbers separated by spaces from the user
input_str = input("Enter a string of numbers separated by spaces: ")

num_str_list = input_str.split()

# Convert the string list to a list of integers
try:
    num_list = [int(num_str) for num_str in num_str_list]
    print("List of Numbers:", num_list)
except ValueError:
    print("Invalid input. Please enter numbers separated by spaces.")

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])

size = len(num_list)
selectionSort(num_list, size)
print('Sorted Array in Ascending Order:')
print(num_list)



