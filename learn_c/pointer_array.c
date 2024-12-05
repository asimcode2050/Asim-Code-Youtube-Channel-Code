#include <stdio.h>
int main()
{
    int arr[5] = {10, 20, 30, 40, 50};
    int *ptr = arr;
    printf("Using pointer and array:\n");
    for (int i = 0; i < 5; i++)
    {
        printf("Element %d: %d\n", i, *(ptr + i));
    }
    printf("\nUsing array indexing:\n");
    for (int i = 0; i < 5; i++)
    {
        printf("Element %d: %d\n", i, arr[i]);
    }
    return 0;
}
