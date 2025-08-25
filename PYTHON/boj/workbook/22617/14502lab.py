import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\yeongenn\\algorithm-study\\PYTHON\\boj\\input.txt", "r")

import copy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]     # 2 : 바이러스, 1 : 벽, 0 : 빈 칸
virus = copy.deepcopy(arr)
# print(virus)

def infect(r, c):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i, j in zip(dy, dx):
        for k in range(max(N, M)):
            ny, nx = r + i * k, c + j * k
            if 0 <= ny < N and 0 <= nx < M:
                if virus[ny][nx] == 0:
                    virus[ny][nx] = 2   # 감염
                    infect(ny, nx)
                elif virus[ny][nx] == 1:
                    break
            
def safe_area(virus):
    count = 0
    for i in range(N):
        for j in range(M):
            if virus[i][j] == 0:
                count += 1
    return count

# 벽을 세우고
# 바이러스 퍼트린 다음
# 빈 칸(안전 영역) 갯수 구하기

# 추가할 벽 위치 조합 구하기
wall_loc = []
for i in range(N):
    for j in range(M):
        if virus[i][j] == 0:
            wall_loc.append([i, j])
# print(wall_loc)

loc = []
for i in range(len(wall_loc)):
    for j in range(len(wall_loc)):
        for k in range(len(wall_loc)):
            if i != j and j != k and k != i:
                loc.append([wall_loc[i], wall_loc[j], wall_loc[k]])
# print(loc)
# print(len(loc))

max_safe_area = 0
for lo in loc:

    # 벽 총 3개
    for l in lo:
        y, x = l
        virus[y][x] = 1
        
    for i in range(N):
        for j in range(M):
            if virus[i][j] == 2:
                infect(i, j)
    
    max_safe_area = max(max_safe_area, safe_area(virus))
    virus = copy.deepcopy(arr)     # 리셋
    
print(max_safe_area)