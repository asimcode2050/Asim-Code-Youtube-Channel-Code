/*
YouTube: Asim Code
Number Guessing Game in C++
https://youtu.be/eRhdcNbBDMk
*/
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int min_num = 0;
    int max_num = 0;
    int guess_count = 0;
    int random_num = 0;
    string user_input = "";
    bool is_running = true;

    while (is_running)
    {
        cout << "#### Number guessing game###\n";
        cout << "Please enter number of guesses: ";
        getline(cin, user_input);
        guess_count = stoi(user_input);

        cout << "Please enter minimum number: ";
        getline(cin, user_input);
        min_num = stoi(user_input);

        cout << "Please enter maximum number: ";
        getline(cin, user_input);
        max_num = stoi(user_input);

        srand((unsigned)time(0));
        random_num = rand() % (max_num - min_num + 1) + min_num;
        // cout <<"Random number : "<<random_num<<endl;
        for (int i = 0; i < guess_count; ++i)
        {
            int user_guess = 0;
            cout << "\n Please enter your guess: ";
            getline(cin, user_input);
            user_guess = stoi(user_input);
            if (user_guess == random_num)
            {
                cout << "You guessed the number!\n";
                break;
            }
            int remain_count = guess_count - (i + 1);
            cout << "Your guess was too " << (user_guess < random_num ? "low. " : "high. ");
            cout << "You have " << remain_count << (remain_count > 1 ? " guesses" : " guess") << " remaining";
            cout << "\nPlease enter 0 to exit or any number to play again : ";
            getline(cin, user_input);
            if (stoi(user_input) == 0)
            {
                is_running = false;
            }
        }
    }

    return 0;
}
