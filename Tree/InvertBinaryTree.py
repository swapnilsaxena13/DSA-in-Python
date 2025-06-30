from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        while queue:
            current = queue.popleft()
            # Swap the left and right children
            current.left, current.right = current.right, current.left
            # Add the children to the queue if they exist
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root
    
    def invertTreeRecursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Invert the left and right subtrees recursively
        left_inverted = self.invertTreeRecursive(root.left)
        right_inverted = self.invertTreeRecursive(root.right)
        
        # Swap the left and right subtrees
        root.left = right_inverted
        root.right = left_inverted
        
        return root

# Helper function to print the tree in level-order (BFS)
def print_tree(root: Optional[TreeNode]):
    if not root:
        print("Tree is empty")
        return
    
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            if node:
                level_nodes.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                level_nodes.append("None")
        print(" ".join(level_nodes))

# Example usage
if __name__ == "__main__":
    # Construct a sample binary tree
    #        4
    #       / \
    #      2   7
    #     / \ / \
    #    1  3 6 9
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    
    print("Original tree:")
    print_tree(root)
    
    solution = Solution()
    
    # Invert the tree iteratively
    inverted_iterative = solution.invertTreeIterative(root)
    print("\nInverted tree (Iterative):")
    print_tree(inverted_iterative)
    
    # Invert the tree recursively (need to re-invert to get back to original)
    inverted_recursive = solution.invertTreeRecursive(inverted_iterative)
    print("\nInverted tree (Recursive - back to original):")
    print_tree(inverted_recursive)  