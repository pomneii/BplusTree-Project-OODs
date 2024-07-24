
"""
    กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode คือ Command Mode (inputของเรานั่นแหละ) 
    โดยจะมีคำสั่งอยู่ 5 แบบ คือ Insert (I) , Left (L) , Right (R) , Backspace (B) และ Delete (D) (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) 
    แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor ที่กฤษฎาต้องการให้หน่อย 
    โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป พร้อมกับตำแหน่งของ Cursor

    ***** อธิบาย Input 5 แบบ *****

    1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป
    2.  L   :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร
    3.  R   :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร
    4.  B   :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร
    5.  D   :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร
"""

class Node :
    def __init__(self, value = None, nexts = None, prev = None) :
        self.value = value
        self.nextNode = nexts
        self.prevNode = prev

class LinkedList :
    def __init__(self, head = None) :
        if head == None :
            self.head = None
        else :
            self.head = Node(head)
        self.cursor = Node("|")
        self.appendLast("|")

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

    def appendBeforeCursor(self, value) :
        new_node = Node(value)
        if self.cursor.prevNode == None :
            new_node.nextNode = self.cursor
            self.cursor.prevNode = new_node
            self.head = new_node
        else :
            self.cursor.prevNode.nextNode = new_node
            new_node.prevNode = self.cursor.prevNode
            new_node.nextNode = self.cursor
            self.cursor.prevNode = new_node 

    def leftMove(self) :
        if self.cursor.prevNode != None :

            left_node = self.cursor.prevNode
            right_node = self.cursor.nextNode

            if left_node.prevNode != None :
                left_node.prevNode.nextNode = self.cursor
            
            self.cursor.prevNode = left_node.prevNode
            self.cursor.nextNode = left_node
            left_node.prevNode = self.cursor
            left_node.nextNode = right_node

            if right_node != None :
                right_node.prevNode = left_node

            if self.cursor.prevNode == None:
                self.head = self.cursor

    def rightMove(self) :
        if self.cursor.nextNode != None :
            right_node = self.cursor.nextNode
            left_node = self.cursor.prevNode

            if right_node.nextNode != None :
                right_node.nextNode.prevNode = self.cursor
            self.cursor.nextNode = right_node.nextNode
            self.cursor.prevNode = right_node
            right_node.nextNode = self.cursor
            right_node.prevNode = left_node

            if left_node != None :
                left_node.nextNode = right_node
            else :
                self.head = right_node

    def backspace(self) :
        if self.cursor.prevNode != None :
            if self.cursor.prevNode.prevNode != None :
                self.cursor.prevNode.prevNode.nextNode = self.cursor
                self.cursor.prevNode = self.cursor.prevNode.prevNode
            else :
                self.head = self.cursor

    def delete(self) :
        if self.cursor.nextNode != None :
            to_delete = self.cursor.nextNode
            if to_delete.nextNode != None :
                self.cursor.nextNode = to_delete.nextNode
                to_delete.nextNode.prevNode = self.cursor
            else :
                self.cursor.nextNode = None

            
    def printList(self) :
        curr = self.head
        while curr != None :
            print(curr.value, end=' ')
            curr = curr.nextNode

inp = input("Enter Input : ").split(',')
temp_lst = []
for element in inp :
    temp_lst.append(element.split(' '))

newLinkedList = LinkedList()

for element in temp_lst :
    if element[0] == 'I' :
        newLinkedList.appendBeforeCursor(element[1])
    elif element[0] == 'L' :
        newLinkedList.leftMove()
    elif element[0] == 'R' :
        newLinkedList.rightMove()
    elif element[0] == 'B' :
        newLinkedList.backspace()
    elif element[0] == 'D' :
        newLinkedList.delete()

newLinkedList.printList()