/*
YouTube: Asim Code
C++ program to prints if the first is a multiple of the second
https://youtu.be/nNyLlTsaP7k
  */
#include <iostream>
using namespace std;

int main()
{
    int numb1, numb2;
    cout << "Please enter two integers: ";
    cin >> numb1 >> numb2;
    if (numb1 % numb2 == 0)
        cout << numb1 << " is a multiple of " << numb2 << endl;
    if (numb1 % numb2 != 0)
        cout << numb1 << " is not a multiple of " << numb2 << endl;

    return 0;
}
