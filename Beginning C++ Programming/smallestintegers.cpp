/*
YouTube: Asim Code
Find the smallest of several integers in C++
https://youtu.be/y2awT8Xv1xU
*/
#include <iostream>
using namespace std;

int main()
{
    int number, value, smallest_value;
    cout << "Please enter the number of integer to be processes: ";
    cin >> number;
    cout << "Please enter an integer: ";
    cin >> smallest_value;

    for (int x = 2; x <= number; x++)
    {
        cout << "Please enter next integer: ";
        cin >> value;
        if (value < smallest_value)
        {
            smallest_value = value;
        }
    }
    cout << "\nThe smallest value is : " << smallest_value << endl;
    return 0;
}
