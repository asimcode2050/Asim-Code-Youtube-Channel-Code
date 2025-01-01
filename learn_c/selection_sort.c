#include <stdio.h>
void selectionSort(int arr[], int n)
{
  for (int i = 0; i < n - 1; i++)
  {
      int minIndex = i;
    for (int j = i + 1; j < n; j++)
    {
      if (arr[j] < arr[minIndex])
      {
          minIndex = j; 
      }
    }
    if (minIndex != i)
    {
        int temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
  }
}

void printArray(int arr[], int size)
{
    printf("Sorted Array: ");
  for (int i = 0; i < size; i++)
  {
      printf("%d ", arr[i]);
  }
  printf("\n");
}

int main()
{
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("Original Array: ");
    printArray(arr, n);
    selectionSort(arr, n);
    printArray(arr, n);
    return 0;
    /*
  Explanation Line-by-line:

  1. **selectionSort function**:
     - **Parameters**:
       - `arr[]`: The array we want to sort.
       - `n`: The number of elements in the array.
     - **How it works**: The algorithm iterates through the array, finds the minimum element in the unsorted part, and places it in the sorted part by swapping it.

  2. **Outer loop (for (int i = 0; i < n - 1; i++))**:
     - This loop controls which element we are currently processing for sorting.
     - **Purpose**: For each `i`, we assume that the element at `i` is the smallest in the unsorted portion of the array. We will find the actual smallest element in the remaining part of the array and swap them.

  3. **Inner loop (for (int j = i + 1; j < n; j++))**:
     - The inner loop searches through the unsorted part of the array (from index `i + 1` to `n - 1`) to find the smallest element.
     - **Purpose**: To compare the element at `j` with the element at `minIndex`. If the element at `j` is smaller, `minIndex` is updated to point to `j`.

  4. **minIndex**:
     - `minIndex` stores the index of the smallest element found in the unsorted part of the array.
     - **Why `minIndex = i` initially?**: We assume that the smallest element starts at index `i`. If a smaller element is found later in the array, `minIndex` is updated.

  5. **Swapping Elements**:
     - After the inner loop, if `minIndex` is different from `i`, it means that the smallest element has been found at a different index.
     - We then swap the element at index `i` with the element at `minIndex` using a temporary variable to perform the swap.
     - **Temporary Variable**: `temp` is used to temporarily store the element at `arr[i]` to facilitate the swap.

  6. **Time Complexity (O(n))**:
     - **Why O(n)?**: The outer loop runs `n-1` times, and for each iteration of the outer loop, the inner loop runs `n-i` times. Hence, the total number of comparisons is approximately `n(n-1)/2`, leading to a quadratic time complexity of **O(n)**.
     - **Best Case**: Even if the array is already sorted, Selection Sort still performs all the comparisons, making it inefficient in the best case compared to more advanced algorithms like QuickSort.

  7. **Space Complexity (O(1))**:
     - **Why O(1)?**: Selection Sort is an **in-place sorting algorithm**, meaning it does not require any extra memory apart from a small amount of space for the temporary variable used during swapping. This gives it a constant space complexity of **O(1)**.

  8. **printArray function**:
     - This function takes the array and its size as parameters and prints the elements of the array to the console.
     - **Purpose**: To display the sorted array after the sorting is completed.

  9. **Main function**:
     - The main function initializes an array `arr[]` and calculates its size `n`.
     - It first prints the original array, then calls `selectionSort` to sort the array, and finally prints the sorted array to show the result.


  */
}
