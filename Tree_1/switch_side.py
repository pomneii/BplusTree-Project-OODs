
"""
    ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ
    จากนั้นให้ สลับทุกๆ node จาก Left node เป็น Right node และจาก Right node เป็น Left node

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
            if self.root == None:
                self.root = Node(data)
            else:
                cur = self.root
                while True:
                    if data < cur.data and cur.left != None:
                        cur = cur.left
                    elif data >= cur.data and cur.right != None:
                        cur = cur.right
                    elif data < cur.data:
                        cur.left = Node(data)
                        break
                    else:
                        cur.right = Node(data)
                        break
            return self.root
        
        def printTree(self, node, level = 0):
            if node != None:
                self.printTree(node.right, level + 1)
                print('     ' * level, node)
                self.printTree(node.left, level + 1)
                
        def reverseTree(self, node):
            #CODE HERE
            

    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in inp:
        root = T.insert(i)
    #CODE HERE
"""

class Node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self) :
        return str(self.data)

class BST:
    def __init__(self) :
        self.root = None
        self.inverse_root = None

    def insert(self, data) :
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data and cur.left != None:
                    cur = cur.left
                elif data >= cur.data and cur.right != None:
                    cur = cur.right
                elif data < cur.data:
                    cur.left = Node(data)
                    break
                else:
                    cur.right = Node(data)
                    break
        return self.root
    
    def inverse_insert(self, new_data) :
        if self.inverse_root == None:
            self.inverse_root = Node(new_data)
        else:
            cur = self.inverse_root
            while True:
                if new_data < cur.data and cur.right != None:
                    cur = cur.right
                elif new_data >= cur.data and cur.left != None:
                    cur = cur.left
                elif new_data < cur.data:
                    cur.right = Node(new_data)
                    break
                else:
                    cur.left = Node(new_data)
                    break
        return self.inverse_root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def reverseTree(self, node):
        pass
        

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
    inverse_root = T.inverse_insert(i)

print("Before: ")
T.printTree(root)
print("After: ")
T.printTree(inverse_root)
