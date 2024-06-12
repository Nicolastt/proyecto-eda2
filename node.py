class Node:
    def __init__(self, id, data=None):
        self.id = id
        self.data = data
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def __str__(self):
        return f"Node({self.id}, {self.data})"
