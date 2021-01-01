#include<iostream>
#include <string>
class DemoClass{
public:
int publicInt = 0;
protected:
int protectedInt = 0;
private:
int privateInt = 0;
};
int main(){
    DemoClass  demo;
    
    std::cout << demo.publicInt<<std::endl;
    std::cout << demo.protectedInt<<std::endl;
    std::cout << demo.privateInt<<std::endl;
  return 0;  
}