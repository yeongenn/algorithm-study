import sys
# sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

from collections import deque
INF = 10e9

# 다익스트라 인접행렬

def dijkstra(sy, sx):
    q = deque([(sy, sx)])
    crushed_walls = [[INF] * M for _ in range(N)]
    dt = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    crushed_walls[sy][sx] = 0       # 시작점은 항상 0
    
    while q:
        y, x = q.popleft()
        
        if crushed_walls[y][x] < arr[y][x]:
            continue
        
        for i, j in dt:
            ny, nx = y + i, x + j
            
            if 0 <= ny and ny < N and 0 <= nx and nx < M:
                walls = crushed_walls[y][x]
                if arr[ny][nx]:
                    walls += 1
                    
                if crushed_walls[ny][nx] <= walls:
                    continue
                    
                crushed_walls[ny][nx] = walls
                q.append((ny, nx))
                
    return crushed_walls

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

answer = dijkstra(0, 0)[N - 1][M - 1]
print(answer)