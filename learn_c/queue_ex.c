#include <stdio.h>
#include <stdlib.h>
#define MAX 5
struct Queue
{
    int items[MAX];
    int front;
    int rear;
};

void initializeQueue(struct Queue *q)
{
    q->front = -1;
    q->rear = -1;
    printf("Queue has been initialized!\n");
}

int isFull(struct Queue *q)
{
    if (q->rear == MAX - 1)
    {
        printf("Queue is full! Cannot enqueue.\n");
        return 1;
    }
    return 0;
}

int isEmpty(struct Queue *q)
{
    if (q->front == -1)
    {
        printf("Queue is empty! Cannot dequeue.\n");
        return 1; 
    }
    return 0;
}
void enqueue(struct Queue *q, int value)
{
    if (isFull(q))
    {
        return; 
    }

    if (q->front == -1)
    {
        q->front = 0; 
    }

    q->rear++;
    q->items[q->rear] = value;
    printf("Enqueued %d to the queue.\n", value);
}

int dequeue(struct Queue *q)
{
    if (isEmpty(q))
    {
        return -1;
    }

    int dequeuedValue = q->items[q->front];

    if (q->front == q->rear)
    {
        q->front = -1;
        q->rear = -1;
    }
    else
    {
        q->front++;
    }

    printf("Dequeued %d from the queue.\n", dequeuedValue);
    return dequeuedValue;
}

int peek(struct Queue *q)
{
    if (isEmpty(q))
    {
        return -1; 
    }

    printf("The front element is %d.\n", q->items[q->front]);
    return q->items[q->front];
}


void display(struct Queue *q)
{
    if (isEmpty(q))
    {
        return;
    }

    printf("Queue elements: ");
    for (int i = q->front; i <= q->rear; i++)
    {
        printf("%d ", q->items[i]);
    }
    printf("\n");
}


int main()
{
    struct Queue q;
    initializeQueue(&q);
    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);
    enqueue(&q, 40);
    enqueue(&q, 50);
    enqueue(&q, 60);
    display(&q);

    peek(&q);

    dequeue(&q);
    dequeue(&q);

    display(&q);

    return 0;
}


