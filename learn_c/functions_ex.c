#include <stdio.h>
int add(int x, int y);
int main()
{
    int x = 10;
    int y = 5;
    int result;
    result = add(x, y);
    printf("The sum of %d and %d is: %d\n", x, y, result);
    return 0;
}
int add(int x, int y)
{
    return x + y;
}
