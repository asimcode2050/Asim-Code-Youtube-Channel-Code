/*
 1. **Dereferencing (`*`)**:
  The `*it` operation dereferences the iterator, allowing access to the value it points to in the container.

    2. **Incrementing (`++`)**:
     The `++it` operation increments the iterator, moving it to the next element in the container.

       3. **Comparison (`==`, `!=`)**:
        The `it != numbers.end()` operation checks if the iterator has not yet reached the end of the container, allowing the loop to continue iterating through the elements.
         */
#include <iostream>
#include <vector>
int main()
{
    std::vector<int> numbers = {10, 20, 30, 40, 50};
    std::vector<int>::iterator it;
    it = numbers.begin();
    while (it != numbers.end())
    {
        std::cout << *it << " ";
        ++it;
    }
    std::cout << std::endl;
    return 0;
}
