#include <stdio.h>
enum Day
{
    Sunday = 1,
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday
};
int main()
{
    enum Day today;
    today = Wednesday;
    printf("Today is day number %d.\n", today);
    switch (today)
    {
    case Sunday:
        printf("It is time to relax! Sunday is here.\n");
        break; // The break statement prevents the program from continuing to check the following cases.
    case Monday:
        printf("Start of the work week. Let's get to work!\n");
        break; // Stop checking the rest of the cases after this block runs.
    case Wednesday:
        printf("It is hump day! The week is half over.\n");
        break; // Again, break out of the switch statement after handling this case.
    default:
        printf("It is just another regular day.\n");
    }
    return 0;
}
