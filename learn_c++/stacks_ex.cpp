#include <iostream>
#include <stack>
int main()
{
    std::stack<int> myStack;
    myStack.push(10);
    myStack.push(20);
    myStack.push(30);
    std::cout << "Top element: " << myStack.top() << std::endl;
    myStack.pop();
    std::cout << "New top element after popping: " << myStack.top() << std::endl;
    myStack.pop();
    myStack.pop();
    if (myStack.empty())
    {
        std::cout << "The stack is now empty." << std::endl;
    }
    return 0;
}
