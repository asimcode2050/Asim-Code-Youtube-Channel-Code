#include <stdio.h>
#include <stdlib.h>
struct Node
{
  int key;
  struct Node *left;
  struct Node *right;
  int height;
};

int height(struct Node *N)
{
  if (N == NULL)
  {
      return 0;
  }
  return N->height;
}

int getBalance(struct Node *N)
{
  if (N == NULL)
  {
      return 0;
  }
  return height(N->left) - height(N->right);
}

struct Node *newNode(int key)
{
    struct Node *node = (struct Node *)malloc(sizeof(struct Node));
    node->key = key;
    node->left = NULL;
    node->right = NULL;
    node->height = 1;
    return node;
}

struct Node *rightRotate(struct Node *y)
{
    struct Node *x = y->left;
    struct Node *T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = 1 + (height(y->left) > height(y->right) ? height(y->left) : height(y->right));
    x->height = 1 + (height(x->left) > height(x->right) ? height(x->left) : height(x->right));
    return x;
}

struct Node *leftRotate(struct Node *x)
{
    struct Node *y = x->right;
    struct Node *T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = 1 + (height(x->left) > height(x->right) ? height(x->left) : height(x->right));
    y->height = 1 + (height(y->left) > height(y->right) ? height(y->left) : height(y->right));

    return y; // Return the new root (y).
}

struct Node *balance(struct Node *root)
{
    int balanceFactor = getBalance(root); // Get the balance factor of the node.
  if (balanceFactor < -1 && getBalance(root->right) <= 0)
  {
      return leftRotate(root);
  }
  if (balanceFactor > 1 && getBalance(root->left) >= 0)
  {
      return rightRotate(root); // Perform right rotation.
  }

  if (balanceFactor > 1 && getBalance(root->left) < 0)
  {
      root->left = leftRotate(root->left);
      return rightRotate(root);
  }

  if (balanceFactor < -1 && getBalance(root->right) > 0)
  {
      root->right = rightRotate(root->right);
      return leftRotate(root);
  }
  return root;

}

struct Node *insert(struct Node *node, int key)
{
  if (node == NULL)
  {
      return newNode(key);
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

  node->height = 1 + (height(node->left) > height(node->right) ? height(node->left) : height(node->right));

  return balance(node);
}

void inorder(struct Node *root)
{
  if (root != NULL)
  {
      inorder(root->left);
      printf("%d ", root->key);
      inorder(root->right);
  }
}

int main()
{
    struct Node *root = NULL;

    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 30); // Insert 30 (this will trigger a rotation)
    root = insert(root, 15);
    root = insert(root, 25);
    printf("Inorder traversal of the AVL tree: ");
    inorder(root);
    printf("\n");

    return 0;
}
