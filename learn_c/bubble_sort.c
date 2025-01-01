#include <stdio.h>
void bubbleSort(int arr[], int n)
{

   for (int i = 0; i < n - 1; i++)
   {
       int swapped = 0;
      for (int j = 0; j < n - i - 1; j++)
      { // Traverse the unsorted part of the array
         if (arr[j] > arr[j + 1])
         {
             int temp = arr[j];
             arr[j] = arr[j + 1];
             arr[j + 1] = temp;

             swapped = 1;
         }
      }
      if (swapped == 0)
      {
          break;
      }
   }
}

void printArray(int arr[], int size)
{
   for (int i = 0; i < size; i++)
   {
       printf("%d ", arr[i]);
   }
   printf("\n");
}

int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90}; // Example unsorted array

    int n = sizeof(arr) / sizeof(arr[0]);
    printf("Unsorted array: \n");
    printArray(arr, n);
    bubbleSort(arr, n);
    printf("Sorted array: \n");
    printArray(arr, n);
    return 0;
}
/*
we are going to break down how Bubble Sort works, one step at a time! 
1. **The Bubble Sort Algorithm**:
    - The idea of Bubble Sort is to repeatedly go through an array, comparing adjacent elements, and swap them if they're in the wrong order.
    - In each pass through the array, the largest unsorted element "bubbles" to its correct position, like a bubble rising to the surface!
Lets start with the `bubbleSort` function.

void bubbleSort(int arr[], int n) {
}

**Outer Loop**: 
    The outer loop (`for (int i = 0; i < n-1; i++)`) means:
    - We repeat the process `n-1` times (since in the worst case, it could take `n-1` passes to fully sort the array).
    - Each time, the largest element "bubbles" up to the correct position, so we reduce the comparison size on each pass.

**Inner Loop**:
    The inner loop (`for (int j = 0; j < n-i-1; j++)`):
    - We compare adjacent elements in the array: `arr[j]` and `arr[j+1]`.
    - If `arr[j] > arr[j+1]`, we swap them to put the elements in order.

**Swapping**:
    When we find two elements out of order, we swap them:
    - We temporarily store `arr[j]` in a variable (`temp`) so we don't overwrite it.
    - Then, we move `arr[j+1]` to `arr[j]` and assign the value in `temp` back to `arr[j+1]`.

**Optimization**: 
    To make Bubble Sort more efficient, we use the `swapped` flag to check if any elements were swapped during a pass.
    If no swaps were made, we break out of the loop early, as the array is already sorted, saving time.
if (swapped == 0) {
    break;  // Exit the loop early because the array is sorted!
}
*/
