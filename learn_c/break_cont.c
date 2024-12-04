#include <stdio.h>
int main()
{
    for (int i = 1; i <= 10; i++)
    { // 'i' is initialized to 1, loop continues while i <= 10
        if (i % 2 == 0)
        {
            continue;
        }
        if (i == 7)
        { // Condition to check if 'i' is 7
            printf("Stopping the loop when i reaches 7.\n");
            break;
        }
        printf("i = %d\n", i); // Print the current value of 'i'
    }
    printf("Loop has finished.\n");
    return 0; // Exit the program with a success status (0 indicates successful execution)
}
