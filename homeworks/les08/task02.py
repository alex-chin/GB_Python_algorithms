"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
"""


# Очередь с приоритетами на основе словаря

class PriorityDictionary(dict):
    def __init__(self):
        self.__heap = []
        dict.__init__(self)

    def smallest(self):
        if len(self) == 0:
            raise IndexError
        heap = self.__heap
        while heap[0][1] not in self or self[heap[0][1]] != heap[0][0]:
            lastItem = heap.pop()
            insertionPoint = 0
            while 1:
                smallChild = 2 * insertionPoint + 1
                if smallChild + 1 < len(heap) and \
                        heap[smallChild] > heap[smallChild + 1]:
                    smallChild += 1
                if smallChild >= len(heap) or lastItem <= heap[smallChild]:
                    heap[insertionPoint] = lastItem
                    break
                heap[insertionPoint] = heap[smallChild]
                insertionPoint = smallChild
        return heap[0][1]

    def __iter__(self):
        def iterfn():
            while len(self) > 0:
                x = self.smallest()
                yield x
                del self[x]

        return iterfn()

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        heap = self.__heap
        if len(heap) > 2 * len(self):
            self.__heap = [(v, k) for k, v in self.iteritems()]
            self.__heap.sort()
        else:
            newPair = (val, key)
            insertionPoint = len(heap)
            heap.append(None)
            while insertionPoint > 0 and \
                    newPair < heap[(insertionPoint - 1) // 2]:
                heap[insertionPoint] = heap[(insertionPoint - 1) // 2]
                insertionPoint = (insertionPoint - 1) // 2
            heap[insertionPoint] = newPair

    def setdefault(self, key, val):
        if key not in self:
            self[key] = val
        return self[key]


# Нахождение кратчайшего пути от начальной вершины до заданной

def Dijkstra(graph, start, end=None):
    final_distances = {}
    parent = {}
    cost = PriorityDictionary()
    cost[start] = 0

    for vertex in cost:
        final_distances[vertex] = cost[vertex]
        if vertex == end:
            break

        for edge in graph[vertex]:
            cost_distance = final_distances[vertex] + graph[vertex][edge]
            if edge in final_distances:
                if cost_distance < final_distances[edge]:
                    raise ValueError
            elif edge not in cost or cost_distance < cost[edge]:
                cost[edge] = cost_distance
                parent[edge] = vertex

    return final_distances, parent


# преобразование в список вершин

def shortestPath(graph, start, end):
    final_distances, parent = Dijkstra(graph, start, end)
    path = []
    while 1:
        path.append(end)
        if end == start:
            break
        if end not in parent:
            path.append(float('inf'))
            break
        end = parent[end]
    path.reverse()
    return path


G = {0: {3: 1, 4: 9, 2: 1}, 1: {3: 4, 6: 7}, 2: {4: 3, 6: 6, 1: 9}, 3: {}, 4: {6: 1}, 5: {6: 5}, 6: {5: 1, 2: 7, 4: 8},
     7: {5: 1, 6: 2}}

print("Все пути в графе от вершины 0")
for end in range(len(G)):
    print(f' {end} - {shortestPath(G, 0, end)}')
