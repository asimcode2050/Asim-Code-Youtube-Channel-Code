/*
YouTube: Asim Code
Prefix increment and postfix increment in C++
https://youtu.be/1S1xWy027qg
*/
#include <iostream>
using namespace std;

int main()
{
    int a{2};
    // postfix increment
    cout << "a before psotincrement: " << a << "\n";
    cout << " postincrementing a: " << a++ << "\n";
    cout << " a after postincrement: " << a << "\n";

    cout << "\n";
    // prefix increment
    int b{5};
    cout << "b before preincrement: " << b << "\n";
    cout << " preincrementing b: " << ++b << "\n";
    cout << " b after preincrement:" << b << "\n";
}
