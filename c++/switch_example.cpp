// https://youtu.be/lcY9BOEQE4A
#include <iostream>

int main(){
    int a = 4;
    switch(a)
    {
        case 1:
        std::cout << "The value of a is 1.";
        break;
        case 2:
        std::cout << "The value of a is 2.";
        break;
        case 3:
        std::cout << "The value of a is 3.";
        break;
        case 4:
        std::cout << "The value of a is 4.";
        break;
        case 5:
        std::cout << "The value of a is 5.";
        break;
        default:
        std::cout << "The value is not found.";
        break;

    }
    return 0;
}
