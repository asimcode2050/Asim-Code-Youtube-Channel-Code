#include <stdio.h>
int partition(int arr[], int low, int high)
{
    int pivot = arr[high]; // 'pivot' is the last element of the subarray (arr[high])
    int i = (low - 1);
  for (int j = low; j < high; j++)
  { 
    if (arr[j] <= pivot)
    {
        i++;
        int temp = arr[i];
        arr[i] = arr[j];   // arr[i] now stores arr[j], which is smaller than or equal to the pivot
        arr[j] = temp;     // arr[j] is now set to the value of arr[i] that we temporarily saved in 'temp'
    }
  }
  int temp = arr[i + 1];
  arr[i + 1] = arr[high];
  arr[high] = temp;
  return (i + 1);
}

void quicksort(int arr[], int low, int high)
{
  if (low < high)
  {
      int pi = partition(arr, low, high);
      quicksort(arr, low, pi - 1);
      quicksort(arr, pi + 1, high); // Recursively sort the right subarray
  }
}

void printArray(int arr[], int size)
{
  for (int i = 0; i < size; i++){
      printf("%d ", arr[i]);
  }
  printf("\n");
}

int main()
{
    int arr[] = {10, 7, 8, 9, 1, 5}; // Array of integers to be sorted

    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the number of elements in the array

    printf("Original array: \n");
    printArray(arr, n); // Call the printArray function to print the original array before sorting

    quicksort(arr, 0, n - 1);

    printf("\nSorted array: \n");
    printArray(arr, n);
    return 0;
}
