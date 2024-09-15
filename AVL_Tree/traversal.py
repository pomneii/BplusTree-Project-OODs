"""
    จงเขียนโปรแกรมเพื่อรับข้อมูล แล้วสร้าง AVL tree และแสดงการแวะผ่านโหนดต่าง ๆ แบบ post-order
    โดยแก้ไข method add คือการเพิ่มข้อมูลเข้าใน AVLTree และ method postOrder คือ บริการแวะผ่านโหนดทุกโหนดแบบหลังลำดับ จากส่วนของโปรแกรมต่อไปนี้
"""

class AVLTree:
    class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a,b)
            return self.height

        def getHeight(self, node):
            return -1 if node == None else node.height

        def balanceValue(self):      
            return self.getHeight(self.right) - self.getHeight(self.left)

    def __init__(self, root = None):
        self.root = None if root is None else root

    def add(self, data):
        self.root = self._add(self.root, int(data))

    def _add(self, root, data):
        if root == None :
            return AVLTree.AVLNode(data)
        if data < root.data :
            root.left = self._add(root.left, data)
        else :
            root.right = self._add(root.right, data)

        root.setHeight()

        balanceFactor = root.balanceValue()
        
        if balanceFactor < -1 :    # left heavy
            if root.left.balanceValue() > 0 :   # LR case
                root.left = AVLTree.rotateLeftChild(root.left)
            return AVLTree.rotateRightChild(root)  # LL case
        
        if balanceFactor > 1 :  # right heavy
            if root.right.balanceValue() < 0 :  # RL case
                root.right = AVLTree.rotateRightChild(root.right)
            return AVLTree.rotateLeftChild(root)  # RR case
        
        return root

    def rotateLeftChild(root) :
        if root.right == None :
            return root
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot

    def rotateRightChild(root) :
        if root.left == None :
            return root
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot  

    def postOrder(self):
        print('AVLTree post-order : ', end='')
        AVLTree._postOrder(self.root)
        print()

    def _postOrder(root):
        if root != None :
            AVLTree._postOrder(root.left)
            AVLTree._postOrder(root.right)
            print(root.data, end=' ')

    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node , level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)

avl1 = AVLTree()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AD":
        avl1.add(i[3:])
    elif i[:2] == "PR":
        avl1.printTree()
    elif i[:2] == "PO":
        avl1.postOrder()