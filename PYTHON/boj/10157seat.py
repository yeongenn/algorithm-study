# import sys
# sys.stdin = open("input.txt", "r")
# from pprint import pprint

# 범위 이내일 때, arr가 0일 때 나아간다
# else: 방향 전환
# cnt가 n**2 이내일 때까지만

N, M = map(int, input().split())
T = int(input())
arr = [[0]*N for _ in range(M)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

y, x, cnt, d = M-1, 0, 1, 0
arr[y][x] = cnt
ry, rx = 0, 0

while cnt < N*M:
    ny = y + dy[d]
    nx = x + dx[d]
    if 0 <= ny < M and 0 <= nx < N and arr[ny][nx] == 0:
        cnt += 1
        arr[ny][nx] = cnt
        y = ny
        x = nx
        if cnt == T:
            ry = ny
            rx = nx
    else:
        d = (d+1) % 4

if T > N*M:
    print(0)
else:
    print(rx, ry)
    print(rx+1, M-ry + 1)




