#include <iostream>
#include <vector>
double calculateTotalPrice(const std::vector<double> &prices, double discount)
{
    double total = 0.0;
    for (double price : prices)
    {
        total += price;
    }
    total *= (1 - discount);
    return total;
}
int main()
{
    std::vector<double> cartPrices = {10.99, 25.50, 7.75, 15.30};
    double discount = 0.10;
    double total = calculateTotalPrice(cartPrices, discount);
    std::cout << "Original total: $" << 10.99 + 25.50 + 7.75 + 15.30 << std::endl;
    std::cout << "Total after " << (discount * 100) << "% discount: $" << total << std::endl;
    return 0;
}
