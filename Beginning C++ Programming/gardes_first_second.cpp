/*
YouTube: Asim Code
C++ program to print highest and second highest marks of students
https://youtu.be/IkyAsADowVU
 */
#include <iostream>
using namespace std;

int main()
{
    int student_marks, number_of_students;
    double marks1 = -1;
    double marks2 = -2;
    cout << "Please enter the number of students: ";
    cin >> number_of_students;
    for (int i = 0; i < number_of_students; i++)
    {
        cout << "Enter a student marks: ";
        cin >> student_marks;
        if (student_marks > marks1)
        {
            marks2 = marks1;
            marks1 = student_marks;
        }
        else if (student_marks > marks2)
        {
            marks2 = student_marks;
        }
    }
    cout << "Highest Student marks is : " << marks1 << endl;
    cout << "Second Highest Student marks is : " << marks2 << endl;

    return 0;
}
