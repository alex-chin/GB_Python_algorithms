"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
import random
import vis_graph


def gen_graph(num):
    graph = {}
    for n in range(num):
        roots = list(range(num))
        del roots[n]
        graph[n] = set(random.sample(roots, random.choice([2, 2])))
    return graph


def recursive_dfs(graph, source, path=[]):
    if source not in path:

        path.append(source)

        if source not in graph:
            # leaf node, backtrack
            return path

        for neighbour in graph[source]:
            path = recursive_dfs(graph, neighbour, path)

    return path


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    # print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


g = gen_graph(10)

print(g)
print(recursive_dfs(g, 0))
print(dfs(g, 0))

vis_graph.GraphVisualization().render(g)
