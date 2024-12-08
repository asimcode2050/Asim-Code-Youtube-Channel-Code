#include <iostream>
#include <string>
int main()
{
    std::string message = "Hello, world!";
    std::cout << "Original message: " << message << std::endl;
    size_t messageLength = message.length();
    std::cout << "Length of the message: " << messageLength << std::endl;
    message += " How are you today?";
    std::cout << "Updated message: " << message << std::endl;
    size_t position = message.find("world");
    if (position != std::string::npos)
    {
        std::cout << "'world' found at position: " << position << std::endl;
    }
    else
    {
        std::cout << "'world' not found in the message." << std::endl;
    }
    std::string substring = message.substr(7, 5);
    std::cout << "Extracted substring: " << substring << std::endl;
    size_t worldPos = message.find("world");
    if (worldPos != std::string::npos)
    {
        message.replace(worldPos, 5, "everyone");
    }
    std::cout << "Final message after replacement: " << message << std::endl;
    return 0;
}
