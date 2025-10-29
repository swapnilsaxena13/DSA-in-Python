"""
104. Maximum Depth of Binary Tree - Explanation
Problem Link

Description
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [1,2,3,null,null,4]

Output: 3
Example 2:

Input: root = []

Output: 0
Constraints:

0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
"""


"""
From the depth perspective the number of level that a tree has will be the depth of the tree.So, we use None maker technique whenever there is a new level we will increase out count variable.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        count=1 
        queue=deque()
        queue.append(root)
        queue.append(None)

        while len(queue)>1:

            node=queue.popleft()
            if node is None:
                count+=1
                queue.append(None)
                continue

            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
        return count
        
"""
this is DFS approach where we traverse through  the tree and when we find that this is the None node we return the "max from both right subtree and left subtree + 1".
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))