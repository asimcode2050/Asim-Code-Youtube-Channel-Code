#include <stdio.h>
#include <stdbool.h>
int main()
{
    bool isWeekend = true;
    bool hasPlans = false;
    if (isWeekend && hasPlans)
    {
        printf("We have weekend plans!\n");
    }
    else if (isWeekend && !hasPlans)
    {
        printf("It is the weekend, but no plans yet.\n");
    }
    else if (!isWeekend)
    {
        printf("It is not the weekend yet.\n"); // If it is not the weekend, print this message.
    }
    int temperature = 30; //
    if (isWeekend || temperature > 25)
    { // Logical OR (||): This checks if either condition is true.
        printf("It is a good day to go outside!\n");
    }
    else
    {
        printf("Maybe stay inside today.\n");
    }
    return 0;
}
