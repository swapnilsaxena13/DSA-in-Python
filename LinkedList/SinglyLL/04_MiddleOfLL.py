# Notes on Finding the Middle of a Linked List in Python

# Concept Explanation:
# The middle of a linked list is the node that is equidistant from both the start and the end of the list.
# If the list has an odd number of nodes, there is a single middle node.
# If the list has an even number of nodes, there are two middle nodes, and we typically consider the second one as the middle.

# There are two common methods to find the middle of a linked list:
# 1. **Method 1: Two-Pass Approach**
#    - Traverse the list once to count the number of nodes.
#    - Traverse the list again to reach the middle node.
#    - Time Complexity: O(N), where N is the number of nodes.
#    - Auxiliary Space: O(1).

# 2. **Method 2: Two-Pointer Approach (Efficient)**
#    - Use two pointers: `slow` and `fast`.
#    - Move `slow` one step at a time and `fast` two steps at a time.
#    - When `fast` reaches the end, `slow` will be at the middle.
#    - Time Complexity: O(N), but only requires a single traversal.
#    - Auxiliary Space: O(1).

# Node Class Definition
class Node:
    def __init__(self, k):
        self.data = k  # Data part of the node
        self.next = None  # Pointer to the next node

# Function to Print the Linked List
def printList(head):
    curr = head
    while curr != None:
        print(curr.data)  # Print the data of the current node
        curr = curr.next  # Move to the next node
    print()

# Method 1: Two-Pass Approach to Find the Middle
def printMiddleTwoPass(head):
    if head == None:
        return  # If the list is empty, return
    
    # Step 1: Count the number of nodes in the list
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    
    # Step 2: Traverse to the middle node
    curr = head
    for _ in range(count // 2):
        curr = curr.next
    
    print(curr.data)  # Print the middle node's data

# Method 2: Two-Pointer Approach to Find the Middle
def printMiddleTwoPointer(head):
    if head == None:
        return  # If the list is empty, return
    
    slow = head  # Slow pointer moves one step at a time
    fast = head  # Fast pointer moves two steps at a time
    
    # Traverse the list
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    
    print(slow.data)  # Print the middle node's data

# Main Code to Demonstrate Finding the Middle
# Create a linked list: 10 -> 10 -> 20
head = Node(10)
head.next = Node(10)
head.next.next = Node(20)

# Print the linked list
print("Linked List:")
printList(head)

# Find the middle using the two-pass approach
print("Middle (Two-Pass Approach):")
printMiddleTwoPass(head)

# Find the middle using the two-pointer approach
print("Middle (Two-Pointer Approach):")
printMiddleTwoPointer(head)

# Output:
# Linked List:
# 10
# 10
# 20
#
# Middle (Two-Pass Approach):
# 10
# Middle (Two-Pointer Approach):
# 10

# Notes:
# - The two-pass approach is straightforward but requires traversing the list twice.
# - The two-pointer approach is more efficient as it finds the middle in a single traversal.
# - Both methods have a time complexity of O(N), but the two-pointer approach is generally preferred due to its efficiency.