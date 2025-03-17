# Notes on Reversing a Linked List in Python

# Concept Explanation:
# Reversing a linked list involves changing the direction of the links between nodes so that the last node becomes the first node, and the first node becomes the last node.
# This can be done using various methods, such as:
# 1. **Using a Stack**: Store the node values in a stack and then reassign them in reverse order.
# 2. **Efficient Method (Iterative)**: Use three pointers (`prev`, `curr`, and `next`) to reverse the links in a single traversal.

# Time Complexity:
# - Both methods have a time complexity of O(N), where N is the number of nodes in the list.
# - The efficient method is preferred as it uses constant space (O(1)), whereas the stack method uses O(N) auxiliary space.

# Node Class Definition
class Node:
    def __init__(self, k):
        self.key = k  # Data part of the node
        self.next = None  # Pointer to the next node

# Function to Print the Linked List
def printList(head):
    curr = head
    while curr != None:
        print(curr.key)  # Print the data of the current node
        curr = curr.next  # Move to the next node
    print()

# Method 1: Using a Stack to Reverse the Linked List
def reverseListStack(head):
    stack = []  # Stack to store node values
    curr = head

    # Step 1: Push all node values into the stack
    while curr is not None:
        stack.append(curr.key)
        curr = curr.next

    # Step 2: Pop values from the stack and reassign them to the nodes
    curr = head
    while curr is not None:
        curr.key = stack.pop()  # Assign the popped value to the current node
        curr = curr.next

    return head  # Return the modified head

# Method 2: Efficient Iterative Method to Reverse the Linked List
def reverseListEfficient(head):
    curr = head
    prev = None  # Pointer to the previous node

    while curr is not None:
        next = curr.next  # Store the next node
        curr.next = prev  # Reverse the link
        prev = curr  # Move `prev` to the current node
        curr = next  # Move `curr` to the next node

    return prev  # `prev` is the new head of the reversed list

# Main Code to Demonstrate Reversing a Linked List
# Create a linked list: 10 -> 20 -> 30 -> 40
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# Print the original linked list
print("Original Linked List:")
printList(head)

# Reverse the linked list using the stack method
print("Reversed Linked List (Using Stack):")
head_stack = reverseListStack(head)
printList(head_stack)

# Reverse the linked list using the efficient method
print("Reversed Linked List (Efficient Method):")
head_efficient = reverseListEfficient(head)
printList(head_efficient)

# Output:
# Original Linked List:
# 10
# 20
# 30
# 40
#
# Reversed Linked List (Using Stack):
# 40
# 30
# 20
# 10
#
# Reversed Linked List (Efficient Method):
# 40
# 30
# 20
# 10

# Notes:
# - The stack method is simple but uses extra space (O(N)) to store node values.
# - The efficient method uses three pointers and reverses the list in place, making it more space-efficient (O(1)).
# - Both methods have a time complexity of O(N), but the efficient method is generally preferred for its space efficiency.