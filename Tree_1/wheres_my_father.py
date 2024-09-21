"""
    ให้น้องรับ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ
    และให้หาพ่อ (Father node) ของ node ที่กำหนด
"""

class Node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) :
        return str(self.data)

class BST :
    def __init__(self, root = None) :
        self.root = root

    def insert(self, data) :
        self.root = self._insert(self.root, data)
        return self.root
    
    def _insert(self, root, data) :
        if root == None :
            return Node(data)
        else :
            if data < root.data :
                root.left = self._insert(root.left, data)
            else :
                root.right = self._insert(root.right, data)
        
        return root
    
    def printTree(self, node, level = 0) :
        if node != None :
            self.printTree(node.right, level + 1)
            print('    ' * level, node)
            self.printTree(node.left, level + 1)

    def find_father(self, root, node) :
        if root == None :
            return f"Not Found Data"
        
        if node == self.root.data and root.data == node :
            return f"None Beacause {node} is Root"
        
        if root.left != None and root.left.data == node :
            return root
        if root.right != None and root.right.data == node :
            return root
        
        if node < root.data and root.left != None :
            return self.find_father(root.left, node)
        elif node > root.data and root.right != None :
            return self.find_father(root.right, node)
        
        return f"Not Found Data"

T = BST()
inp, node = input("Enter Input : ").split('/')
inp = [int(e) for e in inp.split(' ')]
node = int(node)
for element in inp :
    T.insert(element)
T.printTree(T.root)
print(T.find_father(T.root, node))