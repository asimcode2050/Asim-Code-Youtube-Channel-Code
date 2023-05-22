#include <iostream>
using namespace std;

int main(){
const char* myString ="Hello";
    cout<< "Displaying string using a pointer: ";
    const char* strPtr= myString;
    while(*strPtr){
        cout <<*strPtr;
        strPtr++;
    }
    cout <<endl;
    return 0;
}
