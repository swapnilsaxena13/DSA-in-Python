# Tree Traversals (Inorder, Preorder, and Postorder)

# Unlike linear data structures (Array, Linked List, Queues, Stacks, etc.), trees can be traversed
# in multiple ways. The most common methods for traversing trees are:
# 1. Inorder Traversal
# 2. Preorder Traversal
# 3. Postorder Traversal

# Node Class Definition
class Node:
    def __init__(self, key):
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.val = key  # Data stored in the node


# Inorder Traversal
# Algorithm:
# 1. Traverse the left subtree, i.e., call Inorder(left->subtree)
# 2. Visit the root
# 3. Traverse the right subtree, i.e., call Inorder(right->subtree)

# Uses of Inorder Traversal:
# - In Binary Search Trees (BST), Inorder traversal gives nodes in non-decreasing order.
# - To get nodes in non-increasing order, reverse the Inorder traversal.

def printInorder(root):
    if root:
        # First recur on the left child
        printInorder(root.left)
        # Print the data of the node
        print(root.val, end=" ")
        # Recur on the right child
        printInorder(root.right)


# Preorder Traversal
# Algorithm:
# 1. Visit the root
# 2. Traverse the left subtree, i.e., call Preorder(left->subtree)
# 3. Traverse the right subtree, i.e., call Preorder(right->subtree)

# Uses of Preorder Traversal:
# - Preorder traversal is used to create a copy of the tree.
# - It is also used to get prefix expressions from an expression tree.

def printPreorder(root):
    if root:
        # Print the data of the node
        print(root.val, end=" ")
        # Recur on the left child
        printPreorder(root.left)
        # Recur on the right child
        printPreorder(root.right)


# Postorder Traversal
# Algorithm:
# 1. Traverse the left subtree, i.e., call Postorder(left->subtree)
# 2. Traverse the right subtree, i.e., call Postorder(right->subtree)
# 3. Visit the root

# Uses of Postorder Traversal:
# - Postorder traversal is used to delete the tree.
# - It is also useful to get the postfix expression of an expression tree.

def printPostorder(root):
    if root:
        # First recur on the left child
        printPostorder(root.left)
        # Recur on the right child
        printPostorder(root.right)
        # Print the data of the node
        print(root.val, end=" ")


# Driver Code
if __name__ == "__main__":
    # Creating a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function Calls
    print("Inorder Traversal of binary tree is:")
    printInorder(root)  # Output: 4 2 5 1 3
    print("\n")

    print("Preorder Traversal of binary tree is:")
    printPreorder(root)  # Output: 1 2 4 5 3
    print("\n")

    print("Postorder Traversal of binary tree is:")
    printPostorder(root)  # Output: 4 5 2 3 1
    print("\n")


# Time Complexity: O(N)
# - All traversals visit every node exactly once, so the time complexity is O(N).

# Auxiliary Space:
# - If we don’t consider the size of the stack for function calls, then O(1).
# - Otherwise, O(h) where h is the height of the tree.
#   - Worst case (skewed tree): O(N)
#   - Best case (balanced tree): O(Log N)

# Note:
# - The height of a skewed tree is N (number of elements), so the worst space complexity is O(N).
# - The height of a balanced tree is Log N, so the best space complexity is O(Log N).