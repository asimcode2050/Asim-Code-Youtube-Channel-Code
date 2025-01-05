import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
reshaped_array = arr.reshape(3, 4)
print("Reshaped Array (3x4):")
print(reshaped_array)
'''
 [[ 1  2  3  4]
  [ 5  6  7  8]
  [ 9 10 11 12]]
'''
reshaped_array_2 = arr.reshape(4, 3)
print("\nReshaped Array (4x3):")
print(reshaped_array_2)
'''
 [[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]
  [10 11 12]]
'''
try:
    reshaped_array_invalid = arr.reshape(5, 3)
except ValueError as e:
    print("\nError when reshaping to (5, 3):", e)

reshaped_array_auto = arr.reshape(3, -1)
print("\nReshaped Array (3, -1):")
print(reshaped_array_auto)
'''
  [[ 1  2  3  4]
   [ 5  6  7  8]
   [ 9 10 11 12]]
'''
reshaped_array_auto_2 = arr.reshape(4, -1)
print("\nReshaped Array (4, -1):")
print(reshaped_array_auto_2)
'''
 [[ 1  2  3]
  [ 4  5  6]
  [ 7  8  9]
  [10 11 12]]
'''
reshaped_array[0, 0] = 99
print("\nModified reshaped array:")
print(reshaped_array)
print("\nOriginal array after modifying the reshaped array:")
print(arr)

