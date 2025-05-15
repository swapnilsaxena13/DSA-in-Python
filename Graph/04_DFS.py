"""
DFS Key Points to Avoid Mistakes


Loop over indices, not lists:

Use for node in range(len(adj)) instead of for element in adj).
🔑 Reason: adj contains lists, and lists are unhashable (can’t be used in sets).


Use self. for instance variables:

When you define self.res, always access it using self.res, not just res.
🔑 Reason: Without self., Python looks for a local variable, not a class variable.


Avoid modifying a set with unhashable types:

Only store hashable types (like int, str, tuple) in set().
🔑 Mistake: Trying to check or add a list ([2, 3]) in visited causes an error.


Initialize class variables before using them:

Always initialize self.res = [] inside the method before appending to it.
🔑 Reason: Otherwise, it causes NameError or behaves unexpectedly.
"""
# --------------------------------------------------
# Depth First Search (DFS) for a Graph
# --------------------------------------------------
# Depth First Traversal (or Search) for a graph is similar to DFS of a tree.
# The only catch here is that unlike trees, graphs may contain cycles.
# To avoid processing a node more than once, use a boolean visited array.
# A graph can have more than one DFS traversal.

# Example:
# Input: n = 4, e = 6 
# 0 -> 1, 0 -> 2, 1 -> 2, 2 -> 0, 2 -> 3, 3 -> 3 
# Output: DFS from vertex 1 : 1 2 0 3

# Another Example:
# Input: n = 4, e = 6
# 2 -> 0, 0 -> 2, 1 -> 2, 0 -> 1, 3 -> 3, 1 -> 3
# Output: DFS from vertex 2 : 2 0 1 3

# --------------------------------------------------
# DFS Algorithm Overview:
# - Start from the root or any arbitrary node.
# - Mark the node.
# - Move to the adjacent unmarked node.
# - Repeat until no unmarked adjacent node remains.
# - Then backtrack and check for other unmarked nodes.
# - Continue traversal.
# - Finally, print nodes in the DFS path.

# --------------------------------------------------
# Basic DFS Implementation (for connected graphs)
# --------------------------------------------------

from collections import defaultdict

class Graph:
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Helper recursive function for DFS
    def DFSUtil(self, v, visited):
        # Mark current node as visited and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the adjacent vertices
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # DFS traversal starting from a given vertex
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

# Driver Code for connected graph
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.DFS(2)

# Output:
# Following is DFS from (starting from vertex 2)
# 2 0 1 3

# Time complexity: O(V + E) where V = vertices, E = edges
# Auxiliary Space: O(V) due to visited set

# --------------------------------------------------
# Handling a Disconnected Graph
# --------------------------------------------------
# In a disconnected graph, all vertices may not be reachable from a single node.
# To handle this, run DFS from all unvisited nodes one-by-one.

class GraphDisconnected:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self):
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                self.DFSUtil(vertex, visited)

# Driver code for disconnected graph
if __name__ == "__main__":
    print("\nFollowing is Depth First Traversal for complete graph\n")
    g = GraphDisconnected()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.DFS()

# Output:
# Following is Depth First Traversal
# 0 1 2 3

# Time complexity: O(V + E)
# Auxiliary Space: O(V) for visited set
