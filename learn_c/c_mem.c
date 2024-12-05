#include <stdio.h>
void increment(int *ptr)
{
    (*ptr)++;
}
int main()
{
    int num = 5;
    int *ptr = &num; // `ptr` now stores the address where `num` is located in memory.
    printf("Before increment: num = %d, Address of num = %p\n", num, (void *)&num);
    increment(ptr);
    printf("After increment: num = %d, Address of num = %p\n", num, (void *)&num);
    return 0; // Return 0 to indicate the program executed successfully.
}
