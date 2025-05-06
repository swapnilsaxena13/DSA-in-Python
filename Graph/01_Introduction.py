# Introduction to Graphs
# 
# A Graph is a data structure that consists of the following two components:
# 1. A finite set of vertices also called nodes.
# 2. A finite set of ordered pair of the form (u, v) called as edge. The pair is ordered because (u, v) is not the same as (v, u) in case of a directed graph (digraph). The pair of the form (u, v) indicates that there is an edge from vertex u to vertex v. The edges may contain weight/value/cost.
# 
# Graphs are used to represent many real-life applications:
# - Graphs are used to represent networks. The networks may include paths in a city, telephone network, or circuit network. Example: Google GPS
# - Graphs are also used in social networks like LinkedIn, Facebook. Each person is represented with a vertex (or node). Each node is a structure and contains information like person id, name, gender and locale.
# 
# Directed and Undirected Graphs
#
# Directed Graphs: The Directed graphs are such graphs in which edges are directed in a single direction.
# Undirected Graphs: Undirected graphs are such graphs in which the edges are directionless or bi-directional. That is, if there is an edge between vertices u and v, we can use the edge to go from both u to v and v to u.
#
# Representing Graphs
#
# Following two are the most commonly used representations of a graph:
# 1. Adjacency Matrix.
# 2. Adjacency List.
#
# Adjacency Matrix:
# - It is a 2D array of size V x V where V is the number of vertices in a graph.
# - Let the 2D array be adj[][]. A slot adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j.
# - Adjacency matrix for undirected graph is always symmetric.
# - For weighted graphs, if adj[i][j] = w, then there is an edge from vertex i to vertex j with weight w.
# Pros:
# - Representation is easier to implement and follow.
# - Removing an edge takes O(1) time.
# - Queries like whether there is an edge from vertex 'u' to vertex 'v' are efficient and can be done in O(1).
# Cons:
# - Consumes more space O(V^2).
# - Even if the graph is sparse, it consumes the same space.
# - Adding a vertex is O(V^2) time.
#
# Adjacency List:
# - Graph can also be implemented using an array of lists.
# - Every index of the array contains a complete list of adjacent vertices.
# - Size of the array = number of vertices. Every index i stores the list of vertices adjacent to i.
# - Can also be used to represent weighted graphs (use lists of pairs).
# Pros:
# - Saves space O(|V| + |E|).
# - In worst case, there can be C(V, 2) number of edges consuming O(V^2) space.
# - Adding a vertex is easier.
# Cons:
# - Queries like whether there is an edge from vertex u to vertex v are not efficient and can take O(V).

# Python implementation of the adjacency list representation of an undirected graph

# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


# A class to represent a graph. A graph is the list of the adjacency lists.
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as it is an undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


# Driver program to the above graph class
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()

# Output:
# Adjacency list of vertex 0
#  head -> 4 -> 1 
# Adjacency list of vertex 1
#  head -> 4 -> 3 -> 2 -> 0 
# Adjacency list of vertex 2
#  head -> 3 -> 1 
# Adjacency list of vertex 3
#  head -> 4 -> 2 -> 1 
# Adjacency list of vertex 4
#  head -> 3 -> 1 -> 0
