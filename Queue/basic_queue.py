
"""
    ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา

    E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผลค่าที่ทำการ enqueue และ index ของตัวที่ทำการเพิ่มเข้าไป

    D           ให้ทำการ dequeue ตัวที่อยู่หน้าสุดของ Queue ออกและแสดงตัวเลขที่เอาออกและแสดงขนาดของ Queue

                หลังจากทำการ dequeue แล้ว

    *** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty ***

    Enter Input : E 10,E 20,E 30,E 40,D,D
    Add 10 index is 0
    Add 20 index is 1
    Add 30 index is 2
    Add 40 index is 3
    Pop 10 size in queue is 3
    Pop 20 size in queue is 2
    Number in Queue is :  ['30', '40']
"""

class Queue :
    def __init__(self, list = None) :
        if list == None :
            self.items = []
        else :
            self.items = list
    
    def enQueue(self, i) :
        self.items.append(i)

    def deQueue(self) :
        if not len(self.items) == 0 :
            return self.items.pop(0)
        else :
            return None
    
inp = input("Enter Input : ").split(',')
q = Queue()
inp_lst = []
for ele in inp :
    inp_lst.append(ele.split())

for ele in inp_lst :
    if len(ele) == 1 :
        a = q.deQueue()
        if a == None :
            print(f"-1")
        else :
            print(f"Pop {a} size in queue is {len(q.items)}")
    else :
        q.enQueue(ele[1])
        print(f"Add {ele[1]} index is {q.items.index(ele[1])}")

if len(q.items) == 0 :
    print(f"Empty")
else :
    print(f"Number in Queue is :  {q.items}")