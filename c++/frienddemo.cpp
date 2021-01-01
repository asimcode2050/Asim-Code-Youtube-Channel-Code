#include <iostream>
using namespace std;
class Counter{
    friend void setNum(Counter&, int);
    public:
    int getNum() const {return num;}
    private :
    int num{0};
};
void setNum(Counter& c, int n){
    c.num = n;
}

int main(){
 Counter counter ;
 cout << "Counter.num after instattiation: "<<counter.getNum()<<endl;
 setNum(counter,10);
 cout << "counter.num after call to setNum friend function: "
 << counter.getNum() << endl;
    return 0;
}

