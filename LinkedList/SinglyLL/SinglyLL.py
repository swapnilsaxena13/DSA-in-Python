# Simple Linked List Implementation in Python

# A linked list is a linear data structure where elements are stored in nodes.
# Each node contains two parts:
# 1. key (data value)
# 2. next (pointer/reference to the next node in the list)

# A linked list starts with a head node pointing to the first element.
# If the list is empty, head points to None.

# Defining a Node class
class Node:
    def __init__(self, k):
        self.key = k  # Assigning the data value to the node
        self.next = None  # Initializing the next pointer as None (no link initially)

# Creating individual nodes
node1 = Node(10)  # First node with value 10
node2 = Node(20)  # Second node with value 20
node3 = Node(30)  # Third node with value 30

# Linking the nodes to form a linked list
node1.next = node2  # node1 points to node2
node2.next = node3  # node2 points to node3

# Head of the linked list (first node)
head = node1  # head stores reference to the first node

# Printing the elements of the linked list
print(head.key)         # Output: 10 (first node value)
print(head.next.key)    # Output: 20 (second node value)
print(head.next.next.key)  # Output: 30 (third node value)

# Note:
# - This is a simple linked list with three nodes.
# - The last node (node3) has its next pointer as None, indicating the end of the list.
# - The list maintains a sequential connection from head to tail.
