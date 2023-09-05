/*
YouTube: Asim Code
Comparing integers in C++
https://youtu.be/qvbRIv38q24
  */
#include <iostream>
using std::cout;
using std::cin;

int main(){
    int numb1{0};
    int numb2{0};

    cout << "Please enter two integers to compare:";
    cin >> numb1 >> numb2;

    if(numb1 == numb2){
        cout << numb1 << " == " << numb2 << "\n";

    }
    if(numb1 != numb2){
        cout << numb1 << " != " << numb2 << "\n";

    }
    if(numb1 < numb2){
        cout << numb1 << " < " << numb2 << "\n";

    }
    if(numb1 > numb2){
        cout << numb1 << " > " << numb2 << "\n";

    }

    if(numb1 <= numb2){
        cout << numb1 << " <= " << numb2 << "\n";

    }

    if(numb1 >= numb2){
        cout << numb1 << " >= " << numb2 << "\n";

    }

  
}
