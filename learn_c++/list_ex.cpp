#include <iostream>
#include <list>
int main()
{
    std::list<int> numbers;
    numbers.push_back(10);
    numbers.push_back(20);
    numbers.push_back(30);
    numbers.push_back(40);
    std::cout << "List after adding elements: ";
    for (int num : numbers)
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    numbers.pop_front();
    std::cout << "List after removing the first element: ";
    for (int num : numbers)
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    numbers.pop_back();
    std::cout << "List after removing the last element: ";
    for (int num : numbers)
    { // Iterate through the updated list (now without the first and last elements).
        std::cout << num << " ";
    }
    std::cout << std::endl;
    numbers.push_front(5);
    std::cout << "List after adding an element at the front: ";
    for (int num : numbers)
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}
