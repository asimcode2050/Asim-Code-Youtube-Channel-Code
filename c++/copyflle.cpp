#include<iostream>
#include<fstream>
#include<filesystem>
namespace fs = std::filesystem;
using namespace std;
int main(){
    /*
ifstream src("source_file",std::ios::binary);
ofstream dst("dest_file",std::ios::binary);
dst << src.rdbuf();
*/
fs::create_directory("demo");
std::ofstream("demo/file1.txt").put('x');
fs::copy_file("demo/file1.txt","demo/file2.txt");
std::cout <<"File1.txt Data :" 
 << std::ifstream("demo/file1.txt").rdbuf()<<std::endl;
 std::cout <<"File2.txt Data :" 
 << std::ifstream("demo/file2.txt").rdbuf()<<std::endl;

    return 0;
}