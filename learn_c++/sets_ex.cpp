#include <iostream>
#include <set>
int main()
{
    std::set<int> mySet;
    mySet.insert(10);
    mySet.insert(5);
    mySet.insert(15);
    mySet.insert(10);
    std::cout << "Elements in the set: ";
    for (int num : mySet)
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    if (mySet.find(5) != mySet.end())
    {
        std::cout << "5 is in the set!" << std::endl;
    }
    mySet.erase(5);
    std::cout << "Elements after removing 5: ";
    for (int num : mySet)
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}
