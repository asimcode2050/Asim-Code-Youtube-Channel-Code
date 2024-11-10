
import heapq


class MaxPriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, item, priority):
        heapq.heappush(self.heap, (-priority, item))

    def delete_max(self):
        if self.is_empty():
            raise IndexError("delete_max from empty priority queue")
        priority, item = heapq.heappop(self.heap)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        priority, item = self.heap[0]
        return item

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


pq = MaxPriorityQueue()  # Create an instance of the MaxPriorityQueue.
pq.insert("Task 1", 3)  # Insert Task 1 with priority 3.
pq.insert("Task 2", 5)  # Insert Task 2 with priority 5.
pq.insert("Task 3", 1)  # Insert Task 3 with priority 1.
print(pq.peek())  # Output: Task 2 (highest priority).
print(pq.delete_max())  # Output: Task 2 (highest priority item is removed).
print(pq.peek())  # Output: Task 1 (next highest priority).
print(pq.size())  # Output: 2 (remaining elements in the queue).
