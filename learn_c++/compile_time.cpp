#include <iostream>
constexpr int maxValue = 100;
constexpr int calculateSum(int a, int b)
{
    return a + b;
}
int main()
{
    constexpr int result = calculateSum(10, 20);

    std::cout << "The sum is: " << result << std::endl;
    return 0; 
}
