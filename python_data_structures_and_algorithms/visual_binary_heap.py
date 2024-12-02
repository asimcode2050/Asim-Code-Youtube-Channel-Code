import matplotlib.pyplot as plt
import networkx as nx

class MinHeap:
    def __init__(self):
        self.heap = []

    def visualize(self):
        G = nx.DiGraph()
        labels = {}
        for i in range(len(self.heap)):
            G.add_node(i, label=str(self.heap[i]))
            if 2 * i + 1 < len(self.heap):  # Left child index = 2*i + 1
                G.add_edge(i, 2 * i + 1)
            if 2 * i + 2 < len(self.heap):  # Right child index = 2*i + 2
                G.add_edge(i, 2 * i + 2)
            labels[i] = str(self.heap[i])
        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, labels=labels,
                node_size=2000, node_color="skyblue", font_size=10)
        plt.title("Binary Heap Visualization")
        plt.show()

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)
        self.visualize()

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] <= self.heap[index]:
                break
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index

    def extract_min(self):
        if len(self.heap) == 0:
            return None  # Return None if the heap is empty.
        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()  # Remove the last element since it is now at the root.
        self._bubble_down(0)
        self.visualize()  # Visualize the heap structure after the extraction.
        return min_value  # Return the removed minimum value.

    def _bubble_down(self, index):
        left_child_index = 2 * index + 1  # Left child index in a binary heap.
        right_child_index = 2 * index + 2
        smallest = index  # Assume that the current node is the smallest.
        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self._bubble_down(smallest)


heap = MinHeap()  # Create a new MinHeap object.
heap.insert(10)  # Insert 10 into the heap.
heap.insert(20)  # Insert 20 into the heap.
heap.insert(5)   # Insert 5 into the heap (this will become the root).
heap.insert(30)  # Insert 30 into the heap.
heap.insert(15)  # Insert 15 into the heap.
heap.extract_min()
