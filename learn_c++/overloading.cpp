#include <iostream>
using namespace std;
int add(int a, int b)
{
    return a + b;
}
float add(float a, float b)
{
    return a + b;
}
int add(int a, int b, int c)
{
    return a + b + c;
}
int main()
{
    int intResult;
    float floatResult;
    int tripleResult;
    intResult = add(5, 3);
    floatResult = add(4.5f, 5.5f);
    tripleResult = add(1, 2, 3);
    cout << "Sum of 5 and 3 (int): " << intResult << endl;
    cout << "Sum of 4.5 and 5.5 (float): " << floatResult << endl;
    cout << "Sum of 1, 2, and 3 (int): " << tripleResult << endl;
    return 0;
}
