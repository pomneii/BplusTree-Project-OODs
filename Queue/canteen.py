
"""
    โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน 
    ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
    Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear
    Input 
    จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
    E < id >  ->   เป็นการนำพนักงานเข้า Queue
    D         ->   เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty

    อธิบาย TestCase_1 :  จะมีพนักงาน 4 คน คือแผนก 1 id=101,102 และแผนก 2 id=201,202  ต่อมาจะแสดงผล Empty เพราะยังไม่มีพนักงานในแถว  
    และนำพนักงาน id=101และ201 เข้าแถวตามลำดับ ต่อมาจะแสดงผลเป็น 101 เพราะพนักงาน 101 อยู่คนแรกและแสดงผล 201 เพราะอยู่คนแรก

    Enter Input : 1 101,1 102,2 201,2 202/D,E 101,E 201,D,D
    Empty
    101
    201
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
            return self.items.pop(0)[1]
        else :
            return None
        
inp = input("Enter Input : ").split(',')
q = Queue()
temp_lst = []

for element in inp :
    if '/E' in element or '/D' in element :
        command, data = element.split('/')
        temp_lst.append(command.split())
        temp_lst.append(data.split())
    else :
        temp_lst.append(element.split())

for ele in temp_lst :
    if ele[0] == 'E' :
        inserted = False
        for i in range(len(q.items)) :
            if q.items[i][1][0] == ele[1][0] :  
                if i + 1 < len(q.items) and q.items[i][1][0] == q.items[i + 1][1][0] :
                    q.items.insert(i + 2, ele)
                    inserted = True
                    break
                else:
                    q.items.insert(i + 1, ele)
                    inserted = True
                    break
        if not inserted :
            q.enQueue(ele)
    elif ele[0] == 'D'  :
        if len(q.items) == 0 :
            print("Empty")
        else :
            print(q.deQueue())
