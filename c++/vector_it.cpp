// https://youtu.be/bHbCWIyzK-A
#include <iostream>
#include <vector>
using namespace std;
int main(){
 vector <int> v{1,2,3,4,5};
   for(const auto& value: v){
       cout << value << endl;
   }
   for(auto it = begin(v); it!= end(v); ++it){
       cout <<*it << "\n";
   }

   for(size_t i = 0; i< v.size(); ++i){
       cout << v[i] << "\n";
   }

   for(auto rev_it = rbegin(v);rev_it != rend(v); ++rev_it){
       cout << *rev_it << endl;
   }

   for(size_t i =0; i< v.size(); ++i){
       cout << v[v.size()-1-i] << endl;

   }


    return 0;
}
