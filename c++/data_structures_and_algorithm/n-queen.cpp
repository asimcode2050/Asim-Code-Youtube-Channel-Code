#include <iostream>
#include <vector>
using namespace std;
void printSolution(const vector<int> &board, int N)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (board[i] == j)
            {
                cout << "Q "; // Print 'Q' for queen's position
            }
            else
            {
                cout << ". "; // Print '.' for empty space
            }
        }
        cout << endl; // Move to the next row
    }
    cout << endl; // Print an empty line after one solution
}
bool isSafe(const vector<int> &board, int row, int col)
{
    for (int i = 0; i < row; i++)
    {
        if (board[i] == col || board[i] - i == col - row || board[i] + i == col + row)
        {
            return false; // It's unsafe to place the queen
        }
    }
    return true; // It's safe to place the queen
}
void solveNQueen(vector<int> &board, int row, int N)
{
    if (row == N)
    {
        printSolution(board, N);
        return;
    }
    for (int col = 0; col < N; col++)
    {
        if (isSafe(board, row, col))
        {
            board[row] = col; // Place the queen at (row, col)
            solveNQueen(board, row + 1, N);
            board[row] = -1;
        }
    }
}
int main()
{
    int N;
    cout << "Enter the value of N (number of queens): ";
    cin >> N;
    vector<int> board(N, -1);
    cout << "Solutions to the N-Queen problem:" << endl;
    solveNQueen(board, 0, N); // Start solving from the first row

    return 0;
}
