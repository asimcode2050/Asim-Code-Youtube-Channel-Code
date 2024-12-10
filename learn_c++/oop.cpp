#include <iostream>
using namespace std;
class Car
{
private:
    string make;
    string model;
    int year;

public:
    Car(string m, string mo, int y)
    {
        make = m;
        model = mo;
        year = y;
    }
    void displayInfo()
    {
        cout << "Car Make: " << make << endl;
        cout << "Car Model: " << model << endl;
        cout << "Car Year: " << year << endl;
    }
};
int main()
{
    Car myCar("Toyota", "Corolla", 2020);
    myCar.displayInfo();
    return 0;
}
