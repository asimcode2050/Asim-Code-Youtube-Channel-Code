#include <iostream>
using namespace std;
class Shape
{
public:
    virtual double area() const
    {
        return 0.0;
    }
    virtual ~Shape()
    {
        cout << "Shape destroyed." << endl;
    }
};
class Rectangle : public Shape
{
private:
    double width, height;

public:
    Rectangle(double w, double h) : width(w), height(h) {}
    double area() const override
    {
        return width * height;
    }
    ~Rectangle()
    {
        cout << "Rectangle destroyed." << endl;
    }
};
class Circle : public Shape
{
private:
    double radius;

public:
    Circle(double r) : radius(r) {}
    double area() const override
    {
        return 3.14159 * radius * radius; // Circles area =  * r^2
    }
    ~Circle()
    {
        cout << "Circle destroyed." << endl;
    }
};
int main()
{
    Shape *shape1;
    Shape *shape2;
    shape1 = new Rectangle(10.0, 5.0);
    shape2 = new Circle(7.0); // Circle with radius 7.0
    cout << "Area of rectangle: " << shape1->area() << endl;
    cout << "Area of circle: " << shape2->area() << endl;
    delete shape1;
    delete shape2;
    return 0;
}
