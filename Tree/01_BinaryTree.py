# Binary Tree in Python

# A binary tree is a tree data structure in which each node has at most two children,
# referred to as the left child and the right child.

# Binary Tree Representation:
# A binary tree is represented by a pointer to the topmost node (root) of the tree.
# If the tree is empty, the root is NULL.

# A Tree node contains the following parts:
# 1. Data
# 2. Pointer to the left child
# 3. Pointer to the right child

# Below is an example of a tree node with integer data.

# Node Class Definition
class Node:
    def __init__(self, key):
        self.left = None  # Pointer to the left child
        self.val = key  # Data stored in the node
        self.right = None  # Pointer to the right child
        

# Creating a Simple Binary Tree with 4 Nodes
# The tree structure will be as follows:
#        1    <-- root
#      /   \
#     2     3  
#    /   
#   4

if __name__ == '__main__':
    # Create the root node with value 1
    root = Node(1)
    ''' 
    Tree after creating root:
        1
       / \
    None None
    '''
    
    # Create left and right children of the root
    root.left = Node(2)
    root.right = Node(3)
    ''' 
    Tree after adding left and right children:
         1
        / \
        2   3
       / \ / \
    None None None None
    '''
    
    # Create a left child for node 2
    root.left.left = Node(4)
    ''' 
    Final Tree:
          1
        /    \
        2      3
        / \    / \
       4  None None None
      / \
    None None
    '''

# Summary:
# - A tree is a hierarchical data structure.
# - Main uses of trees include maintaining hierarchical data, providing moderate access,
#   and supporting insert/delete operations.
# - Binary trees are a special case of trees where every node has at most two children.