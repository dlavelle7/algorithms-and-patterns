from unittest import TestCase

from python.binary_search_tree import (
    BinarySearchTree, find_tree_height, count_tree_nodes,
)


class TestBinarySearchTree(TestCase):

    def test_binary_search_tree(self):
        bs_tree = BinarySearchTree()

        # test adding
        bs_tree.add(10)
        self.assertIs(bs_tree.root.value, 10)

        bs_tree.add(6)
        self.assertIs(bs_tree.root.left.value, 6)

        bs_tree.add(14)
        self.assertIs(bs_tree.root.right.value, 14)

        bs_tree.add(22)
        self.assertIs(bs_tree.root.right.right.value, 22)

        # test membership
        self.assertTrue(14 in bs_tree)

        self.assertFalse(100 in bs_tree)

        # test count
        self.assertEqual(4, count_tree_nodes(bs_tree))

        # TODO:
        # test height
        #import ipdb; ipdb.set_trace();  # XXX Breakpoint
        #self.assertEqual(3, find_tree_height(bs_tree))

    def test_empty_binary_search_tree(self):
        bs_tree = BinarySearchTree()
        self.assertFalse(1 in bs_tree)
        self.assertEqual(0, count_tree_nodes(bs_tree))
        # TODO:
        #self.assertEqual(3, find_tree_height(bs_tree))
