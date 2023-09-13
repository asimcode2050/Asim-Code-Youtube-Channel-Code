/*
YouTube: Asim Code
C++ program to input an integer and display the string that many times
https://youtu.be/7n30JZ1wh4Y
*/
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int x;
    string mystring = "Hello World!";
    cout << "Please enter an integer value:";
    cin >> x;
    for (int i = 0; i < x; i++)
    {
        cout << mystring << endl;
    }
    return 0;
}
