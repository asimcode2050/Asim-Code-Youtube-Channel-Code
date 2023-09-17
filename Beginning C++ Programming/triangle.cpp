/*
YouTube: Asim Code
Triangle of ampersand in C++
https://youtu.be/TG3genqBY3A
*/
#include <iostream>
using namespace std;

int main()
{
    int x, sp;
    cout << "Please enter height: ";
    cin >> x;
    for (int r = 1, sp = x - 1; r <= x; r++, sp--)
    {
        for (int k = 0; k <= sp; k++)
            cout << " ";
        for (int a = 1; a < 2 * r; a++)
        {
            if (a == 1 || a == 2 * r - 1 || r == x)
                cout << "&";
            else
                cout << " ";
        }
        cout << endl;
    }

    return 0;
}
