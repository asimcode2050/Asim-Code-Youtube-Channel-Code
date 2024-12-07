#include <iostream>
#include <string>
using namespace std;
int main()
{
    string name;
    int age;
    double height;
    cout << "Enter your name: ";
    getline(cin, name);
    cout << "Enter your age: ";
    cin >> age;
    cout << "Enter your height in meters (e.g., 1.75): ";
    cin >> height;
    cout << "Hello, " << name << "!" << endl;
    cout << "You are " << age << " years old and " << height << " meters tall." << endl;
    return 0;
}
