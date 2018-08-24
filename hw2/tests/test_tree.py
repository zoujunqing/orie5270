from tree.tree import Tree, Node
import unittest
import numpy as np


class test_Printtree(unittest.TestCase):
    def test_printtree(self):
        b = Node(1, None, None)
        c = Node(2, b, None)
        d = Node(5, c, None)
        e = Node(7, None, d)
        a = Tree(e)

        res = np.array([['|', '|', '|', 7, '|', '|', '|'],
                        ['|', '|', '|', '|', 5, '|', '|'],
                        ['|', '|', '|', 2, '|', '|', '|'],
                        ['|', '|', 1, '|', '|', '|', '|']])
        assert len(res) == len(a.printTree(e))
