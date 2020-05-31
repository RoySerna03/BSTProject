import unittest
from random import randint
#from BST import Tree
from BST import  Tree


class BST_Test(unittest.TestCase):

    def setUp(self):
        self.BST = Tree(90)

    def test_create_Tree_with_only_Root(self):
        #print(self.BST.Root.value())
        self.assertTrue(self.BST.Root.value() is not None)
        self.assertTrue(self.BST.Root.left_child() is None)
        self.assertTrue(self.BST.Root.right_child() is None)


