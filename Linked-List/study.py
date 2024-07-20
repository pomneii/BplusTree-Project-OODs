
# node class

# class Node :
#     def __init__(self, data, next = None) :
#         self.data = data
#         if next is None :
#             self.next = None
#         else :
#             self.next = next

#     def __str__(self) :
#         return str(self.data)

# p = Node('A', None)
# print(p)

# list 

# class list :
#     def __init__(self, head = None) :
#         if head == None :
#             self.head = self.tail = None
#             self.size = 0
#         else :
#             self.head = head
#             t = self.head
#             self.size = 1
#             while t.next != None : # find tail if t.next != None
#                 t = t.next
#                 self.size += 1
#             self.tail = t

# Creating a List

# class Node :
#     def __init__(self, data, next = None) :
#         self.data = data
#         if next == None :
#             self.next = None
#         else :
#             self.next = next

# class list :
#     def __init__(self) :
#         self.head = None
#         self.size = 0

#     def append(self, data) :
#         p = Node(data)
#         if self.head  == None :
#             self.head = p
#         else :
#             t = self.head
#             while t.next != None :
#                 t = t.next
#             t.next = p
#             self.size += 1

#     def add_head(self, data) :             # inserting at tail
#         p = Node(data)
#         p.next = self.head
#         self.head = p
#         self.size += 1

#     def removeHead(self) :                # removing at the head
#         if self.head == None : 
#             return
#         if self.head.next == None :
#             p = self.head
#             self.head = None
#         else :
#             p = self.head
#             self.head = self.head.next
#         self.size -= 1
#         return p.data
    
#     def removeTail(self) :                # removing at tail
#         if self.head == None : 
#             return
#         if self.head.next == None :
#             self.head = None
#             self.size -= 1
#             return
#         else :
#             p = self.head
#             while p.next.next != None :
#                 p = p.next
#             p.next = p.next.next
#             self.size -= 1

#     def insertAfter(self, i, data) :
#         p = Node(data)
#         q = self.head
#         count = 0
#         while q != None :
#             if count == i :
#                 p.next = q.next
#                 q.next = p
#                 return
#             q = q.next
#             count += 1

#     def deleteAfter(self, i) :
#         q = self.head
#         count = 0
#         while q != None and q.next != None :
#             if count == i :
#                 p = q.next
#                 q.next = p.next
#                 p = None
#                 self.size -= 1
#                 return
#             q = q.next
#             count += 1

#     def printList(self) :
#         p = self.head
#         while p != None :
#             print(p.data, end=' -> ')
#             p = p.next
#         print("None")

# header node
# class list :
#     def __init__(self) :
#         self.header = Node()
#         self.size += 1

#     def append(self, data) :
#         p = Node(data)
#         t = self.header.next
#         while t.next != None :
#             t = t.next
#         t.next = p
#         self.size += 1

#     def removingTail(self) :
#         if self.header.next == None :
#             self.size -= 1
#             return
#         p = self.header.next
#         while p.next.next != None :
#             p = p.next
#         p.next = p.next.next
#         self.size -= 1

# linked-list stack in python 

# class LinkedStack :
    # class _Node :
    #     ___slots__ = '_element', '_next'

    #     def __init__(self, element, next) :
    #         self._element = element
    #         self._next = next

#     # ------------------- stack methods -----------------------------------#
#     def __init__(self) :
#         # create empty stack
#         self._head = None
#         self._size = 0

#     def __len__(self) :
#         #  return the number of element in stack
#         return self._size
    
#     def is_empty(self) :
#         # return true if the stack is empty
#         return self._size == 0
    
#     def push(self, e) :
#         # add element to the top of the stack
#         self._head = self._Node(e, self._head)
#         self._size += 1

#     def top(self) :
#         # return ( but not remove) the element in the top of the stack
#         # raise if stack is empty
#         if self.is_empty() :
#             raise 'Stack is empty'
#         return self._head._element
    
#     def pop(self) :
#         # remove and return the element from the top of the stack
#         # raise if stack is empty

#         if self.is_empty() :
#             raise 'Stack is empty'
#         answer = self._head._element
#         self._head = self._head._element
#         self._size -= 1
#         return answer

# Linked-list queue in python

# class LinkedQueue :
#     class _Node :
#         ___slots__ = '_element', '_next'

#         def __init__(self, element, next) :
#             self._element = element
#             self._next = next
    
#     def __init__(self) -> None:
#         # create an empty queue
#         self._head = None
#         self._tail = None
#         self._size = 0

#     def __len__(self) :
#         # return the element in the queue
#         return self._size
    
#     def is_empty(self) :
#         # return true if queue is empty
#         return self._size == 0
    
#     def first(self) :
#         # return (but not remove) the element at the front of the queue
#         if self.is_empty() :
#             raise "Queue is empty"
#         return self._head._element
    
#     def dequeue(self) :
#         # remove and return the first element of the queue
#         # raise if the queue is empty
#         if self.is_empty() :
#             raise 'Queue is empty'
#         answer = self._head._element
#         self._head = self._head._next
#         self._size -= 1
#         if self.is_empty() :
#             self._tail = None
#         return answer
    
#     def enqueue(self, e) :
#         # add n element to the back of queue
#         newest = self._Node(e, None)
#         if self.is_empty() :
#             self._head = newest
#         else :
#             self._tail._next = newest
#         self.tail = newest
#         self._size += 1

# Doubly-Linked List with header node

# class _DoublyLinkedBase :
#     class _Node :
#         ___slots__ = '_element', '_prev', '_next'

#         def __init__(self, element, prev, next) :
#             self._element = element
#             self._prev = prev
#             self._next = next

#     def __init__(self) :
#         # create an empty list
#         self._header = self._Node(None, None, None)
#         self._trailer = self._Node(None, None, None)
#         self._header._next = self._trailer
#         self._trailer._prev = self._header
#         self._size = 0

#     def __len__(self) :
#         # return the number of elements in the list
#         return self._size
    
#     def is_empty(self) :
#         # return true if list is empty
#         return self._size == 0
    
#     def _insert_between(self, e, predecessor, successor) :
#         # add element e between two existing nodes and return new node
#         newest = self._Node(e, predecessor, successor)
#         predecessor._next = newest
#         successor._prev = newest
#         self._size += 1
#         return newest
    
#     def _delete_node(self, node) :
#         # delete nonsentinel node from the list and return its element
#         predecessor = node._prev
#         successor = node._prev
#         predecessor._next = successor
#         successor._next = predecessor
#         self._size -= 1
#         element = node._element
#         node._prev = node._next = node._element = None
#         return element

# print("Hello")