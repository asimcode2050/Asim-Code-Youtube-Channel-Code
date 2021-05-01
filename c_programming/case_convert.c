// https://youtu.be/JcDgdFrEsDo
/*
C program on Linux to convert words uppercase into lower and lowercase into upper
*/
#include <stdio.h>
#include <string.h>

int main(void){
    char myArray[20] = {0};
    char newcase[20] = {0};
    int i;
    while(fgets(myArray,sizeof(myArray),stdin)!=NULL){
        for(i=0;i<sizeof(myArray);i++){
            //upper case to lower case
            if((myArray[i] >= 65) && (myArray[i] <= 90)){
                newcase[i] = myArray[i] + 32;
            }
            //lower case to upper case
            if((myArray[i] >= 97 && myArray[i] <= 122)){
                newcase[i] = myArray[i] - 32;
            }
        }
        printf("%s\n",newcase);
        memset(myArray,0,sizeof(myArray));
        memset(newcase,0,sizeof(newcase));

    }
    return 0;
}
