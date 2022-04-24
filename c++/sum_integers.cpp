/*
C++ program to find the sum of all the integers between first and last 
Please Subscribe to Asim Code
https://youtu.be/qthNpnLe4_w
*/
#include <iostream>
using namespace std;

int sum_numbers(int first_number, int last_number)
{
    int i, sum = 0;
    if (first_number <= last_number)
    {
        for (i = first_number; i <= last_number; ++i)
        {
            sum += i;
        }
    }
    else
    {
        for (i = first_number; i >= last_number; --i)
            sum += i;
    }
    return sum;
}
int main()
{

    // int result = sum_numbers(9,12);
    int result2 = sum_numbers(11, 8);
    cout << result2;
    return 0;
}
