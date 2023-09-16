/*
YouTube: Asim Code
C++ program to count positive and negative numbers
https://youtu.be/QCczZw6hehc
*/
#include <iostream>
using namespace std;

int main()
{
    int number, pos_num, neg_num;
    pos_num =0, neg_num = 0;
    do
    {
        cout << "Please enter a number : ";
        cin >> number;
        if (number > 0)
        {
            pos_num++;
        }
        else if (number < 0)
        {
            neg_num++;
        }

    } while (number != 0);
    cout << "Total positive numbers : " << pos_num << endl;
    cout << "Total negative numbers : " << neg_num << endl;

    return 0;
}
