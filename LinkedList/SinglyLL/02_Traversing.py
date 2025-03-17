# Notes on Traversing a Linked List in Python

# Concept Explanation:
# A linked list is a linear data structure where each element (called a node) contains two parts:
# 1. Data: The value stored in the node.
# 2. Next: A pointer/reference to the next node in the sequence.

# Traversing a linked list means visiting each node of the list and performing some operation (e.g., printing the data).
# Traversal is a fundamental operation in linked lists and is used in many other operations like searching, insertion, and deletion.

# Time Complexity:
# - Traversal: O(N), where N is the number of nodes in the list.
# - Search: O(N), as we may need to traverse the entire list to find an element.
# - Insertion: O(N), as we may need to traverse the list to find the correct position for insertion.
# - Deletion: O(N), as we may need to traverse the list to find the node to delete.

# Node Class Definition
class Node:
    def __init__(self, key):
        self.key = key  # Data part of the node
        self.next = None  # Pointer to the next node

# Function to Traverse and Print the Linked List
def printList(head):
    curr = head  # Start from the head of the list
    while curr != None:  # Traverse until the end of the list (curr becomes None)
        print(curr.key)  # Print the data of the current node
        curr = curr.next  # Move to the next node

# Main Code to Demonstrate Traversal
# Create a linked list: 10 -> 20 -> 15 -> 30
head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)

# Print the linked list
printList(head)

# Output:
# 10
# 20
# 15
# 30

# Notes:
# - The `printList` function is a general-purpose function that can print any linked list.
# - It starts from the head of the list and traverses each node, printing its data.
# - The traversal continues until the end of the list is reached (i.e., `curr` becomes `None`).
# - The time complexity of traversal is O(N), where N is the number of nodes in the list.
# - This function can be used as a building block for other operations like searching, insertion, and deletion.