
"""
    รับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอและให้หาลูกๆทั้งหมดของของ Node ที่กำหนด

    กำหนดให้ input = 4 2 7 1 3 , 2
    สร้าง BST จาก 4 2 7 1 3 โดยให้ input 4 เป็น Root
    หาลูกๆทั้งหมดของ node 4
    Enter the BST values and search value: 4 2 7 1 3, 2
    Input: root = [4, 2, 7, 1, 3], val = 2
    Output: [2, 1, 3]
"""

class Node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) :
        return str(self.data)

class BST :
    def __init__(self, ) :
        self.root = None
    
    def insert(self, new_data) :
        self.root = self._insert_recursive(self.root, new_data)
        return self.root
    
    def _insert_recursive(self, root_node, new_data) :
        if root_node == None :
            return Node(new_data)
        else :
            if new_data < root_node.data :
                if root_node.left == None :
                    root_node.left = Node(new_data)
                else :
                    self._insert_recursive(root_node.left, new_data)
            elif new_data > root_node.data :
                if root_node.right == None :
                    root_node.right = Node(new_data)
                else :
                    self._insert_recursive(root_node.right, new_data)

        return self.root
    
    def find_parents(self,root, node_find) :
        result = []
        target_node = self._find_recursive(root, node_find)
        
        if target_node == None :
            return None
        
        self._collect_parents(target_node, result)
        
        return result
    
    def _collect_parents(self, node, result) :
        if node == None :
            return
        
        result.append(node)
        self._collect_parents(node.left, result)
        self._collect_parents(node.right, result)
    
    def _find_recursive(self, current_node, node_find) :
        if current_node == None :
            return None
        
        if current_node.data == node_find :
            return current_node
        
        if node_find < current_node.data :
            return self._find_recursive(current_node.left, node_find)
        elif node_find > current_node.data :
            return self._find_recursive(current_node.right, node_find) 

        return None           
        

T = BST()
inp = input("Enter the BST values and search value: ").split(', ')
temp = []

temp.append([int(e) for e in inp[0].split(' ')])
temp.append(int(inp[1]))

for element in temp[0] :
    T.insert(element)

print(f"Input: root = {temp[0]}, val = {temp[1]}")
parents = T.find_parents(T.root, temp[1])
if parents == None :
    print(f"Output: {[]}")
else :
    print(f"Output: {[parent.data for parent in parents]}")