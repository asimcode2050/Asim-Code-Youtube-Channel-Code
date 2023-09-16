/*
YouTube: Asim Code
Sum of the first n odd numbers in C++
https://youtu.be/TqMdSQ3v70k
*/
#include <iostream>
using namespace std;

int main()
{
    int count, num, sum, i;
    sum = 0;
    num = 1;
    cout << " Please enter how many odd integers to add : ";
    cin >> count;
    for (i = 1; i <= count; i++)
    {
        sum = sum + num;
        num = num + 2;
    }
    cout << "Sum of first " << count << " odd integers: " << sum << endl;

    return 0;
}
