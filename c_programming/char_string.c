#include <stdio.h>
void printChars(const char *cPtr);

int main(void)
{
    char string[] = "This is a string";
    puts("String: ");
    printChars(string);
    puts("");
    return 0;
}

void printChars(const char *cPtr)
{
    for (; *cPtr != '\0'; ++cPtr)
    {
        printf("%c\n", *cPtr);
    }
}
