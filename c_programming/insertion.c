#include <stdio.h>
void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++)
    { // Set the key as the current element
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key)
        { // Shift element to the right
            arr[j + 1] = arr[j];
            j = j - 1; // Move to the next element on the left
        }
        arr[j + 1] = key;
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
    printf("Original array: \n");
    printArray(arr, n);
    insertionSort(arr, n);
    printf("Sorted array: \n");
    printArray(arr, n);
    return 0;
}
