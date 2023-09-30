/*
YouTube: Asim Code
C++ Class with Static data Member
https://youtu.be/PU5CmHy-4JE
*/
#include <iostream>
using namespace std;

class Student
{
private:
    int id;
    char name[10];

public:
    static int counter;
    Student()
    {
        counter++;
    }
    void input_data()
    {
        cout << "\n Please enter ID: ";
        cin >> id;
        cout << "\n Please enter Name: ";
        cin >> name;
    }
    void print_data()
    {
        cout << "\nID: " << id << endl;
        cout << "\nName: " << name << endl;
    }
};

int Student::counter = 0;

int main()
{
    Student s1, s2;
    s1.input_data();
    s1.print_data();

    s2.input_data();
    s2.print_data();

    cout << endl
         << "Total Students: " << Student::counter << endl;

    return 0;
}
