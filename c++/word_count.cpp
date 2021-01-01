#include <iostream>
#include <map>
#include <string>
using namespace std;
int main()
{
    map<string,int> my_map{};
    string word{};
    while(cin >> word){
        ++my_map[word];
    }
    for(auto element : my_map){
        cout<<element.first << '\t' << element.second <<'\n';
    }
}