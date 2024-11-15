import numpy as np  # Importing the NumPy library for numerical computations
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])  # A 3x3 matrix
print("Original Array:\n", arr)
element = arr[1, 2]
print("Element at row 1, column 2:", element)
row_slice = arr[1, :]  # Accessing the entire 2nd row (index 1), all columns
print("Row 1 Slice:", row_slice)
column_slice = arr[:, 2]  # Accessing the entire 3rd column (index 2), all rows
print("Column 2 Slice:", column_slice)
subarray = arr[0:2, 1:3]
print("Subarray:\n", subarray)
bool_index = arr > 5
print("Boolean Index Mask:\n", bool_index)
elements_greater_than_5 = arr[bool_index]
print("Elements greater than 5:", elements_greater_than_5)
rows = np.array([0, 2])  # Specify row indices 0 and 2
cols = np.array([1, 2])  # Specify column indices 1 and 2
fancy_indexed_elements = arr[rows, cols]  # Access elements at (0,1) and (2,2)
print("Fancy Indexed Elements:", fancy_indexed_elements)
arr[0, 0] = 99  # Update the element at row 0, column 0 to 99
print("Array after modification:\n", arr)
