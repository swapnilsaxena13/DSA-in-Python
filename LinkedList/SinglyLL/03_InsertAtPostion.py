# Notes on Inserting a Node at a Given Position in a Singly Linked List

# Inserting a node at a given position involves the following steps:
# 1. Check if the given position is valid (i.e., not out of bounds).
# 2. Traverse the list to find the node just before the desired position.
# 3. Create a new node with the given data.
# 4. Adjust the pointers to insert the new node in the correct position.

# Time Complexity: O(N), where N is the number of nodes in the list.
# Auxiliary Space: O(1), as we are using a constant amount of extra space.

# Node Class Definition
class Node:
    def __init__(self, k):
        self.key = k  # Data part of the node
        self.next = None  # Pointer to the next node

# Function to Insert a Node at a Given Position
def insertPos(head, data, pos):
    # Create a new node with the given data
    temp = Node(data)
    
    # If the position is 1, insert at the beginning
    if pos == 1:
        temp.next = head  # Point the new node to the current head
        return temp  # Return the new head
    
    # Traverse the list to find the node just before the desired position
    curr = head
    for i in range(pos - 2):
        if curr == None:
            return head  # If position is out of bounds, return the original head
        curr = curr.next
    
    # Insert the new node
    temp.next = curr.next  # Point the new node to the next node
    curr.next = temp  # Point the previous node to the new node
    
    return head  # Return the head of the modified list

# Function to Print the Linked List
def printList(head):
    curr = head
    while curr != None:
        print(curr.key)  # Print the data of the current node
        curr = curr.next  # Move to the next node
    print()  # Print a newline after the list

# Main Code to Demonstrate the Insertion
# Create a linked list: 10 -> 20 -> 30 -> 40 -> 50
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

# Print the original list
printList(head)

# Insert 45 at position 4
head = insertPos(head, 45, 4)

# Print the modified list
printList(head)

# Output:
# 10
# 20
# 30
# 40
# 50
# 
# 10
# 20
# 30
# 45
# 40
# 50
# 

# Notes:
# - The function `insertPos` handles the insertion at any valid position in the list.
# - If the position is 1, it means we are inserting at the beginning, and the new node becomes the new head.
# - The function traverses the list to find the node just before the desired position and then adjusts the pointers to insert the new node.
# - The time complexity is O(N) because, in the worst case, we may need to traverse the entire list.
# - The space complexity is O(1) because we are using a constant amount of extra space.