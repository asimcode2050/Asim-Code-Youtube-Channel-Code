#include <iostream>
#include <set>
int main()
{
    std::set<int> ourset = {30,-10,5,8,9,6,25};
    int value = 6;
    auto found = ourset.find(value);
    if(found != ourset.end())
    {
        std::cout << "We found it! deleting the value ..."<<'\n';
        ourset.erase(found);
        std::cout<< "Value deleted."<< '\n';
    }
    else {
        std::cout << "Value not found."<<'\n';
    }

    for(auto element : ourset)
    {
        std::cout << element << '\n';
    }

}
