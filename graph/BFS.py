# 构造数据,邻接表
graph = {
    "A": ["B", "C"],
    "B": ["A", "B", "C"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def BFS(graph, s):
    queue = [s]
    seen = set(s)
    # 生成树
    parent = {s: None}
    while len(queue) > 0:
        vertex = queue.pop(0)
        # 放入邻接点
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
                parent[node] = vertex
        # 输出遍历结果
        print(vertex)
    return parent
    pass


parent = BFS(graph, "A")
print('生成树：')
for key in parent:
    print(key, parent[key])
print('D到根的最短路径：')
v = 'D'
while v != None:
    print(v, end=' ')
    v = parent[v]
