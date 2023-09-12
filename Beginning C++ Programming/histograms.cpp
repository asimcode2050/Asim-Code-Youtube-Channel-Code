/*
YouTube: Asim Code
Read a number and print a line containing that number of adjacent asterisks in C++
https://youtu.be/ulrEU1VlAtU
*/
#include <iostream>
using namespace std;

int main()
{
    int number;
    cout << "Please enter 5 numbers : ";
    for (int i = 1; i <= 5; ++i)
    {
        cin >> number;
        for (int j = 1; j <= number; ++j)
        {
            cout << '*';
        }
        cout << '\n';
    }
    cout << endl;
    return 0;
}
