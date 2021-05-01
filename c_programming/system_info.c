/*
C program on Linux to read user information, current working directory, 
the machine's total and free random-access memory (RAM),
and current process ID (PID). Learn to Code Subscribe to Asim Code.
https://youtu.be/pLGXZ17gTRc
*/
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/sysinfo.h>


int main(void){
    char current_dir[100] = {0}; // current dir
    struct sysinfo sys_info; // for system information
    getcwd(current_dir,100);
    sysinfo(&sys_info); // to get system information
    printf("Your user ID : %d\n",getuid());
    printf("Current working directory: %s\n",current_dir);
    printf("Machine has %ld megabytes of total RAM\n",sys_info.totalram / 1024 /1024);
    printf("Machine has %ld megabytes of free RAM\n",sys_info.freeram / 1024 /1024);
    printf("Processes Running:%d \n", sys_info.procs);
    printf("This process ID : %d\n",getpid());
    printf("Parent process ID : %d\n",getppid());
    return 0;
}
