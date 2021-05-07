/*
C program to read the stat,  access rights and ownership of a file.
Learn to Code Subscribe to Asim Code.
https://youtu.be/7BX6eWUVu-M
*/
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <pwd.h>
#include <grp.h>

int main(int argc , char *argv[]){
    struct stat file_stat;
    struct passwd *user_info;
    struct group *group_info;

    if(argc !=2)
    {
        fprintf(stderr, "Usage : %s <file>\n", argv[0]);
        return 1;
    }
    if(stat(argv[1], &file_stat) == -1){

        fprintf(stderr, "Cannot read file %s: %s\n", argv[1],strerror(errno));
        return errno;
    }
    if((user_info = getpwuid(file_stat.st_uid)) == NULL){
        perror("Cannot get username");
        return errno;
    }
    if((group_info = getgrgid(file_stat.st_gid)) == NULL){
        perror("Cannot get groupname");
        return errno;
    }
    printf("Inode: %lu\n",file_stat.st_ino);
    printf("Size: %lu\n",file_stat.st_size);
    printf("Links: %lu\n",file_stat.st_nlink);
    printf("Owner: %d (%s)\n",file_stat.st_uid, user_info->pw_name);
    printf("Group: %d (%s)\n",file_stat.st_gid, group_info->gr_name);
    printf("File mode %o\n", file_stat.st_mode);
    return 0;
}
