/*
YouTube: Asim Code
C++ Program to Find Area of Circle
https://youtu.be/7v_C8q64D6Q
*/
#include <iostream>
using namespace std;

int main()
{
    double radius_value, pi = 3.14159;
    cout << "Please enter the radius: ";
    cin >> radius_value;
    cout << "The diameter is: " << radius_value * 2.0
         << "\n The circumference is: " << 2.0 * pi * radius_value
         << "\n The are is : " << pi * radius_value * radius_value << endl;

    return 0;
}
