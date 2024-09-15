"""
    ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ
    โดยมีการป้อน input ดังนี้

    i <int> = insert data
    d <int> = delete data

    หมายเหตุ การลบนั้นจะใช้หลักการของ Inorder Successor และ จำนวน parameter มีได้มากสุด 3 ตัว

    class Node:
        def __init__(self, data): 
            self.data = data  
            self.left = None  
            self.right = None 
            self.level = None 

        def __str__(self):
            return str(self.data) 

    class BinarySearchTree:
        def __init__(self): 
            self.root = None

        def insert(self, val):  
            #code here
        def delete(self,r, data):
            #code here
                    
    def printTree90(node, level = 0):
        if node != None:
            printTree90(node.right, level + 1)
            print('     ' * level, node)
            printTree90(node.left, level + 1)


    tree = BinarySearchTree()
    data = input("Enter Input : ").split(",")
    #code here

    Enter Input : i 3,i 5,i 2,d 3
    insert 3
    3
    insert 5
        5
    3
    insert 2
        5
    3
        2
    delete 3
    5
        2
"""

class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):  
        self.root = self._insert(self.root, val)
        return self.root

    def _insert(self, root, new_data) :
        if root == None :
           root = Node(new_data)
        else :
            if new_data < root.data :
                if root.left == None :
                    root.left = Node(new_data)
                else :
                    self._insert(root.left, new_data)
            else :
                if root.right == None :
                    root.right = Node(new_data)
                else :
                    self._insert(root.right, new_data)

        return root

    def delete(self,r, data):
        if r == None :
            print(f"Error! Not Found DATA")
            return r
        
        if data < r.data :   # if the delete node is less than the root -> move to the left
            r.left = self.delete(r.left, data)
        elif data > r.data :   # if the delete node is greater than the root -> move to the right
            r.right = self.delete(r.right, data)
        else :   # if the delete node is the root
            # if there is only one child or doesnt has child
            if r.left == None :
                return r.right
            elif r.right == None :
                return r.left
            
            # if there are 2 children -> find inorder successor (the least in right subtree)
            temp = self.minValueNode(r.right)
            r.data = temp.data   # replace the delete node by inorder successor
            r.right = self.delete(r.right, temp.data)   # delete inorder successor

        return r

    def minValueNode(self, node) :
        current = node
        while current.left != None :
            current = current.left
        return current
                
def printTree90(node, level = 0):
    if node != None:    
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
temp = [e.split(' ') for e in data]

for element in temp :
    if element[0] == 'i' :
        print(f"insert {int(element[1])}")
        tree.root = tree.insert(int(element[1]))
    elif element[0] == 'd' :
        print(f"delete {int(element[1])}")
        tree.root = tree.delete(tree.root, int(element[1]))
    printTree90(tree.root)
