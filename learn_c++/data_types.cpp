/*
 * Summary of Common C++ Data Types:
 *
 *  * Data Type | Description | Example
 *  * ----------|-------------|-------------------------------------------------
 *  * `int`     | Integer (whole number) | `int age = 30;`
 *  * `float`   | Floating-point number (single precision) | `float pi = 3.14;`
 *  * `double`  | Floating-point number (double precision) | `double salary = 5000.75;`
 *  * `char`    | Single character | `char letter = 'A';`
 *  * `bool`    | Boolean (true/false) | `bool isActive = true;`
 *  * `string`  | Sequence of characters (text) | `string name = "John";`
 *  * `void`    | Represents no type (used in functions returning nothing) | `void printMessage() {}`
 *  */
#include <iostream>
#include <string>
using namespace std;
double calculateArea(double radius)
{
    const double PI = 3.14159;   // Constant value for PI (not changing)
    return PI * radius * radius; // Expression: Multiplying PI by the square of radius
}
int main()
{
    int age = 30;
    float height = 5.9f;
    double salary = 75000.50;
    char grade = 'A';
    bool isEmployed = true;
    string name = "John Doe"; // String variable 'name' storing the persons full name
    int num1 = 10, num2 = 20;
    int sum = num1 + num2;                // Expression evaluates the sum of 'num1' and 'num2' and stores it in 'sum'
    int scores[5] = {95, 88, 76, 64, 85}; // An array storing scores of 5 subjects
    int *ptr = &age;                      // Pointer 'ptr' holds the address of 'age'
    double &ref = salary;                 // 'ref' directly refers to 'salary', any changes to 'ref' also change 'salary'
    double radius = 7.0;                  // Declare and initialize 'radius' variable
    double area = calculateArea(radius);  // Function call to calculate area of the circle
    cout << "Name: " << name << endl;
    cout << "Age: " << age << endl;
    cout << "Height: " << height << " feet" << endl;
    cout << "Salary: $" << salary << endl;
    cout << "Grade: " << grade << endl;
    cout << "Employment Status: " << (isEmployed ? "Employed" : "Unemployed") << endl;
    cout << "Sum of num1 and num2: " << sum << endl;
    cout << "Area of the circle (radius = " << radius << "): " << area << " square units" << endl;
    cout << "Scores: ";
    for (int i = 0; i < 5; i++)
    {
        cout << scores[i] << " ";
    }
    cout << endl;
    cout << "Address of age: " << &age << endl;
    cout << "Pointer points to: " << *ptr << endl;
    cout << "Salary via reference: " << ref << endl;
    ref = 80000.00;
    cout << "Updated Salary: $" << salary << endl;
    return 0;
}
