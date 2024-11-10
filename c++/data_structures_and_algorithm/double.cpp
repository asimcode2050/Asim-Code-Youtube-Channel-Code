
#include <iostream>
using namespace std;
struct Node
{
    int data;
    Node *next;
    Node *prev;
    Node(int value) : data(value), next(nullptr), prev(nullptr) {}
};
class DoublyLinkedList
{
private:
    Node *head;
    Node *tail;

public:
    DoublyLinkedList() : head(nullptr), tail(nullptr) {}
    void insertAtBeginning(int value)
    {
        Node *newNode = new Node(value);
        if (head == nullptr)
        {
            head = tail = newNode;
        }
        else
        {
            newNode->next = head;
            head->prev = newNode;
            head = newNode;
        }
    }
    void insertAtEnd(int value)
    {
        Node *newNode = new Node(value);
        if (tail == nullptr)
        {
            head = tail = newNode;
        }
        else
        {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }
    void deleteFirst()
    {
        if (head == nullptr)
            return;
        Node *temp = head;
        head = head->next;
        if (head != nullptr)
        {
            head->prev = nullptr;
        }
        else
        {
            tail = nullptr;
        }
        delete temp;
    }
    void deleteLast()
    {
        if (tail == nullptr)
            return;
        Node *temp = tail;
        tail = tail->prev;
        if (tail != nullptr)
        {
            tail->next = nullptr;
        }
        else
        {
            head = nullptr;
        }
        delete temp;
    }
    void printForward()
    {
        Node *temp = head;
        while (temp != nullptr)
        {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
    void printBackward()
    {
        Node *temp = tail;
        while (temp != nullptr)
        {
            cout << temp->data << " ";
            temp = temp->prev;
        }
        cout << endl;
    }
    ~DoublyLinkedList()
    {
        while (head != nullptr)
        {
            deleteFirst();
        }
    }
};
int main()
{
    DoublyLinkedList list;      // Create a new doubly linked list
    list.insertAtBeginning(10); // Insert 10 at the beginning
    list.insertAtEnd(20);       // Insert 20 at the end
    list.insertAtBeginning(5);  // Insert 5 at the beginning
    list.insertAtEnd(30);       // Insert 30 at the end
    cout << "List printed forward: ";
    list.printForward(); // Output the list from start to end
    cout << "List printed backward: ";
    list.printBackward(); // Output the list from end to start
    list.deleteFirst();   // Delete the first node (5)
    cout << "After deleting first node, list: ";
    list.printForward(); // Output after deletion
    list.deleteLast();   // Delete the last node (30)
    cout << "After deleting last node, list: ";
    list.printForward(); // Output after deletion
    return 0;            // End of the program
}
