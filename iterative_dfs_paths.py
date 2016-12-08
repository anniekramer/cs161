def iterative_dfs_paths(graph, start, path=[]):
    q = [start]
    while q:
        v = q.pop(0)
        if v not in path:
            path = path + [v]
            q = graph[v] + q
    return path

graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
print 'iterative dfs ', iterative_dfs_paths(graph, 'A')
