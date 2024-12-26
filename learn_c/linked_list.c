#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *next;
};

void insertAtBeginning(struct Node **head, int newData)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    if (newNode == NULL)
    {
        printf("Memory allocation failed. Exiting...\n");
        return;
    }

    newNode->data = newData;

    newNode->next = *head;
    *head = newNode;
    printf("Inserted %d at the beginning.\n", newData);
}

void printList(struct Node *head)
{
    struct Node *temp = head;
    while (temp != NULL)
    {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

int main()
{
    struct Node *head = NULL;

    insertAtBeginning(&head, 10); // List: 10 -> NULL
    insertAtBeginning(&head, 20); // List: 20 -> 10 -> NULL
    insertAtBeginning(&head, 30); // List: 30 -> 20 -> 10 -> NULL
    insertAtBeginning(&head, 40); // List: 40 -> 30 -> 20 -> 10 -> NULL
    printf("Current Linked List: ");
    printList(head); // Should print: 40 -> 30 -> 20 -> 10 -> NULL

    return 0;
}
