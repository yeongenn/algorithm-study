import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\yeongenn\\algorithm-study\\PYTHON\\boj\\input.txt", "r")

import copy
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]     # 2 : 바이러스, 1 : 벽, 0 : 빈 칸

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]       # 상하좌우
max_safe_area = 0                           # 최대 안전 영역

################################################## DFS로 하니까 시간초과 - 내가 잘못 짰을 듯.. ##################################################
# 감염
def infect():
    queue = deque()
    temp_lab = copy.deepcopy(arr)

    # 바이러스 위치 큐에 넣기
    for i in range(N):
        for j in range(M):
            if temp_lab[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        y, x = queue.popleft()

        for i, j in zip(dy, dx):
            ny, nx = y + i, x + j
            if ny < 0 or ny >= N or nx <0 or nx >= M or temp_lab[ny][nx] == 2 or temp_lab[ny][nx] == 1:
                continue
            temp_lab[ny][nx] = 2        # 감염
            queue.append((ny, nx))
                
    global max_safe_area
    max_safe_area = max(max_safe_area, get_safe_area(temp_lab))

# 안전 영역 구하기
def get_safe_area(virus):
    count = 0
    for i in range(N):
        for j in range(M):
            if virus[i][j] == 0:
                count += 1
    return count

# 벽 세우기
def make_walls(count):
    if count == 3:
        infect()
        return
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1           # 벽 세우기
                make_walls(count + 1)
                arr[i][j] = 0           # 벽 허물기(?)


# 출력
make_walls(0)
print(max_safe_area)

