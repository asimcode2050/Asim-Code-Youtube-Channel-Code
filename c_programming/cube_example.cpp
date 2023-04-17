#include <stdio.h>

void cube(int *ptr);

int main(void){
    int num = 2;
    printf("The number value is :%d", num);
    cube(&num);
    printf("\n The new value of number is %d\n",num);
}

void cube(int *ptr)
{
    *ptr = *ptr * *ptr * *ptr;

}
