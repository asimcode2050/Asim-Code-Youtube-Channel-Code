#include <iostream>
using namespace std;
struct Node
{
    int data;
    Node *left;
    Node *right; 
    Node(int value)
    {
        data = value;
        left = right = nullptr;
    }
};

Node *rightRotate(Node *root)
{
    Node *newRoot = root->left;
    root->left = newRoot->right;
    newRoot->right = root;
    return newRoot; 
}

Node *leftRotate(Node *root)
{
    Node *newRoot = root->right;
    root->right = newRoot->left;
    newRoot->left = root;
    return newRoot;
}

Node *splay(Node *root, int key)
{
    if (root == nullptr || root->data == key)
    {
        return root;
    }

    if (key < root->data)
    {
        if (root->left == nullptr)
        {
            return root;
        }

        if (key < root->left->data)
        {
            root = rightRotate(root); 
        }
        else if (key > root->left->data)
        {
            root->left = leftRotate(root->left);
            root = rightRotate(root);
        }
    }
    else
    {
        if (root->right == nullptr)
        {
            return root;
        }
        if (key > root->right->data)
        {
            root = leftRotate(root); 
        }
        else if (key < root->right->data)
        {
            root->right = rightRotate(root->right);
            root = leftRotate(root);
        }
    }

    return root; 
}

Node *insert(Node *root, int key)
{
    if (root == nullptr)
    {
        return new Node(key);
    }

    root = splay(root, key);
    if (root->data == key)
    {
        return root;
    }
    Node *newNode = new Node(key);
    if (key < root->data)
    {
        newNode->right = root;
        newNode->left = root->left;
        root->left = nullptr;
    }
    else
    {
        newNode->left = root;
        newNode->right = root->right;
        root->right = nullptr; 
    }

    return newNode;
}

Node *search(Node *root, int key)
{
    return splay(root, key);
}

void inorder(Node *root)
{
    if (root != nullptr)
    {
        inorder(root->left);
        cout << root->data << " ";
        inorder(root->right); 
    }
}

int main()
{
    Node *root = nullptr;

    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 30);
    root = insert(root, 40);
    root = insert(root, 50);
    cout << "In-order traversal: ";
    inorder(root);
    cout << endl;  // Print a new line
    root = search(root, 30);
    cout << "After searching for 30, the in-order traversal: ";
    inorder(root);
    cout << endl;

    return 0;
}
