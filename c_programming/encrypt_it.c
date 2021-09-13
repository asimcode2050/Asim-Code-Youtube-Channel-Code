/*
   How to Encrypt a text file in C
   YouTube Channel : Asim Code
   https://youtu.be/PyImxH28Kgk
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFF_SIZE 255
void main(int argc, char* argv[]){
    FILE *fin, *fout;
    int i,n;
    char buffer[BUFF_SIZE];
    fin = fopen(argv[1],"r");
    if(fin == NULL){
        printf("%s file does not exist\n",argv[1]);
        exit(1);

    }
    fout = fopen(argv[2],"w");
    if(fout == NULL){
        perror("Cannot create the file \n");
        exit(1);    
    }
    while(fgets(buffer,sizeof(buffer),fin)!=0){
        n = strlen(buffer);
        for(i=0; i<n; i++)
            buffer[i] = buffer[i] - 45;
        
        fputs(buffer,fout);
    }
    fclose(fin);
    fclose(fout);
}
