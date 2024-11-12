#include <iostream>
#include <algorithm> // For std::max() to calculate maximum of two values
class AVLTreeNode
{
public:
    int key;
    AVLTreeNode *left;
    AVLTreeNode *right;
    int height;
    AVLTreeNode(int value)
    {
        key = value;
        left = right = nullptr;
        height = 1;
    }
};
class AVLTree
{
private:
    AVLTreeNode *root;
    int height(AVLTreeNode *node)
    {
        return node == nullptr ? 0 : node->height;
    }
    int balanceFactor(AVLTreeNode *node)
    {
        return node == nullptr ? 0 : height(node->left) - height(node->right);
    }
    AVLTreeNode *rightRotate(AVLTreeNode *y)
    {
        AVLTreeNode *x = y->left;
        AVLTreeNode *T2 = x->right;
        x->right = y;
        y->left = T2;
        y->height = std::max(height(y->left), height(y->right)) + 1;
        x->height = std::max(height(x->left), height(x->right)) + 1;
        return x;
    }
    AVLTreeNode *leftRotate(AVLTreeNode *x)
    {
        AVLTreeNode *y = x->right;
        AVLTreeNode *T2 = y->left;
        y->left = x;
        x->right = T2;
        x->height = std::max(height(x->left), height(x->right)) + 1;
        y->height = std::max(height(y->left), height(y->right)) + 1;
        return y;
    }
    AVLTreeNode *balance(AVLTreeNode *node)
    {
        int balance = balanceFactor(node);
        if (balance > 1 && balanceFactor(node->left) >= 0)
        {
            return rightRotate(node);
        }
        if (balance < -1 && balanceFactor(node->right) <= 0)
        {
            return leftRotate(node);
        }
        if (balance > 1 && balanceFactor(node->left) < 0)
        {
            node->left = leftRotate(node->left);
            return rightRotate(node);
        }
        if (balance < -1 && balanceFactor(node->right) > 0)
        {
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }
        return node; // No balancing needed
    }
    AVLTreeNode *insert(AVLTreeNode *node, int key)
    {
        if (node == nullptr)
        {
            return new AVLTreeNode(key);
        }
        if (key < node->key)
        {
            node->left = insert(node->left, key);
        }
        else if (key > node->key)
        {
            node->right = insert(node->right, key);
        }
        else
        {
            return node;
        }
        node->height = 1 + std::max(height(node->left), height(node->right));
        return balance(node);
    }
    void inorder(AVLTreeNode *node)
    {
        if (node != nullptr)
        {
            inorder(node->left);           // Traverse left subtree
            std::cout << node->key << " "; // Visit the node
            inorder(node->right);          // Traverse right subtree
        }
    }

public:
    AVLTree() : root(nullptr) {}
    void insert(int key)
    {
        root = insert(root, key);
    }
    void print()
    { // Start the inorder traversal from the root
        inorder(root);
        std::cout << std::endl; // Print a newline at the end
    }
};
int main()
{
    AVLTree tree;
    tree.insert(10);
    tree.insert(20);
    tree.insert(30);
    tree.insert(25); // This will cause a rotation (left-right case)
    tree.insert(5);
    tree.print(); // Should print the values in ascending order
    return 0;
}
