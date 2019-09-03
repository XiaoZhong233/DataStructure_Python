import graph.GraphAL as graph
import graph.GraphDI as graphdi
import unittest


class TestGraph(unittest.TestCase):
    g = None
    data = {
        "A": {"B": 5, "C": 1},
        "B": {"A": 5, "C": 2, "D": 1},
        "C": {"A": 1, "B": 2, "D": 4, "E": 8},
        "D": {"B": 1, "C": 4, "E": 3, "F": 6},
        "E": {"C": 8, "D": 3},
        "F": {"D": 6},
    }

    # 连通网
    data2 = {
        "V1": {"V2": 6, "V3": 1, "V4": 5},
        "V2": {"V1": 6, "V3": 5, "V5": 3},
        "V3": {"V1": 1, "V2": 5, "V4": 5, "V5": 6, "V6": 4},
        "V4": {"V1": 5, "V3": 5, "V6": 2},
        "V5": {"V2": 3, "V3": 6, "V6": 6},
        "V6": {"V3": 4, "V4": 2, "V5": 6},
    }

    # 连通网
    data3 = {
        "a": {"c": 11, "d": 5, "b": 5},
        "b": {"a": 5, "d": 3, "g": 7, "e": 9},
        "c": {"a": 11, "d": 7, "f": 6},
        "d": {"a": 5, "b": 3, "c": 7, "g": 20},
        "e": {"b": 9, "g": 8},
        "f": {"c": 6, "g": 8},
        "g": {"f": 8, "d": 20, "b": 7, "e": 8},

    }

    # 连通网
    data4 = {
        'a': {'b': 19, 'e': 14, 'g': 18},
        'b': {'a': 19, 'e': 12, 'd': 7, 'c': 5},
        'c': {'b': 5, 'd': 3},
        'd': {'c': 5, 'b': 7, 'e': 8, 'f': 21},
        'e': {'a': 14, 'b': 12, 'd': 8, 'g': 16},
        'f': {'d': 21, 'g': 27},
        'g': {'a': 18, 'e': 16, 'f': 27}
    }

    # 有向网AOE
    data5 = {
        'V0': {'V1': 6, 'V2': 4, 'V3': 5},
        'V1': {'V4': 1},
        'V2': {'V4': 1},
        'V3': {'V5': 2},
        'V4': {'V6': 9, 'V7': 7},
        'V5': {'V7': 4},
        'V6': {'V8': 2},
        'V7': {'V8': 4},
        'V8': {}
    }

    # 有向回环图
    data6 = {
        'V0': {'V1': 0},
        'V1': {'V2': 0},
        'V2': {'V3': 0},
        'V3': {'V1': 0},
    }

    # 有向图AOV
    data7 = {
        'C1': {'C4': 0, 'C2': 0, 'C12': 0},
        'C2': {'C3': 0},
        'C3': {'C5': 0, 'C7': 0, 'C8': 0},
        'C4': {'C5': 0},
        'C5': {'C7': 0},
        'C6': {'C8': 0},
        'C7': {},
        'C8': {},
        'C9': {'C10': 0, 'C11': 0, 'C12': 0},
        'C10': {'C12': 0},
        'C11': {'C6': 0},
        'C12': {},
    }

    courseData = {
        'C1': '程序设计基础',
        'C2': '离散数学',
        'C3': '数据结构',
        'C4': '汇编语言',
        'C5': '高级语言程序设计',
        'C6': '计算机原理',
        'C7': '编译原理',
        'C8': '操作系统',
        'C9': '高度数学',
        'C10': '线性代数',
        'C11': '普通物理',
        'C12': '数值分析'
    }

    g = graph.GraphAL(graph=data)
    print("图的结构为：")
    print(g)

    @classmethod
    def setUpClass(cls):
        print("图的结构为：")
        print(TestGraph.g)
        pass

    def setUp(self):
        print()

    def tearDown(self):
        print("------------------------测试完成-----------------------------------\n")

    def test_dfs(self):
        print("dfs测试：")
        dfs, dfsparent = TestGraph.g.dfs("A")
        print("DFS:" + graph.GraphAL.printPath(dfs))
        print("DFS生成路径:" + dfsparent.__str__())
        print("DFS生成路径打印：" + graph.GraphAL.printTreePath(dfsparent).__str__())
        pass

    def test_bfs(self):
        print("bfs测试：")
        bfs, bfsparent = TestGraph.g.bfs("A")
        print("BFS:" + graph.GraphAL.printPath(bfs))
        print("BFS生成路径:" + bfsparent.__str__())
        print("BFS生成路径打印：" + graph.GraphAL.printTreePath(bfsparent).__str__())
        pass

    def test_dijkstra(self):
        print("迪杰斯特拉测试：")
        TestGraph.g.printMinPath("A", "E")
        distance, parent = TestGraph.g.dijkstra('A')
        print("各个顶点到A的最短路径打印:" + graph.GraphAL.printTreePath(parent).__str__())
        print("距离为：\n" + distance.__str__())
        pass

    def test_prim(self):
        print("测试普里姆算法")
        TestGraph.g._graph = TestGraph.data2
        result1 = TestGraph.g.prim('V1')
        # TestGraph.g._graph = TestGraph.data3
        # result2 = TestGraph.g.prim('a')
        # TestGraph.g._graph = TestGraph.data4
        # result3 = TestGraph.g.prim('a')
        print(result1)
        # print(result2)
        # print(result3)

    def test_kruskal(self):
        print("测试克鲁斯卡尔算法")
        TestGraph.g._graph = TestGraph.data2
        result1 = TestGraph.g.kruskal()
        print(result1)
        # TestGraph.g._graph = TestGraph.data3
        # result2 = TestGraph.g.kruskal()
        # print(result2)
        # TestGraph.g._graph = TestGraph.data4
        # result3 = TestGraph.g.kruskal()
        # print(result3)
        # TestGraph.g._graph = TestGraph.data
        pass

    def test_topological_sort(self):
        print("拓扑排序测试")
        gd = graphdi.GraphDI(TestGraph.data5)
        result = gd.topological_sort()
        print(result)

        gd = graphdi.GraphDI(TestGraph.data6)
        result = gd.topological_sort()
        if not result:
            print("有向环，不能使用拓扑排序")
        else:
            print(result)


        gd = graphdi.GraphDI(TestGraph.data7)
        result = gd.topological_sort()
        courseResult = []
        for key in result:
            courseResult.append(TestGraph.courseData[key])
        print(courseResult)

    def test_criticalPath(self):
        print("关键路径测试")
        gd = graphdi.GraphDI(TestGraph.data5)
        print(gd)
        result, cps = gd.criticalPath()
        for key in result.keys():
            print('事件 %s : 最早开始时间：%s；最晚开始时间：%s' % (key, result[key][0], result[key][1]))
        for cp in cps:
            print('关键路径:%s -> %s' % (cp[0], cp[1]))
        pass

    def test_normal(self):
        print("常规测试")
        vertexNum = TestGraph.g.get_vertexNum()
        print(TestGraph.g.isConnect('A', 'B'))
        # print(TestGraph.g._graph['A']['B'])
        # print(vertexNum)

    def test_digraph(self):
        print("有向图常规测试")
        gd = graphdi.GraphDI(TestGraph.data5)
        print(gd)
        print("顶点个数：" + gd.get_vertexNum().__str__())
        print("V4-V6的边：" + gd.get_edge('V4', 'V6').__str__())
        print("V1的出边：" + gd.get_outEdge('V1').__str__())
        print("V4的入边：" + gd.get_inEdge('V4').__str__())
        print("V0的入边：" + gd.get_inEdge('V0').__str__())


if __name__ == '__main__':
    unittest.main()
