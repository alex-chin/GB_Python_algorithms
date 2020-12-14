# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt


# Defining a Class
class GraphVisualization:

    def __init__(self):
        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.visual = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

    # Driver code
    def render(self, graph):
        for key_from, v_from in graph.items():
            for v in v_from:
                self.addEdge(key_from, v)
        self.visualize()


# G = GraphVisualization()
# graph = {0: {1, 4}, 1: {2, 4}, 2: {1, 3}, 3: {1, 2}, 4: {0, 2}}
# graph = {0: {1, 4}, 1: {0, 3}, 2: {0, 3}, 3: {0, 4}, 4: {1, 3}}
# graph = {0: {1, 2, 3, 4}, 1: {0, 3}, 2: {1, 3}, 3: {0, 2}, 4: {0, 3}}
# graph = {0: {1, 3, 4, 6}, 1: {0, 8, 3, 6}, 2: {9, 5}, 3: {8, 7}, 4: {1, 2, 3, 7}, 5: {8, 2}, 6: {9, 2, 5, 7}, 7: {8, 1}, 8: {0, 2, 3, 7}, 9: {8, 3}}
# graph = {0: {5, 6}, 1: {2, 4}, 2: {3, 7}, 3: {0, 7}, 4: {0, 9}, 5: {8, 1}, 6: {8, 1}, 7: {8, 9}, 8: {1, 6}, 9: {1, 7}}
# graph = {0: {8, 5}, 1: {3, 7}, 2: {9, 7}, 3: {9, 7}, 4: {8, 9}, 5: {2, 7}, 6: {2, 3}, 7: {1, 4}, 8: {5, 7}, 9: {4, 7}}
# [0, 8, 5, 2, 9, 4, 7, 1, 3]

# G.render(graph)
# for key_from, v_from in graph.items():
#     for v in v_from:
#         G.addEdge(key_from, v)

# G.addEdge(0, 2)
# G.addEdge(1, 2)
# G.addEdge(1, 3)
# G.addEdge(5, 3)
# G.addEdge(3, 4)
# G.addEdge(1, 0)

# G.visualize()
