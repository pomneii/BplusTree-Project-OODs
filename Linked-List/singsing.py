
"""
    วันหนึ่งนายที่มาก่อน y แต่หลัง w อยากลองทดสอบเสียงจึงไล่คีย์โน้ต โด เร มี ฟา ซอน ลา ที แต่เขาไม่ชอบที่ร้องซ้ำคีย์เดิม และมีคีย์อยู่ในหัวใจ 
    แต่คนอื่นในจักรวาลมักจะให้คีย์ที่ไม่ถูกใจเขา เขาจึงอยากวอนขอให้โปรแกรมเมอร์ระดับจักรวาลช่วยเขียนโปรแกรมนี้ขึ้นมา โดยการทำงานมีดังนี้

    อินพุทแรก จะรับคีย์โน้ตโดยสามารถซ้ำกันได้ และคั่นด้วยช่องว่าง

    อินพุทที่สอง จะรับ serie of operation และจะคั่นด้วยคอมม่า โดยมี 3 รูปแบบดังนี้

    D(Delete) : ให้ทำการลบตัวหลังสุดของ LinkedList

    R(Rename) : ให้เปลี่ยนคีย์โน้ตตัวหลังสุดของ LinkedList ตามที่ป้อนมา เช่น R mi แปลว่า เปลี่ยนจาก … เป็น mi

    A(Add) : ให้เพิ่มคีย์โน้ตตามที่ป้อมมา เช่น A mi แปลว่า เพิ่มโน้ต mi ต่อท้าย LinkedList

    ด้วยการรับมาในครั้งเดียว แบ่ง อินพุททั้ง 2 ด้วยเครื่องหมาย / 
    ให้แสดงผล LinkedList 3 ครั้ง โดยมีรูปแบบเป็นไปตาม Test Case
    ก่อนจะทำตาม operation ต่างๆที่ป้อนมา
    หลังจากทำตาม operation
    LinkedList ที่ไม่มีข้อมูลซ้ำกัน

    สามารถเพิ่มโค้ดในบรรทัดที่เขียนว่า #CODE HERE หรือเพิ่ม method ในคลาส LinkedList ได้

    ****Note****
    -หากมี Error เกิดขึ้นในระหว่างที่ทำ operation ให้แสดงคำว่า Error!!! ทันที
    -ถ้า LinkedList ว่าง ให้แสดงคำว่า LinkedList is empty!

    *******ห้ามใช้ List! ให้ใช้ class Node ในการทำ Linked List เท่านั้น*********
"""


class Node :
    def __init__(self, value=None, next=None) :
        self.value = value
        self.next = next


class LinkList :
    def __init__(self) :
        self.head = None
        self.size = 0

    def appendHead(self, value) :
        node = Node(value, self.head)
        self.head = node
        self.size += 1

    def appendLast(self, value) :
        if self.head == None :
            self.appendHead(value)
            return
        p = self.head
        while p.next != None :
            p = p.next
        p.next = Node(value)
        self.size += 1

    def removeLast(self) :
        if self.head == None :
            return "Error"
        if self.head.next == None :
            self.head = None
            self.size -= 1
            return
        p = self.head
        while p.next.next != None :
            p = p.next
        p.next = None
        self.size -= 1

    def rename(self, newName) :
        if self.head == None :
            return "Error"
        p = self.head
        while p.next != None :
            p = p.next
        p.value = newName

    def printList(self) :
        if self.head == None :
            print("Linklist is empty!")
            return
        p = self.head
        while p != None :
            if p.next == None :
                print(p.value)
                return
            print(p.value, end=' -> ')
            p = p.next

    def printListWithNoDuplicate(self) :
        if self.head is None :
            print("Linklist is empty!")
            return
        result = set()
        p = self.head
        first_element_printed = False
        while p is not None :
            if p.value not in result:
                if first_element_printed:
                    print(" -> ", end='')
                print(p.value, end='')
                result.add(p.value)
                first_element_printed = True
            p = p.next
        print()

def convertToLinkList(ls) :
    link_list = LinkList()
    for ele in ls :
        link_list.appendLast(ele)
    return link_list

print("*** My Favourite Keynote ***")

inp1, inp2 = input("Enter Input / List of operation : ").split('/')
temp_operation = []

listSong = inp1.split()
operations = inp2.strip().split(", ")
for ele in operations:
    temp_operation.append(ele.split())
myLinkList = convertToLinkList(listSong)

myLinkList.printList()

for ele in temp_operation:
    if ele[0] == 'A' :
        myLinkList.appendLast(ele[1])
    elif ele[0] == 'R':
        if myLinkList.rename(ele[1]) == "Error" :
            print("Error!!!")
    elif ele[0] == 'D' :
        if myLinkList.removeLast() == "Error" :
            print("Error!!!")

if myLinkList == None :
    print("LinkedList is empty!")
else :
    myLinkList.printList()

myLinkList.printListWithNoDuplicate()

