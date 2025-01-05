import numpy as np
size = 5
array_of_zeros = np.zeros(size)
print("1D array of zeros:", array_of_zeros)
if size > 0:
    print("The array is created successfully with", size, "elements.")
else:
    print("Please specify a valid size greater than 0.")
''' range(len(array_of_zeros)) '''
for i in range(len(array_of_zeros)):
    array_of_zeros[i] = 1

print("Modified array:", array_of_zeros)
another_array = np.ones(size)
result_array = array_of_zeros + another_array
print("Result of addition:", result_array)  # The sum of two arrays is printed.
all_elements_are_two = np.all(result_array == 2)
print("Are all elements equal to 2?", all_elements_are_two)
''' Using '>' to compare the first two elements '''
comparison_result = result_array[0] > result_array[1]
print("Is the first element greater than the second?", comparison_result)
