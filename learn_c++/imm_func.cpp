#include <iostream>
#include <functional>
#include <cmath>
int main()
{
    auto result = []()
    {
        std::cout << "This lambda function is executed immediately upon definition." << std::endl;
        return 42;
    }();

    std::cout << "The result of the immediate function is: " << result << std::endl;
    auto sum = [](int a, int b)
    {
        std::cout << "This lambda function adds two integers." << std::endl;
        return a + b;
    }(5, 7);
    std::cout << "The sum of 5 and 7 is: " << sum << std::endl;
    std::function<int(int, int)> multiply = [](int x, int y)
    {
        std::cout << "Multiplying two numbers immediately." << std::endl;
        return x * y;
    };
    auto product = multiply(4, 6);
    std::cout << "The product of 4 and 6 is: " << product << std::endl;
    return 0;
}
