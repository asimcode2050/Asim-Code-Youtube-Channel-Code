#include <stdio.h>
int main()
{ // The main function, where the execution of the program begins.
    FILE *file;
    file = fopen("example.txt", "r");
    if (file == NULL)
    {
        printf("Error opening the file.\n");
        return 1; // Exit the program if the file could not be opened.
    }
    char line[100];
    while (fgets(line, sizeof(line), file))
    {
        printf("%s", line);
    }
    fclose(file);
    return 0;
}
