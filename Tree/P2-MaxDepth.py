from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional['TreeNode']) -> int:
        """
        Calculates the maximum depth (or height) of a binary tree using 
        level order traversal (Breadth-First Search) with a count variable.

        Approach:
        - Use a queue (deque) to perform level-order traversal.
        - Each level of the tree contributes +1 to the depth.
        - Use `count = len(queue)` to process all nodes at the current level.
        - For each node, enqueue its left and right children.
        - Increment the depth after each level is fully processed.

        Why use this approach?
        - It is iterative (no risk of stack overflow for deep trees).
        - You can easily modify it to find level-wise statistics like:
          max value per level, average value, node count, etc.
        """
        if root is None:
            return 0

        eq = deque()
        eq.append(root)
        depth = 0

        while len(eq) > 0:
            count = len(eq)

            for _ in range(count):
                curr = eq.popleft()

                if curr.left is not None:
                    eq.append(curr.left)
                if curr.right is not None:
                    eq.append(curr.right)

            depth += 1

        return depth

# ---------- Test Code Below ----------

# Construct the following binary tree:
#         1
#        / \
#       2   3
#      / \
#     4   5
#
# Expected depth = 3

if __name__ == "__main__":
    # Building the tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Create Solution object and call maxDepth
    sol = Solution()
    depth = sol.maxDepth(root)
    print("Maximum Depth of the Binary Tree:", depth)
