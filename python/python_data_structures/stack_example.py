class Node(object):
    def __init__(self,data, next=None):
        self.data = data
        self.next = next
'''
Python Implement a stack with push, pop, peek
https://youtu.be/M9mvKj5kNzk

'''
class Stack(object):

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.peek() is None

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.is_empty())




