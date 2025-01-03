#include <stdio.h>
int sequentialSearch(int arr[], int size, int target)
{
  for (int i = 0; i < size; i++)
  {
    if (arr[i] == target)
    {
        return i; // Returning the index where the target is found
    }
  }

  return -1; // Target not found
}

/*
 * Main function where the execution of the program starts.
 * We define the array, the target, and the size of the array here.
 */
int main()
{
    int numbers[] = {15, 23, 7, 9, 42, 5, 88, 13}; // Example array of integers
    int target = 42;
    int size = sizeof(numbers) / sizeof(numbers[0]);
/*
The size of the array is calculated using `sizeof(numbers) / sizeof(numbers[0])`.
*/
    int result = sequentialSearch(numbers, size, target);
  if (result == -1)
  {
      printf("Element %d not found in the array.\n", target);
  }
  else
  {
      printf("Element %d found at index %d.\n", target, result);
  }

  return 0;
}

/*
 * Explanation:
 *
 * 1. **Array**:
 *    - An array is a collection of elements, all of the same type, stored in contiguous memory locations.
 *    - In our code, the array `numbers[]` holds integers.
 *
 * 2. **Looping**:
 *    - A `for` loop is used to iterate over each element of the array.
 *    - The loop runs from `i = 0` to `i < size`, where `i` is the index of each element in the array.
 *
 * 3. **Indexing**:
 *    - Arrays in C are zero-indexed, which means the first element has an index of 0, the second has 1, and so on.
 *    - This is critical because it helps us locate each element based on its position in the array.
 *
 * 4. **Return Value**:
 *    - The function `sequentialSearch` returns the index where the target is found, or -1 if it's not found.
 *    - The `-1` return value is often used to indicate that the search was unsuccessful.
 *
 * 5. **Time Complexity of Sequential Search**:
 *    - The time complexity of sequential search is O(n), where n is the number of elements in the array.
 *    - In the worst case, we might have to check every single element before finding the target (or not finding it).
 *    - This makes sequential search slower as the array size increases, especially when compared to more efficient algorithms like binary search.
 *
 * 6. **Why Sequential Search?**:
 *    - Sequential search is simple and works on both sorted and unsorted arrays.
 *    - However, it is inefficient for large arrays, as it checks each element one by one.
 *    - For small or unsorted arrays, sequential search is often fine because of its simplicity.
 *    - When dealing with large arrays, more efficient searching methods like binary search (for sorted arrays) or hash tables should be considered.
 */
 
