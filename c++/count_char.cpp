#include <iostream>
using namespace std;

int main()
{
    enum
    {
        L_IN_ALPHA = 26
    };
    int freqOfLetters[L_IN_ALPHA] = {};
    while (cin)
    {
        char ch;
        cin >> ch;
        ch = toupper(ch);
        if (cin)
            if (isalpha(ch))
                ++freqOfLetters[ch - 'A'];
    }
    cout << "Requencies :\n";
    cout << "Letter\t Frequency\n";
    for (char ch = 'A'; ch <= 'Z'; ++ch)
        cout << ch << '\t' << freqOfLetters[ch - 'A'] << '\n';

    return 0;
}
