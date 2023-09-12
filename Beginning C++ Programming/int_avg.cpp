/*
YouTube: Asim Code
C++ program to prints the average of several integers
https://youtu.be/FBqml-Hwdsg
*/
#include <iostream>
using namespace std;

int main()
{
    int numb, count = 0, total = 0;
    cout << "Please enter an integer (1111 to end) :";
    cin >> numb;
    while (numb != 1111)
    {
        total += numb;
        ++count;
        cout << "Please enter next integer (1111 to end) :";
        cin >> numb;
    }
    if (count != 0)
    {
        cout << "\n The average is :"
             << static_cast<double>(total) / count << endl;
    }
    else
    {
        cout << "\n No values were entered." << endl;
    }
    return 0;
}
