import array
arr = array.array('i', [1, 2, 3, 4, 5])
print("Initial array:", arr)  # Expected output: array('i', [1, 2, 3, 4, 5])
print("Element at index 2:", arr[2])  # Expected output: 3
arr[1] = 10
print("Array after modification:", arr)
arr.append(7)
print("Array after appending 7:", arr)
arr.remove(3)
print("Array after removing 3:", arr)
popped_value = arr.pop()
print("Popped value:", popped_value)  # Expected output: 7
print("Array after popping an element:", arr)
array_length = len(arr)
print("Length of the array:", array_length)  # Expected output: 4
print("Elements in the array:")
for value in arr:
    print(value)
