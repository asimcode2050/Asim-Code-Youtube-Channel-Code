/*
https://youtu.be/ECqNBqOGkuo
Please Subscribe to Asim Code.
YouTube Channel: Asim Code
*/
#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream f1("f1.txt",ios::binary);
    ofstream f2("f2.txt",ios::binary);
    f2 << f1.rdbuf();
}
