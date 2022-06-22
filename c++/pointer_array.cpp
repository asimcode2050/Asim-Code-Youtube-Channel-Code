/*
C++ Pointer array by Using pointer increment and Using pointer index
https://youtu.be/tQPwp8mEC2c
 Please Like and Subscribe to my channel
*/
#include <iostream>

using namespace std;

int main()
{
    int arraySize = 5;
    int *ptr = new int[arraySize]{50, 70, 90, 100, 150};
    cout << "Using Pointer Increment" << endl;
    cout << "Values\tAddress" << endl;
    while (*ptr)
    {
        cout << *ptr << "\t";
        cout << ptr << endl;
        ptr++;
    }
    ptr = ptr - 5;
    cout << "Using pointer index" << endl;
    cout << "Value\tAddress" << endl;
    for (int i = 0; i < arraySize; ++i)
    {
        cout << ptr[i] << "\t";
        cout << &ptr[i] << endl;
    }

    return 0;
}
