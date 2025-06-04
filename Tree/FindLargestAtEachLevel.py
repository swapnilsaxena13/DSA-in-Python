from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        Finds the largest value in each row (level) of a binary tree.

        Approach:
        - Use level-order traversal (BFS) with a queue.
        - Track the number of nodes at each level using `count = len(queue)`.
        - For each level, initialize `maxVal` to negative infinity.
        - Traverse all nodes at the current level, updating `maxVal` as you go.
        - Enqueue left and right children of the current node.
        - After finishing the level, append `maxVal` to the result list.

        Why use this approach?
        - Efficiently handles each level independently.
        - Easy to modify for other level-based stats like min, average, sum, etc.
        - Avoids recursion and stack overflow for deep trees.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(w), where w is the maximum width of the tree.
        """

        if root is None:
            return []

        q = deque()
        q.append(root)
        result = []

        while q:# while q > 0:  # ❌ Wrong: comparing deque object with int
            count = len(q)
            maxVal = float('-inf')  # Reset max value per level

            for _ in range(count):
                curr = q.popleft()
                maxVal = max(curr.val, maxVal)

                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)

            result.append(maxVal)

        return result

# ---------- Test Code Below ----------

if __name__ == "__main__":
    # Construct the following binary tree:
    #         0
    #        /
    #      -1
    #
    # Expected output: [0, -1]

    root = TreeNode(0)
    root.left = TreeNode(-1)

    sol = Solution()
    output = sol.largestValues(root)
    print("Largest values in each row:", output)
