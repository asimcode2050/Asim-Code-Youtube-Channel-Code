#include <iostream>
using namespace std;

int main()
{
    int x = 5;
    int& xr = x;
    cout <<"x = "<<x <<", xr= "<<xr<<endl;
    xr = xr + 10;
    cout <<"x = "<<x <<", xr= "<<xr<<endl;
    return 0;
}
