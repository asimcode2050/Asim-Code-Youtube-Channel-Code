
#include <iostream>
#include <string>
using namespace std;

class Dog
{
    public:
    Dog(string name);
    ~Dog();
    void bark() const;
    string getName() const;
    private:
    string name;
};

Dog::Dog(string name){
    this->name = name;
}
Dog::~Dog(){}
void Dog::bark() const
{
    cout << "Wuff Wuff"<<endl;
}
string Dog::getName() const
{
    return this->name;
}

int main()
{
    Dog myDog("Max");
    cout << myDog.getName() << endl;
    myDog.bark();
}
