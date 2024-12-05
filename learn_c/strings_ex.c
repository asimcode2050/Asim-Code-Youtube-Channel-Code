#include <stdio.h>
#include <string.h>
int main()
{
    char greeting[20] = "Hello";
    char name[] = "Alice";
    strcat(greeting, " "); // Concatenates a space to the string 'greeting'. Now, greeting = "Hello ".
    strcat(greeting, name);
    printf("Greeting: %s\n", greeting);
    printf("Length of greeting: %lu\n", strlen(greeting)); // Output will be 11, which is the total length of the string.
    char copiedGreeting[20];
    strcpy(copiedGreeting, greeting);
    printf("Copied Greeting: %s\n", copiedGreeting);
    if (strcmp(greeting, copiedGreeting) == 0)
    {
        printf("The greeting strings are identical.\n");
    }
    else
    {
        printf("The greeting strings are different.\n");
    }
    return 0;
}
