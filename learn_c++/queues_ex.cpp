#include <iostream>
#include <queue>
using namespace std;
int main()
{
    queue<int> orderQueue;
    orderQueue.push(101);
    orderQueue.push(102);
    orderQueue.push(103);
    while (!orderQueue.empty())
    { // The condition checks if the queue is not empty.
        int currentOrder = orderQueue.front();
        cout << "Processing order: " << currentOrder << endl;
        orderQueue.pop();
    }
    cout << "All orders have been processed!" << endl;
    return 0;
}
