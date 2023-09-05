#include <iostream>

int main(){
    int numb1{0};
    int numb2{0};
    int sum{0};
    std::cout << "Please enter first integer: ";
    std::cin >> numb1;
    std::cout << "Please enter second integer: ";
    std::cin >> numb2;
    sum = numb1 + numb2;
    std::cout << "Sum is : "<< sum << "\n";
    
}
