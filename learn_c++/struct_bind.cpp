#include <iostream>
#include <tuple>
int main()
{
    std::tuple<int, double, std::string> myTuple = {10, 3.14, "Hello, world!"};

    auto [x, y, z] = myTuple;
    std::cout << "x = " << x << std::endl;
    std::cout << "y = " << y << std::endl;
    std::cout << "z = " << z << std::endl;
    return 0;
}
