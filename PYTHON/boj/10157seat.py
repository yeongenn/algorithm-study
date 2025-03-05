import sys
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

N, M = map(int, input().split())
T = int(input())
arr = [[0] * N for _ in range(M)]

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]   # 상우하좌

y, x = M, 0     # 시작점
k = 0       # 좌석 번호
d = 0       # 초기 방향
ry, rx = 0, 0   # T의 좌표

if T > N * M:
    print(0)
    exit()      # 번호가 좌석 범위 밖이면 종료

while k < N * M:
    ny = y + dy[d]
    nx = x + dx[d]
    if 0 <= ny < M and 0 <= nx < N and arr[ny][nx] == 0:
        k += 1
        arr[ny][nx] = k
        y, x = ny, nx
        if k == T:
            ry, rx = ny, nx
    else:   # 범위 밖이거나 이미 배정되었다면
        d = (d + 1) % 4     # 방향 전환

else:
    print(rx + 1, M - ry)