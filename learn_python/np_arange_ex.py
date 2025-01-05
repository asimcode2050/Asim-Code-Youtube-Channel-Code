import numpy as np
start = 0
stop = 10
step = 2
arr = np.arange(start, stop, step)
print("Generated array:", arr)
if arr.size == 0:
    print("The array is empty!")
else:
    print("The array is not empty, and contains elements.")
for num in arr:
    print(f"Element: {num}")

added = arr + 5
print("Array after adding 5:", added)  # Display the result of addition
subtracted = arr - 1
print("Array after subtracting 1:", subtracted)

multiplied = arr * 2
print("Array after multiplying by 2:", multiplied)
divided = arr / 2
print("Array after dividing by 2:", divided)
greater_than_4 = arr > 4
print("Elements greater than 4:", greater_than_4)
logical_and = (arr > 2) & (arr < 8)
print("Array elements between 2 and 8:", logical_and)
logical_or = (arr < 2) | (arr > 6)
print("Array elements less than 2 or greater than 6:", logical_or)
def create_range(start, stop, step):
    return np.arange(start, stop, step)  # The function returns a NumPy array

result_array = create_range(5, 20, 3)
print("Custom generated array using function:", result_array)
