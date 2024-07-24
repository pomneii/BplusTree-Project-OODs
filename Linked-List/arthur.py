
"""
    Arthur เป็นเด็กหนุ่มผู้หลงใหลในการเขียนโปรแกรมและการแก้ปริศนา หนึ่งวันหนึ่ง เขาได้รับ จดหมายลึกลับที่บอกว่าเขาถูกเชิญให้ไปที่เมืองปริศนา ซึ่งเป็นเมืองที่ถูกสร้างขึ้นมาจากโครงสร้างข้อมูล แบบ Linked List ทั้งหมด
    เมื่อ Arthur มาถึงเมืองปริศนา เขาพบว่าที่นี่มีการจัดการแข่งขันเขียนโปรแกรม โดยมีเป้าหมายคือ การแก้ปริศนาและช่วยเหลือผู้อยู่อาศัยในเมืองปริศนาให้พ้นจากปัญหาต่างๆ ที่เกิดขึ้นจากโครงสร้าง ข้อมูลที่ซับซ้อน Arthur 
    ได้รับภารกิจแรกคือการแก้ปัญหาการจัดเรียงข้อมูลใน Linked List เพื่อทำให้ข้อมูลเรียงลำดับถูกต้อง

    ระดับความยาก : ง่ายคดๆ

    หมายเหตุ:

    - หลักการจัดวางคือ ตัวเลข, ตัวอักษรพิมพ์ใหญ่, ตัวอักษรพิมพ์เล็ก (คุ้นๆไหมมันคืออะไร?)
    - ไม่อนุญาตให้ใช้ .sort() เพราะตรวจ code นะจ๊ะ
"""

class Node :
    def __init__(self, value = None, nexts = None, prev = None) :
        self.value = value
        self.nextNode = nexts
        self.prevNode  = prev

class LinkedList :
    def __init__(self, head = None) :
        if head == None :
            self.head = None
        else :
            self.head = Node(head)
        self.size = 0

    def appendHead(self, value) :
        new_node = Node(value)
        if self.head != None :
            new_node.nextNode = self.head
            self.head.prevNode = new_node
            self.head = new_node
        else :
            self.head = new_node

    def appendLast(self, value) :
        new_node = Node(value)
        if self.head == None :
            self.appendHead(value)
            return
        curr = self.head
        while curr.nextNode != None :
            curr = curr.nextNode
        curr.nextNode = new_node
        curr.nextNode.prevNode = curr

    def sortList(self) :
        if self.head == None :
            return
        swapped = True
        while swapped != False :
            swapped = False
            curr = self.head
            while curr.nextNode != None :
                if curr.value > curr.nextNode.value :
                    curr.value, curr.nextNode.value = curr.nextNode.value, curr.value
                    swapped = True
                curr = curr.nextNode

    def printList(self) :
        curr = self.head
        while curr is not None :
            if curr.nextNode != None :
                print(curr.value, end=' -> ')
            else :
                print(curr.value)
            curr = curr.nextNode

def convertToLinkedList(lst) :
    linkList = LinkedList()
    for element in lst :
        linkList.appendLast(element)
    return linkList

inp = input("Enter unsorted Linked List: ").split(' ')
newLinkedList = convertToLinkedList(inp)
print("Before: ", end='')
newLinkedList.printList()
newLinkedList.sortList()
print("After : ", end='')
newLinkedList.printList()
