#include <iostream>
#include <string>
class Animal
{
public:
    Animal(std::string name) : name(name) {}
    virtual void speak()
    {
        std::cout << "Animal makes a sound" << std::endl;
    }
    std::string getName()
    {
        return name;
    }

private:
    std::string name;
};
class Lion : public Animal
{
public:
    Lion(std::string name) : Animal(name) {}
    void speak() override
    {
        std::cout << getName() << " roars!" << std::endl;
    }
};
class Elephant : public Animal
{ // 'Elephant' class inherits from the 'Animal' base class
public:
    Elephant(std::string name) : Animal(name) {}
    void speak() override
    {
        std::cout << getName() << " trumpets!" << std::endl;
    }
};
int main()
{
    Lion lion("Simba");
    Elephant elephant("Dumbo");
    lion.speak();
    elephant.speak();
    return 0;
}
