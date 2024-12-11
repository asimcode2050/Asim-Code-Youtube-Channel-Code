#include <iostream>
#include <stdexcept>
double divide(double numerator, double denominator)
{
    if (denominator == 0)
    {
        throw std::runtime_error("Error: Division by zero is not allowed.");
    }
    return numerator / denominator;
}
int main()
{
    double num1, num2;
    std::cout << "Enter the numerator: ";
    std::cin >> num1;
    std::cout << "Enter the denominator: ";
    std::cin >> num2;
    try
    {
        double result = divide(num1, num2);
        std::cout << "Result: " << result << std::endl;
    }
    catch (const std::exception &e)
    {
        std::cout << e.what() << std::endl;
    }
    return 0;
}
