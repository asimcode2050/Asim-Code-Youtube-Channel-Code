#include <fstream>
#include <iterator>
#include <string>
#include <vector>
using namespace std;
int main(){
   vector<string> my_vector;
   my_vector.push_back("Hello");
   my_vector.push_back("This");
   my_vector.push_back("Is");
   my_vector.push_back("a");
   my_vector.push_back("simple");
   my_vector.push_back("example");
   ofstream out_file("outfile.txt");
   ostream_iterator<string> out_iterator(out_file,"\n");
   copy(my_vector.begin(),my_vector.end(),out_iterator);
   
}