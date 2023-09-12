/*
YouTube: Asim Code
C++ program to print the sum, product, difference, and quotient of the two numbers.
https://youtu.be/uzvoDOLtIvA
  */
#include <iostream>
using namespace std;

int main()
{
    int numb1, numb2;
    cout << "Please enter two integers :";
    cin >> numb1 >> numb2;
    cout << "The sum is : " << numb1 + numb2
         << "\n The product is : " << numb1 * numb2
         << "\n The difference is: " << numb1 - numb2
         << "\n The quotient is : " << numb1 / numb2 << endl;
    return 0;
}
