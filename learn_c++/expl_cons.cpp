#include <iostream>
using namespace std;
class MyClass
{
public:
    explicit MyClass(int a)
    {
        x = a;
    }

    int getX()
    {
        return x;
    }

private:
    int x;
};

int main()
{
    MyClass obj(10);
    cout << "The value of x is: " << obj.getX() << endl;
    return 0;
}
