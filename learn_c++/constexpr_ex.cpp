#include <iostream>
constexpr int factorial(int n)
{
    if (n <= 1)
    {
        return 1;
    }
    return n * factorial(n - 1);
}

int main()
{
    constexpr int value = factorial(5);
    std::cout << "Factorial of 5 is: " << value << std::endl;
    int n = 6;
    int result = factorial(n);
    std::cout << "Factorial of " << n << " is: " << result << std::endl;
        return 0;
}
