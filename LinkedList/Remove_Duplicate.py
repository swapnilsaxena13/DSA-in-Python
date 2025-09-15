
"""
# Hints

## Hint 1

The brute-force approach to this problem is to use a hash table or a set to keep track of all node values that exist while traversing the linked list and to simply remove nodes that have a value that already exists. This approach works, but can you solve this problem without using an auxiliary data structure?

---

## Hint 2

What does the fact that the nodes are sorted tell you about the location of all duplicate nodes? How can you use this fact to solve this problem with constant space?

---

## Hint 3

Since the linked list's nodes are sorted, you can loop through them and, at each iteration, simply remove all successive nodes that have the same value as the current node. For each node, change its next pointer to the next node in the linked list that has a different value. This will remove all duplicate-value nodes.

---

## Optimal Space & Time Complexity

O(n) time | O(1) space - where n is the number of nodes in the Linked List
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

def print_list(node):
    """Helper function to print the linked list"""
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

def main():
    # Print the hints text
    print("Hints from the image:")
    print(hints_text)
    print("\n" + "="*50 + "\n")
    
    # Example usage of the solution
    print("Example usage:")
    
    # Create a sample linked list: 1 -> 1 -> 2 -> 3 -> 3
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    
    print("Original list:")
    print_list(head)
    
    # Remove duplicates
    solution = Solution()
    result = solution.deleteDuplicates(head)
    
    print("List after removing duplicates:")
    print_list(result)

if __name__ == "__main__":
    main()