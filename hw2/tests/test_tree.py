from tree.tree import Tree, Node
import unittest


class test_Printtree(unittest.TestCase):
    def test_printtree(self):
        a = Node(1, Node(2, Node(4, None, None), None), Node(3, None, None))
        b = Tree(a)

        res = [['|', '|', '|', '1', '|', '|', '|'],
               ['|', '2', '|', '|', '|', '3', '|'],
               ['4', '|', '|', '|', '|', '|', '|']]
        assert res == b.printTree(a)
