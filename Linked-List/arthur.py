
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
    def __init__(self, value = None, next = None, prev = None) :
        self.value = value
        if next == None :
            self.next = None
        else :
            self.next = next
        self.prev = prev

    def __str__(self) :
        return str(self.value)
    
class LinkList :
    def __init__(self) :
        self.head = None
        self.size = 0

    def appendHead(self, value) :
        node = Node(value)
        if self.head != None :
            self.head = node
            self.head.next = self.head
            self.head.prev = self.head
        else :
            tail = self.head.prev
            node.next = self.head
            node.prev = tail
            self.head.prev = node
            tail.next = node
            self.head = node
        self.size += 1

    def appendLast(self, value) :
        if self.head == None :
            self.appendHead(value)
            return
        tail = self.head.prev
        node = Node(value, self.head, tail)
        tail.next = node
        self.head.prev = node
        self.size += 1

def convertToLinkedList(lst) :
    linkList = LinkList()
    for element in lst :
        linkList.appendLast(element)
    return linkList

inp = input("Enter unsorted Linked List: ").split(' ')
print(inp)
