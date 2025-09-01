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
graph = [list(map(int, input().split())) for _ in range(N)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

shark_weight = 2

INF = 1e9

# 아기 상어 위치
cy, cx = 0, 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            cy, cx = i, j
            graph[i][j] = 0
            break

# BFS
def path():
    queue = deque([])   
    # 이동하면서 cy, cx가 변경되므로 밖에서 초기화 X
    queue.append((cy, cx))

    # 방문 배열 밖에서 정의(초기화)하면 오답....
    visited = [[-1] * N for _ in range(N)]
    visited[cy][cx] = 0         # 상어 현재 위치 방문 처리

    while queue:
        y, x = queue.popleft()

        for i, j in zip(dy, dx):
            ny, nx = y + i, x + j

            # 상어가 이동 가능한지만 확인 - 같거나 커야함
            # 물고기 먹기는 따로 체크
            if 0 <= ny < N and 0 <= nx < N:
                if shark_weight >= graph[ny][nx] and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))

    return visited

# 먹을 물고기 찾기 - True / False 반환
def eat_fish(visited):
    # print(visited)
    y, x = cy, cx
    min_dist = INF
    for i in range(N):
        for j in range(N):
            # BFS에서 지나지 않는 경로는 최단 경로가 아님 + 아기 상어가 먹을 수 있는지 확인
            if visited[i][j] != -1 and 1 <= graph[i][j] < shark_weight:
                if visited[i][j] < min_dist:
                    min_dist = visited[i][j]
                    y, x = i, j

    # 다 탐색해도 그대로 1e9면 먹을 물고기 없다는 거겟징
    if min_dist == INF:
        return False
    else:
        return y, x, min_dist
    
answer = 0
fish_eaten = 0

# 갈 수 있는 경로가 있고, 먹을 수 있는 물고기가 있는 동안
# 물고기 먹으러~
while True:
    result = eat_fish(path())

    # 먹을 수 있는 물고기가 없으면
    if not result:
        print(answer)
        break
    else:
        # 이동, 물고기 먹으면서 현재 위치 조정
        cy, cx = result[0], result[1]
        answer += result[2]
        graph[cy][cx] = 0
        fish_eaten += 1

    if fish_eaten >= shark_weight:
        shark_weight += 1
        fish_eaten = 0
