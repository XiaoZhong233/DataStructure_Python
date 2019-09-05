from search.BST import DictBST as BST
from search.BST import Assoc
from search.AVLNode import AVLNode


class AVL(BST):
    def __init__(self):
        BST.__init__(self)
        pass

    def insert(self, key, value):
        # a指向离插入位置最近的BF非0的节点，p是扫描变量，p从a的子节点开始遍历，用于更新BF，pa指向a的父节点,q是插入节点的父节点
        a = p = self._root
        if a is None:
            self._root = AVLNode(Assoc(key, value))
            return
        pa = q = None
        while p is not None:  # 确定插入位置的最小非平衡子树，也就是找出a的指向
            if key == p.data.key():  # key存在，更新值结束
                p.data.setValue(value)
                return
            if p.bf != 0:
                pa, a = q, p  # 已知最小非平衡树
            # 把q指向p的也就是指向插入位置的父节点
            q = p
            if key < p.data.key():
                p = p.left
            else:
                p = p.right
        node = AVLNode(Assoc(key, value))
        if key < q.data.key():
            q.left = node  # 作为左节点
        else:
            q.right = node  # 作为右节点
        # 新节点已经插入，a是最小不平衡子树
        if key < a.data.key():
            p = b = a.left
            d = 1  # d记录新节点在a的哪颗子树
        else:
            p = b = a.right
            d = -1
        # 修改b到新节点路径上各节点的BF值,b为a的子节点
        while p != node:
            if key < p.data.key():  # p的左子树增高
                p.bf = 1
                p = p.left
            else:  # p的右子树增高
                p.bf = -1
                p = p.right
        if a.bf == 0:  # a的原BF为0，不会失衡
            a.bf = d
            return
        if a.bf == -d:  # 新节点在较低的子树中
            a.bf = 0
            return
        # 新节点在较高的子树中，发生失衡，需要调整
        if d == 1:
            if b.bf == 1:
                b = AVL.LL(a, b)
            else:
                b = AVL.LR(a, b)
        else:
            if b.bf == -1:
                b = AVL.RR(a, b)
            else:
                b = AVL.RL(a, b)

        if pa is None:  # 原a为树根，修改根
            self._root = b
        else:
            if pa.left == a:
                pa.left = b
            else:
                pa.right = b

    # LL型调整，右旋，踢掉左孩子的右孩子，被踢掉的孩子变成旋转节点的左孩子，返回调整后的节点
    # a为根节点，b为a的孩子节点，下同
    @staticmethod
    def LL(a, b):
        print("LL型调整 %s结点与%s结点 " % (str(a.data.key()), str(b.data.key())))
        a.left = b.right
        b.right = a
        a.bf = b.bf = 0
        return b

    # RR型调整，左旋
    @staticmethod
    def RR(a, b):
        print("RR型调整 %s结点与%s结点 " % (str(a.data.key()), str(b.data.key())))
        a.right = b.left
        b.left = a
        a.bf = b.bf = 0
        return b

    # LR型调整，先左旋再右旋
    @staticmethod
    def LR(a, b):
        print("LR型调整 %s结点与%s结点 " % (str(a.data.key()), str(b.data.key())))
        c = b.right  # 找到根节点的左子树的右子树
        # 左旋和右旋
        a.left, b.right = c.right, c.left
        c.left, c.right = b, a
        if c.bf == 0:  # 本身就是新插入的节点
            a.bf = b.bf = 0
        elif c.bf == 1:  # 新节点为c的左子树
            a.bf = -1
            b.bf = 0
        else:  # 新节点为c的右子树
            a.bf = 0
            b.bf = 1
        c.bf = 0  # 实现平衡
        return c

    # RL型调整，先右旋再左旋
    @staticmethod
    def RL(a, b):
        print("RL型调整 %s结点与%s结点 " % (str(a.data.key()), str(b.data.key())))
        c = b.left  # 找到根节点的右子树的左子树
        a.right, b.left = c.left, c.right
        c.left, c.right = a, b
        if c.bf == 0:
            a.bf = 0
            b.bf = 0
        elif c.bf == 1:
            a.bf = 0
            b.bf = -1
        else:
            a.bf = -1
            b.bf = 0
        c.bf = 0
        return c


if __name__ == '__main__':
    tree = AVL()
    tree.insert(57, "57")
    tree.insert(36, "36")
    tree.insert(23, "23")
    tree.insert(11, "11")
    tree.insert(18, "18")
    tree.insert(69, "69")
    tree.insert(81, "81")
    tree.insert(63, "63")
    tree.insert(60, "60")

    tree.print()
    pass
