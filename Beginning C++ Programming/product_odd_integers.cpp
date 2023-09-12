/*
YouTube: Asim Code
Product of the odd integers in C++
https://youtu.be/Uqu3XR6eXH0
*/
#include <iostream>
using namespace std;

int main()
{
    long product_value = 1;
    for (long x = 3; x <= 10; x += 2)
    {
        product_value *= x;
    }
    cout << "Product of the odd integers (1-10): " << product_value << endl;
    return 0;
}
