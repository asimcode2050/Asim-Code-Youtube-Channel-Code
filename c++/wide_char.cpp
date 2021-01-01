#include <iostream>
using namespace std;
int main(){
    setlocale(LC_ALL,"");
    const wchar_t chinese_message[] =L"你好，世界";
    const wchar_t hebrew_message[] = L"שלום עולם";
    const wchar_t tamil_message[] = L"ஹலோ உலகம்";
    wcout <<chinese_message<<endl;
    wcout <<hebrew_message<<endl;
    wcout <<tamil_message<<endl;
    
    return 0;

    }