#include <iostream>
using namespace std;
int main()
{
    int temperature = 25;
    if (temperature > 30)
    {
        cout << "It is hot outside!" << endl;
    }
    else if (temperature > 20)
    {
        cout << "It is warm outside!" << endl;
    }
    else
    {
        cout << "It is cold outside!" << endl;
    }
    return 0;
}
