import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

import pprint

N = int(input())    # 색종이 장수
paper = [[0] * 1001 for _ in range(1001)]
for n in range(1, 1 + N):
    sy, sx, ey, ex = map(int, input().split())
    for i in range(sy, sy + ey):
        for j in range(sx, sx + ex):
            paper[i][j] = n

# pprint.pprint(paper)
result = [0] * 1001
for i in range(1001):
    for j in range(1001):
        result[paper[i][j]] += 1

for x in range(1, 1 + N):
    print(result[x])