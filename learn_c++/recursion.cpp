#include <iostream>
using namespace std;
int factorial(int n)
{
    if (n == 0 || n == 1)
    {
        return 1;
    }
    return n * factorial(n - 1); // Multiply n with the factorial of (n-1)
}
int main()
{
    int num; // Declare a variable to store the number entered by the user
    cout << "Enter a number to find its factorial: ";
    cin >> num;
    cout << "Factorial of " << num << " is: " << factorial(num) << endl;
    return 0; // Return 0 to indicate the program ran successfully
}
