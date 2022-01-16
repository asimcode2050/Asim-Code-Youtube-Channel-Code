/*
How to count the number of occurrences of each word in a text file in C++ Counting word frequencies
Please Subscribe to Asim Code.
YouTube Channel: Asim Code
https://youtu.be/t-I0Q26HVRE
*/
#include <iostream>
#include <fstream>
#include <map>
#include <string>
typedef std::map<std::string, int> StringIntMap;
void count_words(std::istream &in, StringIntMap &words)
{
    std::string text;
    while (in >> text)
    {
        ++words[text];
    }
}

int main(int argc, char **argv)
{
    std::ifstream in("readme.txt");
    StringIntMap words_map;
    count_words(in, words_map);

    for (StringIntMap::iterator it = words_map.begin(); it != words_map.end(); ++it)
    {
        std::cout << it->first << " occured " << it->second << std::endl;
    }
}
