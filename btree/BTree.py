from Node import Node


class BTree:
    def __init__(self):
        self.root = None

    def insert(self, key, node = None):
        if node is None:
            node = self.root

        if self.root is None:
            self.root = Node(key)
        else:
            if Node(key) <= node:
                if node.left is None:
                    node.left = Node(key)
                    node.left.parent = node
                    return
                else:
                    return self.insert(key, node.left)
            else:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                    return
                else:
                    return self.insert(key, node.right)

    def print(self, node):
        if node == None:
            node = self.root

        if self.root == None:
            print('Nada inserido.')

        if node.left != None:
            print('<--- left key: ' + str(node.left.key))
            self.print(node.left)

        if node.right != None:
            print('---> right key: ' + str(node.right.key))
            self.print(node.right)
