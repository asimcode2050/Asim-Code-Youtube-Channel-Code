/*
YouTube: Asim Code
C++ Single Inheritance example
https://youtu.be/B_S3XkPXPYY
*/
#include <iostream>
using namespace std;
const float pi = 22 / 7.0;

class circle
{
public:
    float radius;
    void area()
    {
        cout << "Please enter radius for circle: ";
        cin >> radius;
        cout << "Area of Circle is: " << (pi)*radius * radius;
    }
};

class sphere : public circle
{
public:
    void volume()
    {
        cout << "\n Please enter the radius for sphere: ";
        cin >> radius;
        cout << "Volume of Sphere is "<< (4 * (pi)*radius * radius * radius) / 3;
    }
};

int main()
{
    circle my_circle;
    sphere my_sphere;
    my_circle.area();
    my_sphere.volume();

    return 0;
}
