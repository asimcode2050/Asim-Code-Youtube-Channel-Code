/*
C program to delete an element from an array
https://youtu.be/rM18rdo9LAs
*/
#include <stdio.h>
int main(){
    int arr[100], i, j, a;
    printf("Please enter the length of array: ");
    scanf("%d",&j);
    printf("Please enter %d elements of array\n",j);
    for(i=0;i<=j-1;i++){
        scanf("%d",&arr[i]);
    }
    for(i=0;i<=j-1;i++){
        printf("%d\n",arr[i]);
    }
    printf("Please enter location to delete: ");
    scanf("%d",&a);
    a--;
    for(i=a;i<=j-2;i++){
        arr[i] = arr[i+1];
    }
    arr[j-1] =0;
    printf("Array after deleting the element:\n");
    for(i=0;i<=j-2;i++){
        printf("%d\n",arr[i]);
    }

    return 0;
}
