import networkx as nx
import matplotlib.pyplot as plt


class GraphVisualization:

    def __init__(self):
        # the set of edges that constitutes a
        self.visual = []

    #  inputs edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # creates a graph with a given list
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        # plots the graph
        nx.draw_networkx(G)
        # displays the graph
        plt.show()

    def render(self, graph):
        for key_from, v_from in graph.items():
            for v in v_from:
                self.addEdge(key_from, v)
        self.visualize()


if __name__ == '__main__':
    graph = {0: {8, 5}, 1: {3, 7}, 2: {9, 7}, 3: {9, 7}, 4: {8, 9}, 5: {2, 7}, 6: {2, 3}, 7: {1, 4}, 8: {5, 7},
             9: {4, 7}}
    # [0, 8, 5, 2, 9, 4, 7, 1, 3]
    GraphVisualization().render(graph)
