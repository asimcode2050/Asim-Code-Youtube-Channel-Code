#include <stdio.h>
#define ARRAY_SIZE 100
size_t linear_search(const int array[], int key, size_t size);

int main(void)
{

    int our_array[ARRAY_SIZE];
    size_t x;
    int our_key;
    size_t element;

    for (x = 0; x < ARRAY_SIZE; ++x)
    {
        our_array[x] = 2 * x;
    }
    puts("Our Array Values:");
    for (x = 0; x < ARRAY_SIZE; ++x)
    {
        printf("%4d", our_array[x]);
    }
    puts("\nPlease enter search key:");
    scanf("%d", &our_key);
    element = linear_search(our_array, our_key, ARRAY_SIZE);
    if (element != -1)
    {
        printf("Found key in element %d\n", element);
    }
    else
    {
        puts("Value not found");
    }

    return 0;
}

size_t linear_search(const int array[], int key, size_t size)
{
    size_t counter;
    for (counter = 0; counter < size; ++counter)
    {
        if (array[counter] == key)
        {
            return counter;
        }
    }
    return -1;
}
