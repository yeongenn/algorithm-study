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

for o, dr in way:
    wheels[o - 1]