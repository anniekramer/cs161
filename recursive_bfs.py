def recursive_bfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    queue = [start]
    
    while queue:
        vertex = queue.pop(0)
        visited.add(vertex)
        queue.extend(graph[vertex] - visited)
        
        for next_vertex in graph[start] - visited:
            recursive_bfs(graph, next_vertex, visited)
    
    return visited

# undirected graph w/o edge weightings
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print recursive_bfs(graph, 'A')
