visit = lambda data: print(data, end=" ")


class BinTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "data:%s,left:%s,right:%s" % (self.data, self.left.data, self.right.data)

    @staticmethod
    def count_BinTNodes(t):
        if t is None:
            return 0
        else:
            return 1 + BinTNode.count_BinTNodes(t.right) + BinTNode.count_BinTNodes(t.left)

    @staticmethod
    def preorder(t, proc):
        if t is None:
            return
        proc(t.data)
        t.preorder(t.left, proc)
        t.preorder(t.right, proc)
        pass

    @staticmethod
    def midorder(t, proc):
        if t is None:
            return
        t.midorder(t.left, proc)
        proc(t.data)
        t.midorder(t.right, proc)
        pass

    @staticmethod
    def lastorder(t, proc):
        if t is None:
            return
        t.lastorder(t.left, proc)
        t.lastorder(t.right, proc)
        proc(t.data)
        pass

    @staticmethod
    def print_BinTnodes(t):
        if t is None:
            print("^", end="")
            return
        print("(" + str(t.data), end="")
        t.print_BinTnodes(t.left)
        t.print_BinTnodes(t.right)
        print(")", end="")

    @staticmethod
    def levelorder(t, proc):
        queue = [t]
        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            queue.append(node.left)
            queue.append(node.right)
            proc(node.data)
        pass

    @staticmethod
    def preorder_nonrec(t, proc):
        stack = []
        while t is not None or stack:
            while t is not None:  # 沿左分支下行
                proc(t.data)
                stack.append(t.right)  # 暂时保存右分支
                t = t.left
            t = stack.pop()  # 遇到空树，回溯

    @staticmethod
    def midorder_nonrec(t, proc):
        stack = []
        while t is not None or stack:
            while t is not None:
                stack.append(t)  # 根节点先保存起来
                t = t.left
            t = stack.pop()  # 出栈，访问根节点
            proc(t.data)
            # if not stack:
            #     proc(t.data)
            t = t.right  # 遍历右子树

    @staticmethod
    def lastorder_nonrec(t, proc):
        stack = []
        while t is not None or stack:
            while t is not None:  # 循环，直到栈顶的两个子树空
                stack.append(t)
                t = t.left if t.left is not None else t.right
            t = stack.pop()  # 当前子树根节点
            proc(t.data)
            if stack and stack[stack.__len__() - 1].left == t:
                t = stack[stack.__len__() - 1].right  # 栈非空且当前节点是栈顶节点的左节点
            else:
                t = None  # 栈顶节点没有右子树或者右子树已遍历完成，强制退栈
        pass


if __name__ == '__main__':
    t = BinTNode(1, BinTNode(2, BinTNode(5)), BinTNode(3))
    print("打印节点")
    BinTNode.print_BinTnodes(t)
    print("\n节点数统计:")
    print(BinTNode.count_BinTNodes(t))
    print("\n先序遍历")
    BinTNode.preorder(t, visit)
    print("\n中序遍历")
    BinTNode.midorder(t, visit)
    print("\n后序遍历")
    BinTNode.lastorder(t, visit)
    print("\n层次遍历")
    BinTNode.levelorder(t, visit)
    print("\n非递归先序遍历")
    BinTNode.preorder_nonrec(t, visit)
    print("\n非递归中序遍历")
    BinTNode.midorder_nonrec(t, visit)
    print("\n非递归后序遍历")
    BinTNode.lastorder_nonrec(t, visit)
