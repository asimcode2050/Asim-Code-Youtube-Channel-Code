
class Node:
    def __init__(self, data):
        self.data = data  # The value/data of the node
        self.next = None  # Initially, the next pointer is set to None


class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty, so head is None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # If the list is empty, new node becomes the head
            self.head = new_node
            return
        last_node = self.head  # Start with the head node
        while last_node.next:  # Traverse the list until the last node
            last_node = last_node.next
        last_node.next = new_node  # Set the next pointer of the last node to the new node

    def prepend(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point the new node's next to the current head
        self.head = new_node  # Update the head to the new node

    def delete(self, data):
        if self.head is None:  # If the list is empty, nothing to delete
            print("Error: The list is empty!")
            return
        if self.head.data == data:
            self.head = self.head.next  # Update the head to the next node
            return
        current_node = self.head
        while current_node.next:  # Traverse the list
            if current_node.next.data == data:  # Found the node to delete
                current_node.next = current_node.next.next  # Bypass the node to delete
                return
            current_node = current_node.next  # Move to the next node
        print(f"Error: {data} not found in the list.")  # If data not found

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True  # Node found
            current_node = current_node.next  # Move to the next node
        return False  # Node not found

    def display(self):
        if self.head is None:
            print("The list is empty.")
            return
        current_node = self.head
        while current_node:  # Traverse until the end of the list
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # Indicates the end of the list


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.prepend(5)
    ll.display()  # Expected Output: 5 -> 10 -> 20 -> 30 -> None
    ll.delete(20)
    ll.display()  # Expected Output: 5 -> 10 -> 30 -> None
    print(ll.search(10))  # Expected Output: True
    print(ll.search(100))  # Expected Output: False
