#include <stdio.h> // The standard input-output header file is included for using functions like printf.
int main()
{
    int grades[5] = {85, 92, 78, 90, 88};
    int sum = 0;
    for (int i = 0; i < 5; i++)
    {
        sum += grades[i];
    }
    float average = sum / 5.0;
    printf("Total Sum of Grades: %d\n", sum);
    printf("Average Grade: %.2f\n", average);
    return 0;
}
