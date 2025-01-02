/*
 O(n log n)
*/
#include <stdio.h>
/*
    int n1 = mid - left + 1; // Length of the left subarray
    int n2 = right - mid;    // Length of the right subarray
*/
/*
    int L[n1], R[n2];  // L is for left, and R is for right subarray
*/
/*
    L[i] = arr[left + i]; // Copy data to left subarray
    R[j] = arr[mid + 1 + j]; // Copy data to right subarray
*/
/*
    if (L[i] <= R[j]) { arr[k] = L[i]; i++; } else { arr[k] = R[j]; j++; }
*/
/*
    while (i < n1) { arr[k] = L[i]; i++; k++; }
    while (j < n2) { arr[k] = R[j]; j++; k++; }
*/
void merge(int arr[], int left, int mid, int right)
{
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int L[n1], R[n2];

  for (int i = 0; i < n1; i++)
  {
      L[i] = arr[left + i];
  }
  for (int j = 0; j < n2; j++)
  {
      R[j] = arr[mid + 1 + j];
  }

  int i = 0, j = 0, k = left;
  while (i < n1 && j < n2)
  {
    if (L[i] <= R[j])
    {
        arr[k] = L[i];
        i++;
    }
    else
    {
        arr[k] = R[j];
        j++;
    }
    k++;
  }
  while (i < n1)
  {
      arr[k] = L[i];
      i++;
      k++;
  }
  while (j < n2)
  {
      arr[k] = R[j];
      j++;
      k++;
  }
}
/*
    if (left < right) { ... }
*/

/*
    int mid = left + (right - left) / 2; // Midpoint calculation
*/
/*
    mergeSort(arr, left, mid); // Sort the first half
    mergeSort(arr, mid + 1, right); // Sort the second half
*/
/*
    merge(arr, left, mid, right); // Merge both halves in sorted order
*/

void mergeSort(int arr[], int left, int right)
{
  if (left < right)
  {
      int mid = left + (right - left) / 2;
      mergeSort(arr, left, mid);
      mergeSort(arr, mid + 1, right);

      merge(arr, left, mid, right);
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

/*
    int arr[] = {38, 27, 43, 3, 9, 82, 10};
*/
/*
    int arr_size = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array
*/
/*
    mergeSort(arr, 0, arr_size - 1);  // Sort the array
*/
/*
    printArray(arr, arr_size);  // Print the sorted array
*/
int main()
{
    int arr[] = {38, 27, 43, 3, 9, 82, 10};
    int arr_size = sizeof(arr) / sizeof(arr[0]);
    printf("Original array: \n");
    printArray(arr, arr_size);
    mergeSort(arr, 0, arr_size - 1);
    printf("\nSorted array: \n");
    printArray(arr, arr_size);
    return 0;
}
