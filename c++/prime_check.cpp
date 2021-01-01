#include <iostream>
#include <string>
using namespace std;

int main(){
    int number =0;
    cout <<"Enter the number to check:";
    cin >> number;
    if(number <=1){
        cout << "Number is not prime.";
        return 0;
    }
    else if(number == 2){
        cout << "Number is prime.";
        return 0;
    }
    for(int i=2;i<number ; ++i){
        if(number %i ==0){
            cout <<"Number is not prime.";
            return 0;
        }
    }
    cout << "Number is prime :"<<number<<endl; 
}