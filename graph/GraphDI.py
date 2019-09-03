import heapq
import math


class GraphError(Exception):
    pass


# 有向网（图）
class GraphDI:
    def __init__(self, graph={}):
        self._graph = graph
        self._vnum = len(graph)

    def _invalid(self, vertex):
        return self._graph.__contains__(vertex)

    def add_vertex(self, vertex):
        if self._invalid(vertex):
            raise GraphError("添加顶点失败，已经有该顶点。")
        self._graph[vertex] = {}
        self._vnum += 1

    def add_edge(self, start, end, val):
        if not self._invalid(start) or not self._invalid(end):
            raise GraphError("不存在" + start + "或者" + end + "这样的顶点")
        self._graph[start].update({end: val})

    def get_edge(self, start, end):
        if not self._invalid(start) or not self._invalid(end):
            raise GraphError("不存在" + start + "或者" + end + "这样的顶点")
        return self._graph[start][end]

    def get_vertexNum(self):
        return self._graph.__len__()

    def get_outEdge(self, vertex):
        if not self._invalid(vertex):
            raise GraphError("不存在" + vertex + "这样的顶点")
        return self._graph[vertex]

    def get_inEdge(self, vertex):
        if not self._invalid(vertex):
            raise GraphError("不存在" + vertex + "这样的顶点")
        result = {}
        for start in self._graph:
            if vertex in self._graph[start]:
                if self._graph[start][vertex] is not None:
                    result[start] = self._graph[start][vertex]
        return result

    # 拓扑排序
    def topological_sort(self):
        indegree = {}  # 入度表
        zerov = []  # 利用0度栈记录已知的入度为0的但还未处理的顶点
        m = 0  # 输出顶点计数
        topo = []  # 拓扑排序结果
        # 生成入度表和0度栈
        for vetx in self._graph:
            indegree[vetx] = self.get_inEdge(vetx).__len__()
            if indegree[vetx] == 0:
                zerov.append(vetx)
            pass

        while zerov.__len__() != 0:
            Vi = zerov.pop()
            topo.append(Vi)
            m += 1
            for Vj in self.get_outEdge(Vi).keys():  # 对顶点Vi的每个邻接点入度减1，如果Vj的入度变为0，则将Vj入栈，表示Vj就是下一个需要处理的顶点
                indegree[Vj] -= 1
                if indegree[Vj] == 0:
                    zerov.append(Vj)

        if m < self.get_vertexNum():  # 该有向图有回路
            return False
        return topo

    # 关键路径
    def criticalPath(self, delay=0):
        topo = self.topological_sort()
        if not topo:
            raise GraphError("存在有向环！")
        ve = [0 for i in range(len(topo))]  # 事件最早开始时间
        vl = [0 for i in range(len(topo))]  # 事件最迟开始时间
        cp = []  # 关键路径
        result = {}  # 返回结果
        # --------------------------------计算事件的最早发生时间-------------------------------------------------------
        for i in range(topo.__len__()):
            start = topo[i]  # 取出拓扑节点
            for node in self.get_outEdge(start).keys():  # 获取拓扑节点的邻接点，计算ve
                w = self._graph[start][node]  # 当前节点与邻接节点的边
                j = topo.index(node)  # 邻接节点的下标
                if ve[j] < ve[i] + w:  # 更新邻接点的最早发生时间，选大的时间
                    ve[j] = ve[i] + w
                pass
        # --------------------------------计算事件的最晚发生时间-------------------------------------------------------
        for i in range(topo.__len__()):  # 给每个事件的最迟发生时间置初值，初值为最早发生时间中的最大值
            vl[i] = ve[topo.__len__() - 1] + delay
        for i in reversed(range(topo.__len__())):
            k = topo[i]  # 取出拓扑节点
            for node in self.get_inEdge(k).keys():  # 获取拓扑节点的逆邻接点，计算vl
                w = self._graph[node][k]  # 逆邻接点和当前节点的边
                j = topo.index(node)  # 逆邻接点的下标
                if vl[j] > vl[i] - w:  # 更新逆邻接点的最晚发生时间，选小的时间
                    vl[j] = vl[i] - w
                pass
        # --------------------------------判断每一活动是否为关键路径---------------------------------------------------
        for i in range(topo.__len__()):
            start = topo[i]
            for node in self.get_outEdge(start).keys():
                j = topo.index(node)  # 获得邻接顶点的下标
                w = self._graph[start][node]  # 当前节点与邻接节点的边
                e = ve[i]  # 计算活动<start,node>的最早开始时间
                l = vl[j] - w - delay  # 计算活动<start,node>的最晚开始时间
                if e == l:
                    cp.append((start, node))  # 如果相等就说明为关键路径
                pass

        for i in range(topo.__len__()):
            result[topo[i]] = (ve[i], vl[i])
            pass
        return result, cp

    def __str__(self):
        s = ""
        for kv in self._graph.items():
            s += kv.__str__() + "\n"
        return s
