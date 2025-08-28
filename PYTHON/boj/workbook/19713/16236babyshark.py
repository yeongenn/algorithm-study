import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\yeongenn\\algorithm-study\\PYTHON\\boj\\input.txt", "r")

# 크기가 같은 물고기는 먹을 수는 X, 그 물고기가 있는 칸은 지나갈 수 O
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가

# 아기 상어 이동 위치 결정 방법
# 1. 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움 요청
# 2. 먹을 수 있는 물고기가 1마리라면 그 물고기 꿀꺽
# 3. 먹을 수 있는 물고기가 여러 마리라면 거리가 가장 가까운 물고기 꿀꺽
#   -1. 거리는 아기상어-물고기 사이 지나가야하는 칸의 최솟값
#   -2. 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기 -> 가장 왼쪽에 있는 물고기

# 0: 빈 칸
# 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
# 9: 아기 상어의 위치

from collections import deque

N = int(input())
list = [list(map(int, input().split())) for _ in range(N)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

fish_eaten = 0
shark_weight = 2
dist = [[0] * N for _ in range(N)]
queue = deque()

# 아기 상어 위치
cy, cx = -1, -1
for i in range(N):
    for j in range(N):
        if list[i][j] == 9:
            cy, cx = i, j
            break

# 
queue.append((cy, cx))
dist[cy][cx] = 1

while queue:
    y, x = queue.popleft()

    for i, j in zip(dy, dx):
        ny, nx = y + i, x + j
        if 0 <= ny < N and 0 <= nx < N:
            if list[ny][nx] > shark_weight:
                continue

            if list[ny][nx] < shark_weight:
                fish_eaten += 1
                list[ny][nx] = 0
            
            dist[ny][nx] = dist[y][x] + 1
            queue.append((ny, nx))

    if fish_eaten == shark_weight:
        shark_weight += 1
        fish_eaten = 0

print(dist)
