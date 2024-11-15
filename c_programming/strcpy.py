#include <stdio.h>
#include <string.h>
int main()
{
    char source[] = "Hello, World!";
    char destination[50]; // Make sure destination is large enough
    char *src = source;
    char *dest = destination;
    strcpy(dest, src);
    printf("Source: %s\n", src);
    printf("Destination: %s\n", dest);
    return 0;
}
