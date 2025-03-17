# Python program to demonstrate Circular Linked List traversal

# Approach:
# 1. Create a Node class to represent each node in the linked list with a key and a pointer to the next node.
# 2. Define a function 'printCircular' that prints all the nodes in the circular linked list.
#    - If the list is empty (head is None), return without printing.
#    - Start printing from the head node, then traverse and print each node's key until the traversal reaches the head again.
# 3. Create nodes, form a circular linked list by linking the last node to the first, and call the printCircular function.

# Node class definition
class Node:
    # Constructor to initialize the node with key value
    def __init__(self, k):
        self.key = k  # Data part of the node
        self.next = None  # Pointer to the next node (initially None)

# Function to print the elements of the circular linked list
def printCircular(head):
    # Check if the list is empty
    if head == None:
        return  # If head is None, simply return (no elements to print)
    
    # Print the key of the head node (first element)
    print(head.key, end=" ")
    
    # Initialize the current node as the node after head
    curr = head.next
    
    # Traverse the list until we reach back to the head node
    while curr != head:
        print(curr.key, end=" ")  # Print the key of the current node
        curr = curr.next  # Move to the next node in the list

# Main function to demonstrate circular linked list
if __name__ == "__main__":
    # Create the nodes of the circular linked list
    head = Node(10)  # First node with key 10
    head.next = Node(20)  # Second node with key 20
    head.next.next = Node(30)  # Third node with key 30
    head.next.next.next = head  # Link back the last node to the head (circular behavior)
    
    # Call the function to print the circular linked list
    printCircular(head)

# Output: 
# 10 20 30 
