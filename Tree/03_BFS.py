from collections import deque

# ------------------------------------------
# Node Class Definition
# ------------------------------------------
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

# ------------------------------------------
# Standard Level Order Traversal (Single Line BFS)
# ------------------------------------------
def printLevelOrder(root):
    """
    Perform Level Order Traversal of a binary tree.
    Uses a queue to process nodes level by level in a single line.
    
    Steps:
    1. Enqueue the root node.
    2. Loop until the queue is empty:
       - Dequeue a node & print its value.
       - Enqueue left and right children (if they exist).
    
    When to use:
    - When you only need to print all nodes in order.
    - Fastest method for simple BFS traversal.
    
    Args:
        root (Node): The root node of the binary tree.
    """
    if root is None:
        return
    
    queue = []
    queue.append(root)
    
    while len(queue) > 0:
        print(queue[0].key, end=" ")
        node = queue.pop(0)
        
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    print()

# ------------------------------------------
# Level Order Traversal by Line (Using None Marker)
# ------------------------------------------
def printLevelByLine_NoneMarker(root):
    """
    Perform Level Order Traversal and print each level on a new line.
    Uses None as a marker to separate levels.
    
    Steps:
    1. Enqueue root and a `None` marker for the first level.
    2. Loop while the queue has more than 1 element:
       - Dequeue a node.
       - If it's `None`, print newline and enqueue another `None` if queue is not empty.
       - If it's not `None`, print its value and enqueue left and right children if they exist.
    
    When to use:
    - When working with dynamic tree structures or tracking depth.
    - Best for problems like Top View, Bottom View, and checking if two nodes are cousins.
    
    Args:
        root (Node): The root node of the binary tree.
    """
    if root is None:
        return
    
    q = deque()
    q.append(root)
    q.append(None)
    
    while len(q) > 1:
        curr = q.popleft()
        if curr is None:
            print()
            q.append(None)
            continue 
        print(curr.key, end=" ")
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)
    print()

# ------------------------------------------
# Level Order Traversal by Line (Using Count Variable)
# ------------------------------------------
def printLevelByLine_CountVariable(root):
    """
    Perform Level Order Traversal and print each level on a new line.
    Uses a count variable to track the number of nodes at each level.
    
    Steps:
    1. Enqueue the root node.
    2. Loop while the queue is not empty:
       - Store `count = len(queue)` to get number of nodes at the current level.
       - Process `count` nodes:
         - Dequeue and print each node.
         - Enqueue left and right children (if they exist).
       - Print a newline after processing the level.
    
    When to use:
    - When you need to process each level separately.
    - Useful for problems like finding max width, level sum, and deepest leaves sum.
    
    Args:
        root (Node): The root node of the binary tree.
    """
    if root is None:
        return
    
    q = deque()
    q.append(root)
    
    while len(q) > 0:
        count = len(q)
        for _ in range(count):
            curr = q.popleft()
            print(curr.key, end=" ")
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)
        print()

# ------------------------------------------
# Driver Code
# ------------------------------------------
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

print("Standard Level Order Traversal:")
printLevelOrder(root)
print("\nLevel Order Traversal by Line (None Marker Method):")
printLevelByLine_NoneMarker(root)
print("\nLevel Order Traversal by Line (Count Variable Method):")
printLevelByLine_CountVariable(root)

# ------------------------------------------
# Important Notes & DSA Tricks
# ------------------------------------------
# 1. **Use Standard Level Order Traversal** when a simple BFS traversal is needed.
# 2. **Use Count Variable Method** when levels need to be processed separately (e.g., finding max width, level sum).
# 3. **Use None Marker Method** for dynamically growing trees or when tracking depth.
# 4. **Time Complexity**: O(N) for all methods, as each node is visited once.
# 5. **Space Complexity**:
#    - O(N) in worst case (complete binary tree where queue stores all nodes of last level).
# 6. **Applications of Level Order Traversal**:
#    - Finding Maximum Width of a Tree
#    - Deepest Leaves Sum
#    - Zigzag Level Order Traversal
#    - Checking if Two Nodes are Cousins
# 7. **Quick Selection Guide:**
#    - Standard Level Order Traversal → Simple BFS traversal without level distinction.
#    - Count Variable Method → Process levels separately (finding max width, level sum, zigzag traversal).
#    - None Marker Method → Track depth, check cousin nodes, or process dynamic tree structures.
# 8. **Useful Trick:**
#    - Use a `deque` instead of a list for better performance when frequently popping from the front.
#    - If solving problems related to levels in a tree, always check whether level-based processing is needed.

