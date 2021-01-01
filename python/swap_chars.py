#include<string>
#include <iostream>
#include <cassert>
using namespace std;

bool check_unique(string s){
    char count[128] = {0};
    for(char& c : s){
        assert(c> -1 && c < 128);
        if(count[c]++ == 1)
            return false;
    }
    return true;
}
int main(){
    cout << check_unique("hello")<<endl;
    cout << check_unique("tom")<<endl;
    return 0;
}