#include <iostream>  // Include the header file for input/output operations
using namespace std; // Use the standard namespace to avoid writing std:: before each standard function or object
int binarySearch(int arr[], int n, int target)
{
    int low = 0;
    int high = n - 1;
    while (low <= high)
    {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target)
        {
            return mid;
        }
        if (arr[mid] < target)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }
    return -1;
}
int main()
{
    int arr[] = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 10;
    int result = binarySearch(arr, n, target);
    if (result != -1)
    {
        cout << "Element found at index " << result << endl; // If found, print the index
    }
    else
    {
        cout << "Element not found in the array" << endl; // If not found, print a not found message
    }
    return 0; // End of the program, return 0 to indicate successful execution
}
