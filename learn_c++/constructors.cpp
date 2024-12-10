#include <iostream>
using namespace std;
class Rectangle
{
private:
    int length;
    int width;

public:
    Rectangle()
    {
        length = 0;
        width = 0;
        cout << "Default constructor called. Rectangle is set to length " << length << " and width " << width << endl;
    }
    Rectangle(int l, int w)
    {
        length = l;
        width = w;
        cout << "Parameterized constructor called. Rectangle is set to length " << length << " and width " << width << endl;
    }
    int calculateArea()
    {
        return length * width;
    }
    void display()
    {
        cout << "Length: " << length << ", Width: " << width << endl;
    }
    ~Rectangle()
    {
        cout << "Rectangle object with length " << length << " and width " << width << " is being destroyed." << endl;
    }
};
int main()
{
    Rectangle rect1;
    rect1.display();
    Rectangle rect2(10, 5);
    rect2.display();
    cout << "Area of rect2: " << rect2.calculateArea() << endl;
    return 0;
}
