/*
How to Print the English name of an integer in C++
Please Subscribe to Asim Code
https://youtu.be/Q5Fu8d5tPtc
*/
#include <iostream>
using namespace std;

void int_name(int digit)
{
    switch (digit)
    {
    case 1:
        cout << "one";
        break;
    case 2:
        cout << "two";
        break;
    case 3:
        cout << "three";
        break;
    case 4:
        cout << "four";
        break;
    case 5:
        cout << "five";
        break;
    case 6:
        cout << "six";
        break;
    case 7:
        cout << "seven";
        break;
    case 8:
        cout << "eight";
        break;
    case 9:
        cout << "nine";
        break;
    default:
        cout << "Not in range" << endl;
    }
}
int main()
{
    int_name(5);
}
