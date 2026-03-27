import sys
# sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

# 다익스트라 기본
import heapq
INF = 10e9

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (N + 1)
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
    u, v, w = map(int, input().split())
    arr[u].append((v, w))
    arr[v].append((u, w))   # 양방향
    
answer = dijkstra(1)[N]
print(answer)