import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

# 다익스트라
import heapq

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def dijkstra():
    dists = [[int(21e8)] * N for _ in range(N)]
    dists[0][0] = graph[0][0]       # 시작점 초기화
    
    pq = [(0, 0, 0)]    # (dist, y, x) 형태, dist는 누적거리
    
    while pq:
        dist, y, x = heapq.heappop(pq)
        
        for i, j in zip(dy, dx):
            ny, nx = y + i, x + j
            
            if 0 <= ny < N and 0 <= nx < N:
                new_dist = dists[y][x] + graph[ny][nx]      # 거리 누적
                
                # 이미 더 작거나 같은 시간으로 온 적이 있으면 탐색할 필요 X
                if dists[ny][nx] <= new_dist:   
                    continue
                
                # 도착하는 순간 최단거리가 될거니까 그 바로 직전에 구한 new_dist 바로 반환
                if ny == N - 1 and nx == N - 1:
                    return new_dist
                
                dists[ny][nx] = new_dist
                heapq.heappush(pq, (new_dist, ny, nx))
                
    return dists[N - 1][N - 1]


T = int(input())
for t in range(T):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    
    print(f'#{t + 1} {dijkstra()}')
    
#######################################################################

""""
다익스트라 쓸 수 없는 경우에는

- 벨만-포드
    - 모든 간선들을 확인하면서 진행
- 플로이드-워셜
    - 모든 정점에서 다른 모든 정점까지 최단 경로
    - 시간 복잡도 : O(N ^ 3) : 모든 정점에서 다익스트라 진행하는 거랑 큰 차이가 없다
"""