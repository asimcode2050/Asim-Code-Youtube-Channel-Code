#include <iostream>
using namespace std;

int main(){
    int arr[10]{1,5,10,20,30,40,50,60,70,80};
    int *p = nullptr;
    p = &arr[2];
    cout <<"*p"<<*p<<",arr[2] = "<<arr[2]<<endl;
    cout <<p[3]<< " == "<<arr[5]<<endl;
    return 0;
}