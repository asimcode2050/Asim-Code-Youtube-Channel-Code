
class Node {

    int data;
    Node next;
    Node prev;

    public Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class CircularDoublyLinkedList {

    private Node head;

    public CircularDoublyLinkedList() {
        head = null;     // Initially, the list is empty

    }

    public boolean isEmpty() {
        return head == null;
    }

    public void insertAtEnd(int data) {
        Node newNode = new Node(data);
        if (isEmpty()) {
            head = newNode;
            newNode.next = newNode;
            newNode.prev = newNode;
        } else {
            Node tail = head.prev;
            tail.next = newNode;
            newNode.prev = tail;
            newNode.next = head;
            head.prev = newNode;
        }
    }

    public void displayForward() {
        if (isEmpty()) {
            System.out.println("List is empty.");
            return;
        }
        Node current = head;
        do {
            System.out.print(current.data + " "); // Print the current node's data
            current = current.next;              // Move to the next node

        } while (current != head);               // Stop when back to the head

        System.out.println();
    }

    public void displayBackward() {
        if (isEmpty()) {
            System.out.println("List is empty.");
            return;
        }
        Node tail = head.prev;
        Node current = tail;
        do {
            System.out.print(current.data + " "); // Print the current node's data

            current = current.prev; // Move to the previous node

        } while (current != tail);               // Stop when back to the tail

        System.out.println();
    }

    public void deleteByValue(int value) {
        if (isEmpty()) {

            System.out.println("List is empty. Deletion not possible.");
            return;
        }
        Node current = head;
        do {

            if (current.data == value) { // Check if the current node holds the value

                if (current == head && current.next == head) {

                    head = null; // Set head to null

                } else {
                    Node prevNode = current.prev;

                    Node nextNode = current.next;

                    prevNode.next = nextNode;
                    nextNode.prev = prevNode;
                    if (current == head) {
                        head = nextNode;

                    }
                }
                System.out.println("Deleted node with value " + value);
                return; // Exit after deletion

            }
            current = current.next;

        } while (current != head);
        System.out.println("Value " + value + " not found in the list.");
    }

}

public class Main {

    public static void main(String[] args) {
        CircularDoublyLinkedList list = new CircularDoublyLinkedList();
        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        list.insertAtEnd(40);

        System.out.println("List in forward direction:");
        list.displayForward();
        System.out.println("List in backward direction:");
        list.displayBackward();
        System.out.println("Deleting value 20:");
        list.deleteByValue(20);

        System.out.println("List in forward direction after deletion:");
        list.displayForward();
    }

}


