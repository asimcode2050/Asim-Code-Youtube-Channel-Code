#include <stdio.h>
#define SIZE 10
int main(void)
{
    int my_array[SIZE] = {4, 2, 6, 8, 10, 9, 15, 1, 3, 5};
    int pass;
    size_t i;
    int temp;
    puts("Array Values in original order:");
    for (i = 0; i < SIZE; ++i)
    {
        printf("%4d", my_array[i]);
    }

    for (pass = 1; pass < SIZE; ++pass)
    {
        for (i = 0; i < SIZE - 1; ++i)
        {
            if (my_array[i] > my_array[i + 1])
            {
                temp = my_array[i];
                my_array[i] = my_array[i + 1];
                my_array[i + 1] = temp;
            }
        }
    }
    puts("\nArray items in ascending Order:");
    for (i = 0; i < SIZE; ++i)
    {
        printf("%4d", my_array[i]);
    }
    puts("");

    return 0;
}
