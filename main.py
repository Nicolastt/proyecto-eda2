from graph import Graph


def load_graph_from_file(filename, graph):
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if parts[0] == 'NODE':
                graph.add_node(parts[1], parts[2])
            elif parts[0] == 'EDGE':
                graph.add_edge(parts[1], parts[2])


graph = Graph()
load_graph_from_file('graph_data.txt', graph)

print(graph)

print("-------- BFS --------")
found_bfs = graph.search_bfs("R1")

print()
print("-------- DFS --------")
dfs_component = graph.search_dfs("R1")
