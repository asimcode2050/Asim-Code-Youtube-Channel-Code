#include <iostream>
#include <fstream>
#include <string>
int main()
{
    std::string fileName = "example.txt";
    std::ifstream inputFile(fileName);
    if (!inputFile)
    { // If 'inputFile' failed to open (false condition), then:
        std::cerr << "Error: Could not open the file " << fileName << std::endl;
        return 1;
    }
    std::string line;
    while (getline(inputFile, line))
    { // Loop continues as long as 'getline' reads a line successfully
        std::cout << line << std::endl;
    }
    inputFile.close();
    return 0;
}
