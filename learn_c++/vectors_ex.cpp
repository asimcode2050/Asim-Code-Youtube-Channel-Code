#include <iostream>
#include <vector>
int main()
{
    std::vector<int> numbers;
    numbers.push_back(10);
    numbers.push_back(20);
    numbers.push_back(30);
    std::cout << "The size of the vector is: " << numbers.size() << std::endl;
    std::cout << "First element: " << numbers[0] << std::endl;
    std::cout << "Second element: " << numbers[1] << std::endl;
    std::cout << "Third element: " << numbers[2] << std::endl;
    numbers.pop_back();
    std::cout << "The size of the vector after pop_back() is: " << numbers.size() << std::endl;
    std::cout << "Elements in the vector after removal: ";
    for (int i = 0; i < numbers.size(); i++)
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;
    numbers[0] = 100;
    std::cout << "Vector after modifying the first element: ";
    for (int i = 0; i < numbers.size(); i++)
    {
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}
