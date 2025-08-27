import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\yeongenn\\algorithm-study\\PYTHON\\boj\\input.txt", "r")

from collections import deque

# 7576에 높이가 더해짐 -> 3차원

M, N, H = map(int, input().split())             # M: 열, N: 행, H: 높이
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dy, dx, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
queue = deque()

# 익은 토마토 찾기
# 3차원: for문 돌릴 때 역순으로
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 1:
                queue.append((h, n, m))

# 토마토 익히기~
while queue:
    z, y, x = queue.popleft()
    
    for i, j, k in zip(dz, dy, dx):
        nz, ny, nx = z + i, y + j, x + k
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and tomatoes[nz][ny][nx] == 0:
            tomatoes[nz][ny][nx] = tomatoes[z][y][x] + 1
            queue.append((nz, ny, nx))

min_period = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 0:
                print(-1)
                exit()
            elif tomatoes[h][n][m] == -1:
                continue
            else:
                min_period = max(min_period, tomatoes[h][n][m])

print(min_period - 1)