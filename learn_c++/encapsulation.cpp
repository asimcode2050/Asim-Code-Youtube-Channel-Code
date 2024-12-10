#include <iostream>
#include <string>
using namespace std;
class Student
{
private:
    string name;
    double grade;

public:
    Student(string studentName, double initialGrade)
    {
        name = studentName;
        if (initialGrade >= 0 && initialGrade <= 100)
        {
            grade = initialGrade; // If valid, set the grade.
        }
        else
        {
            grade = 0; // If invalid (out of range), set it to 0 as a fallback value.
        }
    }
    void setGrade(double newGrade)
    {
        if (newGrade >= 0 && newGrade <= 100)
        {
            grade = newGrade; // If valid, the grade is updated to the new value.
        }
        else
        {
            cout << "Invalid grade. Grade must be between 0 and 100." << endl;
        }
    }
    double getGrade()
    {
        return grade;
    }
    string getName()
    {
        return name; // Return the students name.
    }
};
int main()
{
    Student student1("John Doe", 85);
    cout << "Student Name: " << student1.getName() << endl;
    cout << "Student Grade: " << student1.getGrade() << endl;
    student1.setGrade(92);
    cout << "Updated Grade: " << student1.getGrade() << endl;
    student1.setGrade(110);
    cout << "Grade after invalid input: " << student1.getGrade() << endl;
    return 0;
}
