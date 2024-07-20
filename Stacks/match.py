
"""
    ให้น้องๆเขียนโปรแกรมรับ input เป็นวงเล็บ โดยมีรูปแบบดังนี้  วงเล็บเปิด :  (  กับ  [    วงเล็บปิด :  )  กับ  ]   
    โดยให้หาว่าถ้าหากนำวงเล็บมาจับคู่กัน จะครบทุกคู่หรือไม่  โดยให้แสดงผลลัพธ์ที่บอกว่าคู่วงเล็บที่ Input เข้ามานั้น Match กันหรือไม่
"""

class Stack:
    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = lst
        self.size = len(self.items)

    def push(self, item):
        self.items.append(item)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.items.pop()
        return None

def check_bracket(opens, closes) :
    open_lst = '(['
    close_lst = ')]'

    return open_lst.index(opens) == close_lst.index(closes)

def check_match(input_string):
    stack = Stack()
    for char in input_string:
        if char in '[(':
            stack.push(char)
        elif char in ')]':
            if stack.size > 0:
                if not check_bracket(stack.pop(), char):
                    return "Parentheses : Unmatched ! ! !"
            else:
                return "Parentheses : Unmatched ! ! !"
    
    if stack.size == 0:
        return "Parentheses : Matched ! ! !"
    else:
        return "Parentheses : Unmatched ! ! !"

a = input("Enter Input : ")
print(check_match(a))

