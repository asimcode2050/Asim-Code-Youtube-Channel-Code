// https://youtu.be/qxVdQ9wI-WE
#include <iostream>
#include <vector>
#include<list>
using namespace std;
int main(){
   vector<int> v1{1,2,3,4,5};
   vector<int> v2(3,1); //{1,1,1}
   vector<int> v3(3); // v3 {0,0,0}
   vector<int> v4(v1);
   vector<int> v5 = v2;
   vector<int> v6(std::move(v3));
   vector<int> v7 = std::move(v4);
   vector<int> v8(v1.begin(),v1.begin()+3);
   int a[] = {1,2,3,4,5};
   vector<int> v9(a,a+3); // v9 becomes {1,2,3}
   list<int> mylist{1,2,3};
   vector<int> v10(mylist.begin(),mylist.end());
   v3.assign(3,100); // v3 {100,100,100}
   for(vector<int>::iterator it = v3.begin(); it!= v3.end();++it){
       cout<< *it << " ";
   }
   
    return 0;
}
