#include <iostream>
#include<fstream>
#include<sstream>
using namespace std;
int main(){
  ifstream f("infile.txt");
  if(f)
  {
   stringstream buffer;
    buffer << f.rdbuf();
    cout << buffer.str();
    f.close();



  }
    return 0;
}