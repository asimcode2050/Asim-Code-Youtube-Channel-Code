# In this video we will write Python code that demonstrates how to add 2D NumPy arrays with differing shapes
import numpy as np

# Define a 2D array A with shape (3, 2)
A = np.array([[1, 2],[3, 4],[5, 6]])

# Define a 2D array B with shape (1, 2)
B = np.array([[10, 20]])

# Adding A and B
# Since B has shape (1, 2), it will be broadcasted to match the shape of A (3, 2)
result = A + B

# Print the result
print("Result of adding A and B:")
print(result)


# Define another 2D array C with shape (3, 1)
C = np.array([[100],[200],[300]])

# Adding A and C
# C has shape (3, 1) and will be broadcasted to match A's shape (3, 2)
result2 = A + C

# Print the result
print("\nResult of adding A and C:")
print(result2)

