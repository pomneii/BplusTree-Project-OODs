"""
    ให้น้องๆสร้าง AVL Tree ด้วย Class โดยผลลัพธ์ให้แสดงเป็น Tree ในแต่ละรอบหลังจาก Insert ให้ตรวจสอบว่า balance หรือยัง หากไม่ให้ ปรับ Balance ให้เรียบร้อยแล้วและแสดงผล
    ** ถ้าสงสัยสามารถดู visualization ของ AVL ได้ที่ website นี้ : https://www.cs.usfca.edu/~galles/visualization/AVLtree.html

    #code เป็นเพียงตัวอย่างเท่านั้นสามารถเขียนขึ้นเองโดยไม่ต้องอ้างอิงจาก code นี้ก็ได้

    class TreeNode(object): 
        def __init__(self, val): 
            self.val = val 
            self.left = None
            self.right = None
            self.height = 1

        def __str__(self):
            return str(self.val)
  
    class AVL_Tree(object): 
        #code here

    def printTree90(node, level = 0):
        if node != None:
            printTree90(node.right, level + 1)
            print('     ' * level, node)
            printTree90(node.left, level + 1)
    
    myTree = AVL_Tree() 
    root = None

    data = input("Enter Input : ").split()
    for e in data:
        print("insert :",e)
        root = myTree.insert(root, e)
        printTree90(root)
        print("===============")
"""
class TreeNode(object): 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        self.height = self.setHeight()

    def __str__(self):
        return str(self.data)
    
    def setHeight(self) :
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height

    def getHeight(self, node) :
        return -1 if node == None else node.height
        
    def balanceValue(self) :
        return self.getHeight(self.right) - self.getHeight(self.left)
  
class AVL_Tree(object): 
    def __init__(self, root = None) :
        self.root = None if root is None else root

    def insert(self, root, data) :
        self.root = self._insert(root, int(data))
        return self.root

    def _insert(self, root, data) :
        if root == None :
            return TreeNode(data)
        if data < root.data :
            root.left = self._insert(root.left, data)
        else :
            root.right = self._insert(root.right, data)

        root.setHeight()

        balanceFactor = root.balanceValue()

        if balanceFactor < -1 :    # right heavy
            print("Not Balance, Rebalance!")
            if root.left.balanceValue() > 0 :   # RL case
                root.left = self.rotateLeftChild(root.left)
            return self.rotateRightChild(root)  # RR case
        
        if balanceFactor > 1 :  # left heavy
            print("Not Balance, Rebalance!")
            if root.right.balanceValue() < 0 :  # LR case
                root.right = self.rotateRightChild(root.right)
            return self.rotateLeftChild(root)  # LL case

        return root
    
    def rotateLeftChild(self, root) :
        if root.right is None:
            return root
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot
    
    def rotateRightChild(self, root) :
        if root.left is None:
            return root
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot
    
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)
  
myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :", e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")