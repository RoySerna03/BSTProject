"""This is a module that defines
a Node and a Tree class.
"""

from random import randint




class Node:
    """Class defines a node:
    It contains a

    """

    def __init__(self,value):
        self.value=value
        self.left_child=None
        self.right_child=None

    def value(self):
        return self._value

    def addnode(self,node,val):

        if val < node.value:

            if node.left_child is None:
                node.left_child = Node(val)
            else:
                self.addnode(node.left_child,val)
        elif val > node.value:

            if node.right_child is None:
                node.right_child = Node(val)
            else:
                self.addnode(node.right_child,val)


class Tree:

    def __init__(self,value):
        self.Root = Node(value)

    def addNode(self,val):
        self.Root.addnode(self.Root,val)

    def InOrder(self,node):
        if node.left_child is not None:
            self.InOrder(node.left_child)
        print(node.value)
        if node.right_child is not None:
            self.InOrder(node.right_child)

    def InOrderPrint(self):
        self.InOrder(self.Root)

    def PostOrder(self,node):
        if node.right_child is not None:
            self.PostOrder(node.right_child)
        print(node.value)
        if node.left_child is not None:
            self.PostOrder(node.left_child)

    def postOrderPrint(self):
        self.PostOrder(self.Root)


# Tree = Tree(100)
# for number in range(0,100):
#     Tree.addNode(randint(1,100))
# #Tree.InOrderPrint()
# Tree.postOrderPrint()







