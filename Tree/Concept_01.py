# Binary Tree Node Definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node's value
        self.left = left  # Left child
        self.right = right  # Right child

# Core Recursive Concept:
# A binary tree is a recursive data structure.
# Each subtree is itself a tree, so we apply the same function recursively.

class BinaryTree:

    # Base Structure of Recursion
    def solve(self, root):
        # 1. Base Case: Handle null nodes (stopping condition)
        if root is None:
            return <base_case_value>  # This depends on the problem (0, False, -inf, etc.)

        # 2. Solve the left subtree
        left_result = self.solve(root.left)

        # 3. Solve the right subtree
        right_result = self.solve(root.right)

        # 4. Combine results (this depends on the problem)
        return <operation_on_results>  # Example: sum, max, comparison, etc.

# Example of a tree (structure, not values)
# Each subtree is treated as a smaller problem of the same type.
#
#        (root)
#        /    \
#    (left)  (right)
#    /   \     /   \
# (..)  (..) (..)  (..)
#
# The function first solves left, then right, then combines.

# Key Points:
# - The **base case** stops recursion.
# - The **left and right recursive calls** break the problem into smaller parts.
# - The **final return statement** combines results.

# Recursion is the fundamental way to traverse and process binary trees.
# Mastering this structure makes solving tree problems easier.
