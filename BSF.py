from collections import deque

def bfs(graph, start):
    visited = set()          # Track visited nodes
    queue = deque([start])   # Initialize queue with start node

    print("BFS Traversal Order:")

    while queue:
        vertex = queue.popleft()  # Dequeue a node
        if vertex not in visited:
            print(vertex, end=" → ")
            visited.add(vertex)
            # Enqueue all unvisited neighbors
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example Graph using Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS
print("\n--- Breadth First Search (BFS) Traversal ---\n")
bfs(graph, 'A')
print("\n\n✅ BFS Traversal Completed.")
