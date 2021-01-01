#include <iostream>
using std::cout;
using std::endl;
using std::cin;

int main()
{
    int n;
    cout<< "Enter 3 numbers between 1 and 50: ";
    for(int i=1;i<=3; ++i){
        cin >> n;
        for (int x = 1;x <= n;++x){
            cout << '*';
        }
        cout <<'\n';
    }
    cout <<endl;
    return 0;
}