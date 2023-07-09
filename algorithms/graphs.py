from abc import ABC, abstractmethod


class Graph(ABC):
    data: ...
    is_directed: bool

    def __str__(self):
        return str(self.data)

    @abstractmethod
    def add_vertex(self, vertex):
        pass

    @abstractmethod
    def add_edge(self, source, to):
        pass

    @abstractmethod
    def remove_edge(self, source, to):
        pass


class AdjacencyListGraph(Graph):
    data: dict[int, list[int]]

    def __init__(self, is_directed=False):
        self.data = {}
        self.is_directed = is_directed

    def add_vertex(self, vertex):
        if vertex not in self.data:
            self.data[vertex] = []

    def add_edge(self, source, to):
        try:
            self.data[source].append(to)
            if not self.is_directed:
                self.data[to].append(source)
        except KeyError:
            raise Exception("Cannot create edge from/to unexisting vertex")

    def remove_edge(self, source, to):
        try:
            self.data[source].remove(to)
            if not self.is_directed:
                self.data[to].remove(source)
        except KeyError:
            raise Exception("Cannot remove edge from/to unexisting vertex")


class AdjacencyMatrixGraph(Graph):
    data: list[list[int]]
    vertex_number: int

    def __init__(self, vertex_number, is_directed=False):
        self.vertex_number = vertex_number
        self.is_directed = is_directed
        self.data = [[0] * vertex_number for _ in range(vertex_number)]

    def add_vertex(self, vertex):
        self.vertex_number += 1
        for row in self.data:
            row.append(0)
        self.data.append([0] * self.vertex_number)

    def add_edge(self, source, to):
        self.data[source - 1][to - 1] = 1
        if not self.is_directed:
            self.data[to - 1][source - 1] = 1

    def remove_edge(self, source, to):
        self.data[source][to] = 0
        if not self.is_directed:
            self.data[to][source] = 0
