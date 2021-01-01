#include <iostream>
#include <string>
class Increment{
   int x {0};
   public:
   void IncrementX(){
       x++;
       std::cout<<"X: "<<x<<std::endl;
   };
};
int main(){
    Increment inc;
    inc.IncrementX();
    return 0;
}