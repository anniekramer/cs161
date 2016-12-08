def iterative_bfs_paths(graph, start, path=[]):
    q = [start]
    while q:
        v = q.pop(0)
        if not v in path:
            path = path + [v]
            q = q + graph[v]
    return path

graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
print 'iterative bfs ', iterative_bfs_paths(graph, 'A')
