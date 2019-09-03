import tree.BTNode as BinTNode


class Assoc:
    def __init__(self, key, value):
        self._key = key
        self._value = value

    def key(self):
        return self._key

    def value(self):
        return self._value

    def setValue(self, value):
        self._value = value


# 基于二叉排序树实现的字典类
class DictBST:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key():
                bt = bt.left
            elif key > entry.key():
                bt = bt.right
            else:
                return entry.value()
            pass

    def insert(self, key, value):
        bt = self._root
        if bt is None:
            self._root = BinTNode.BinTNode(Assoc(key, value))
            return
        while True:
            entry = bt.data
            if key < entry.key():
                if bt.left is None:
                    bt.left = BinTNode.BinTNode(Assoc(key, value))
                    return
                bt = bt.left
            elif key > entry.key():
                if bt.right is None:
                    bt.right = BinTNode.BinTNode(Assoc(key, value))
                    return
                bt = bt.right
            else:
                entry.setValue(value)
                return

    # 中序遍历
    def values(self):
        t, s = self._root, []
        while t is not None or s:
            while t is not None:
                s.append(t)
                t = t.left
            t = s.pop()
            yield t.data.value()
            t = t.right

    # 中序
    def entries(self):
        t, s = self._root, []
        while t is not None or s:
            while t is not None:
                s.append(t)
                t = t.left
            t = s.pop()
            yield t.data.key(), t.data.value()
            t = t.right

    def delete(self, key):
        bt = self._root
        f = None  # f为关键字节点的双亲节点
        while bt is not None:
            entry = bt.data
            if key < entry.key():
                f = bt
                bt = bt.left
            elif key > entry.key():
                f = bt
                bt = bt.right
            else:
                break
            pass
        if bt is None:
            return False
        # ---------------------------三种情况，无右子树，无左子树，左右子树均有-----------------------------------------
        p = bt  # 保存待删除的节点
        if bt.right is None:
            bt = bt.left
        elif bt.left is None:
            bt = bt.right
        else:
            # 用其左子树的中序的最后一个节点代替待删除的结点
            s = bt  # 待替换的节点
            q = bt  # 指向中序遍历的最后一个节点的双亲节点
            bt = bt.left
            while bt.right is not None:
                q = bt
                bt = bt.right
            s.data.setValue(bt.data.value())  # 此时的bt指向了待替换的节点的左子树中序遍历的最后一个节点，也就是待替换节点的“前驱”
            if q is not s:
                q.right = bt.left  # 缺右子树，用左孩子填补
            else:
                q.left = bt.right  # 缺左子树，用右孩子填补
            del bt
            return True

        if f is None:  # 删除的节点为根节点
            self._root = None
        elif f.left == p:  # 待删除的节点在其双亲节点的左子树
            f.left = bt
        elif f.right == p:
            f.right = bt
        return True
        pass

    def printValues(self):
        for v in dbst.values():
            print(v, end=" ")

    def print(self):
        for k, v in self.entries():
            print("("+str(k), str(v)+")", end=" ")


if __name__ == '__main__':
    dbst = DictBST()
    dbst.insert(53, '53')
    dbst.insert(17, '17')
    dbst.insert(78, '78')
    dbst.insert(9, '9')
    dbst.insert(45, '45')
    dbst.insert(70, '70')
    dbst.insert(94, '94')
    dbst.insert(23, '23')
    dbst.insert(60, '60')
    dbst.insert(75, '75')
    dbst.insert(88, '88')

    print("原始")
    dbst.print()

    print("\n查找key=3的值")
    print(dbst.search(1))
    print("\n删除key=45的节点")
    print(dbst.delete(45))
    dbst.printValues()

    print("\n删除key=78的节点")
    print(dbst.delete(78))
    dbst.printValues()

    print("\n删除key=70的节点")
    print(dbst.delete(70))
    dbst.printValues()

    pass
