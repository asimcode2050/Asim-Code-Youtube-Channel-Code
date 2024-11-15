#include <iostream>
using namespace std;
class Base
{
protected:
    int protectedValue;

public:
    Base(int value) : protectedValue(value) {}
    void showValue() const
    {
        cout << "Protected value: " << protectedValue << endl;
    }
};
class Derived : public Base
{
public:
    Derived(int value) : Base(value) {}
    void changeValue(int newValue)
    {
        protectedValue = newValue;
    }
    void display() const
    {
        cout << "Changed protected value: " << protectedValue << endl;
    }
};
int main()
{
    Derived d(10);
    d.showValue();
    d.changeValue(20);
    d.display();
    return 0;
}
