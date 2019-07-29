"""
二叉树的遍历
"""

from appname.utility_class.lqueue import *


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = root

    # 先序遍历
    def preOrder(self, node):
        if node is None:
            return
        print(node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序遍历
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.val)
        self.inOrder(node.right)

    # 后序遍历
    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.val)

    # 　层次遍历
    def levelOrder(self, node):
        """
        node先入队,循环判断,队列不为空时,出队表示遍历,
        同时让出队元素的左右孩子入队
        """
        lq = LQueue()
        lq.enqueue(node)
        while not lq.is_empty():
            node = lq.dequeue()
            print(node.val)  # 遍历元素
            if node.left:
                lq.enqueue(node.left)
            if node.right:
                lq.enqueue(node.right)


if __name__ == '__main__':
    b = Node('B')
    f = Node('F')
    g = Node('G')
    d = Node('D', f, g)
    h = Node('H')
    i = Node('I')
    e = Node('E', h, i)
    c = Node('C', d, e)
    a = Node('A', b, c)  # 整个树根

    bt = BinaryTree(a)  # 把a作为根节点进行遍历

    bt.preOrder(bt.root)
    print("========================")
    bt.inOrder(bt.root)
    print("========================")
    bt.postOrder(bt.root)
    print("========================")
    bt.levelOrder(bt.root)
