/*
YouTube: Asim Code
C++ program to display Squares of asterisks
https://youtu.be/O_Q4jJaA0yg
*/
#include <iostream>
using namespace std;

int main()
{
    int x, y;
    for (x = 1; x <= 5; x++)
    {
        for (y = 1; y <= 5; y++)
            if (x == 1 || y == 1 || x == 5 || y == 5)
                cout << "*";
            else
                cout << " ";
        cout << endl;
    }

    return 0;
}
