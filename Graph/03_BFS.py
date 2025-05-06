"""
Breadth First Search or BFS for a Graph

Breadth-First Traversal (or Search) for a graph is similar to BFS of a tree. 
Unlike trees, graphs may contain cycles, so we use a visited array to avoid 
processing nodes more than once.

Steps to implement BFS:
1. Declare a queue and insert the starting vertex.
2. Initialize a visited array and mark the starting vertex as visited.
3. Loop until the queue is empty:
   - Remove the front vertex.
   - Mark it as visited.
   - Do the work (like printing it).
   - Insert all its unvisited neighbors into the queue.

Time Complexity: O(V + E)
Auxiliary Space: O(V)

There are multiple BFS orders depending on the graph structure.

Basic example:
Graph:
0 --> 1
0 --> 2
1 --> 2
2 --> 0, 3
3 --> 3

Starting from vertex 2, BFS traversal: 2 0 3 1
"""

from collections import defaultdict

# Graph class using adjacency list
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Dictionary to store graph

    def addEdge(self, u, v):
        self.graph[u].append(v)  # Add edge from u to v

    def BFS_connected(self, start):
        """Basic BFS traversal for connected graph"""

        visited = [False] * (max(self.graph) + 1)  # Track visited vertices
        queue = []  # Initialize queue for BFS

        queue.append(start)     # Enqueue start node
        visited[start] = True   # Mark start as visited

        while queue:
            current = queue.pop(0)       # Remove node from front of queue
            print(current, end=' ')      # Work: print current node

            for neighbor in self.graph[current]:  # Visit neighbors
                if not visited[neighbor]:
                    visited[neighbor] = True      # Mark visited
                    queue.append(neighbor)        # Enqueue neighbor


"""
Now, consider a disconnected graph. We need to call BFS from every unvisited node.
This ensures all disconnected components are covered.
"""

def bfs_disconnected_graph(V, adj):
    """
    Generic BFS for disconnected graphs (directed/undirected).
    V - number of vertices
    adj - adjacency list
    """
    visited = [False] * V  # Track visited nodes
    bfs_traversal = []     # Store result

    for i in range(V):
        if not visited[i]:         # Start BFS if node not visited
            queue = [i]
            visited[i] = True

            while queue:
                current = queue.pop(0)     # Dequeue front node
                bfs_traversal.append(current)  # Store result

                for neighbor in adj[current]:  # Loop through neighbors
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

    return bfs_traversal


"""
Alternative BFS implementation using Python's queue module (used for large scale)
Also uses:
    remove → mark → work → add neighbors
"""

import queue  # Queue for thread-safe FIFO

# Helper function to add edges in undirected graph
def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)  # Remove this if graph is directed

# BFS utility for one component
def BFSUtil(u, adj, visited):
    q = queue.Queue()     # Create a FIFO queue
    visited[u] = True     # Mark initial node visited
    q.put(u)              # Enqueue start node

    while not q.empty():
        current = q.get()             # Remove node
        print(current, end=' ')       # Work: print current

        for neighbor in adj[current]:  # Traverse neighbors
            if not visited[neighbor]:
                visited[neighbor] = True   # Mark visited
                q.put(neighbor)           # Add to queue

# Calls BFS for all components
def BFS_full(adj, V):
    visited = [False] * V  # Keep track of all visited nodes
    for u in range(V):
        if not visited[u]:
            BFSUtil(u, adj, visited)  # Call BFS for each unvisited node


"""
Driver Code for Connected Graph BFS
"""
print("Connected Graph BFS (starting from node 2):")
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# Perform BFS on connected graph
g.BFS_connected(2)

print("\n\nDisconnected Graph BFS (Generic Function):")
V = 5
adj = [[] for _ in range(V)]

# Build adjacency list for undirected graph
addEdge(adj, 0, 4)
addEdge(adj, 1, 2)
addEdge(adj, 1, 3)
addEdge(adj, 1, 4)
addEdge(adj, 2, 3)
addEdge(adj, 3, 4)

# Perform BFS for disconnected graph using function
result = bfs_disconnected_graph(V, adj)
print("Traversal:", result)

print("\nDisconnected Graph BFS (using queue.Queue and util function):")
# Perform BFS for disconnected graph using queue module
BFS_full(adj, V)
