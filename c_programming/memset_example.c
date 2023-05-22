#include <stdio.h>
#include<stdlib.h>
#include <string.h>

int main(){
    int *ptr = malloc(5 * sizeof(int));
    if(ptr){
        memset(ptr, 0, 5 * sizeof(int));
        for(int i=0; i< 5; i++){
            printf("%d ",ptr[i]);
        }
        free(ptr);

    }
    return 0;
}
