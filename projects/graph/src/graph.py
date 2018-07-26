"""
Simple graph implementation compatible with BokehGraph class.
"""
from draw import BokehGraph


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge from start to end."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Error - vertices not in graph!")
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def search(self, start, target=None, method="dfs"):
        """Search the graph using BFS or DFS."""
        quack = [start]  # Queue or stack, depending on method
        pop_index = 0 if method == "bfs" else -1
        visited = set()

        while quack:
            current = quack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            # Add possible (unvisited) vertices to queue
            quack.extend(self.vertices[current] - visited)

        return visited


def main():
    from graph import Graph

    graph = Graph()
    graph.add_vertex("0")
    graph.add_vertex("1")
    graph.add_vertex("2")
    graph.add_vertex("3")
    graph.add_edge("0", "1")
    graph.add_edge("0", "3")
    bg = BokehGraph(graph)
    bg.show()


if __name__ == "__main__":
    main()
