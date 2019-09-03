class GraphError(Exception):
    pass


# unconn 无关联参数
# 邻接矩阵实现
class Graph:
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        # 检查是否为方阵
        for x in mat:
            if len(x) != vnum:
                raise ValueError("参数错误：不为方阵")
        # 拷贝数据
        self._mat = [mat[i][:] for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum

    def vertex_num(self):
        return self._vnum

    def _invalid(self, v):
        return v < 0 or v >= self._vnum

    def add_vertex(self):
        raise GraphError("邻接矩阵不支持加入顶点")

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError("顶点不合法")
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError("顶点不合法")
        return self._mat[vi][vj]

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError("顶点不合法")
        return self.out_edge(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

    def __str__(self):
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]" \
               + "\nUnconnected: " + str(self._unconn)


# 邻接表实现（压缩邻接矩阵形式）
class GraphAL(Graph):
    def __init__(self, mat=[], unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("参数错误：不为方阵")
        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise GraphError("无法为空图增加边")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError("顶点不合法")

        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj:  # 没有到与vj的边，退出循环加入边
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError("顶点不合法")
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError("顶点不合法")
        return self._mat[vi]
