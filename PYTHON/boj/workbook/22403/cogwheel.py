import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

"""
첫번째 줄은 톱니 상태
12시 방향부터 시계방향
N극은 0, S극은 1

1은 시계 방향 회전, -1은 반시계

2, 6
"""
from collections import deque

wheels = [deque(map(int, input())) for _ in range(4)]
K = int(input())
way = [list(map(int, input().split())) for _ in range(K)]

# # cw, ccw
# wheels[0].rotate(1)
# wheels[0].rotate(-1)

"""
회전하고 난 다음에 비교하는게 아니라 처음 상태를 비교...
극 비교 -> 회전
"""

# def turn_left_cogs(idx, cog, dir):
#     if idx < 0:
#         return
    
#     if dir != 0:
#         if wheels[idx][2] != cog:
#             dir = -dir
#             wheels[idx].rotate(dir)
#         else:
#             dir = 0
#         turn_left_cogs(idx - 1, wheels[idx][6], dir)
#     else:
#         return
    
# 바퀴 돌지 않는 경우는 생각 안해도 된다 -> rotate 안 시키면 된다
# 내가 놓친 부분: 한번 회전 멈추면 그 뒤로는 쭉 회전 X
def left_wheel(idx, cog, dir):
    if idx < 0:
        return
    
    # 같은 극이 아닐 떄만 회전 + 오른쪽 나머지 바퀴 체크
    if wheels[idx][2] != cog:
        left_wheel(idx - 1, wheels[idx][6], -dir)
        wheels[idx].rotate(-dir)

def right_wheels(idx, cog, dir):
    if idx > 3:
        return
    
    if wheels[idx][6] != cog:
        right_wheels(idx + 1, wheels[idx][2], -dir)
        wheels[idx].rotate(-dir)
        

for idx, dr in way:
    # 인덱스 조정
    idx -= 1
    left_wheel(idx - 1, wheels[idx][6], dr)
    right_wheels(idx + 1, wheels[idx][2], dr)
    wheels[idx].rotate(dr)
    
score = 0
for i in range(4):
    if wheels[i][0] == 1:
        score += (2 ** i)
    
print(score)