#include <iostream>
using namespace std;
int main()
{
    int x = 10;
    int *ptr = &x; // 'ptr' is an integer pointer that stores the address of 'x'.
    cout << "The value of x: " << *ptr << endl;
    int *arr = new int[5]; // Allocate an array of 5 integers on the heap. 'arr' points to the first element.
    for (int i = 0; i < 5; ++i)
    {
        arr[i] = (i + 1) * 2;
    }
    cout << "The values in the dynamically allocated array: ";
    for (int i = 0; i < 5; ++i)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    delete[] arr;
    arr = nullptr;
    if (arr == nullptr)
    {
        cout << "arr is now a null pointer, it points to no memory." << endl;
    }
    return 0;
}
