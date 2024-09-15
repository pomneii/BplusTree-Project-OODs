
"""
    ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
        
        def __str__(self):
            return str(self.data)

    class BST:
        def __init__(self):
            self.root = None

        def insert(self, data):
            # Code Here
        
        def printTree(self, node, level = 0):
            if node != None:
                self.printTree(node.right, level + 1)
                print('     ' * level, node)
                self.printTree(node.left, level + 1)

    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in inp:
        root = T.insert(i)
    T.printTree(root)
"""

class Node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self) :
        return str(self.data)

class BST :
    def __init__(self) :
        self.root = None

    def insert(self, data) :
        self.root = self._insert_recursive(self.root, data)
        return self.root

    def _insert_recursive(self, node_root, new_data)  :
        if node_root == None :
            return Node(new_data)
        else :
            if new_data < node_root.data :
                if node_root.left == None :
                    node_root.left = Node(new_data)
                else :
                    node_root.left = self._insert_recursive(node_root.left, new_data)
            elif new_data > node_root.data :
                if node_root.right == None :
                    node_root.right = Node(new_data)
                else :
                    node_root.right = self._insert_recursive(node_root.right, new_data)
        
        return node_root

    def printTree(self, node, level = 0) :
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)