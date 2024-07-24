
"""
    เขียนโปรแกรมคลุกคำ (scramble) สร้าง singly linked list ของคำในจดหมาย scramble จดหมายโดยทำคล้ายตัด ไพ่และกรีดไพ่ 
    ผู้รับจดหมาย descramble กรีดกลับและตัดกลับจนได้จดหมายฉบับเดิมที่อ่านได้(หากออกแบบดีๆ สามารถ scramble กี่ครั้งก็ได้ ขึ้นแรกให้ทำ ครั้งเดียวก่อน)  

    ***** รูปแบบ input *****

    แบ่งเป็น 2 ฝั่ง ได้แก่ ฝั่งซ้าย (Linked List เริ่มต้น  ความยาวขั้นต่ำของ Linked List รับประกันว่าขั้นต่ำคือ 10)  |  
                    ฝั่งขวา BottomUp กับ Riffle โดยการแทนด้วย B กับ R ซึ่งการรับ R กับ B สามารถสลับที่กันได้ เช่น   R 40,B 60  <->  B 60,R 40

    1.  B   < percentage >  :  bottomUp ตัด ยกส่วนบน (lift) ออกตาม % input ที่รับเข้ามา นำส่วนล่างมาซ้อนทับส่วนบน
    2.  R   < percentage >  :  riffleShuffle กรีด (จากด้านบน) lift ตาม % นำ node ของแต่ละลิสต์มาสลับกันทีละ node จากต้นลิสต์ ส่วนเกินนำมาต่อท้าย

    ***** ถ้าหากคิดเปอร์เซ็นของความยาว Linked List แล้วได้ทศนิยม ให้ปัดลงทั้งหมด *****
    ***** การแสดงผลมี Pattern เป็น   Bottomup  ->  Riffle  ->  Deriffle  -> Debottomup นะครับ

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        def __str__(self):
            return str(self.value)

    def createLL(LL):
        # Code Here

    def printLL(head):
        # Code Here

    def SIZE(head):
        # Code Here

    def scramble(head, b, r, size):
        # Code Here

    inp1, inp2 = input('Enter Input : ').split('/')
    print('-' * 50)
    h = createLL(inp1.split())
    for i in inp2.split('|'):
        print("Start : {0}".format(printLL(h)))
        k = i.split(',')
        if k[0][0] == "B" and k[1][0] == "R":
            scramble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
        elif k[0][0] == "R" and k[1][0] == "B":
            scramble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
        print('-' * 50)
"""

class Node :
    def __init__(self, value = None, nexts = None) :
        self.value = value
        self.nextNode = nexts

    def __str__(self) :
        return str(self.value)
    
class LinkedList :
    def __init__(self, head = None) :
        self.head = head

    def appendHead(self, value) :
        new_node = Node(value, self.head)
        self.head = new_node

    def appendLast(self, value) :
        if self.head == None :
            self.appendHead(value)
            return
        curr = self.head
        while curr.nextNode != None :
            curr = curr.nextNode
        curr.nextNode = Node(value)

def createLL(LL) :
    new_linkedList = LinkedList()
    for ele in LL :
        new_linkedList.appendLast(ele)
    return new_linkedList  

def printLL(head) :
    result = []
    curr = head.head
    while curr != None :
        result.append(curr.value)
        curr = curr.nextNode
    
    return ' '.join(map(str, result))

def SIZE(head) :
    count = 0
    curr = head.head
    while curr != None :
        count += 1
        curr = curr.nextNode
    return count

def bottomUp(head, b) :
    count = 0
    curr = head.head
    prev = None

    while count < b :
        prev = curr
        curr = curr.nextNode
        count += 1

    if curr == None :
        return head
    
    new_head = curr
    prev.nextNode = None

    tail = new_head
    while tail.nextNode != None :
        tail = tail.nextNode
    tail.nextNode = head.head
    head.head = new_head

    return head

def riffle(head, r) :
    r = int(r)
    if r == 0 or head.head == None :
        return head

    # Split the list into two halves
    count = 0
    firstHead = head.head
    secondHead = head.head

    for _ in range(r):
        if secondHead != None :
            secondHead = secondHead.nextNode

    firstHeadCurr = firstHead
    secondHeadCurr = secondHead

    # Detach the second half
    temp = firstHead
    for i in range(r - 1) :
        temp = temp.nextNode
    if temp != None :
        temp.nextNode = None

    dummy = Node()
    tail = dummy

    while firstHeadCurr != None and secondHeadCurr != None :
        tail.nextNode = firstHeadCurr
        firstHeadCurr = firstHeadCurr.nextNode
        tail = tail.nextNode

        tail.nextNode = secondHeadCurr
        secondHeadCurr = secondHeadCurr.nextNode
        tail = tail.nextNode

    while firstHeadCurr != None :
        tail.nextNode = firstHeadCurr
        firstHeadCurr = firstHeadCurr.nextNode
        tail = tail.nextNode

    while secondHeadCurr != None :
        tail.nextNode = secondHeadCurr
        secondHeadCurr = secondHeadCurr.nextNode
        tail = tail.nextNode

    head.head = dummy.nextNode

    return head

# def deriffle(head, r) :
#     r = int(r)
#     if r == 0 or head.head is None:
#         return head

#     firstHead = head.head
#     secondHead = firstHead.nextNode

#     firstHeadList = []
#     secondHeadList = []

#     current = head.head
#     index = 0
#     while current is not None:
#         if index % 2 == 0:
#             firstHeadList.append(current)
#         else:
#             secondHeadList.append(current)
#         current = current.nextNode
#         index += 1

#     dummy = Node()
#     tail = dummy

#     for node in firstHeadList:
#         tail.nextNode = node
#         tail = tail.nextNode
#     tail.nextNode = None

#     second_head = None
#     for node in reversed(secondHeadList):
#         node.nextNode = second_head
#         second_head = node

#     tail.nextNode = second_head

#     head.head = dummy.nextNode
#     return head

# def debottomUp(head, r) :
#     size = SIZE(head)
#     split_point = size - r
#     return bottomUp(head, split_point)


def scramble(head, b, r, size) :
    bottom_up_per = (b * size) // 100
    riffle_per = (r * size) // 100

    start = printLL(head)
    
    print(f"BottomUp{b: .3f} % : ", end='')
    bottomHead = bottomUp(head, bottom_up_per)
    x = printLL(bottomHead)
    print(x)

    print(f"Riffle{r: .3f} % : ", end='')
    riffleHead = riffle(bottomHead, riffle_per)
    print(printLL(riffleHead))

    head = head
    print(f"Deriffle{r: .3f} % : ", end='')
    # deriffleHead = deriffle(riffleHead, riffle_per)
    # deriffleHead = bottomUp(head, bottom_up_per)
    print(x)

    print(f"DebottomUp{b: .3f} % : ", end='')
    # debottomHead = debottomUp(deriffleHead, bottom_up_per)
    print(start)

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
for i in inp2.split('|') :
    h = createLL(inp1.split())
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R" :
        scramble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B" :
        scramble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)
