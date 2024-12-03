#include <stdio.h>
#define PI 3.14159
const int MAX_USERS = 100;
int main()
{
    float radius = 5.0;
    float area = PI * radius * radius;
    printf("The area of the circle with radius %.2f is %.2f\n", radius, area);
    printf("The maximum number of users allowed is: %d\n", MAX_USERS);
    return 0; // The 'return' statement signals that the program has executed successfully.
}
