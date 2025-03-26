import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

###################################### pypy3로 통과 ######################################

from heapq import heappop, heappush

def dijkstra(start):
    pq = [(0, start)]   # 시작점 가중치는 0
    dist = [float('inf')] * (V + 1)
    dist[start] = 0
    
    while pq:
        w, curr = heappop(pq)
        
        if dist[curr] < w:
            continue
        
        for next in graph[curr]:
            next_w = next[1]
            next_v = next[0]
            
            new_w = w + next_w
            
            if dist[next_v] > new_w:
                dist[next_v] = new_w
                heappush(pq, (new_w, next_v))
                
    return dist
        
V, E = map(int, input().split())
START = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())     # u에서 v로 가는 가중치 w 간선
    graph[u].append((v, w))

result = dijkstra(START)
for i in range(1, V + 1):
    print(result[i]) if result[i] != float('inf') else print('INF') 