#include <iostream>
using namespace std;
enum Color
{
    RED,
    BLACK
};

struct Node
{
    int data;
    Node *parent;
    Node *left;
    Node *right;
    Color color;
    Node(int value) : data(value), parent(nullptr), left(nullptr), right(nullptr), color(RED) {}
};

class RedBlackTree
{
private:
    Node *root;
    void leftRotate(Node *x)
    {
        cout << "Performing Left Rotate on node with data: " << x->data << endl;
        Node *y = x->right;
        x->right = y->left;

        if (y->left != nullptr)
        {
            y->left->parent = x;
        }

        y->parent = x->parent;
        if (x->parent == nullptr)
        {
            root = y;
        }
        else if (x == x->parent->left)
        {
            x->parent->left = y;
        }
        else
        {
            x->parent->right = y; 
        }

        y->left = x;
        x->parent = y; 
    }

    void rightRotate(Node *y)
    {
        cout << "Performing Right Rotate on node with data: " << y->data << endl;

        Node *x = y->left;
        y->left = x->right;

        if (x->right != nullptr)
        {
            x->right->parent = y;
        }

        x->parent = y->parent; 
        if (y->parent == nullptr)
        {
            root = x; 
        }
        else if (y == y->parent->left)
        {
            y->parent->left = x;
        }
        else
        {
            y->parent->right = x; 
        }

        x->right = y;
        y->parent = x;
    }

    void fixInsert(Node *k)
    {
        while (k != root && k->parent->color == RED)
        {
            if (k->parent == k->parent->parent->left)
            {
                Node *uncle = k->parent->parent->right;
                if (uncle != nullptr && uncle->color == RED)
                {
                    cout << "Case 1: Recoloring" << endl;
                    k->parent->color = BLACK;
                    uncle->color = BLACK;
                    k->parent->parent->color = RED;
                    k = k->parent->parent;  
                }
                else
                {
                    if (k == k->parent->right)
                    {
                        cout << "Case 2: Left Rotate" << endl;
                        k = k->parent;
                        leftRotate(k); 
                    }

                    cout << "Case 3: Right Rotate" << endl;
                    k->parent->color = BLACK;
                    k->parent->parent->color = RED;
                    rightRotate(k->parent->parent);
                }
            }
            else
            {
                Node *uncle = k->parent->parent->left;

                if (uncle != nullptr && uncle->color == RED)
                {
                    cout << "Case 1: Recoloring" << endl;
                    k->parent->color = BLACK;
                    uncle->color = BLACK;
                    k->parent->parent->color = RED;
                    k = k->parent->parent;
                }
                else
                {
                    if (k == k->parent->left)
                    {
                        cout << "Case 2: Right Rotate" << endl;
                        k = k->parent;
                        rightRotate(k);
                    }

                    cout << "Case 3: Left Rotate" << endl;
                    k->parent->color = BLACK;
                    k->parent->parent->color = RED;
                    leftRotate(k->parent->parent);
                }
            }
        }

        root->color = BLACK;
    }

    void insert(int value)
    {
        Node *newNode = new Node(value);
        Node *y = nullptr;
        Node *x = root;

        while (x != nullptr)
        {
            y = x;
            if (newNode->data < x->data)
            {
                x = x->left;
            }
            else
            {
                x = x->right; 
            }
        }

        newNode->parent = y; 
        if (y == nullptr)
        {
            root = newNode;
        }
        else if (newNode->data < y->data)
        {
            y->left = newNode; 
        }
        else
        {
            y->right = newNode; 
        }

        fixInsert(newNode); 
    }

public:
    RedBlackTree() : root(nullptr) {}

    void insertNode(int value)
    {
        insert(value); 
    }

    void display(Node *root)
    {
        if (root != nullptr)
        {
            display(root->left); // Recursively display the left subtree
            cout << root->data << " (";
            cout << (root->color == RED ? "RED" : "BLACK") << ") ";
            display(root->right); 
        }
    }

    void showTree()
    {
        display(root);
        cout << endl; 
    }
};

int main()
{
    RedBlackTree tree;
    tree.insertNode(10);
    tree.insertNode(20);
    tree.insertNode(30);
    tree.insertNode(15);
    cout << "Red-Black Tree after insertions: ";
    tree.showTree();

    return 0;
}
