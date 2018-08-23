import numpy as np


class Tree(object):

    def __init__(self, root):
        self.root = root

    """
    def get_value_root(self):
        if self.root is not None:
            return self.root.value
        else:
            return None
    """

    def get_height(self, root):
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def printTree(self, root):
        N = self.get_height(root)
        M = 2 ** N - 1
        ret = [["|"] * M for x in range(N)]

        bfs = [(root, 0, 0, M)]
        for x in bfs:
            node, i, l, r = x[0], x[1], x[2], x[3]
            j = (r + l) // 2
            ret[i][j] = str(node.value)
            if node.left:
                bfs.append((node.left, i + 1, l, j))
            if node.right:
                bfs.append((node.right, i + 1, j, r))

        return np.mat(ret)


class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


"""
if __name__ == '__main__':
    a = Node(1, None, None)
    b = Tree(a)

    print(b.get_value_root())
"""

if __name__ == '__main__':
    a = Node(1, Node(2, Node(4, None, None), None), Node(3, None, None))
    b = Tree(a)
    print(b.printTree(a))

