#include <fstream>
#include <iostream>
using namespace std;
int main()
{
    ofstream outFile("example.txt");
    if (outFile.is_open())
    {
        outFile << "Hello, World!";
        outFile.close(); // Closes the file after we are done writing to it.
    }
    else
    {
        cout << "Error opening file." << endl;
    }
    return 0;
}
