from tree.tree import Tree, Node

import unittest


class TestPrinttree(unittest.TestCase):
    def test_printtree(self):
        b = Node(1, None, None)
        c = Node(2, b, None)
        d = Node(5, c, None)
        e = Node(7, None, d)
        a = Tree(e)

        res = [['|', '|', '|', 7, '|', '|', '|'], ['|', '|', '|', '|', 5, '|', '|'], ['|', '|', '|', 2, '|', '|', '|'],
               ['|', '|', 1, '|', '|', '|', '|']]
        for i in range(4):
            res[i] = ''.join(list(map(str, res[i])))
        assert '\n'.join(res) == a.print_tree()