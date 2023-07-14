from graphs import AdjacencyListGraph, AdjacencyMatrixGraph

if __name__ == '__main__':
    list_graph = AdjacencyListGraph(is_directed=True)
    for vertex in (-1, -2, 1, 2, 3, 4):
        list_graph.add_vertex(vertex)

    list_graph.add_edge(2, 1)
    list_graph.add_edge(2, 3)
    list_graph.add_edge(1, -2)
    list_graph.add_edge(-2, -1)
    list_graph.add_edge(3, 4)

    print(list_graph)

    matrix_graph = AdjacencyMatrixGraph(is_directed=True, vertex_number=4)

    matrix_graph.add_edge(1, 2)
    matrix_graph.add_edge(3, 2)
    matrix_graph.add_edge(4, 2)
    matrix_graph.add_edge(2, 3)
    matrix_graph.add_edge(3, 4)

    print(matrix_graph)

    list_graph.breadth_first_search(2)
    print("\n--------------")
    matrix_graph.depth_first_search(0)
