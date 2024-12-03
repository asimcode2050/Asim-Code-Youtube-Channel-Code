#include <stdio.h>
float calculate_area(float width, float height)
{
    return width * height; // The result is returned as a float value.
}
int main()
{
    float width = 5.0;                    // Initialized with a value of 5.0.
    float height = 3.0;                   // Initialized with a value of 3.0.
    float area;                           // Not initialized yet; it will be assigned a value after calling the function.
    area = calculate_area(width, height); // The returned value (area) is assigned to the variable 'area'.
    printf("Width of rectangle: %.2f\n", width);
    printf("Height of rectangle: %.2f\n", height);
    printf("Area of rectangle: %.2f\n", area);
    return 0;
}
