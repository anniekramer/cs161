def recursive_bfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    queue = [start]
    vertex = queue.pop(0)

    if vertex not in visited:
        visited.add(vertex)
        queue.extend(graph[vertex] - visited)
    while queue:
        recursive_bfs(visited[graph] - start)
    
    return visited

# undirected graph w/o edge weightings
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print recursive_bfs(graph, 'A')
