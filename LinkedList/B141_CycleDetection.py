"""
LeetCode 141 - Linked List Cycle

====================================================
Problem:
Given the beginning of a linked list head, return True if there is a cycle in the linked list.
Otherwise, return False.

A cycle exists if at least one node in the list can be visited again by following the next pointer.

Note:
- "index" is used internally by LeetCode to create a cycle for testing.
- You are NOT given index in the function.

====================================================
Examples:

Example 1:
Input: head = [1,2,3,4], index = 1
Output: True
Explanation: Tail connects to node at index 1 (0-based).

Example 2:
Input: head = [1,2], index = -1
Output: False

Constraints:
1 <= Length of list <= 1000
-1000 <= Node.val <= 1000

====================================================
This file explains TWO approaches:

1) Hash Set (Visited Nodes)
2) Fast and Slow Pointers (Floyd's Cycle Detection Algorithm)

Along with detailed explanation of how memory references are stored.
"""


# ====================================================
# Definition for singly-linked list.
# ====================================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


# ====================================================
# APPROACH 1: Hash Set (Visited Nodes)
# ====================================================
class SolutionHashSet:
    """
    Intuition:
    We remember every node we visit.
    If we ever see the same node again, it means a cycle exists.

    Key Point (IMPORTANT CONCEPT):
    --------------------------------
    We store the *node objects themselves* in the set, NOT their values.

    Each node is a separate object in memory.
    Even if two nodes have the same value, they are still different objects.

    Example:
        Node A: ListNode(5)
        Node B: ListNode(5)

        A != B (different memory references)
        But A.val == B.val

    So when we do:
        seen.add(cur)
    we are storing the memory reference (object identity) of the node,
    not just its value.

    If we encounter the same node again (same reference),
    Python can detect it using hashing and equality.

    This avoids confusion when multiple nodes contain the same value.
    """

    def hasCycle(self, head: ListNode) -> bool:
        seen = set()      # Will store node references (objects)
        cur = head

        while cur:
            # If the same node object is visited again, cycle exists
            if cur in seen:
                return True

            # Store the current node reference in the set
            seen.add(cur)

            # Move to the next node
            cur = cur.next

        # If we reach None, there is no cycle
        return False


# ====================================================
# APPROACH 2: Fast and Slow Pointers (Floyd's Algorithm)
# ====================================================
class SolutionTwoPointers:
    """
    Intuition:
    Use two pointers:
    - slow moves one step at a time
    - fast moves two steps at a time

    If a cycle exists:
        fast will eventually catch up to slow inside the loop.

    If no cycle:
        fast will reach None.

    Why it works:
    Think of a race track. If one runner is faster, they will eventually
    lap the slower runner if the track is circular.

    Space Efficient:
    This approach does NOT require extra memory.
    """

    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next    # Move 2 steps

            # If both pointers meet, a cycle exists
            if slow == fast:
                return True

        # If fast reaches end, no cycle exists
        return False


# ====================================================
# TIME & SPACE COMPLEXITY
# ====================================================
"""
1) Hash Set Approach:
   Time Complexity: O(n)
   Space Complexity: O(n)
   - Because we store up to n nodes in the set.

2) Two Pointers Approach:
   Time Complexity: O(n)
   Space Complexity: O(1)
   - No extra memory is used.

====================================================
IMPORTANT MISUNDERSTANDING CLARIFIED:
====================================================

❌ WRONG THINKING:
"I am storing node values in the set, so duplicate values will cause a false cycle."

✅ CORRECT THINKING:
You are storing the *node object (memory reference)*, not the value.

Python set stores object identity (hash based on object reference by default),
not the internal value unless you override __hash__ and __eq__.

So:
    seen.add(cur)

means:
    Store the address/reference of this node in memory.

If later you encounter:
    cur in seen

it only returns True if it's the SAME NODE OBJECT,
not just another node with the same value.

====================================================
WHEN TO USE WHICH?
====================================================

✔ Use Hash Set:
- When clarity is more important than memory.
- Easy to understand and implement.
- Useful for debugging.

✔ Use Two Pointers:
- When memory efficiency matters.
- Preferred in interviews.
- Elegant mathematical solution.

====================================================
EXAMPLE FOR TESTING
====================================================
"""


# ====================================================
# HELPER FUNCTIONS TO CREATE LINKED LISTS
# ====================================================
def create_linked_list_with_cycle(values, index):
    """
    Creates a linked list.
    If index != -1, it connects the last node to the node at 'index'
    to form a cycle.

    Example:
    values = [1,2,3,4], index = 1
    Cycle: 4 -> 2
    """
    if not values:
        return None

    nodes = [ListNode(val) for val in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if index != -1:
        nodes[-1].next = nodes[index]   # Create cycle

    return nodes[0]


# ====================================================
# TESTING
# ====================================================
if __name__ == "__main__":
    # Example 1: Cycle exists
    head1 = create_linked_list_with_cycle([1, 2, 3, 4], 1)

    # Example 2: No cycle
    head2 = create_linked_list_with_cycle([1, 2], -1)

    print("Using HashSet Approach:")
    print("Example 1:", SolutionHashSet().hasCycle(head1))  # True
    print("Example 2:", SolutionHashSet().hasCycle(head2))  # False

    print("\nUsing Two Pointers Approach:")
    print("Example 1:", SolutionTwoPointers().hasCycle(head1))  # True
    print("Example 2:", SolutionTwoPointers().hasCycle(head2))  # False
