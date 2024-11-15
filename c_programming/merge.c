#include <stdio.h>
void merge(int arr[], int temp[], int left, int right)
{
    if (left == right)
    {
        return;
    }
    int mid = (left + right) / 2;
    merge(arr, temp, left, mid);
    merge(arr, temp, mid + 1, right);
    int i = left;
    int j = mid + 1;
    int k = left;
    while (i <= mid && j <= right)
    {
        if (arr[i] <= arr[j])
        {
            temp[k++] = arr[i++];
        }
        else
        {
            temp[k++] = arr[j++];
        }
    }
    while (i <= mid)
    {
        temp[k++] = arr[i++];
    }
    while (j <= right)
    {
        temp[k++] = arr[j++];
    }
    for (i = left; i <= right; i++)
    {
        arr[i] = temp[i];
    }
}
void mergeSort(int arr[], int n)
{
    int temp[n];
    merge(arr, temp, 0, n - 1); // Call the merge function
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
    int arr[] = {12, 11, 13, 5, 6, 7}; // Example array to be sorted
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("Unsorted array: \n");
    printArray(arr, n);
    mergeSort(arr, n);
    printf("\nSorted array: \n");
    printArray(arr, n); // Print the sorted array
    return 0;
}
