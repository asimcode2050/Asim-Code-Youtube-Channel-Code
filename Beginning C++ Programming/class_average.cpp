/*
YouTube: Asim Code
Calculate Class Average in C++
https://youtu.be/uJ5tilWKjy0
  */
#include <iostream>
using namespace std;

int main()
{
    int sum_grades{0};
    int grade_counter{1};

    while (grade_counter <= 5)
    {
        cout << "Please enter grade:";
        int grade;
        cin >> grade;
        sum_grades = sum_grades + grade;
        grade_counter = grade_counter + 1;
    }
    int avg{sum_grades / 5};
    cout << "\n Total of all 5 grade is : " << sum_grades;
    cout << "\n Class average is : " << avg << "\n";
}
