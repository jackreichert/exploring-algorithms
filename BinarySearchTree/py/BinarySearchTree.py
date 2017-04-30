#!/usr/local/bin/python3

class BinarySearchTree:
    def __init__(self):
        self.root = self.Node()

    class Node:
        def __init__(self):
            self.left = None
            self.right = None
            self.value = None

    def insert(self, value, node=None):
        if node is None:
            node = self.root

        if node.value is None:
            node.value = value
            node.left = self.Node()
            node.right = self.Node()
        elif node.value > value:
            self.insert(value,node.left)
        elif node.value < value:
            self.insert(value,node.right)

    def search(self, value, node=None):
        if node is None:
            node = self.root

        if node.value == value:
            return True
        elif node.left is None and node.right is None:
            return False
        elif node.value > value:
            return self.search(value,node.left)
        elif node.value < value:
            return self.search(value,node.right)
