#include <stdio.h>
#include <string.h>
struct Person
{
    char name[50];
    int age;
    float height;
};
int main()
{
    struct Person person1;
    strcpy(person1.name, "Alice");
    person1.age = 30;
    person1.height = 1.75;
    printf("Name: %s\n", person1.name);              // Prints: Alice
    printf("Age: %d\n", person1.age);                // Prints: 30
    printf("Height: %.2f meters\n", person1.height); // Prints: 1.75 meters
    return 0;
}
