#include<iostream>
#include<iterator>
#include<vector>
#include<iomanip>
int main(){
    std::vector<int> v ={4,5,6};
    std::cout <<std::setprecision(3);
    std::fixed(std::cout);
    std::copy(v.begin(),v.end(), std::ostream_iterator<float>(std::cout,"!"));
    std::cout<<std::endl;
   
    return 0;
}