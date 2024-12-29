#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
};

struct Node *newNode(int value)
{
    struct Node *node = (struct Node *)malloc(sizeof(struct Node));
  if (!node)
  {
      printf("Memory allocation failed!\n");
      exit(1);
  }
  node->data = value;
  node->left = node->right = NULL;
  return node;
}

/* Root -> Left Subtree -> Right Subtree. */

void preorder(struct Node *root)
{
  if (root == NULL)
  {
      return;
  }

  printf("%d ", root->data);

  preorder(root->left);
  preorder(root->right);
}

/* Left Subtree -> Root -> Right Subtree */
void inorder(struct Node *root)
{
  if (root == NULL)
  {
      return;
  }

  inorder(root->left);
  printf("%d ", root->data);
  inorder(root->right);
}

/* Left Subtree -> Right Subtree -> Root. */
void postorder(struct Node *root)
{
  if (root == NULL)
  {
      return;
  }

  postorder(root->left);
  postorder(root->right);
  printf("%d ", root->data);
}

int main()
{
    struct Node *root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    root->right->left = newNode(6);
    root->right->right = newNode(7);
    printf("Preorder Traversal: ");
    preorder(root);
    printf("\n");
    printf("Inorder Traversal: ");
    inorder(root);
    printf("\n");
    printf("Postorder Traversal: ");
    postorder(root);
    printf("\n");

    return 0;
}
