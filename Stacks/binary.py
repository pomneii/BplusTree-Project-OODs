
"""
    จงเขียนโปรแกรมโดยใช้ stack เพื่อรับตัวเลขฐาน 10 แล้วเปลี่ยนเป็นเลขฐาน 2 แล้วให้แสดงผลดังตัวอย่าง

    class Stack :

        ### Enter Your Code Here ###

    def dec2bin(decnum):

        s = Stack()

        ### Enter Your Code Here ###

    print(" ***Decimal to Binary use Stack***")

    token = input("Enter decimal number : ")

    print("Binary number : ",end='')

    print(dec2bin(int(token)))
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
            return self.items.pop()
        
        def peek(self) :
            return self.items[-1]
        
        def isEmpty(self) :
            return self.items == []
        
        def __str__(self) -> str:
            return ''.join(map(str, self.items[::-1]))
        

def dec2bin(decnum) :

    s = Stack()
    while (decnum > 0) : 
        r = decnum % 2
        s.push(r)
        decnum = decnum // 2
    
    return s

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))