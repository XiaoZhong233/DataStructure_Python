from tree.BTNode import BinTNode


class AVLNode(BinTNode):
    def __init__(self, data):
        BinTNode.__init__(self, data)
        self.bf = 0  # 平衡因子，Balanced Factor，计算为左子树的深度减右子树的深度




