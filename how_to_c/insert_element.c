/*
https://www.youtube.com/watch?v=KaNO8_bo6bw&ab_channel=AsimCode
*/
#include<stdio.h>
#define max 100
int main(){
    int a[max], size, i , k , j;
    printf("Please enter length of array:");
    scanf("%d",&size);

    for(i=0;i<=size-1;i++){
        scanf("%d",&a[i]);
    }

    printf("\nArray is:");
    for (i=0;i<=size-1;i++){
        printf("%d\n",a[i]);
    }
    printf("\nPlease enter position where to insert:");
    scanf("%d",&k);
    k--;
    for(j=size-1;j>=k;j--){
        a[j+1] = a[j];
    }
    printf("\nEnter the value to insert:");
    scanf("%d",&a[k]);
    printf("\nArray values after insertion\n");
    
    for(i=0;i<=size;i++){
        printf("%d\n",a[i]);
    }
   
    return 0;
}
