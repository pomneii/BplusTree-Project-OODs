"""
    นำ code จากข้อ 1 มาเปลี่ยนเป็น

    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in range(1, len(inp)):
        root = T.insert(inp[i])
    T.printTree(root)
    T.checkpos(inp[0])
    เพื่อหาว่าค่าแรกที่ใส่เข้าไปอยู่ที่ตำแหน่งใดใน BST

    Binary Tree Example

    ##code output

    print("Not exist")
    print("Root")
    print("Inner")
    print("Leaf")
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
    
    def findNode(self, currentNode, nodeFind) :

        if currentNode == None :
            return None
        
        if currentNode.data == nodeFind :
            return currentNode
        
        if nodeFind < currentNode.data :
            return self.findNode(currentNode.left, nodeFind)
        elif nodeFind > currentNode.data :
            return self.findNode(currentNode.right, nodeFind)
        
        return None
    
    def checkpos(self, node) :
        new_node = self.findNode(self.root, node)

        if new_node == None :
            print("Not exist")
            return
        
        if new_node == self.root :
            print("Root")
            return
        else :
            if new_node.left == None and new_node.left == None :
                print("Leaf")
                return
            else :
                print("Inner")
                return
        
    def printTree(self, node, level = 0) :
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])