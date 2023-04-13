#include <stdio.h>
#include <string.h>

int main(void)
{
    const char *str1 = "abc";
    const char *str2 = "four";
    printf("The length of str1 is %u\n", strlen(str1));
    printf("The length of str2 is %u\n", strlen(str2));
    return 0;
}
