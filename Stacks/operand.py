
"""
    ให้รับ Input เป็น  Infix  และแสดงผลลัพธ์ออกมาเป็น  Postfix   โดยจะมี Operator  5  แบบ  ได้แก่  +   -   *   /   ^

    class Stack:

        def __init__(self):

        def push(self, value):

        def pop(self):

        def get_size(self):

        def isEmpty(self):

    inp = input('Enter Infix : ')

    S = Stack()

    print('Postfix : ', end='')

    ### Enter Your Code Here ###

    while not S.isEmpty():

        print(S.pop(), end='')

    print()
"""

class Stack :
    def __init__(self, list = None):
        if list == None :
            self.items = []
        else :
            self.items = list
        self.size = len(self.items)

    def push(self, value):
        self.items.append(value)
        self.size += 1

    def pop(self):
        if not self.isEmpty() :
            self.size -= 1
            return self.items.pop()
        return None
    
    def get_size(self):
        return self.size

    def isEmpty(self):
        return self.items == []
    
    def peek(self) :
        if not self.isEmpty():
            return self.items[-1]
        return None

inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')

operand = ['-', '+', '*', '/', '^', '(', ')']

def check_operand(chars) :
    if chars == '^' :
        return 3
    elif chars == '*' or chars == '/' :
        return 2
    elif chars == '+' or chars == '-' :
        return 1
    else :
        return 0

for i in range(len(inp)) :
    if inp[i].isalnum() :
        print(inp[i], end='')
    else :
        if S.isEmpty() :
            S.push(inp[i])
        elif inp[i] == '(' :
            S.push(inp[i])
        elif inp[i] == ')' :
            while not S.isEmpty() and S.peek() != '(':
                print(S.pop(), end='')
            S.pop()
        elif inp[i] in operand :
            while not S.isEmpty() and check_operand(inp[i]) <= check_operand(S.peek()) :
                print(S.pop(), end='')
            S.push(inp[i])

while not S.isEmpty():

    print(S.pop(), end='')

