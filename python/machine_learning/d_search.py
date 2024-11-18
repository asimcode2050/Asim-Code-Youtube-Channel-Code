
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:  # Keep going as long as there are nodes to explore
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            stack.extend(reversed(graph[node]))


dfs(graph, 'A')
