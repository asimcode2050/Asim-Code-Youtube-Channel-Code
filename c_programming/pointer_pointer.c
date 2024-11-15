#include <stdio.h>
int main()
{ // Declare an integer variable
    int num = 5;
    int *ptr = &num;
    int **ptr2 = &ptr;
    printf("Value of num: %d\n", num);
    printf("Value via ptr: %d\n", *ptr);
    printf("Value via ptr2: %d\n", **ptr2);
    return 0;
}
