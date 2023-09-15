/*
YouTube: Asim Code
Check whether a character is Lowercase
https://youtu.be/7JeZzJS2C3o
*/
#include <iostream>
using namespace std;

int main()
{
    char input;
    cout << "Please enter a character: ";
    cin >> input;
    if (input >= 'a' && input < +'z')
    {
        cout << "Letter is a lowercase." << endl;
    }
    else
    {
        cout << "Letter is not lowercase." << endl;
    }
    return 0;
}
