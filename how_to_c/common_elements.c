#include<stdio.h>
#define max 100

int if_exists(int z[],int u, int y){
    int i;
    if (u==0)
    return 0;
    for(i=0;i<=u;i++){
        if(z[i]==y) {
            return (1);
        }
    return (0);
    }

}
void main(){
    int a[max], b[max], c[max];
    int length1, length2;
    int i,j,k;
    k = 0;
    printf("Please enter the length for first array:\n");
    scanf("%d",&length1);
    printf("\nPlease enter %d elements for first Array:\n",length1);
    for(i=0;i<length1;i++){
        scanf("%d",&a[i]);

    }
    printf("Please enter the length for second array:\n");
    scanf("%d",&length2);
    printf("\nPlease enter %d elements for second Array:\n",length2);
    for(i=0;i<length2;i++){
        scanf("%d",&b[i]);
        
    }
    k = 0;
    for(i=0;i<length1;i++){
        for (j=0;j<length2;j++){
            if(a[i] == b[j]){
                if(!if_exists(c,k,a[i])){
                    c[k] = a[i];
                    k++;
                }
            }
        }
    }

   if(k>0)
   {
       printf("\nCommon elements are :\n");
       for(i = 0;i<k;i++){
           printf("%d\n",c[i]);
       }
   }
   else{
       printf("There are no common elements!\n");
   }
    }


