#include<sstream>
#include<string>
#include<iostream>
using namespace std;
int main(){
    ostringstream ss;
    ss<< "Some text:" <<100;
    const string result = ss.str();
    cout <<result<<endl;
    return 0;
}