def recursive_dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    
    for next_vertex in graph[start] - visited:
        recursive_dfs(graph, next_vertex, visited)
    
    return visited

# undirected graph w/o edge weightings
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print recursive_dfs(graph, 'A')
