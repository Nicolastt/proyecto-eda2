from graph import Graph
# Proyecto EDA 2 Primer Bimestre

graph = Graph()
graph.add_node("R1", "Start")
graph.add_node("R2", "Quito")
graph.add_node("R3", "Guayaquil")
graph.add_node("R4", "Cuenca")
graph.add_node("R5", "Ambato")
graph.add_node("R6", "Puyo")
graph.add_node("R7", "Tena")
graph.add_node("R8", "Ibarra")
graph.add_node("R9", "Manabi")
graph.add_node("R10", "Finish")

graph.add_edge("R1", "R8")
graph.add_edge("R8", "R2")
graph.add_edge("R2", "R9")
graph.add_edge("R2", "R5")
graph.add_edge("R9", "R3")
graph.add_edge("R3", "R4")
graph.add_edge("R4", "R10")
graph.add_edge("R1", "R7")
graph.add_edge("R7", "R5")
graph.add_edge("R7", "R6")
graph.add_edge("R6", "R4")

print(graph)

found_bfs = graph.search_bfs("R1")
print("BFS Encontrado:", found_bfs)
print()

dfs_component = graph.search_dfs("R1")
print("DFS Componente:", dfs_component)

