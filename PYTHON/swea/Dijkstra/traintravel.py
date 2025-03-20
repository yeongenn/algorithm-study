import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

import heapq
INF = int(21e8)

def search(start):
    q = [(0, start)]
    dists = [INF] * N
    dists[start] = 0        # 시작 노드 최단 거리는 0
    
    while q:
        dist, node = heapq.heappop(q)
        
        if dists[node] < dist:
            continue
        
        for next_info in adj[node]:
            next_dist = next_info[0]    # 가중치
            next_node = next_info[1]    # 다음 노드 번호
            
            new_dist = dist + next_dist     # 거리 누적
            
            if dists[next_node] <= new_dist:
                continue
            
            dists[next_node] = new_dist
            heapq.heappush(q, (new_dist, next_node))
            
    return dists

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N)]    # 리스트
    
    for _ in range(M):
        a, b, w = map(int, input().split())
        adj[a].append((w, b))
        
    result = search(0)
    
    print(f'#{t + 1}', end=" ")
    print(result[N - 1]) if result[N - 1] != INF else print('impossible')