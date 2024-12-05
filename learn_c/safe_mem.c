#include <stdio.h>
#include <stdlib.h>
void safeMemoryManagementExample()
{
    int *ptr = NULL;
    ptr = malloc(sizeof(int));
    if (ptr == NULL)
    {
        printf("Memory allocation failed!\n");
        return;
    }
    *ptr = 25;
    printf("Value at ptr: %d\n", *ptr);
    free(ptr);
    ptr = NULL;
}
int main()
{
    safeMemoryManagementExample();
    return 0;
}
