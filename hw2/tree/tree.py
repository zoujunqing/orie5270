class Tree(object):
    def __init__(self, root):
        """
        initialize the class
        :param root: a Node object, the root of the tree
        """
        self.root = root

    def get_height(self, root):
        """
        get the hight of the tree
        :param root: a Node object
        :return: the height value of the tree
        """
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def printTree(self, root):
        """
        print the tree
        :param root: a Node object, the root of the tree
        :return: a list of tree
        """
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
        return ret


class Node(object):

    def __init__(self, value, left, right):
        """
        initialize an instance of node class.
        :param value: the value of the node, int
        :param left: the left node, belong to the Node() class.
        :param right:the right node, belong to the Node() class.
        """
        self.value = value
        self.left = left
        self.right = right
