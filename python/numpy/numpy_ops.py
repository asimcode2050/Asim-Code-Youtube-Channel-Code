import numpy as np
a = np.array([1, 2, 3, 4, 5])
print("1D array (a):", a)
b = np.array([[1, 2], [3, 4], [5, 6]])
print("\n2D array (b):\n", b)
print("\nDimensions of a:", a.ndim)
print("Shape of a:", a.shape)
print("\nDimensions of b:", b.ndim)
print("Shape of b:", b.shape)
a_reshaped = a.reshape(1, 5)
print("\nReshaped a to 1x5 array:\n", a_reshaped)
a_plus_10 = a + 10
print("\nArray a after adding 10:", a_plus_10)
a_times_2 = a * 2
print("Array a after multiplying by 2:", a_times_2)
sqrt_a = np.sqrt(a)
print("\nSquare root of each element of a:", sqrt_a)
print("\nSlicing array a:", a[1:4])
c = np.array([6, 7, 8, 9, 10])
vertical_stack = np.vstack((a, c))
print("\nVertical stack of a and c:\n", vertical_stack)
horizontal_stack = np.hstack((a, c))
print("\nHorizontal stack of a and c:", horizontal_stack)
matrix_dot = np.dot(b, a[:2])
print("\nDot product of b and first two elements of a:", matrix_dot)
array_a = np.array([[1], [2], [3]])
array_b = np.array([10, 20, 30])
broadcast_result = array_a + array_b
print("\nResult of broadcasting array_a + array_b:\n", broadcast_result)
print("\nSum of all elements in array a:",
      np.sum(a))  # Sum of elements in array a
print("Mean of elements in array a:", np.mean(a))
print("Maximum element in array a:", np.max(a))  # Maximum element in array a
condition = a > 3
print("\nCondition (a > 3):", condition)
filtered_a = a[condition]
print("Elements of a greater than 3:", filtered_a)
random_integers = np.random.randint(1, 10, size=5)
print("\nRandom integers between 1 and 10:", random_integers)
transpose_b = b.T  # Transposing the matrix b (swap rows and columns)
print("\nTranspose of matrix b:\n", transpose_b)
