"""
Problem Statement:
Given a binary tree where each leaf node is an integer value and each internal node is one of the following operations:
- -1 represents addition (+)
- -2 represents subtraction (-)
- -3 represents division (/), which should truncate toward zero
- -4 represents multiplication (*)

Write a function that evaluates the expression represented by this binary tree and returns the result.

Example Input:
       -1
      /   \
    -2    -3
   / \    / \
 -4  10  3  2
 / \
2  3

This represents: ((2 * 3) - 10) + (3 / 2) = (6 - 10) + 1 = -4 + 1 = -3

The function should return -3.

The solution should have O(n) time complexity and O(h) space complexity, where n is the number of nodes and h is the height of the tree.
"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(h) space - where n is the number of nodes in the Binary Tree,
# and h is the height of the Binary Tree
def evaluateExpressionTree(tree):
# Use post-order traversal (Left → Right → Root). Why?

# Because you need the results of both subtrees (left and right operands) before applying the operation at the current node.
    # Base Case: if it's a leaf node, return the value directly
    if tree.left is None and tree.right is None:
        return tree.value

    leftValue = evaluateExpressionTree(tree.left)
    rightValue = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return leftValue + rightValue
    if tree.value == -2:
        return leftValue - rightValue
    if tree.value == -3:
        return int(leftValue / rightValue)
    if tree.value == -4:
        return leftValue * rightValue



# Example usage:
# Create a binary tree representing the expression: (8 / 4) + (7 - 2)
# Which is equivalent to:
#       +
#      / \
#     /   \
#    *     -
#   / \   / \
#  8  4  7  2

# Leaf nodes
eight = BinaryTree(8)
four = BinaryTree(4)
seven = BinaryTree(7)
two = BinaryTree(2)

# Inner nodes representing operations
division = BinaryTree(-3, eight, four)       # 8 / 4
subtraction = BinaryTree(-2, seven, two)     # 7 - 2

# Root node representing addition
addition = BinaryTree(-1, division, subtraction)  # (8 / 4) + (7 - 2)

# Evaluate the expression
result = evaluateExpressionTree(addition)
print("Result:", result)  # Output should be (2) + (5) = 7