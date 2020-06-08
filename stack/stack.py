"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return int(self.size)

#     def push(self, value):
#         self.value = value
#         self.storage.append(self.value)
#         self.size = self.size + 1

#     def pop(self):
#         if self.size >= 1:
#             self.size = self.size - 1
#             return self.storage.pop(self.size)

# # Used to test code
#     def __repr__(self):
#         return "{self.storage}".format(self=self)

# new_stack = Stack()
# print(new_stack)
# new_stack.push(1)
# new_stack.push(2)
# new_stack.push(3)
# print(new_stack)
# print(new_stack.__len__())
# new_stack.pop()
# print(new_stack)
# new_stack.pop()
# print(new_stack)
# new_stack.pop()
# print(new_stack)
# new_stack.pop()
# print(new_stack)


class Stack:
    def __init__(self):
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        self.size = self.size + 1

    def pop(self):
        self.size = self.size - 1