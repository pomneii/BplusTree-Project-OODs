
"""
    ณ เมืองแห่งหนึ่ง ที่มีชื่อว่า ... อืม (เอ้าผู้แต่งโจทย์คิดชื่อไม่ออก เอาเป็นว่าไม่ต้องสนใจก็ได้) 
    จะมีบริการคมนาคมสาธารณะ ซึ่งเป็นสิ่งที่น้องๆ พี่ๆ อาจารย์ หรือ บุคคลอื่นๆ ที่อาจจะคุณเคยกันหรือเคยนั้งก็มานั้นก็คือ "รถไฟฟ้า" นั้นเอง
    โดยแต่ละเมือง จะเปรียบเหมือน Node ของ Linked List ซึ่งรถไฟฟ้าจะมีทั้งขาไปขากลับนั้นเอง และ 
    รถไฟฟ้าขาไป ผ่านสถานีสุดท้ายของทางรถไฟฟ้าจะวนกลับมาสถานีแรก หรือในทางกลับกัน 
    รถไฟฟ้าขากลับผ่านสถานีแรกก็จะวนกลับไปสถานีสุดท้ายเช่นกัน 
    เพื่อให้ "พี่โบ๊ท" ที่เป็นชาวเมืองนี้มีรถไฟฟ้านั้นไปทำงานหรือท่องเทียวในเมืองนี้ได้สะดวกขึ้น 
    ต่อไปก็เป็นหน้าที่ของน้อง ๆ แล้วล่ะ ที่จะสานฝันให้เมืองนี้และ "พี่โบ๊ท" มี ระบบรถไฟฟ้าที่ "สมบูรณ์แบบ" ที่สร้างขึ้นมาจากน้ำมือของน้องเองๆ 

    input จะเป็น
    บรรทัดแรก จะเป็น list ของ ชื่อสถาณี
    บรรทัดสอง จะเป็น สถานีต้นทาง,สถานีปลายทาง,ทิศทางของรถไฟฟ้า(ถ้าไม่ใส่ให้แสดงผลในขาที่ระยะทางสั้นที่สุด ถ้าเกิดเท่ากัน ให้แสดงผลลัพธ์ทั้งขาไปและขากลับ)
    โดย F จะเป็น รถไฟฟ้าขาไป
        B จะเป็น รถไฟฟ้าขากลับ
    output จะเป็น
    แสดงการเดินทางของรถไฟฟ้า,จำนวนสถานีที่จะถึงปลายทาง

    ***Railway on route***
    Input Station name/Source, Destination, Direction(optional): A,B,C,D,E,F,G/C,G,F
    Forward Route: C->D->E->F->G,4
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
        if not self.head :
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

    def findIndex(self, value) :
        p = self.head
        index = 0
        while p.value != value :
            p = p.next
            index += 1
            if p == self.head :    # when loop from back to head, value not found
                return -1
        return index
    
    def length(self) :
        if self.head == None :
            return "Error"
        p = self.head
        count = 0
        while True :
            count += 1
            p = p.next
            if p == self.head :
                break
        return count

    def findPath(self, first, destination, direction = None) :
        startIndex = self.findIndex(first)
        endIndex = self.findIndex(destination)
        
        length = self.length()

        forward = (endIndex - startIndex) % length
        backward = (startIndex - endIndex) % length

        if backward < forward :
            way = "backward"
        elif forward < backward :
            way = "forward"
        elif forward == backward :
            way = "both"

        def printPath(start, end, direction) :
            path = []
            p = self.head
            while p.value != start :
                p = p.next
            while p.value != end :
                path.append(p.value)
                if direction == "forward" :
                    p = p.next
                else :
                    p = p.prev
            path.append(p.value)
            return "->".join(path), len(path) - 1

        if direction == None :
            if way == "forward" :
                result, count = printPath(first, destination, "forward")
                print(f"Forward Route: {result},{count}")
            if way == "backward" :
                result, count = printPath(first, destination, "backward")
                print(f"Backward Route: {result},{count}")
            if way == "both" :
                result1, count1 = printPath(first, destination, "forward")
                result2, count2 = printPath(first, destination, "backward")
                print(f"Forward Route: {result1},{count1}")
                print(f"Backward Route: {result2},{count2}")
        else :
            if direction == 'F' :
                result, count = printPath(first, destination, "forward")
                print(f"Forward Route: {result},{count}")
            if direction == 'B' :
                result, count = printPath(first, destination, "backward")
                print(f"Backward Route: {result},{count}")

def convertToLinkList(lst) :
    linkList = LinkList()
    for element in lst :
        linkList.appendLast(element)
    return linkList

print("***Railway on route***")
inp = input("Input Station name/Source, Destination, Direction(optional): ")
inp1, inp2 = inp.split('/')
inp1 = inp1.split(',')
inp2 = inp2.split(',')

newLinkList = convertToLinkList(inp1)

if len(inp2) == 2 :
    firstStation = inp2[0]
    destinationStation = inp2[1]
    direction = None
elif len(inp2) == 3 :
    firstStation = inp2[0]
    destinationStation = inp2[1]
    direction = inp2[2]

newLinkList.findPath(firstStation, destinationStation, direction)