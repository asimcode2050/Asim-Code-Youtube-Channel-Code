#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TABLE_SIZE 10
typedef struct Node
{
    char *key;
    int value;
    struct Node *next;
} Node;

typedef struct HashTable
{
    Node *table[TABLE_SIZE];
} HashTable;

unsigned int hash(char *key)
{
    unsigned int hashValue = 0;
    while (*key)
    {
        hashValue = (hashValue << 5) + *key++;
    }

    return hashValue % TABLE_SIZE;
}
Node *createNode(char *key, int value)
{
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->key = strdup(key);
    newNode->value = value;
    newNode->next = NULL;
    return newNode;
}

HashTable *createHashTable()
{
    HashTable *hashTable = (HashTable *)malloc(sizeof(HashTable));

    for (int i = 0; i < TABLE_SIZE; i++)
    {
        hashTable->table[i] = NULL;
    }
    return hashTable;
}

void insert(HashTable *hashTable, char *key, int value)
{
    unsigned int index = hash(key);
    Node *newNode = createNode(key, value);
    if (hashTable->table[index] == NULL)
    {
        hashTable->table[index] = newNode;
    }
    else
    {
        Node *current = hashTable->table[index];
        while (current != NULL)
        {
            if (strcmp(current->key, key) == 0)
            {
                current->value = value;
                free(newNode->key);
                free(newNode);
                return;
            }
            current = current->next;
        }

        newNode->next = hashTable->table[index];
        hashTable->table[index] = newNode;
    }
}

int get(HashTable *hashTable, char *key)
{
    unsigned int index = hash(key);
    Node *current = hashTable->table[index];

    while (current != NULL)
    {
        if (strcmp(current->key, key) == 0)
        {
            return current->value;
        }
        current = current->next;
    }

    printf("Key '%s' not found!\n", key);
    return -1;
}

void delete(HashTable *hashTable, char *key)
{
    unsigned int index = hash(key);
    Node *current = hashTable->table[index];
    Node *prev = NULL;
    while (current != NULL)
    {
        if (strcmp(current->key, key) == 0)
        {
            if (prev == NULL)
            {
                hashTable->table[index] = current->next;
            }
            else
            {
                prev->next = current->next;
            }
            free(current->key);
            free(current);
            return;
        }
        prev = current;
        current = current->next;
    }
    printf("Key '%s' not found!\n", key);
}

void printHashTable(HashTable *hashTable)
{
    for (int i = 0; i < TABLE_SIZE; i++)
    {
        Node *current = hashTable->table[i];

        if (current != NULL)
        {
            printf("Bucket %d: ", i);
            while (current != NULL)
            {
                printf("{%s: %d} -> ", current->key, current->value);
                current = current->next;
            }
            printf("NULL\n"); // Mark the end of the list.
        }
    }
}

int main()
{
    HashTable *myHashTable = createHashTable();

    insert(myHashTable, "apple", 10);
    insert(myHashTable, "banana", 20);
    insert(myHashTable, "grape", 30);

    printHashTable(myHashTable);

    printf("Value for 'apple': %d\n", get(myHashTable, "apple"));
    printf("Value for 'banana': %d\n", get(myHashTable, "banana"));

    delete (myHashTable, "banana");
    printf("After deleting 'banana':\n");
    printHashTable(myHashTable);

    return 0; // End of the program.
}
