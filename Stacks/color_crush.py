"""
    หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  
    ผิดทั้งหมดกฤษฎาได้กล่าวไว้  เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน 
    เช่น  A B B B A  -> A A เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา

    โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงลำดับของสีที่เหลือจากขวาไปซ้าย
"""

class Stack :
    def __init__(self, lst = None) :
        if lst == None :
            self.items = []
        else :
            self.items = lst
    
    def isEmpty(self) :
        return len(self.items) == 0
    
    def push(self, i) :
        self.items.append(i)

    def pop(self) :
        if self.isEmpty() :
            return None
        return self.items.pop()
    
inp = input("Enter Input : ").split(' ')
inp = inp[::-1]
s = Stack()

count = 0

for i in range(len(inp)) :
    s.push(inp[i])
    if len(s.items) > 2 :
        if s.items[-3] == s.items[-1] and s.items[-1] == s.items[-2] :
            s.pop()
            s.pop()
            s.pop()
            count += 1

print(len(s.items))
if len(s.items) == 0 :
    print("Empty")
else :
    print(''.join(s.items))
if count >= 2 :
    print("Combo 2 !!!")