from collections import defaultdict

class Graph(object):

    def _init_(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections_to_graph(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add_connection_between_nodes(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove_references_to_node(self,node):
        for node, connections in self._graph.iteritems():
            try:
                connections.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
                pass

    def is_connected_nodes(self, node1, node2):
        return node1 in self._graph and node2 in self._graph[node1]

    def find_shortest_path_between_nodes(self, node1, node2, path=[]):
        path = path + node1
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in graph[node1]:
            if node not in path:
                new_path = self.find_path(node1, node2)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
