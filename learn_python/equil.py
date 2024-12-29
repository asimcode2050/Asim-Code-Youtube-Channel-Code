'''
 [ -7, 1, 5, 2, 3, 0, 1, 2 ]
'''
''' (O(n^2) '''
def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]

        if left_sum == right_sum:
            print(f"Equilibrium index found at: {i}")
            return i

        left_sum += arr[i]

    print("No equilibrium index found.")
    return -1  # Return -1 if no equilibrium index is found.


arr = [-7, 1, 5, 2, 3, 0, 1, 2]
find_equilibrium_index(arr)

arr2 = [1, 2, 3, 4, 5, 6]
find_equilibrium_index(arr2)
''' because left sum = right sum at index 3 '''
arr3 = [1, 2, 3, 4, 6]
find_equilibrium_index(arr3)
