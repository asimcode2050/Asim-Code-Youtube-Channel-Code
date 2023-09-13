/*
YouTube: Asim Code
C++ Program to Convert Fahrenheit to Celsius
https://youtu.be/-outQYgDhC8
  */
#include <iostream>
using namespace std;

int main()
{
    float f, celsius;
    cout << "Please enter the temperature in Fahrenheit: ";
    cin >> f;
    celsius = ((f - 32) / 9) * 5;
    cout << "Temperature in Celsius = " << celsius << endl;
    return 0;
}
