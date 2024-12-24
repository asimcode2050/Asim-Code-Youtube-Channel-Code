#include <iostream>
#include <vector>

int main()
{ 
  // The main function, where execution starts in any C++ program.

    auto x = 5;
    std::cout << "x is: " << x << std::endl;
    auto y = 3.14;
    std::cout << "y is: " << y << std::endl;
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    for (auto num : numbers)
    {
        std::cout << "Number is: " << num << std::endl;
        
    }

    for (auto it = numbers.begin(); it != numbers.end(); ++it)
    {
        std::cout << "Iterator points to: " << *it << std::endl;
    }

    return 0;
}
