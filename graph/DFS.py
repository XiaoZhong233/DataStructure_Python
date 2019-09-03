# 构造数据,邻接表
graph = {
    "A": ["B", "C"],
    "B": ["A", "B", "C"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def DFS(graph, s):
    stack = [s]
    seen = set()
    seen.add(s)
    while len(stack) > 0:
        vertex = stack.pop()
        # 放入邻接点
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print(vertex)
    pass


DFS(graph, "E")
