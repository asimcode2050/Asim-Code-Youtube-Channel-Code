#include <stdio.h>
int main()
{
    int age = 25;
    float height = 5.9;
    char grade = 'A';
    char name[] = "Alice";
    printf("Hello, my name is %s.\n", name);
    printf("I am %d years old.\n", age);
    printf("I am %.2f meters tall.\n", height);
    printf("My grade is %c.\n", grade);
    printf("\nSummary of details:\n");
    printf("\tName: %s\n", name);
    printf("\tAge: %d\n", age);
    printf("\tHeight: %.2f\n", height);
    printf("\tGrade: %c\n", grade);
    return 0;
}
