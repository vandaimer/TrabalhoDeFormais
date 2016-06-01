import unittest
from BTree import BTree
from Node import Node

class TestBTree(unittest.TestCase):
    def test_insert_root_with_left_none(self):
        b = BTree()
        b.insert(2)
        self.assertIsNone(b.root.left)

    def test_insert_root_with_right_none(self):
        b = BTree()
        b.insert(2)
        self.assertIsNone(b.root.right)

    def test_left_of_root_not_is_none(self):
        b = BTree()
        b.insert(2)
        b.insert(1)
        self.assertNotEqual(b.root.left, None)

    def test_right_of_root_not_is_none(self):
        b = BTree()
        b.insert(2)
        b.insert(3)
        self.assertNotEqual(b.root.right, None)

    def test_left_of_left_root_not_is_none(self):
        b = BTree()
        b.insert(3)
        b.insert(2)
        b.insert(1)
        self.assertNotEqual(b.root.left.left, None)

    def test_right_of_left_root_not_is_none(self):
        b = BTree()
        b.insert(4)
        b.insert(2)
        b.insert(3)
        self.assertNotEqual(b.root.left.right, None)

    def test_left_of_right_root_not_is_none(self):
        b = BTree()
        b.insert(5)
        b.insert(7)
        b.insert(6)
        self.assertNotEqual(b.root.right.left, None)

    def test_right_of_right_root_not_is_none(self):
        b = BTree()
        b.insert(4)
        b.insert(5)
        b.insert(6)
        self.assertNotEqual(b.root.right.right, None)
