
# class Queue :
#     def __init__(self) :
#         self.items = []

# q = Queue()
# print(q.items)

# default argument
# class Queue :
#     def __init__(self, list = None) :
#         if list == None :
#             self.items = []
#         else :
#             self.items = list

# q = Queue()
# print(q.items)
# q1 = Queue(['A', 'B', 'C'])
# print(q1.items)

# enQueue()
# class Queue :
#     def __init__(self, list = None) :
#         if list == None :
#             self.items = []
#         else :
#             self.items = list

#     def enQueue(self, i) :
#         self.items.append(i)

# q = Queue()
# print(q.items)
# q.enQueue('A')
# print(q.items)
# q.enQueue('B')
# print(q.items)
# q.enQueue('C')
# print(q.items)

# deQueue()
# class Queue :
#     def __init__(self, list = None) :
#         if list == None :
#             self.items = []
#         else :
#             self.items = list

#     def enQueue(self, i) :
#         self.items.append(i)

#     def deQueue(self) :
#         return self.items.pop(0)
    
# q = Queue(['A', 'B'])
# print(q.items)
# print(q.deQueue())
# print(q.items)
# print(q.deQueue())
# print(q.items)

# isEmpty()
# class Queue :
#     def __init__(self, list = None) :
#         if list == None :
#             self.items = []
#         else :
#             self.items = list

#     def enQueue(self, i) :
#         self.items.append(i)

#     def deQueue(self) :
#         return self.items.pop(0)
    
#     def isEmpty(self) :
#         return self.items == [] # return len(self.items) == 0

# q = Queue(['A', 'B'])
# print(q.isEmpty())

# size()
# class Queue :
#     def __init__(self, list = None) :
#         if list == None :
#             self.items = []
#         else :
#             self.items = list

#     def enQueue(self, i) :
#         self.items.append(i)

#     def deQueue(self) :
#         return self.items.pop(0)
    
#     def isEmpty(self) :
#         return self.items == [] # return len(self.items) == 0
    
#     def get_size(self) :
#         return len(self.items)
    
# q = Queue(['A', 'B'])
# print(q.items)
# print(q.get_size())

# from collections import deque

# class Queue :
#     def __init__(self) :
#         self.items = deque()

#     def enQueue(self, i) :
#         self.items.append(i)

#     def deQueue(self) :
#         return self.items.popleft()
    
#     def isEmpty(self) :
#         return len(self.items) == 0
    
#     def get_size(self) :
#         return len(self.items)

print(ord('g'))
a = '2 203 41'
print(a.find('/E'))