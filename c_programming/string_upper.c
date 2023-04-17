#include <stdio.h>
#include <ctype.h>
void toUpperCase(char *cPtr);
int main(void)
{
    char string[] = "Hello World";
    printf("Original String: %s", string);
    toUpperCase(string);
    printf("\n The string after conversion is : %s\n");
}

void toUpperCase(char *cPtr)
{
    while (*cPtr != '\0')
    {
        *cPtr = toupper(*cPtr);
        ++cPtr;
    }
}
