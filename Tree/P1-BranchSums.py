"""
Problem Statement:
Given a binary tree, return a list of all branch sums, where each sum is the total of values from the root to a leaf. The sums should appear in the order of left-to-right leaf traversal.

Example:
Input:
    1  
   / \  
  2   3  
 / \  
4   5  
Output: [7, 8, 4] *(1+2+4, 1+2+5, 1+3)*


🔍 Approach: Depth-First Search (DFS)

1.Start at the root with an initial sum of 0.

2.Recursively traverse the tree:
    -At each node, add its value to the running sum.
    -If it’s a leaf node (no left or right child), add the running sum to the result list.

3.Return the list of all branch sums once traversal is complete.

"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    # ❌ MISTAKE #1: You are not returning the result.
    # The function modifies `sums`, but doesn't return it, so it prints `None`.
    return sums  # ✅ Fix: Add this line to return the final result

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return
    
    branchRunningSum = runningSum + node.value
    
    if node.left is None and node.right is None:
        sums.append(branchRunningSum)
        return # ✅ Best practice: Return here to avoid unnecessary recursion
    
    # ❌ MISTAKE #2: Recursive calls missing required arguments.
    # You're only passing `root.left` and `root.right`, but the function expects 3 parameters.
    # So this will throw a TypeError when executed.

    calculateBranchSums(node.left, branchRunningSum, sums)
    calculateBranchSums(node.right, branchRunningSum, sums)

# Test
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

# ❌ MISTAKE #3: The original function didn't return anything, so this would print `None`
# ✅ Fix: Now that `branchSums` returns a value, this will print the correct output
print(branchSums(root))  # Expected: [7, 8, 4]
