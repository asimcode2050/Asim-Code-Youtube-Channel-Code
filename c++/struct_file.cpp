#include<iostream>
#include<vector>
#include<fstream>
struct person_type
{
    std::string name;
    int age;
  friend std::istream& operator>>(std::istream& is, person_type& person){
      is >>std::ws;
      std::getline(is,person.name);
      is >> person.age;
      return is;
  }

};

int main(){
    auto file = std::ifstream("p.txt");
    std::vector<person_type> v;
    for(person_type person; file >> person;){
        v.push_back(person);
    }
    for(auto const& person:v)
{
    std::cout<< "Person Name: "<<person.name<<std::endl;
    std::cout<<"Person Age: "<<person.age<<std::endl;
    std::cout<<std::endl;
}    return 0;
}