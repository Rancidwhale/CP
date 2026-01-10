def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
        
    visited.add(node)  # Mark the node as visited
    print(node)  # Process the current node
    
    for neighbor in graph[node]:
        print("check visit node , neighbor ",node," ",neighbor)
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Recursively visit the neighbor

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')
