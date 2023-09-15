/*
YouTube: Asim Code
Input a series of numbers and displays the minimum value in C++
https://youtu.be/xxRU5Y9NvPk
 */
#include <iostream>
using namespace std;

int main()
{
    int min, counter, value;
    cout << "Please enter a Number: ";
    cin >> min;
    for (counter = 0; counter < 3; counter++)
    {
        cout << "Please enter a Number: ";
        cin >> value;
        if (value < min)
        {
            min = value;
        }
    }
    cout << "Min value is : " << min << endl;

    return 0;
}
