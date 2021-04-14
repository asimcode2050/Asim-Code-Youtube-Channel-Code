// https://youtu.be/uTVWrYS6Tfo
#include <iostream>
#include <string>
using namespace std;

string replaceStr(string orig_str, const string& replace_string, const string& with_string){
    size_t pos = orig_str.find(replace_string);
    if(pos != std::string::npos)
        orig_str.replace(pos, replace_string.length(),with_string);
    return orig_str;
    }

int main(){
    string orig = "This is a testing";
    string rep = "testing";
    string wit ="test";
    cout << replaceStr(orig,rep,wit) << endl;
    return 0;
}
