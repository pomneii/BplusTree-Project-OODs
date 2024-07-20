
"""
    ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
    +: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
    -: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
    *: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
    /: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
    DUP: Duplicate (not double) ค่าบนสุดของ stack
    POP: Pop ค่าบนสุดออกจาก stack และ discard.
    PSH: ทำการ push ตัวเลขลง stack
    หมายเหตุ 1. คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
    2. การนำค่าออกจาก stack สำหรับ calculator นี้ให้ การนำค่าออกจาก stack ครั้งแรกเป็น operand ด้านซ้าย และ การนำค่าออกจาก stack ครั้งที่ 2 เป็น operand ด้านขวา
    *************************************************
    print("* Stack Calculator *")
    arg = input("Enter arguments : ")
    machine = StackCalc()
    machine.run(arg)
    print(machine.getValue())
"""

class StackCalcTemp :

    def __init__(self, list = None) :
        if list == None :
            self.items_temp = []
        else :
            self.items_temp = list

    def push(self, i) :
        self.items_temp.append(i)

    def pop(self) :
        if not len(self.items_temp) == 0:
            return self.items_temp.pop()    
        else :
            return None
        
    def peek(self) :
        if not len(self.items_temp) == 0 :
            return self.items_temp[-1]
        else :
            return None

class StackCalc :

    def __init__(self, list = None) :
        if list == None :
            self.items = []
        else :
            self.items = list

    def run(self, inp_lst) :
        for ele in inp_lst :
            self.items.append(ele)
        
        for element in self.items :
            operand = ['+', '-', '*', '/', 'DUP', 'POP', 'PSH']
            if element.isdigit() :
                temp.push(int(element))
            else :
                if element in operand :
                    if element == '+' :
                        a = temp.pop()
                        b = temp.pop()
                        temp.push(a+b)
                    elif element == '-' :
                        a = temp.pop()
                        b = temp.pop()
                        temp.push(a-b)
                    elif element == '*' :
                        a = temp.pop()
                        b = temp.pop()
                        temp.push(a*b)
                    elif element == '/' :
                        a = temp.pop()
                        b = temp.pop()
                        temp.push(a/b)
                    elif element == 'DUP' :
                        temp.push(temp.peek())
                    elif element == 'POP' :
                        temp.pop()
                else :
                    temp.push(element)
                    break

    def getValue(self) :
        if not str(temp.peek()).isalpha() :
            return int(temp.peek())
        elif len(temp.items_temp) == 0 :
            return 0
        else :
            return f"Invalid instruction: {temp.peek()}"

print("* Stack Calculator *")
arg = input("Enter arguments : ").split(' ')
machine = StackCalc()
temp = StackCalcTemp()
machine.run(arg)
print(machine.getValue())