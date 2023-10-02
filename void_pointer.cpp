/*
YouTube: Asim Code
void pointer in C++
https://youtu.be/puQ36ZtqxGI
*/
#include <iostream>
using namespace std;

int main()
{
    void *void_ptr;
    float f = 5.6;
    int x = 12;

    void_ptr = &x;
    cout << "\n The content of pointer is:";
    cout << *(static_cast<int *>(void_ptr));

    void_ptr = &f;
    cout << "\n The content of pointer is:";
    cout << *(static_cast<float *>(void_ptr));

    cout << endl;

    return 0;
}
