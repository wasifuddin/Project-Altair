# Creation of adjacency list to be passed to the DFS algorithm to check if all vertices is covered
def create_adjacency_list(vertices, edges):
    # Initializing an empty dictionary to store the adjacency list
    adjacency_list = {i: [] for i in range(vertices)}
    # Populating the adjacency list using the edges value
    for edge in edges:
        src, dest = edge # Extracting the source and destination points
        adjacency_list[src].append(dest)
        adjacency_list[dest].append(src)  # We are adding both directions since it's an undirected graph
    return adjacency_list

# DFS algorithm usage to check if all vertices has been visited

# Parameters: graph: The Adjacency list created, start: Source Vertices, visited = set to contain the visited vertices
def dfs(graph, start, visited=None):
    # Creating the set of vertices visited if it doesn't exist
    if visited is None:
        visited = set()
    visited.add(start)
    # Applying a recursion of dfs function with vertices that has not been visited
    # Here converting the value of graph[start] to set as it is originally of type List
    for next in set(graph[start]) - visited:
        dfs(graph, next, visited)
    return len(visited)

# Given dataset
vertices = 7
edges = [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]


# Storing the created adjacency list created passing the vertices number and edges in the function
adj_list = create_adjacency_list(vertices, edges)

# Comparing if the total number of vertices number is equal to the total number of vertices actually possible to be
# travelled Prints True if the total number of vertices possible to be travelled is equal to given vertices number
# The Depth First Search Algorithm Function at first takes input the adjacency list then the source vertex
print(vertices==dfs(adj_list, 0))  # The output is False
