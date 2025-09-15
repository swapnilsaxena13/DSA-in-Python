"""
Hint 1
Since you are given a Singly Linked List, you do not have access to any of the list's nodes' previous nodes. Thus, traversing the entire list and then counting k nodes back isn’t an option.
Is there a way for you to traverse the entire list and to know which node is the kth node from the end by the time you reach the final node in the list?

Hint 2
Can you accomplish the task mentioned in Hint #1 by traversing the list all the while keeping track of two nodes at a time? How could this work?

Hint 3
Initialize two variables pointing to the first node in the list. Traverse k nodes in the list, updating the second variable at every node (that is, take k steps with the second variable).
Then, traverse the remainder of the list, this time updating both the second and the first variables (that is, take as many steps with the first variable as the number of steps between the kth node from the start and the end of the list).
Once you reach the end of the list, the first variable should point to the kth node from the end.

Optimal Space & Time Complexity
Time: O(n)

Space: O(1), where n is the number of nodes in the Linked List

🧠 Concept of Dummy Node
A dummy node is a placeholder node placed before the head of a linked list.
It helps simplify operations like deletion, especially when the node to be deleted is the head node itself.

Without a dummy node, if you need to remove the head, you'd have to write separate logic.
With a dummy node, all deletions are handled the same way — including the head — since you always have a node before the one you want to remove.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Step 1: Create a dummy node pointing to head
        dummy = ListNode(0)
        dummy.next = head

        # Step 2: Initialize two pointers at dummy
        fast = dummy
        slow = dummy

        # Step 3: Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Step 4: Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Step 5: Skip the node to be deleted
        slow.next = slow.next.next

        # Step 6: Return the new head (may have changed)
        return dummy.next

# Utility function to print a linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example Usage:
if __name__ == "__main__":
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)

    print("Original list:")
    printList(head)

    sol = Solution()
    updated_head = sol.removeNthFromEnd(head, 2)  # Remove 2nd node from end (which is 4)

    print("\nUpdated list after removing 2nd node from end:")
    printList(updated_head)
