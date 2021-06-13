class Graph:
    def __init__(self, graph_dict: dict[str, list[str]] = None) -> None:
        if graph_dict is None:
            self.vertices: dict[str, list[str]] = {}
        else:
            self.vertices = graph_dict

    def adjacency_list(self) -> str:
        result: str = ''
        for vertex in self.vertices:
            result += f"{vertex} : {' -> '.join((str(tmp) for tmp in self.vertices[vertex]))}\n"
        return result

    def adjacency_matrix(self) -> str:
        matrix = []
        for key in self.vertices.keys():
            tmp_matrix = []
            for elem in self.vertices.keys():
                if elem in self.vertices[key]:
                    tmp_matrix.append(1)
                else:
                    tmp_matrix.append(0)
            matrix.append(tmp_matrix)

        result: str = f"  {' '.join((str(key) for key in self.vertices.keys()))}\n"
        for index, key in enumerate(self.vertices.keys()):
            result += f"{key} {' '.join((str(_) for _ in matrix[index]))}\n"
        return result

    def add_edge(self, starting_vertex: str, ending_vertex: str) -> None:
        if starting_vertex in self.vertices:
            self.vertices[starting_vertex].append(ending_vertex)
        else:
            self.vertices[starting_vertex] = [ending_vertex]

    def bfs(self, starting_vertex: str) -> str:
        if starting_vertex not in self.vertices:
            return 'Starting vertex not in Graph'
        result = ''
        visited = set()
        queue = []
        visited.add(starting_vertex)
        queue.append(starting_vertex)
        result += f"grey {queue[0]} | {queue[0]}\n"
        while queue:
            vertex = queue[0]
            for adj_vert in self.vertices[vertex]:
                if adj_vert not in visited:
                    queue.append(adj_vert)
                    visited.add(adj_vert)
                    result += f"grey {adj_vert} | {' '.join((str(q) for q in queue))}\n"
            result += f"black {queue[0]} | {' '.join((str(q) for q in queue[1:]))}\n"
            queue.pop(0)
        return result

    def dfs(self, starting_index: str) -> str:
        explored, stack = set(starting_index), [starting_index]
        result: str = ''
        while stack:
            vertex = stack[0]
            explored.add(vertex)
            for adj in self.vertices[vertex]:
                if adj not in explored:
                    stack.append(adj)
            result += (f"From {stack[0]} visit -> {' -> '.join((str(tmp) + (' ( visited )' if tmp in explored else ' ( not visited )') for tmp in self.vertices[stack[0]]))}\n")
            stack.pop(0)
        return result


if __name__ == '__main__':
    graph1 = {
        '1': ['2', '5', '4'],
        '2': ['1'],
        '3': ['5'],
        '4': ['1', '5'],
        '5': ['1', '4', '3', '6'],
        '6': ['5']
    }
    graph = {
        'a': ['b', 'c', 'd'],
        'b': ['a', 'e', 'f'],
        'c': ['a', 'g', 'h'],
        'd': ['a'],
        'e': ['b'],
        'f': ['b'],
        'g': ['c'],
        'h': ['c']
    }
    g = Graph(graph)
    print(g.adjacency_matrix())
    print(g.adjacency_list())
    print(g.bfs('b'))
    print(g.dfs('b'))
