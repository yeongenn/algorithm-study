import sys
# sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

import heapq
INF = 10e9

def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q)
        
        if distance[node] < dist:
            continue
        
        for next_node, next_dist in arr[node]:
            new_dist = dist + next_dist
            
            if distance[next_node] <= new_dist:
                continue
            
            distance[next_node] = new_dist
            heapq.heappush(q, (new_dist, next_node))
            
    return distance

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
    
S, T = map(int, input().split())    # S에서 T까지

answer = dijkstra(S)[T]
print(answer)