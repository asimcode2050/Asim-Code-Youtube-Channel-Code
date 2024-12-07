#include <iostream>
using namespace std;
void greet();
int main()
{ // The main function where the execution of the program begins.
    int age = 25;
    float salary = 4500.50;
    char grade = 'B';
    float taxRate = 0.1;
    float taxAmount = salary * taxRate;
    cout << "Age: " << age << endl;
    cout << "Salary: " << salary << endl;
    cout << "Grade: " << grade << endl;
    cout << "Tax Amount: " << taxAmount << endl;
    greet();
    return 0;
}
void greet()
{
    cout << "Welcome to the program!" << endl;
}
