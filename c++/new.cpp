#include <iostream>
using namespace std;
int main()
{
    int *ptr = new int;
    *ptr = 10;
    cout << "The value of the dynamically allocated integer is: " << *ptr << endl;
    int *arr = new int[5];
    for (int i = 0; i < 5; ++i)
    {
        arr[i] = i * 2; // Initializing array elements with values (0, 2, 4, 6, 8)
    }
    cout << "The values in the dynamically allocated array are: ";
    for (int i = 0; i < 5; ++i)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    delete ptr;   // delete releases memory allocated for a single variable
    delete[] arr; // delete[] releases memory allocated for an array
    return 0;
}
