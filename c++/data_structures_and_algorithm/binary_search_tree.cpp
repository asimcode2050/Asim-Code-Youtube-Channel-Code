#include <iostream>
using namespace std;
struct Node
{
    int data;
    Node *left;
    Node *right;
    Node(int val)
    {
        data = val;
        left = nullptr;
        right = nullptr;
    }
};
Node *insert(Node *root, int value)
{
    if (root == nullptr)
    {
        return new Node(value);
    }
    if (value < root->data)
    {
        root->left = insert(root->left, value);
    }
    else if (value > root->data)
    {
        root->right = insert(root->right, value);
    }
    return root;
}
bool search(Node *root, int value)
{
    if (root == nullptr)
    {
        return false;
    }
    if (root->data == value)
    {
        return true;
    }
    if (value < root->data)
    {
        return search(root->left, value);
    }
    else
    {
        return search(root->right, value);
    }
}
Node *findMin(Node *root)
{
    while (root != nullptr && root->left != nullptr)
    {
        root = root->left;
    }
    return root;
}
Node *deleteNode(Node *root, int value)
{
    if (root == nullptr)
    {
        return root;
    }
    if (value < root->data)
    {
        root->left = deleteNode(root->left, value);
    }
    else if (value > root->data)
    {
        root->right = deleteNode(root->right, value);
    }
    else
    {
        if (root->left == nullptr && root->right == nullptr)
        {
            delete root;
            return nullptr;
        }
        else if (root->left == nullptr)
        {
            Node *temp = root->right;
            delete root;
            return temp;
        }
        else if (root->right == nullptr)
        {
            Node *temp = root->left;
            delete root;
            return temp;
        }
        else
        {
            Node *temp = findMin(root->right);
            root->data = temp->data;
            root->right = deleteNode(root->right, temp->data);
        }
    }
    return root;
}
void inorder(Node *root)
{
    if (root != nullptr)
    {
        inorder(root->left);       // Visit left subtree
        cout << root->data << " "; // Visit node
        inorder(root->right);      // Visit right subtree
    }
}
int main()
{
    Node *root = nullptr; // Start with an empty tree
    root = insert(root, 50);
    root = insert(root, 30);
    root = insert(root, 20);
    root = insert(root, 40);
    root = insert(root, 70);
    root = insert(root, 60);
    root = insert(root, 80);
    cout << "Inorder traversal: ";
    inorder(root);
    cout << endl;
    int searchValue = 40;
    if (search(root, searchValue))
    {
        cout << "Found " << searchValue << " in the tree!" << endl;
    }
    else
    {
        cout << "Did not find " << searchValue << " in the tree!" << endl;
    }
    int deleteValue = 20;
    root = deleteNode(root, deleteValue);
    cout << "Inorder traversal after deletion: ";
    inorder(root);
    cout << endl;
    return 0;
}
