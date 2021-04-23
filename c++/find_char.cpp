// https://youtu.be/stzVv7RAAO4
#include <iostream>
#include <string>

int main(){
    std::string text = "C++ Hello World.";
    char c = 'H';
    auto charFound = text.find(c);
    if(charFound != std::string::npos){
        std::cout << "Character Found At : " << charFound << '\n';
    }
    else{
        std::cout << "Character was not found." << '\n';
    }
    return 0;
}
