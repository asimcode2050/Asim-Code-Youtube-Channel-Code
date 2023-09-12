/*
YouTube: Asim Code
C++ program to find the two largest values among the 5 numbers
https://youtu.be/-MxMMeHQlCQ
*/
#include <iostream>
using namespace std;

int main()
{
    int number_counter = 0, number, largest, second_largest = 0;
    cout << "Please enter the first number: ";
    cin >> largest;
    while (++number_counter < 5)
    {
        cout << "Please enter next number : ";
        cin >> number;
        if (number > largest)
        {
            second_largest = largest;
            largest = number;
        }
        else if (number > second_largest)
            second_largest = number;
    }
    cout << "\n Largest is : " << largest << "\n Second Largest is: " << second_largest << endl;

    return 0;
}
