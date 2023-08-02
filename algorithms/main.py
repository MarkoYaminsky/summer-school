from graphs import AdjacencyListGraph, AdjacencyMatrixGraph

if __name__ == "__main__":
    weighted_graph = AdjacencyListGraph()
    for vertex in range(1, 8):
        weighted_graph.add_vertex(vertex)

    weighted_graph.add_edge(1, 2, 1)
    weighted_graph.add_edge(1, 3, 15)
    weighted_graph.add_edge(2, 4, 2)
    weighted_graph.add_edge(3, 5, 14)
    weighted_graph.add_edge(4, 5, 2)
    weighted_graph.add_edge(4, 6, 3)
    weighted_graph.add_edge(3, 7, 1)
    weighted_graph.add_edge(6, 7, 7)

    print(weighted_graph.dijkstra(1))
