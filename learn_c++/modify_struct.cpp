#include <iostream>
#include <cstring>
struct Person
{
    char name[50];
    int age;
    float height;
};
int main()
{
    Person person1;
    strcpy(person1.name, "John Doe");
    person1.age = 30;
    person1.height = 5.9;
    std::cout << "Name: " << person1.name << std::endl;
    std::cout << "Age: " << person1.age << std::endl;
    std::cout << "Height: " << person1.height << " ft" << std::endl;
    return 0;
}
