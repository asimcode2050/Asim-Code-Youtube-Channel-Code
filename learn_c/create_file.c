#include <stdio.h>
int main()
{
    FILE *filePtr;
    filePtr = fopen("example.txt", "w");
    if (filePtr == NULL)
    {
        printf("Error opening the file.\n");
        return 1; // Return 1 indicates an error.
    }
    fprintf(filePtr, "Hello, this is a test file created in C!\n");
    fprintf(filePtr, "This is the second line of the file.\n");
    fclose(filePtr);
    printf("File created and data written successfully.\n");
    return 0;
}
