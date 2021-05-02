/*
C Program to Create files and updating the timestamp.
Learn to Code Subscribe to Asim Code: https://www.youtube.com/channel/UC2wyJKxwEEk_CK_HkqgZ_6g
https://youtu.be/25yj2qF0we0
*/
#include <stdio.h>
#include <fcntl.h>
#include <string.h>
#include <errno.h>
#include <utime.h>

int main(int argc , char *argv[]){
    char file_name[100] = {0};
    if(argc !=2)
    {
        fprintf(stderr, "Please enter a file name\n");
        return 1;
    }
    strncat(file_name,argv[1], sizeof(file_name)-1);
    if(utime(file_name, NULL) == -1){
        if(errno == ENOENT){
            if(creat(file_name,00644) == -1){
                perror("Cannot create file");
                return errno;
            }
        }
        //if cannot update timestamp
        else{
            perror("Cannot update the time stamp");
            return errno;
        }

    }
    return 0;
}
