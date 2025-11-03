"""
00. Same Tree - Explanation
Description
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [4,7], q = [4,null,7]
Output: false

Example 3:
Input: p = [1,2,3], q = [1,3,2]
Output: false
Constraints:

0 <= The number of nodes in both trees <= 100.
-100 <= Node.val <= 100
"""


"""
Mistake in :
You’re not weak in logic — you’re skipping the recursive connection step between child and parent results.
Once you force yourself to think “combine child results logically”, this entire category of bugs disappears.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        if p and q:
            ls=self.isSameTree(p.left,q.left)
            rs=self.isSameTree(p.right,q.right)
            return p.val==q.val and ls and rs
        return False        


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        que1=deque()
        que1.append(p)
        que2=deque()
        que2.append(q)

        while que1 and que2:
            curr1=que1.popleft()      
            curr2=que2.popleft() 
            if not curr1 or not curr2:
                return False
            if curr1.val != curr2.val:
                return False
            if (curr1.left is None) != (curr2.left is None):
                return False
            if (curr1.right is None) != (curr2.right is None):
                return False
            if curr1.left is not None:
                que1.append(curr1.left)
            if curr1.right is not None:
                que1.append(curr1.right)
            if curr2.left is not None:
                que2.append(curr2.left)
            if curr2.right is not None:
                que2.append(curr2.right)
        return True