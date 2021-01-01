#include <iostream>
#include <string>
using namespace std;

class Demo
{
    public:
    Demo(int data){
        this->data = data;
    }
    ~Demo(){};
    Demo& operator=(const Demo& rhs){
        data = rhs.data;
        return *this;
    }
    int data;
};

int main(){
    Demo demo1(2);
    Demo demo2(50);
    demo1 = demo2;
    cout <<demo1.data<<endl;
}