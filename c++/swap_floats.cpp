/*
swap floats in C++
Please Subscribe to Asim Code
https://youtu.be/2jaff-QQbGA
*/
#include <iostream>
using namespace std;
void swap_values(int &x, int &y)
{
    float temp_value = x;
    x = y;
    y = temp_value;
}
int main()
{
    int a = 10;
    int b = 20;
    swap_values(a, b);
    cout << "Value of a : " << a << endl;
    cout << "Value of b : " << b << endl;
}
