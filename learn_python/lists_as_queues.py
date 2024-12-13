queue = []  # 'queue' is a variable holding an empty list.
queue.append('apple')
queue.append('banana')  # Similarly, 'banana' is added to the end of the list.
queue.append('cherry')  # Now, 'cherry' is appended to the queue.
print("Queue after enqueuing elements:", queue)
first_item = queue.pop(0)
print("Removed item:", first_item)
print("Queue after dequeuing one item:", queue)
second_item = queue.pop(0)
print("Removed item:", second_item)
print("Queue after dequeuing one item:", queue)
third_item = queue.pop(0)
print("Removed item:", third_item)
print("Queue after dequeuing all items:", queue)
