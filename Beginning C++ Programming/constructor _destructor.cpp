/*
YouTube: Asim Code
Constructor and Destructor in C++
https://youtu.be/jKPxdZTSjJw
*/
#include <iostream>
using namespace std;

class base
{
public:
    base()
    {
        cout << "Base class constructor called " << endl;
    }
    ~base()
    {
        cout << "Base class destructor called " << endl;
    }
};

class derived : public base
{
public:
    derived()
    {
        cout << "derived class constructor called " << endl;
    }
    ~derived()
    {
        cout << "derived class destructor called " << endl;
    }
};

int main()
{
    derived d;
    cout<<endl;
    return 0;
}
