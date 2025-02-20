from collections import deque
import sys

input = sys.stdin.readline

N = int(input())    # 자료구조 갯수

A = list(map(int, input().split()))  # 0 : 큐, 1 : 스택
B = [deque([i]) for i in list(map(int, input().split()))]
M = int(input())    # 삽입할 수열 길이
C = list(map(int, input().split()))  # queuestack에 삽입할 원소 담고 있는 길이 M의 수열

result = []

##############################시간 초과##############################
# for i in C:
#     temp = i  # 다음 자료구조에 넘길 원소
#     for j in range(N):
#         if A[j] == 0:   # queue
#             B[j].append(temp)
#             # temp = B[j].pop(0)
#             temp = B[j].popleft()
#         elif A[j] == 1:   # stack
#             B[j].append(temp)
#             temp = B[j].pop()
#     result.append(temp)

# print(*result)

##############################시간 초과##############################

for i in C:
    temp = i  # 다음 자료구조에 넘길 원소
    for j in range(N):
        if A[j] == 0:   # queue
            B[j].append(temp)
            temp = B[j].popleft()
    result.append(temp)

print(*result)


