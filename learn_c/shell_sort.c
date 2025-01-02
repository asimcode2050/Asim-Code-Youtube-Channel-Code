#include <stdio.h>
void shellSort(int arr[], int n)
{

/* (`gap /= 2`) */

int gap = n / 2;
  while (gap > 0)
  {
    for (int i = gap; i < n; i++)
    {
        int temp = arr[i]; // Store the current element for insertion.

        int j = i;
      while (j >= gap && arr[j - gap] > temp)
      {
          arr[j] = arr[j - gap];
          j -= gap;
      }
      arr[j] = temp; 
    }

    printf("Array after gap %d: ", gap);
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");

    gap /= 2;
  }
}

void printArray(int arr[], int size)
{
    printf("Sorted array: ");
  for (int i = 0; i < size; i++)
  {
      printf("%d ", arr[i]);
  }
  printf("\n");
}

int main()
{
    int arr[] = {5, 2, 9, 1, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Original array: ");
  for (int i = 0; i < n; i++)
  {
      printf("%d ", arr[i]);
  }
  printf("\n");

  shellSort(arr, n);

  printArray(arr, n);

  return 0;

  /*
Shell Sort Overview:
- Shell Sort improves upon Insertion Sort by comparing elements that are further apart.
- This reduces the total number of comparisons and shifts needed.

Initialization:
- `gap` is initialized as half of the array size (`n / 2`).
- This controls the distance between elements to compare and move.

Main Sorting Logic:
- Outer Loop: Continues until `gap` becomes 0. After each pass, the `gap` is halved.
- Inner Loop: Processes the array by comparing and shifting elements that are `gap` apart, using a modified insertion sort approach.
- Insertion Sort Logic: Elements are shifted if they are larger than the current element (`temp`), allowing the array to get sorted progressively.

Gap Reduction:
- After every pass, `gap` is halved (`gap /= 2`), bringing elements closer together until the gap is 0.

Printing the Array:
- The array is printed after each gap pass to visualize the progress of sorting.
- The final sorted array is printed after all passes are completed.
*/

}
