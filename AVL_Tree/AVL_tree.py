"""
    ให้นักศึกษาสร้าง AVL Tree แล้วแสดงผล Tree ในแต่ละรอบหลังจาก insert และตรวจสอบว่า Balance หรือเปล่าถ้าไม่ Balance 
    ปรับให้เรียบร้อยและแสดงรอบแบบการปรับ Tree ว่าเป็นการ Rotation แบบไหน

    ตัวอย่างการทำงาน

    *** AVL Tree Insert Element ***
    Enter Input : 1 2 3 4
    insert : 1
    1
    ====================
    insert : 2
        2
    1
    ====================
    insert : 3
    Left Left Rotation
        3
    2
        1
    ====================
    insert : 4
            4
        3
    2
        1
    ====================
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

        # Right-Left (RL) case
        if balanceFactor < -1 and root.left.balanceValue() > 0 :
            print("Right Left Rotation")
            root.left = self.rotateLeftChild(root.left)
            return self.rotateRightChild(root)

        # Right-Right (RR) case
        if balanceFactor < -1 and root.left.balanceValue() <= 0 :
            print("Right Right Rotation")
            return self.rotateRightChild(root)

        # Left-Right (LR) case
        if balanceFactor > 1 and root.right.balanceValue() < 0 :
            print("Left Right Rotation")
            root.right = self.rotateRightChild(root.right)
            return self.rotateLeftChild(root)

        # Left-Left (LL) case
        if balanceFactor > 1 and root.right.balanceValue() >= 0 :
            print("Left Left Rotation")
            return self.rotateLeftChild(root)

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

print(" *** AVL Tree Insert Element ***")
data = input("Enter Input : ").split()
for e in data:
    print("insert :", e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("====================")