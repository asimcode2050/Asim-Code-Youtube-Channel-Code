def constant_time_example():
    print("Constant Time: O(1)")  # This line always takes constant time
    return 42  # Returning a constant value takes constant time


def linear_time_example(arr):
    for item in arr:
        print(item)  # This operation is executed once for each element in the array
        return "Done"  # This line takes O(1) time, but it's outside the loop


def quadratic_time_example(arr):
    for i in range(len(arr)):  # Outer loop runs n times
        for j in range(len(arr)):  # Inner loop also runs n times
            print(f"Comparing {arr[i]} with {arr[j]}")
            return "Finished"


def logarithmic_time_example(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def n_log_n_example(arr):
    arr.sort()
    return arr


def exponential_time_example(n):
    if n <= 1:
        return 1
    else:
        return exponential_time_example(n - 1) + exponential_time_example(n - 1)


print(constant_time_example())  # O(1)
print(linear_time_example([1, 2, 3, 4, 5]))  # O(n), where n = 5
print(quadratic_time_example([1, 2, 3]))  # O(n^2), where n = 3
sorted_arr = [1, 3, 5, 7, 9, 11]
print(logarithmic_time_example(sorted_arr, 5))  # O(log n), where n = 6
arr = [9, 2, 5, 3, 7]
print(n_log_n_example(arr))  # O(n log n), where n = 5
print(exponential_time_example(4))  # O(2^n), where n = 4
