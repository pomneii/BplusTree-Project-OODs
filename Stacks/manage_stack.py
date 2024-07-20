
"""
    จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้

    A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack

    P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )

    D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  

    LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

    MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

    การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

    *** Hint ***

    ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่าง ๆ

    Enter Input : P,P,MD 7,LD 7,D 7
    -1
    -1
    -1
    -1
    -1
    Value in Stack = []
"""

class Stack :
    def __init__(self, list = None) :
        if list == None :
            self.items = []
        else :
            self.items = list
        
    def push(self, i) :
        self.items.append(i)

    def pop(self) :
        if not self.isEmpty() :
            return self.items.pop()
        return None
    
    def isEmpty(self) :
        return len(self.items) == 0
    
    def peek(self) :
        if not self.isEmpty() :
            return self.items[-1]
        return None
    
    def delete(self, i) :
        for ele in self.items[:] :
            if ele == i :
                s2.push(ele)
                self.items.remove(ele)
                print(f"Delete = {ele}")
        
    def less_del(self, i) :
        for ele in self.items[:] :
            if ele < i :
                if i <= 0 :
                    s3.push(ele)
                    self.items.remove(ele)
                else :
                    s2.push(ele)
                    self.items.remove(ele)
                    print(f"Delete = {s2.peek()} Because {s2.peek()} is less than {i}")
        
        s3.item_delete_negative.sort()
        for num in s3.item_delete_negative :
            print(f"Delete = {num} Because {num} is less than {i}")

    def more_del(self, i) :
        for ele in self.items[:] :
            if ele > i :
                s2.push(ele)
                self.items.remove(ele)
                print(f"Delete = {s2.peek()} Because {s2.peek()} is more than {i}")

class StackDelete :
    def __init__(self, item_del = None) :
        if item_del == None :
            self.item_delete = []
        else :
            self.item_delete = item_del

    def push(self, i) :
        self.item_delete.append(i)

    def peek(self) :
        return self.item_delete[-1]

class StackDeleteNegative :
    def __init__(self, item_del = None) :
        if item_del == None :
            self.item_delete_negative = []
        else :
            self.item_delete_negative = item_del

    def push(self, i) :
        self.item_delete_negative.append(i)

    def peek(self) :
        return self.item_delete_negative[-1]
    
    
inp = input("Enter Input : ").split(',')
s = Stack()
s2 = StackDelete()
s3 = StackDeleteNegative()

for ele in inp :
    temp = ele.split(' ')
    
    if temp[0] == 'A' :
        s.push(int(temp[1]))
        print("Add =", s.peek())
    elif temp[0] == 'P' :
        if s.isEmpty() :
            print(-1)
        else :
            print("Pop =", s.pop())
    elif temp[0] == 'D' :
        if s.isEmpty() :
            print(-1)
        else :
            s.delete(int(temp[1]))
    elif temp[0] == 'LD' :
        if s.isEmpty() :
            print(-1)
        else :
            s.less_del(int(temp[1]))
    elif temp[0] == 'MD' :
        if s.isEmpty() :
            print(-1)
        else :
            s.more_del(int(temp[1]))

print("Value in Stack =", s.items)
