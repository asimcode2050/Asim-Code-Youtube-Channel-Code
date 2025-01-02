#include <stdio.h>
void swap(int *a, int *b)
{

    int temp = *a;
    *a = *b;
    *b = temp;
}
void heapify(int arr[], int n, int i)
{

    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

  if (left < n && arr[left] > arr[largest])
  {
      largest = left;
  }

  if (right < n && arr[right] > arr[largest])
  {
      largest = right;
  }

  if (largest != i)
  {
      swap(&arr[i], &arr[largest]);
      heapify(arr, n, largest);
  }
}
void buildHeap(int arr[], int n)
{
/* n/2 - 1 */
  for (int i = n / 2 - 1; i >= 0; i--)
  {
      heapify(arr, n, i); // Heapify each subtree starting from the last non-leaf node.
  }
}

void heapSort(int arr[], int n)
{
    buildHeap(arr, n);
  for (int i = n - 1; i > 0; i--)
  {
      swap(&arr[0], &arr[i]);

      heapify(arr, i, 0);
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
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("Unsorted array: ");
    printArray(arr, n);
    heapSort(arr, n);
    printf("Sorted array: ");
    printArray(arr, n);

    return 0;
}
