# from collections import defaultdict
# n , m = map(int,input().split())
# edges = [tuple(map(int,input().split())) for _ in range(m)]

# print(edges)
from collections import defaultdict

def minimum_drops(n, edges):
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [-1] * (n + 1)  # -1: unvisited, 0: color 0, 1: color 1
    dropped = 0  # Total number of dropped students

    def dfs(node, color):
        stack = [(node, color)]
        component_colors = [0, 0]  # Track the count of nodes in each color group

        while stack:
            current, current_color = stack.pop()
            if visited[current] == -1:
                visited[current] = current_color
                component_colors[current_color] += 1
            elif visited[current] != current_color:
                return None  # Conflict occurs; this component cannot be bipartite

            for neighbor in graph[current]:
                if visited[neighbor] == -1:  # Not visited
                    stack.append((neighbor, 1 - current_color))
                elif visited[neighbor] == current_color:
                    return None  # Conflict occurs

        return component_colors

    # Process each connected component
    for i in range(1, n + 1):
        if visited[i] == -1:  # Node not yet processed
            colors = dfs(i, 0)
            if colors is None:  # Conflict found
                dropped += 1
            else:
                # No conflict: Add the minimum of the two groups
                dropped += min(colors)

    return dropped


# Example Input
n , m = map(int,input().split())
edges = [tuple(map(int,input().split())) for _ in range(m)]

# Output
print(minimum_drops(n, edges))  # Output: 0
