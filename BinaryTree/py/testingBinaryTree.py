#!/usr/local/bin/python3

import unittest
import inspect
import random
from BinaryTree import BinaryTree

INT_MAX = 4294967296
INT_MIN = -4294967296

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.binaryTree = BinaryTree()

    def test_0(self):
        print("{} Can create linked list object".format(inspect.stack()[0][3]))
        self.assertTrue(type(self.binaryTree) is BinaryTree)

    def test_1(self):
        print("{} Newly created tree, root value should be None".format(inspect.stack()[0][3]))
        self.assertEqual(self.binaryTree.root.value, None)

    def test_2(self):
        print("{} Insert value in new tree, root.value is inserted value".format(inspect.stack()[0][3]))
        self.binaryTree.insert(5)
        self.assertEqual(self.binaryTree.root.value, 5)

    def test_3(self):
        print("{} Insert value, search returns true for value inserted".format(inspect.stack()[0][3]))
        self.binaryTree.insert(5)
        self.assertTrue(self.binaryTree.search(5))

    def test_4(self):
        print("{} Insert value, search returns false for value not inserted".format(inspect.stack()[0][3]))
        self.binaryTree.insert(5)
        self.assertFalse(self.binaryTree.search(6))

    def test_5(self):
        print("{} Insert two values, search returns true for both values".format(inspect.stack()[0][3]))
        self.binaryTree.insert(5)
        self.binaryTree.insert(6)
        self.assertTrue(self.binaryTree.search(5))
        self.assertTrue(self.binaryTree.search(6))

    def test_6(self):
        print("{} Fill BST, see if is BST".format(inspect.stack()[0][3]))
        for x in range(0, 50):
            self.binaryTree.insert(random.randint(0,50))
        self.assertTrue(self.isBST(self.binaryTree.root))

    # Returns true if the given tree is a binary search tree
    def isBST(self, node):
        return (self.isBSTUtil(node, INT_MIN, INT_MAX))

    # Returns true if the given tree is a BST and its values
    # >= min and <= max
    def isBSTUtil(self, node, mini, maxi):
        # An empty tree is BST
        if node.value is None:
            return True

        # False if this node violates min/max constraint
        if node.value < mini or node.value > maxi:
            return False

        # Otherwise check the subtrees recursively
        # tightening the min or max constraint
        return (self.isBSTUtil(node.left, mini, node.value -1) and
              self.isBSTUtil(node.right, node.value+1, maxi))


if __name__ == '__main__':
    unittest.main()
