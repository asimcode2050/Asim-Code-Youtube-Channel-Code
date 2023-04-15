/*
Singly linked list in C++
https://youtu.be/PVAmSCbKsa0
YouTube: Asim Code
*/
#include <iostream>
#include <cstdlib>
using namespace std;
// HEAD ->[data][next]->[data][next]->[data][next]->NULL
struct Node
{
    int data;
    struct Node *next;
};
struct Node *head = NULL;

// 3 -> 5 -> 2 -> NULL
void insert(int data)
{
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->next = head;
    head = new_node;
}

void printList()
{
    struct Node *ptr;
    ptr = head;
    while (ptr != NULL)
    {
        cout << ptr->data << " ";
        ptr = ptr->next;
    }
}
int main(void)
{
    insert(2);
    insert(5);
    insert(3);
    printList();

    return 0;
}
