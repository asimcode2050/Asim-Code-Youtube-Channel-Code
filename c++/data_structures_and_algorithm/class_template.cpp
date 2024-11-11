#include <iostream>
using namespace std;
template <typename T>
class Box
{
private:
    T value; // Data member of type T
public:
    Box(T val) : value(val) {}
    T getValue() const
    {
        return value;
    }
    void setValue(T val)
    {
        value = val;
    }
};
int main()
{
    Box<int> intBox(10);
    cout << "Integer value: " << intBox.getValue() << endl;
    Box<double> doubleBox(3.14);
    cout << "Double value: " << doubleBox.getValue() << endl;
    doubleBox.setValue(2.71);
    cout << "Updated double value: " << doubleBox.getValue() << endl;
    return 0;
}
