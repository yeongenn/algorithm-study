import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\yeongenn\\algorithm-study\\PYTHON\\boj\\input.txt", "r")

from collections import deque
import copy

M, N = map(int, input().split())            # M: 열, N: 행
tomatoes = [list(map(int, input().split())) for _ in range(N)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
min_period = 0

queue = deque()


# 익은 토마토
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append((i, j))

while queue:
    y, x = queue.popleft()
    
    for i, j in zip(dy, dx):
        ny, nx = y + i, x + j
        if 0 <= ny < N and 0 <= nx < M and tomatoes[ny][nx] == 0:
            # 가중치 1 이라 dist 배열 필요 X, 바로 배열에서 마킹
            tomatoes[ny][nx] = tomatoes[y][x] + 1
            queue.append((ny, nx))

# 출력
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            min_period = -1
            print(min_period)
            exit()
        elif tomatoes[i][j] == -1:
            continue
        else:
            min_period = max(min_period, tomatoes[i][j])

print(min_period - 1)