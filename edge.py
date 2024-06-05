class Edge:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

    def __str__(self):
        return f"Edge({self.origin.id} -> {self.destination.id})"
