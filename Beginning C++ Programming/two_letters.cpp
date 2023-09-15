/*
YouTube: Asim Code
C++ program to Input letter and print next two letters
https://youtu.be/9nm81ifF_-g
*/
#include <iostream>
using namespace std;

int main()
{
    char my_char;
    cout << "Please enter your letter: ";
    cin >> my_char;
    cout << "Next two letters are: " << endl;
    cout << (char)(my_char + 1) << endl;
    cout << (char)(my_char + 2) << endl;
    return 0;
}
