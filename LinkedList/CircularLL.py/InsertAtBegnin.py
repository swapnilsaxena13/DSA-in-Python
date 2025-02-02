# Python program for Insertion at the Beginning of Circular Linked List

# Approach (O(N) time complexity):
# 1. Create a new node 'T' with the given data.
# 2. If the list is empty (head is None), set the new node to point to itself and return it as the head.
# 3. Otherwise, traverse the list to find the last node.
# 4. Make the last node's next point to the new node.
# 5. Set the new node's next to the old head to complete the circular link.
# 6. Return the new node as the new head of the list.

class Node:
    # Constructor to initialize the node with data and pointer
    def __init__(self, data):
        self.data = data  # Store the data part of the node
        self.next = None  # Initially, the next pointer is set to None

# Function to insert a new node at the beginning of the circular linked list (O(N) time complexity)
def insertBeg(head, x):
    temp = Node(x)  # Create a new node with the given value x
    if head == None:  # If the list is empty, make the new node point to itself
        temp.next = temp
        return temp  # Return the new node as the head
    curr = head
    while curr.next != head:  # Traverse to the last node
        curr = curr.next
    curr.next = temp  # Make the last node point to the new node
    temp.next = head  # Make the new node point to the old head
    return temp  # Return the new node as the new head of the list

# Function to print the elements of the circular linked list
def printCircular(head):
    if head == None:  # If the list is empty, return
        return
    print(head.data, end=" ")  # Print the head's data
    curr = head.next
    while curr != head:  # Traverse and print all elements until the traversal reaches back to the head
        print(curr.data, end=" ")
        curr = curr.next
    print()  # Print a newline after printing all elements

# Approach (Constant Time Complexity):
# 1. Create a new node 'T' with the given data.
# 2. If the list is empty (head is None), set the new node to point to itself and return it as the head.
# 3. Otherwise, make the new node's next point to the node after the head.
# 4. Set the head's next pointer to the new node.
# 5. Swap the data between the head and the new node to make the new node the head.
# 6. Return the head.

# Function to insert a new node at the beginning of the circular linked list (Constant Time Complexity)
def insertBegConstant(head, x):
    temp = Node(x)  # Create a new node with the given value x
    if head == None:  # If the list is empty, make the new node point to itself
        temp.next = temp
        return temp  # Return the new node as the head
    else:
        temp.next = head.next  # Make the new node point to the node after the head
        head.next = temp  # Make the head point to the new node
        head.data, temp.data = temp.data, head.data  # Swap the data between the head and the new node
        return head  # Return the head of the list

# Main function to demonstrate circular linked list insertion
if __name__ == "__main__":
    head = Node(20)  # Create the first node with value 20
    head.next = Node(30)  # Create the second node with value 30
    head.next.next = head  # Make the last node point to the head (circular structure)
    
    print("Original Circular List:")
    printCircular(head)  # Print the original list

    # Insert at the beginning using O(N) approach
    head = insertBeg(head, 10)
    print("List after insertion at the beginning (O(N) approach):")
    printCircular(head)  # Print the updated list

    # Insert at the beginning using constant time approach
    head = insertBegConstant(head, 5)
    print("List after insertion at the beginning (constant time approach):")
    printCircular(head)  # Print the updated list

# Output for O(N) and Constant Time Complexity approaches:
# Original Circular List:
# 20 30
# List after insertion at the beginning (O(N) approach):
# 10 20 30
# List after insertion at the beginning (constant time approach):
# 5 20 30 10
