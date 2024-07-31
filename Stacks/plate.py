"""
    กฤษฎาได้ถูกคุณแม่ไหว้วานให้ล้างจานกองเป็นภูเขา  แต่ทว่ากฤษฎาก็ได้สังเกตเห็นว่าจานแต่ละใบนั้นมีน้ำหนักที่แตกต่างกัน และบนจานยังมีตัวเลขอีกด้วย  
    กฤษฎาได้เหม่อลอยเนื่องจากครุ่นคริสว่าตัวเลขนั้นหมายถึงอะไร  กฤษฎาก็ได้ทำจานหลุดมือจนจานแตก  และเมื่อจานแตกได้มีเสียงที่มีความถี่ตามเลขบนจาน  
    กฤษฎาจึงนึกสนุกได้นำจานขนาดต่างๆและมีความถี่ต่างกันมาวางซ้อนๆกัน  โดยถ้าหากนำจานที่มีน้ำหนักมากกว่ามาวางบนจานที่มีน้ำหนักน้อยกว่า จะทำให้จานที่มีน้ำหนักน้อยกว่า แตก !!! 
    และจะแตกไปเรื่อยๆจนกว่าจานใบด้านล่างจะมีน้ำหนักเท่ากันหรือมากกว่า หรือจนกว่าจะไม่มีจานด้านล่างมารองรับแล้ว

    ให้น้องๆเขียนโปรแกรมอ่านลำดับของจานที่กฤษฎาได้วางลงไปโดยให้ใส่จานทีละใบ  ซึ่งรวมถึงขนาดของจานและความถี่ของจาน  
    จากนั้นให้หาว่าลำดับของความถี่ของจานที่ได้ยินเมื่อวางจานลงไปตามนั้นแล้วจะเป็นเช่นใด

    อธิบาย Input : จะมีแค่รูปแบบเดียวคือ   < a  b >  โดยที่  a = น้ำหนักของจาน  ,  b = ความถี่ของจาน

    Enter Input : 1 10,5 20,3 30,3 40,4 50
    10
    40
    30
"""

class Stack :
    def __init__(self, lst = None) :
        if lst == None :
            self.items = []
        else :
            self.items = lst
    
    def push(self, i) :
        self.items.append(i)

    def pop(self) :
        if self.isEmpty() :
            return None
        return self.items.pop()

    def isEmpty(self) :
        return len(self.items) == 0
    
    def peek(self) :
        if self.isEmpty() :
            return None
        return self.items[-1]
    
inp = input("Enter Input : ").split(',')
temp = [e.split(' ') for e in inp]
s = Stack()

for element in temp :
    if s.isEmpty() :
        s.push(element)
    else :
        if element[0] > s.peek()[0] :
            print(s.pop()[1])
            if not s.isEmpty() :
                if element[0] > s.peek()[0] :
                    print(s.pop()[1])
                elif element[0] == s.peek()[0] :
                    print(s.pop()[1])
        elif element[0] <= s.peek()[0] :
            s.push(element)
