'''
Example graph data:

6 nodes here: A, B, C, D, E, F
Each node represented by a key in a dictionary.
For each key in the dict, the value is a list that contains the nodes connected to the start node (key).


    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
'''

def find_first_path_between_nodes(graph, start, end, path=[]):
    # Add start node to path array
    path = path + [start]

    # If the start and end nodes are the same, just return a list that simply
    # contains that starting node.
    if start == end:
        return path

    # Check whether or not the graph object contains the given start key.
    if not graph.has_key(start):
        return None

    # For a given node in the list of nodes corresponding to the start node key,
    # check if the node is in the path list. If not, create a new path and return it.
    for node in graph[start]:
        if node not in path:
            new_path = find_first_path_between_nodes(graph, node, end, path)
            
            if new_path:
                return new_path

    return None

def find_all_paths_between_nodes(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    if not graph.has_key(start):
        return []

    paths = []

    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths_between_nodes(graph, node, end, path)

            for new_path in new_paths:
                paths.append(new_path)

    return paths

def find_shortest_path_between_nodes(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    if not graph.has_key(start):
        return None

    shortest_path_between_nodes = None

    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path_between_nodes(graph, node, end, path)

            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest_path_between_nodes = new_path

    return shortest_path_between_nodes
