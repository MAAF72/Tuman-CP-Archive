from collections import defaultdict, deque


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

g = Graph()

kode = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    dungeon = []
    num = 1
    for j in range(n):
        path = list(input())
        for item in range(len(path)):
            if path[item] == 'S':
                path[item] = kode[0]
                g.add_node(kode[0])
            elif path[item] == 'E':
                path[item] = kode[25]
                g.add_node(kode[25])
            elif path[item] != '#':
                path[item] = kode[num]
                g.add_node(kode[num])
                num += 1
        dungeon.append(path)

    for x in range(n):
        for y in range(m):
            countwall = 0
            if dungeon[x][y] != '#':
                for x1 in range(x,n):
                    for y1 in range(y,m):
                        if dungeon[x1][y1] == '#':
                            countwall += 1
                        else:
                            g.add_edge(dungeon[x][y], dungeon[x1][y1], countwall**2)
                            g.add_edge(dungeon[x1][y1], dungeon[x][y], countwall**2)

    print("shortest path: ", shortest_path(g, 'a', 'z'))