#include <stdio.h>
#include <stdlib.h>
#define MAX 5
struct Stack
{
    int arr[MAX];
    int top;
};

void initStack(struct Stack *s)
{
    s->top = -1;
    printf("Stack Initialized!\n");
}

int isFull(struct Stack *s)
{
    if (s->top == MAX - 1)
    {
        return 1; 
    }
    return 0;
}

int isEmpty(struct Stack *s)
{
    if (s->top == -1)
    {
        return 1;
    }
    return 0;
}

void push(struct Stack *s, int value)
{
    if (isFull(s))
    {
        printf("Error: Stack Overflow! Can't push %d\n", value);
    }
    else
    {
        s->arr[++(s->top)] = value;
        printf("Pushed %d onto the stack\n", value);
    }
}

int pop(struct Stack *s)
{
    if (isEmpty(s))
    {
        printf("Error: Stack Underflow! Can't pop from empty stack\n");
        return -1;
    }
    else
    {
        int value = s->arr[s->top--];
        printf("Popped %d from the stack\n", value);
        return value;
    }
}

int peek(struct Stack *s)
{
    if (isEmpty(s))
    {
        printf("Error: Stack is empty! Nothing to peek\n");
        return -1;
    }
    else
    {
        return s->arr[s->top];
    }
}

int main()
{
    struct Stack myStack;
    initStack(&myStack);
    push(&myStack, 10);
    push(&myStack, 20);
    push(&myStack, 30);
    push(&myStack, 40);
    push(&myStack, 50);
    push(&myStack, 60);
    int topValue = peek(&myStack);
    if (topValue != -1)
    {
        printf("Top element is: %d\n", topValue);
    }

    pop(&myStack);
    pop(&myStack);
    pop(&myStack);

    pop(&myStack);
    pop(&myStack);
    pop(&myStack);
    return 0;
}
