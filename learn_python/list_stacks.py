'''
stack = [] initializes an empty stack

stack.append(1) adds an item to the stack

 stack.pop() removes and returns the most recently added item
 '''
stack = []
stack.append(1)
stack.append(2)
stack.append(3)  # The append() function adds the integer 3 to the 'stack'.
top_element = stack.pop()
print(top_element)
next_element = stack.pop()
print(next_element)  # Output: 2, because we popped 2 from the stack.
final_element = stack.pop()
print(final_element)
'''
- 'stack' is a list that holds the elements. Its type is 'list'.
- The append() method is used to add items to the list (stack). The argument for append() is the element to be added.
- The pop() method is used to remove the last element added to the list (stack). pop() returns the element being removed.
- Variables like 'top_element', 'next_element', and 'final_element' hold the values returned by pop().
'''
