# Function to add an undirected edge between vertices u and v
def addEdge(adj, u, v):
    adj[u].append(v)   # Add v to u's adjacency list
    adj[v].append(u)   # Add u to v's adjacency list (because it's undirected)

# Function to print the adjacency list representation of the graph
def printGraph(adj):
    for u, l in enumerate(adj):     # Loop through each vertex and its adjacency list
        print(u, l)                 # Print the vertex and its list of neighbors

# ---------- MAIN ----------

v = 4  # Number of vertices in the graph

# Create an adjacency list with v empty lists (one for each vertex)
adj = [[] for i in range(v)]

# Add edges to the graph
addEdge(adj, 0, 1)  # Add edge between vertex 0 and 1
addEdge(adj, 0, 2)  # Add edge between vertex 0 and 2
addEdge(adj, 1, 2)  # Add edge between vertex 1 and 2
addEdge(adj, 1, 3)  # Add edge between vertex 1 and 3

# Print the adjacency list of the graph
printGraph(adj)
