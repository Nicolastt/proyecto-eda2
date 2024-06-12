from collections import deque

from edge import Edge
from node import Node


class Graph:
    def __init__(self, directed=False):
        self.nodes = {}
        self.edges = []
        self.directed = directed

    def add_node(self, id, data=None):
        if id not in self.nodes:
            self.nodes[id] = Node(id, data)
        return self.nodes[id]

    def add_edge(self, origin_id, destination_id):
        if origin_id in self.nodes and destination_id in self.nodes:
            origin = self.nodes[origin_id]
            destination = self.nodes[destination_id]
            edge = Edge(origin, destination)
            self.edges.append(edge)
            origin.add_neighbor(destination)
            if not self.directed:
                destination.add_neighbor(origin)

    def is_fulfilled(self, node):
        return node.data == "Finish"

    def search_bfs(self, start_id):
        if start_id not in self.nodes:
            return False

        search_queue = deque()
        search_queue.append(self.nodes[start_id])
        visited = set()
        predecessors = {self.nodes[start_id]: None}

        while search_queue:
            node = search_queue.popleft()
            if node not in visited:
                if self.is_fulfilled(node):
                    print(f"{node.id} fulfils the condition")
                    path = []
                    while node:
                        path.append(node.id)
                        node = predecessors[node]
                    print("Path:", " -> ".join(path[::-1]))
                    return True
                else:
                    visited.add(node)
                    for neighbor in node.neighbors:
                        if neighbor not in visited and neighbor not in predecessors:
                            search_queue.append(neighbor)
                            predecessors[neighbor] = node
        return False

    def search_dfs(self, start_id):
        if start_id not in self.nodes:
            return False

        # Initialize the search state
        visited = {node_id: False for node_id in self.nodes}
        component = []

        def dfs(node_id):
            node = self.nodes[node_id]
            component.append(node.id)
            visited[node_id] = True
            print(f"Visiting {node.id}, Neighbors: {[neighbor.id for neighbor in node.neighbors]}")

            for neighbor in node.neighbors:
                if not visited[neighbor.id]:
                    dfs(neighbor.id)
                    print(f"Finaliza {neighbor.id}")
                    print(f"Vuelve a {node.id}")
                    print()

        # Start the DFS from the start node
        dfs(start_id)
        print("DFS Component:", " -> ".join(component))
        return component

    def __str__(self):
        result = "Nodes:\n"
        for node in self.nodes.values():
            result += str(node) + "\n"
        result += "Edges:\n"
        for edge in self.edges:
            result += str(edge) + "\n"
        return result
