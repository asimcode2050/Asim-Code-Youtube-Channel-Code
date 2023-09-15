/*
YouTube: Asim Code
Age Calculator using C++
https://youtu.be/24kioNwMVoo
*/
#include <iostream>
using namespace std;

int main()
{
    int age, age_months, age_days = 0;
    cout << "Please enter age in years: ";
    cin >> age;
    age_months = age * 12;
    age_days = age * 365;
    cout << "Age in months: " << age_months << endl;
    cout << "Age in days: " << age_days << endl;
    return 0;
}
