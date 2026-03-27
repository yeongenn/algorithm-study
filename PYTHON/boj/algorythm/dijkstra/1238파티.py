import sys
# sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

import heapq
INF = 10e9

def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, start))   # 시작점 가중치는 0
    distance[start] = 0
    
    
    while q:
        dist, node = heapq.heappop(q)
        
        if distance[node] < dist: continue
                
        for next_node, next_dist in arr[node]:
            new_dist = dist + next_dist
            
            if distance[next_node] <= new_dist: continue
            
            distance[next_node] = new_dist
            heapq.heappush(q, (new_dist, next_node))
            
    return distance
    

N, M, X = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    arr[u].append((v, w))   # 단방향
    
max_dist = 0
student_idx = -1
for i in range(1, N + 1):
    student_dist = dijkstra(i)[X] + dijkstra(X)[i]      # 돌아와야 한다!
    max_dist = max(student_dist, max_dist)
    
print(max_dist)