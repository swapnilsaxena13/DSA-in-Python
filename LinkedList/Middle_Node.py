# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle node of a linked list using the slow and fast pointer approach.
        
        Hint 1: The middle node of a Linked List will always be at index length / 2.
        Hint 2: While the LinkedList class has no length, you can calculate it by simply iterating through the entire list.
        Hint 3: If you create a slow and a fast pointer, with the fast one iterating at twice the speed, 
                the slow one will be in the middle when the fast one reaches the end.
                
        Optimal Space & Time Complexity: O(n) time | O(1) space - where n is the number of nodes in the linked list
        """
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

# For proper execution, you would also need to import Optional from typing
from typing import Optional

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

solution = Solution()
middle = solution.middleNode(node1)
print(middle.val)  # Output: 3