import heapq
from abc import ABC, abstractmethod


class Graph(ABC):
    data: ...
    is_directed: bool

    def __str__(self):
        return str(self.data)

    @abstractmethod
    def add_edge(self, source, to):
        pass


class AdjacencyListGraph(Graph):
    data: dict[int, list[tuple[int, int]]]

    def __init__(self, is_directed=False):
        self.data = {}
        self.is_directed = is_directed

    def add_vertex(self, vertex):
        if vertex not in self.data:
            self.data[vertex] = []

    @property
    def vertices(self):
        return self.data.keys()

    def add_edge(self, source, to, weight=1):
        try:
            self.data[source].append((to, weight))
            if not self.is_directed:
                self.data[to].append((source, weight))
        except KeyError:
            raise Exception("Cannot create edge from/to unexisting vertex")

    def remove_edge(self, source, to, weight):
        try:
            self.data[source].remove((to, weight))
            if not self.is_directed:
                self.data[to].remove((source, weight))
        except KeyError:
            raise Exception("Cannot remove edge from/to unexisting vertex")

    def get_edge_weight(self, source, to):
        for edge in self.data[source]:
            if edge[0] == to:
                return edge[1]

    def get_neighbours(self, current_vertex):
        return [vertex for vertex, _ in self.data[current_vertex]]

    def breadth_first_search(self, starting_vertex):
        queue = [starting_vertex]
        visited_vertices = {starting_vertex}
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=" ")
            for neighbour in self.get_neighbours(current_vertex):
                if neighbour not in visited_vertices:
                    queue.append(neighbour)
            visited_vertices.add(current_vertex)

    @property
    def is_acyclic(self):
        if not self.is_directed:
            return False
        visited_vertices = set()
        for vertex in self.vertices:
            if vertex in visited_vertices:
                continue
            visited_in_one_going = set()
            stack = [vertex]
            while stack:
                current_vertex = stack.pop()
                visited_vertices.add(current_vertex)
                visited_in_one_going.add(current_vertex)
                for neighbour in self.get_neighbours(current_vertex):
                    if neighbour in visited_in_one_going:
                        return False
                    if neighbour not in visited_vertices:
                        stack.append(neighbour)
        return True

    def _topological_sort_helper(self, vertex, visited, sorted_graph):
        visited.add(vertex)
        for neighbour in self.get_neighbours(vertex):
            if neighbour not in visited:
                self._topological_sort_helper(neighbour, visited, sorted_graph)
        sorted_graph.append(vertex)

    def topological_sort(self):
        if not self.is_acyclic:
            raise Exception("Can perform topological sort only in DAG.")
        visited_vertices = set()
        sorted_graph = []
        for vertex in self.vertices:
            if vertex not in visited_vertices:
                self._topological_sort_helper(vertex, visited_vertices, sorted_graph)
        return sorted_graph

    def dijkstra(self, start_vertex):
        shortest_paths = {vertex: float("inf") for vertex in self.vertices}

        priority_queue = [(0, start_vertex)]
        shortest_paths[start_vertex] = 0

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > shortest_paths[current_vertex]:
                continue

            neighbours = self.get_neighbours(current_vertex)
            for neighbour in neighbours:
                edge_weight = self.get_edge_weight(current_vertex, neighbour)
                possible_shortest_path = current_distance + edge_weight
                if possible_shortest_path < shortest_paths[neighbour]:
                    shortest_paths[neighbour] = possible_shortest_path
                    heapq.heappush(priority_queue, (possible_shortest_path, neighbour))

        return shortest_paths


class AdjacencyMatrixGraph(Graph):
    data: list[list[int]]
    vertex_number: int

    def __init__(self, vertex_number, is_directed=False):
        self.vertex_number = vertex_number
        self.is_directed = is_directed
        self.data = [[0] * vertex_number for _ in range(vertex_number)]

    def add_edge(self, source, to):
        self.data[source - 1][to - 1] = 1
        if not self.is_directed:
            self.data[to - 1][source - 1] = 1

    def remove_edge(self, source, to):
        self.data[source][to] = 0
        if not self.is_directed:
            self.data[to][source] = 0

    def get_neighbours(self, current_vertex):
        return [index for index, value in enumerate(self.data[current_vertex]) if value]

    def depth_first_search(self, starting_vertex):
        stack = [starting_vertex]
        visited_vertices = {starting_vertex}
        while stack:
            current_vertex = stack.pop()
            print(current_vertex, end=" ")
            for neighbour in self.get_neighbours(current_vertex):
                if neighbour not in visited_vertices:
                    stack.append(neighbour)
            visited_vertices.add(current_vertex)
