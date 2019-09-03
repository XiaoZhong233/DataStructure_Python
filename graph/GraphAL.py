import heapq
import math


class GraphError(Exception):
    pass


# 邻接表实现无向网（图）（字典形式）
class GraphAL:
    def __init__(self, graph={}):
        self._graph = graph
        self._vnum = len(graph)

    def _invalid(self, vertex):
        return self._graph.__contains__(vertex)

    def add_vertex(self, vertex):
        if self._invalid(vertex):
            raise GraphError("添加顶点失败，已经有该顶点")
        self._graph[vertex] = {}
        self._vnum += 1

    def add_edge(self, vi, vj, val):
        if not self._invalid(vi) or not self._invalid(vj):
            raise GraphError("不存在" + vi + "或者" + vj + "这样的顶点")
        self._graph[vi].update({vj: val})
        self._graph[vj].update({vi: val})

    def get_edge(self, vi, vj):
        if not self._invalid(vi) or not self._invalid(vj):
            raise GraphError("不存在" + vi + "或者" + vj + "这样的顶点")
        return self._graph[vi][vj]

    def get_vertexNum(self):
        return self._graph.__len__()

    # 在无向网（图）中是边，有向网（图）是出边，取决于数据
    def out_edge(self, vertex):
        if not self._invalid(vertex):
            raise GraphError("不存在" + vertex + "这样的顶点")
        return self._graph[vertex]

    # 广度优先遍历
    def bfs(self, start):
        if not self._invalid(start):
            raise GraphError("不存在" + start + "这样的顶点")
        queue = [start]  # 队列实现BFS
        seen = set(start)  # 记录访问过的顶点
        parent = {start: None}  # Node代表根节点，数组形式保存树
        result = []
        while queue.__len__() > 0:  # 队非空时
            vertex = queue.pop(0)  # 队首顶点出队
            nodes = self._graph[vertex]  # 获得其邻接顶点
            for node in nodes:
                if node not in seen:
                    queue.append(node)  # 其邻接顶点如果没有被访问，则入队，并且保留父顶点
                    seen.add(node)
                    parent[node] = vertex
            result.append(vertex)
        return result, parent

    # 深度优先遍历
    def dfs(self, start):
        if not self._invalid(start):
            raise GraphError("不存在" + start + "这样的顶点")
        stack = [start]  # 栈实现DFS
        seen = set(start)  # 记录访问过的顶点
        parent = {start: None}  # Node代表根节点，数组形式保存树
        result = []
        while stack.__len__() > 0:  # 栈非空时
            vertex = stack.pop()  # 顶点出栈
            nodes = self._graph[vertex]  # 获取出栈顶点的邻接顶点
            for node in nodes:
                if node not in seen:
                    stack.append(node)
                    seen.add(node)
                    parent[node] = vertex
            result.append(vertex)
        return result, parent

    # 检查两条边是否连通(无向图（网）)
    def isConnect(self, v1, v2):
        # and前的条件判断end是否与start建立过关系，如果没有则为true
        # end not in self._graph 表示在邻接表中没有这个end顶点
        # not self._graph[end] 表示虽然end顶点已经在邻接表中了，但是他的边为空，所以还是视作未被连通
        # return end not in self._graph[start] and (end not in self._graph or not self._graph[end])
        return self._invalid(v1) and self._invalid(v2) and v2 in self._graph[v1] and v1 in self._graph[v2] \
               and (self._graph[v1][v2] is not None and self._graph[v1][v2] is not math.inf
                    and self._graph[v1][v2] != '') \
               and (self._graph[v2][v1] is not None and self._graph[v2][v1] is not math.inf
                    and self._graph[v2][v1] != '')

    # prim算法，最小生成树，前提该图必须是连通网
    def prim(self, start):
        if not self._invalid(start):
            raise GraphError("不存在" + start + "这样的顶点")
        result = GraphAL({})
        edgeCount = 0
        pqueue = []  # 优先级队列,候选列表
        # 初始化优先级队列
        for node in self._graph[start]:
            heapq.heappush(pqueue, (self._graph[start][node], start, node))
            pass
        while edgeCount < self.get_vertexNum() - 1 and not pqueue.__len__() == 0:
            # 出队
            pair = heapq.heappop(pqueue)
            distance = pair[0]
            start = pair[1]
            end = pair[2]
            # 判断是否有该顶点,如果没有就要加入
            if start not in result._graph:
                result.add_vertex(start)
            if end not in result._graph:
                result.add_vertex(end)
            # 如果当前点与下一节点未建立边，则尝试建立边
            # 方式是检查下一节点是否在result中，如果有则说明这个节点已经建立过边了，再建立边的话会可能会形成连通，因此直接舍弃该边的建立
            if end not in result._graph[start]:
                # 如果下一个节点如果未被其他节点连接则result._graph[end]返回false，开始构造边，
                # 如果下一个节点已经被连接了，则result._graph[end]返回true，舍弃该边的建立
                if not result._graph[end]:
                    result.add_edge(start, end, distance)
                    edgeCount += 1
                    pass
            start = end
            # 子节点入队
            for node in self._graph[start]:
                if node not in result._graph:
                    heapq.heappush(pqueue, (self._graph[start][node], start, node))
            pass
        return result

    # kruskal算法，最小生成树，前提该图必须是连通网
    def kruskal(self):
        # 初始化代表元和结果图
        result, reps, pqueue, edgesCount = GraphAL(graph={}), {}, [], 0
        for key in self._graph.keys():
            reps[key] = key
        # 边入队，按优先级排序,选出最短边
        for key in self._graph:
            for end in self._graph[key].keys():
                edges = self._graph[key][end]
                heapq.heappush(pqueue, (edges, key, end))  # 边入队
            pass
        # 当边数达到n-1条时，即成功得到最小生成树时停止
        while edgesCount < self.get_vertexNum() - 1 and not pqueue.__len__() == 0:
            # 出队
            pair = list(heapq.heappop(pqueue))
            # 判断是否有该顶点,如果没有就要加入
            if pair[1] not in result._graph:
                result.add_vertex(pair[1])
            if pair[2] not in result._graph:
                result.add_vertex(pair[2])
            # 检查两点是否属于不同连通分量
            if reps[pair[1]] != reps[pair[2]]:
                result.add_edge(pair[1], pair[2], pair[0])
                edgesCount += 1
                # 合并连通分量
                rep, orep = reps[pair[1]], reps[pair[2]]
                for key in reps.keys():
                    if reps[key] == orep:
                        reps[key] = rep
        return result
        pass

    # 迪杰斯特拉法算最短路径
    def dijkstra(self, start):
        if not self._invalid(start):
            raise GraphError("不存在" + start + "这样的顶点")
        graph = self._graph
        pqueue = []  # 优先级队列
        heapq.heappush(pqueue, (0, start))  # 根顶点进队，最高优先级
        seen = set()  # 记录访问过的顶点
        parent = {start: None}  # 生成树
        distance = self.__init_distance(start)  # 初始化距离
        while pqueue.__len__() > 0:
            pair = heapq.heappop(pqueue)  # pop弹出的是元组，第一个参数是距离（优先级），第二个是顶点
            dist = pair[0]
            vertex = pair[1]
            seen.add(vertex)  # 记录访问过的顶点
            nodes = graph[vertex].keys()  # 获取其顶点的邻接顶点
            for node in nodes:
                if node not in seen:
                    if dist + graph[vertex][node] < distance[node]:  # 如果当前顶点到开始顶点的距离小于距离列表中的值，更新距离
                        heapq.heappush(pqueue, (dist + graph[vertex][node], node))
                        parent[node] = vertex
                        distance[node] = dist + graph[vertex][node]
            # 输出遍历结果
            # print(vertex)
        return distance, parent
        pass

    # 打印最短路径（迪杰斯特拉）
    def printMinPath(self, s, t):
        distance, parent = self.dijkstra(s)
        print("生成路径为：")
        print(parent)
        dis = distance[t]
        path = []
        target = t
        while t is not None:
            path.append(t)
            t = parent[t]
        path.reverse()
        pathStr = GraphAL.printPath(path)
        print(
            s.__str__() + "到" + target + "最短路径为：" + pathStr + " \n" + s.__str__() + "到" + target + "最短距离为：" + dis.__str__())

    # 初始化距离（为了实现按距离优先级排序）
    def __init_distance(self, s):
        distance = {s: 0}
        for vertex in self._graph:
            if vertex != s:
                distance[vertex] = math.inf
        return distance

    def __str__(self):
        s = ""
        for kv in self._graph.items():
            s += kv.__str__() + "\n"
        return s

    # 打印路径
    @staticmethod
    def printPath(path):
        return "->".join(str(i) for i in path)

    # 打印生成路径
    @staticmethod
    def printTreePath(path={}):
        paths = []
        # 获得每条树的路径，用数组保存
        for key in path.keys():
            pathstr = []
            if path[key] is None:
                # pathstr.append(key)
                pass
            else:
                start = key
                while start is not None:
                    pathstr.append(start)
                    start = path[start]
            paths.append(pathstr)
        # 生成路径字符串
        pathstrs = ''
        for path in paths:
            path.reverse()
            pathstrs += GraphAL.printPath(path) + "\n"
        return pathstrs
        pass
