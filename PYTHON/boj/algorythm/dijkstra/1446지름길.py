import sys
# sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

# D <= 10000
import heapq
INF = int(21e8)

def search(start):
    queue = [(start, 0)]
    distances = [INF] * (D + 1)
    distances[start] = 0         # 시작점 최단 거리는 0
    
    while queue:
        node, dist = heapq.heappop(queue)
        
        if distances[node] < dist:  # 
            continue
        
        for next_info in shortcuts[node]:
            next_node, next_dist = next_info[0], next_info[1]
            
            new_dist = dist + next_dist     # 거리 누적
            
            if distances[next_node] <= new_dist:    #
                continue
            
            distances[next_node] = new_dist
            heapq.heappush(queue, (next_node, new_dist))

    return distances

N, D = map(int, input().split())
shortcuts = [[] for _ in range(D + 1)]

for i in range(D):
    shortcuts[i].append(((i + 1), 1))

for _ in range(N):
    a, b, w = map(int, input().split())
    if b <= D:
        shortcuts[a].append((b, w))
    
result = search(0)    # 시작점 0
print(result[D])