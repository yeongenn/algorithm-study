from collections import deque
import sys

N, F = map(int, sys.stdin.readline().split())

def peek(stack):
    length = len(stack)
    
    if length == 0:
        return -1
    return stack[length - 1]

########################################### 시간 초과 ###########################################

# cnt = 0
# stack = [[] for _ in range(7)]  # dat
# for _ in range(N):
#     str_num, f_num = map(int, input().split())
#     # 프렛 여러 개 -> 가장 높은 프렛 기준
#     # 줄 여러 개 -> 가장 높은 줄 기준

#     if peek(stack[str_num]) < f_num:
#         stack[str_num].append(f_num)
#         cnt += 1
#     elif peek(stack[str_num]) > f_num:
#         while peek(stack[str_num]) > f_num:
#             stack[str_num].pop()
#             cnt += 1
#         else:
#             if peek(stack[str_num]) == f_num:
#                 continue
#             elif peek(stack[str_num]) < f_num:
#                 stack[str_num].append(f_num)
#                 cnt += 1
#     else:
#         continue
     
# print(cnt) # 결과 출력

################################################################################################

# input() -> sys.stdin.readline()으로 수정
cnt = 0
stack = deque([[] for _ in range(7)])
for _ in range(N):
    str_num, f_num = map(int, sys.stdin.readline().split())

    if peek(stack[str_num]) < f_num:
        stack[str_num].append(f_num)
        cnt += 1
    elif peek(stack[str_num]) > f_num:
        while peek(stack[str_num]) > f_num:
            stack[str_num].pop()
            cnt += 1
        else:
            if peek(stack[str_num]) == f_num:
                continue
            elif peek(stack[str_num]) < f_num:
                stack[str_num].append(f_num)
                cnt += 1
    else:
        continue
print(cnt)