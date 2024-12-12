#include <iostream>
#include <map>
int main()
{
    std::map<std::string, int> studentScores;
    studentScores["Alice"] = 85;
    studentScores["Bob"] = 90;
    studentScores["Charlie"] = 88;
    std::cout << "Student Scores:\n"; // Print the header.
    for (auto it = studentScores.begin(); it != studentScores.end(); ++it)
    {
        std::cout << it->first << ": " << it->second << std::endl;
    }
    std::string searchStudent = "Bob";
    auto searchResult = studentScores.find(searchStudent);
    if (searchResult != studentScores.end())
    {
        std::cout << "\n"
                  << searchStudent << "s score is: " << searchResult->second << std::endl;
    }
    else
    {
        std::cout << "\n"
                  << searchStudent << " was not found in the map." << std::endl;
    }
    std::string studentToRemove = "Charlie";
    studentScores.erase(studentToRemove);
    std::cout << "\nUpdated Student Scores:\n";
    for (auto it = studentScores.begin(); it != studentScores.end(); ++it)
    {
        std::cout << it->first << ": " << it->second << std::endl;
    }
    return 0;
}
