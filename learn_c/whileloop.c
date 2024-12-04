#include <stdio.h>
int main()
{
    int i = 1; // Starting the loop with 1, as we want to print numbers from 1 to 5
    while (i <= 5)
    {
        printf("%d\n", i); // Print the current value of 'i'
        i++;               // Increment 'i' by 1
    }
    return 0; // End the program and return a successful exit status
}
