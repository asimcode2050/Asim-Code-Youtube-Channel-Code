/*
YouTube: Asim Code
Sum of even integers in C++
https://youtu.be/wLVMrEmVEQo
*/
#include <iostream>
using namespace std;

int main()
{
    int sum{0};
    for (int num{2}; num <= 10; num += 2)
    {
        sum += num;
    }
    cout << "Sum is :" << sum << "\n";
}
