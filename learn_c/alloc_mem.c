#include <stdio.h>
#include <stdlib.h>
struct Person
{
    char name[50];
    int age;
    float height;
};
int main()
{
    struct Person *p1 = (struct Person *)malloc(sizeof(struct Person));
    if (p1 == NULL)
    {
        printf("Memory allocation failed\n");
        return 1;
    }
    snprintf(p1->name, 50, "Alice");
    p1->age = 30;
    p1->height = 1.75;
    printf("Name: %s\n", p1->name);
    printf("Age: %d\n", p1->age);
    printf("Height: %.2f meters\n", p1->height);
    free(p1);
    return 0;
}
