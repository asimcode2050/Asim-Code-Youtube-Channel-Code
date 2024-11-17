class Stack:
    def __init__(self):
        self.items = []  # This list will hold the elements of the stack

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top of the stack:", stack.peek())
    print("Stack size:", stack.size())
    print("Popped item:", stack.pop())
    print("Top of the stack after pop:", stack.peek())
    print("Stack size after pop:", stack.size())  # Should print 2
    print("Popped item:", stack.pop())  # Should print 20
    print("Popped item:", stack.pop())  # Should print 10
    print("Popped item from empty stack:", stack.pop())
