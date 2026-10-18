from collections import defaultdict
class Graph:
    def __init__(self, vert):
        # Fix: change int to list so we can append connected nodes
        self.graph = defaultdict(list)
        self.vert = vert

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, node, visited):
        # 1. Mark the current node as visited and print it
        visited.add(node)
        print(node, end=" ")

        # 2. Look at all neighbors connected to this node
        for neighbor in self.graph[node]:
            # 3. If a neighbor hasn't been visited, dive down into it!
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start_node):
        # Keep track of nodes we've already visited to avoid infinite loops
        visited = set()
        print(f"DFS Traversal starting from node {start_node}:")
        self.dfs_util(start_node, visited)
        print()


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.dfs(2)  # Output: 2 0 1 3