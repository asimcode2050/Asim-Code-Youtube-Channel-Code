#include <iostream>
double calculateArea(double length, double width);
int main()
{
    double length, width;
    std::cout << "Enter the length of the rectangle: ";
    std::cin >> length;
    std::cout << "Enter the width of the rectangle: ";
    std::cin >> width;
    double area = calculateArea(length, width);
    std::cout << "The area of the rectangle is: " << area << std::endl;
    return 0;
}
double calculateArea(double length, double width)
{
    double area = length * width;
    return area;
}
