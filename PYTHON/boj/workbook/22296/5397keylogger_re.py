import sys
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

# java to py
####################################### 시간 초과 #######################################

# T = int(input())

# class ListIterator:
#     def __init__(self, li):
#         self.li = li
#         self.index = 0
        
#     def next(self): # 현재 커서 기준 오른쪽
#         if not self.hasnext():
#             return None
#         val = self.li[self.index]
#         self.index += 1 # 한 칸 이동
#         return val

#     def previous(self):
#         if not self.hasprevious:
#             return None
#         val = self.li[self.index - 1]
#         self.index -= 1
#         return val
    
#     def hasnext(self):
#         return self.index < len(self.li)
    
#     def hasprevious(self):
#         return self.index > 0
    
#     def add(self, val):
#         self.li.insert(self.index, val)
#         self.index += 1
        
#     def delete(self):
#         self.li.pop(self.index - 1)
#         self.index -= 1
        
#     def print(self):
#         print(''.join(self.li))


# for _ in range(T):
#     logged = list(input())
#     password = []
#     l_iter = ListIterator(password)
    
#     for char in logged:
#         if char == "<":
#             if l_iter.hasprevious():
#                 l_iter.previous()
#         elif char == ">":
#             if l_iter.hasnext():
#                 l_iter.next()
#         elif char == "-":
#             if l_iter.hasprevious():
#                 l_iter.delete()
#         else:
#             l_iter.add(char)
        
#     l_iter.print()
    
######################################################################################

# deque로 풀거나 커서 위치 기준으로 left, right stack 각각 두기
from collections import deque

T = int(input())
    
for _ in range(T):
    logged = list(input())
    temp = []
    password = []
    
    for char in logged:
        if char == "<":
            if len(password) != 0:
                temp.append(password.pop())
        elif char == ">":
            if len(temp) != 0:
                password.append(temp.pop())
        elif char == "-":
            if len(password) != 0:
                password.pop()
        else:
            password.append(char)
    
    while temp:
        password.append(temp.pop())
        
    print(''.join(password))