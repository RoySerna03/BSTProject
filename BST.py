"""This is a module that defines
a Node and a Tree class.
"""

from random import randint


class Node:
    """Class defines a node:
    It contains a get methods for 3 internal variables:
    Node Value, Node left child and Node right Child
    """

    def __init__(self, value):
        self._value = value
        self._left_child = None
        self._right_child = None

    def value(self):
        return self._value

    def left_child(self):
        return self._left_child

    def right_child(self):
        return self._right_child

    def add_node(self, node, val):
        """Adds a new node based on its value.
        If it is < than the current node value, it will insert to the left.
        If it is > than the current node value, it will insert to the right"""

        if val < node.value():
            if node.left_child() is None:
                node._left_child = Node(val)
            else:
                self.add_node(node.left_child(), val)
        elif val > node.value():
            if node.right_child() is None:
                node._right_child = Node(val)
            else:
                self.add_node(node.right_child(), val)


class Tree:
    """Class that defines a Tree.
    A tree will have a root value"""

    def __init__(self,value):
        self.Root = Node(value)


    def addNode(self,val):
        self.Root.add_node(self.Root, val)

    def InOrder(self,node):
        if node.left_child() is not None:
            self.InOrder(node.left_child())
        print(node.value())
        if node.right_child() is not None:
            self.InOrder(node.right_child())

    def InOrderPrint(self):
        self.InOrder(self.Root)

    def PostOrder(self,node):
        if node.right_child() is not None:
            self.PostOrder(node.right_child())
        print(node.value())
        if node.left_child() is not None:
            self.PostOrder(node.left_child())

    def postOrderPrint(self):
        self.PostOrder(self.Root)


# Tree = Tree(100)
# for number in range(0,100):
#     Tree.addNode(randint(1,100))
# Tree.InOrderPrint()
# Tree.postOrderPrint()







