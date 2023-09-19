/*
YouTube: Asim Code
C++ program to create inline function
https://youtu.be/LpSAeSmTCls
*/
#include <iostream>
using namespace std;
inline float area_circle(float radius)
{
    cout << "Area of circle is : " << 22 / 7.0 * radius * radius << endl;
}

int main()
{
    float radius;
    cout << "Please enter radius of circle: ";
    cin >> radius;
    area_circle(radius);

    return 0;
}
