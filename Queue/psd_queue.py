
"""
    PSD48 (P-Saderd 48 Group) เป็นวงไอดอลวงหนึ่งที่กระแสกำลังมาแรง ณ ตอนนี้โดยเพลงที่ได้รับความนิยมอย่างมากคือเพลงจี่หอย โดยวง PSD48 กำลังจะจัดงานจับมือขึ้น โดยมีกฎอยู่ว่าถ้าหากคนที่กำลังต่อแถวอยู่เป็นคนจาก กองกำลังสำรวจ จะได้สิทธิพิเศษในการแทรกแถวไปข้างหน้าสุดทันที (แต่ถ้าหากคนหน้าสุดก็เป็นคนของกองกำลังสำรวจก็ต้องต่อหลังเขาอยู่ดี)  PSD48 อยากให้คุณช่วยเขียนโปรแกรมสำหรับหาว่าจะมีโอตะ id ใดบ้างที่ได้จับมือ

    เพลงประกอบ : https://youtu.be/Jd4Hd-HFgls

    Input :
    EN <value>  เป็นโอตะธรรมดา  id = value
    ES <value>  เป็นโอตะของกองกำลังสำรวจ  id = value
    D           เป็นคำสั่งแสดงผล value ของหัวแถว ถ้าหากในแถวไม่มีคนจะแสดงคำว่า Empty

    Enter Input : EN 1,EN 2,D,D,D,EN 3,D
    1
    2
    Empty
    3
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
        if len(self.items) == 0 :
            return None
        return self.items.pop(0)[1]

inp = input("Enter Input : ").split(',')
q = Queue()
input_lst = []
for ele in inp :
    if len(ele) == 1 :
        input_lst.append(ele)
    else :
        input_lst.append(ele.split())

for element in input_lst :
    if element[0] == 'D':
        if len(q.items) == 0 :
            print("Empty")
        else :
            print(q.deQueue())
    elif element[0] == 'ES' :
        inserted = False
        for i in range(len(q.items)) :
            if q.items[i][0] == 'EN' :
                q.items.insert(i, element)
                inserted = True
                break
        if not inserted :
            q.enQueue(element)
    elif element[0] == "EN" :
        q.enQueue(element)


