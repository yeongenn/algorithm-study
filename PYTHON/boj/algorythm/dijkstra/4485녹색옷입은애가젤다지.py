import sys
# sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

# 다익스트라 - 인접행렬 버전

from collections import deque
INF = 10e9
problem = 1

def dijkstra(sy, sx):
    q = deque([(sy, sx)])
    weight = [[INF] * N for _ in range(N)]
    # visited = [[0] * N for _ in range(N)] # 방문 처리 X
    dt = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 시계방향
    weight[sy][sx] = arr[sy][sx]
    
    while q:
        u, v = q.popleft()
        
        if weight[u][v] < arr[u][v]:
            continue
        
        for i, j in dt:
            nu, nv = u + i, v + j
            
            if (0 <= nu and nu < N) and (0 <= nv and nv < N):
                new_weight = weight[u][v] + arr[nu][nv]
                
                if weight[nu][nv] <= new_weight: continue
                
                weight[nu][nv] = new_weight
                q.append((nu, nv))
                
    return weight

while True:
    N = int(input())
    if N == 0: exit()

    arr = [list(map(int, input().split())) for _ in range(N)]
                
    answer = INF
    for i in range(N):
        answer = min(answer, arr[i][i])
    
    answer = dijkstra(0, 0)[N - 1][N - 1]
    
    print(f'Problem {problem}: {answer}')
    problem += 1