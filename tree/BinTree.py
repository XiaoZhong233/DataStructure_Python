from tree.BTNode import BinTNode


class BinTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def get_root(self):
        return self.root

    def leftChild(self):
        return self.root.left

    def rightChild(self):
        return self.root.right

    def set_root(self, rootNode):
        self.root = rootNode

    def set_left(self, leftChild):
        self.root.left = leftChild

    def set_right(self, rightChild):
        self.root.right = rightChild

    def preorder_elements(self):
        t, s = self.get_root(), []
        while t is not None or s:
            while t is not None:
                s.append(t.right)
                yield t.data
                t = t.left
            t = s.pop()


if __name__ == '__main__':
    t = BinTree()
    root = BinTNode(1, BinTNode(2, BinTNode(5)), BinTNode(3))
    t.set_root(root)
    for data in t.preorder_elements():
        print(data)
