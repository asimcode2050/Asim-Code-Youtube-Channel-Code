#include <stdio.h>
#include <string.h>

int main(void)
{
    char my_string[] = "This is a sentence";
    char *tokenPtr;
    tokenPtr = strtok(my_string, " ");
    while (tokenPtr != NULL)
    {
        printf("%s\n", tokenPtr);
        tokenPtr = strtok(NULL, " ");
    }
}
