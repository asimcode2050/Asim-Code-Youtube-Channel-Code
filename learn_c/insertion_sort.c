#include <stdio.h>
void insertionSort(int arr[], int n)
{
  for (int i = 1; i < n; i++)
  {
      int key = arr[i];
      int j = i - 1;
/* (arr[0], arr[1], ..., arr[i-1]) */
    while (j >= 0 && arr[j] > key)
    {
        arr[j + 1] = arr[j];
        j--;
    }

    arr[j + 1] = key;
/* arr[0] to arr[i] will be sorted up to the current element (arr[i]) */
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
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("Original array: ");
    printArray(arr, n);
    insertionSort(arr, n);
    printf("Sorted array: ");
    printArray(arr, n);

    return 0;
}
