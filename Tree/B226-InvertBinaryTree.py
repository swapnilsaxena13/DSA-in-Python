
""""
226. Invert Binary Tree - Explanation
Description
You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,3,2,7,6,5,4]

Example 2:
Input: root = [3,2,1]
Output: [3,1,2]

Example 3:
Input: root = []
Output: []
Constraints:
0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100


           1
         /   \
        3     2
       / \   / \
      7   6 5   4

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
       
        if root is None:
            return None
        
        rs=self.invertTree(root.right)
        ls=self.invertTree(root.left)

        root.left = rs
        root.right = ls
# Here in base Case we are checking root so it might be possible that in these type of problem we generally return the base case. we will see this further 
        return root
 """       
Now, We will be doing this with breadth first search. Means we will be changing the data while traversing through breadth of the tree.
In tree parent has access to its child so we will swap the value while travesing through bfs after entering into the queue.
"""
from collections import deque


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return
        queue = deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return root



