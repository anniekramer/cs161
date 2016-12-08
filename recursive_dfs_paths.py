def recursive_dfs_paths(graph, start, path=[]):
    path = path + [start]

    for node in graph[start]:
        if not node in path:
            path = recursive_dfs_paths(graph, node, path)

    return path

graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
print 'recursive dfs ', recursive_dfs_paths(graph, 'A')
