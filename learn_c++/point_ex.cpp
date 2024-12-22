#include <iostream>
#include <string>
struct Point
{
    double x;
    double y;
};

struct Rectangle
{
    Point topLeft;
    Point bottomRight;
};

int main()
{
    Rectangle rect = {
        .topLeft = {.x = 0.0, .y = 10.0},
        .bottomRight = {.x = 10.0, .y = 0.0}};

    std::cout << "Rectangle corners:\n";
    std::cout << "Top-Left: (" << rect.topLeft.x << ", " << rect.topLeft.y << ")\n";
    std::cout << "Bottom-Right: (" << rect.bottomRight.x << ", " << rect.bottomRight.y << ")\n";

    struct ComplexStructure
    {
        int id;
        std::string name;
        double values[3];
        bool isActive;
    };

    ComplexStructure complex = {
        .id = 42,
        .name = "Example",
        .values = {1.1, 2.2, 3.3},
        .isActive = true};

    std::cout << "\nComplex Structure:\n";
    std::cout << "ID: " << complex.id << "\n";
    std::cout << "Name: " << complex.name << "\n";
    std::cout << "Values: [" << complex.values[0] << ", " << complex.values[1] << ", " << complex.values[2] << "]\n";
    std::cout << "Is Active: " << (complex.isActive ? "true" : "false") << "\n";
    return 0;
}
