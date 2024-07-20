
# class Stack:
#     total = 0
#     def __init__(self, list = None) :
#         if list == None :
#             self.items = []
#         else :
#             self.items = list

# s = Stack()
# s1 = Stack(['A', 'B', 'C'])

"""
    push() : ใส่ด้านบน top
    pop() : เอา top ออกก่อน
    peek() : ดูแค่ top แต่ไม่เอาออก
    isEmpty() : เช็คว่า stack ว่างไหม
    size() : เช็คว่ามีของกี่อัน
"""

# push()

# class Stack :
#     def __init__(self, list = None) :
#         if list == None :
#             self.items = []
#         else :
#             self.items = list

#         self.size = len(self.items)

#     def push(self, i) :
#         self.items.append(i)
#         self.size += 1

# s = Stack()
# s.push('A')
# s.push('B')
# s.push('C')

# pop()
# class Stack :
#     def __init__(self, list = None) :
#         if list == None :
#             self.items = []
#         else :
#             self.items = list
#         self.size = len(self.items)
    
#     def push(self, i) :
#         self.items.append(i)
#         self.size += 1

#     def pop(self) :
#         return self.items.pop()
    
# s = Stack()
# s.push('A')
# s.push('B')
# s.push('C')
# print(s.items)
# print(s.pop())
# print(s.pop())
# s.pop()

# peek()
# class Stack :
#     def __init__(self, list = None) :
#         if list == None :
#             self.items = []
#         else :
#             self.items = list
#         self.size = len(self.items)
    
#     def push(self, i) :
#         self.items.append(i)
#         self.size += 1
    
#     def pop(self) :
#         return self.items.pop()
    
#     def peek(self) :
#         return self.items[-1]
    
# s = Stack(['A', 'B'])
# print(s.items)
# print(s.peek())
# print(s.items)

# isEmpty()
# class Stack :
#     def __init__(self, list = None) :
#         if list == None :
#             self.items = []
#         else :
#             self.items = list
#         self.size = len(self.items)
    
#     def push(self, i) :
#         self.items.append(i)
#         self.size += 1
    
#     def pop(self) :
#         return self.items.pop()
    
#     def peek(self) :
#         return self.items[-1]
    
#     def isEmpty(self) :
#         return self.items == []  # return len(self.items) == 0
    
# s = Stack(['A', 'B'])
# print(s.items)
# print(s.isEmpty())

# size()
# class Stack :
#     def __init__(self, list = None) :
#         if list == None :
#             self.items = []
#         else :
#             self.items = list
#         self.size = len(self.items)
    
#     def push(self, i) :
#         self.items.append(i)
#         self.size += 1
    
#     def pop(self) :
#         return self.items.pop()
    
#     def peek(self) :
#         return self.items[-1]
    
#     def isEmpty(self) :
#         return self.items == []  # return len(self.items) == 0
    
#     def get_size(self) :
#         return len(self.items)
    
# s = Stack(['A', 'B'])
# print(s.items)
# print(s.get_size())

# class Stack :
    # def __init__(self, list = None) :
    #     if list == None :
    #         self.items = []
    #     else :
    #         self.items = list
    #     self.size = len(self.items)
    
    # def push(self, i) :
    #     self.items.append(i)
    #     self.size += 1
    
    # def pop(self) :
    #     return self.items.pop()
    
    # def peek(self) :
    #     return self.items[-1]
    
    # def isEmpty(self) :
    #     return self.items == []  # return len(self.items) == 0
    
#     def get_size(self) :
#         return len(self.items)
    
    # def __str__(self) -> str:
    #     s = 'Stack of ' + str(self.get_size()) + ' items : '
    #     for ele in self.items :
    #         s += str(ele) + ' '

#         return s
    
# s1 = Stack([1, 2, 3])
# print(s1.items)
# print(s1)
# operand = ['+', '-', '*', '/', '^']

# print(operand.index('+') < operand.index('*'))
# a = 'A 1'
# print(len(a))

a = '2d'
print(a.isdigit())