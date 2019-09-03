import heapq
import math
# 构造数据,邻接表
graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6},
}


def init_distance(graph, s):
    distance = {s: 0}
    for vertex in graph:
        if vertex != s:
            distance[vertex] = math.inf
    return distance


def dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    # 最小生成树
    parent = {s: None}
    distance = init_distance(graph, s)
    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)
        # 放入邻接点
        nodes = graph[vertex].keys()
        for node in nodes:
            if node not in seen:
                if dist + graph[vertex][node] < distance[node]:
                    heapq.heappush(pqueue, (dist + graph[vertex][node], node))
                    parent[node] = vertex
                    distance[node] = dist + graph[vertex][node]
        # 输出遍历结果
        # print(vertex)
    return parent, distance
    pass


def getMinPath(graph, s, t):
    parent, distance = dijkstra(graph, s)
    dis = distance[t]
    path = ""
    while t != None:
        path += t + " "
        t = parent[t]
    return path, dis


parent, distance = dijkstra(graph, "A")
print(parent)
print(distance)

print('E到A的最短路径：')
path, dis = getMinPath(graph, 'A', 'E')
print(path)
print("长度为：", dis)

