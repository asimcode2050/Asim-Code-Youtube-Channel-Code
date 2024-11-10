#include <iostream>
using namespace std;
#define N 9
void printGrid(int grid[N][N])
{
    for (int row = 0; row < N; row++)
    {
        for (int col = 0; col < N; col++)
        {
            cout << grid[row][col] << " "; // Print each element in the row
        }
        cout << endl; // New line after each row
    }
}
bool isSafe(int grid[N][N], int row, int col, int num)
{
    for (int x = 0; x < N; x++)
    {
        if (grid[row][x] == num)
        {
            return false; // Number found in the row
        }
    }
    for (int x = 0; x < N; x++)
    {
        if (grid[x][col] == num)
        {
            return false; // Number found in the column
        }
    }
    int startRow = row - row % 3, startCol = col - col % 3;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (grid[i + startRow][j + startCol] == num)
            {
                return false; // Number found in the 3x3 grid
            }
        }
    }
    return true; // Safe to place the number
}
bool solveSudoku(int grid[N][N])
{
    int row, col;
    bool empty = false;
    for (row = 0; row < N; row++)
    {
        for (col = 0; col < N; col++)
        {
            if (grid[row][col] == 0)
            { // Found an empty cell
                empty = true;
                break;
            }
        }
        if (empty)
            break; // Break outer loop if empty cell is found
    }
    if (!empty)
    {
        return true;
    }
    for (int num = 1; num <= 9; num++)
    {
        if (isSafe(grid, row, col, num))
        {
            grid[row][col] = num; // Place the number
            if (solveSudoku(grid))
            {
                return true; // Puzzle solved
            }
            grid[row][col] = 0;
        }
    }
    return false; // Trigger backtracking if no number fits
}
int main()
{
    int grid[N][N] = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}};
    if (solveSudoku(grid))
    {
        cout << "Sudoku puzzle solved!" << endl;
        printGrid(grid); // Print the solved Sudoku grid
    }
    else
    {
        cout << "No solution exists for this Sudoku puzzle!" << endl;
    }
    return 0;
}
