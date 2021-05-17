/*
C Program to Write to files with streams on Linux
https://youtu.be/scfnW3bRzb0
*/
#include <stdio.h>
 int main(int argc, char *argv[])
 {  
   FILE *fp;
   char line_buffer[1024] = {0};
   if(argc != 2){
       fprintf(stderr, "Usage: %s [path]\n",argv[0]);
       return 1;
   }
   if((fp = fopen(argv[1],"w")) == NULL)
   {
       perror("Cannot open file.");
       return 1;
   }

   while(fgets(line_buffer, sizeof(line_buffer), stdin) != NULL){
        fprintf(fp,line_buffer);
  }
   fclose(fp);
     return 0;
 }
