#include <iostream>
#include<fstream>
#include<vector>
#include<iterator>
using namespace std;
int main(){
   ifstream file("infile.txt");
   vector<string>v;
   string str;
   while(file >> str){
       v.push_back(str);
   }
copy(v.begin(),v.end(),ostream_iterator<string>(cout,"\n"));

 
    return 0;
}