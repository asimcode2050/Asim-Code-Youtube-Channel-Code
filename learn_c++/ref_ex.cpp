#include <iostream>
using namespace std;
int addValue(int &number)
{
    number += 10;
    return number;
}
int main()
{
    int x = 5;
    cout << "Original value of x: " << x << endl;
    int result = addValue(x);
    cout << "Value of x after function call: " << x << endl;
    cout << "Return value from the function: " << result << endl;
    return 0;
}
