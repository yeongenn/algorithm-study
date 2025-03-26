import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
# sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

from heapq import heappop, heappush

def dijkstra(start, end):
    pq = [(0, start)]   # 시작점 가중치는 0
    dist = [float('inf')] * (N + 1)
    dist[start] = 0

    while pq:
        w, curr = heappop(pq)
        
        if dist[curr] < w:
            continue

        for next in graph[curr]:
            next_n = next[0]    # 다음 노드
            next_w = next[1]    # 그까지의 가중치

            # 가중치 갱신
            new_w = w + next_w

            if dist[next_n] > new_w:
                dist[next_n] = new_w
                heappush(pq, (new_w, next_n))
    
    if dist[end] == float('inf'):
        print(-1)
        exit()
    else:
        return dist[end]
        
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))     # a 정점에서 b 정점까지 양방향 길, 그 거리가 c
    graph[b].append((a, c))
    
v1, v2 = map(int, input().split())       # 반드시 거쳐야 하는 정점

path_1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
path_2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

result = min(path_1, path_2)
print(result)

####################################### review #######################################
# 내가 계속 놓쳤던 부분
# v1, v2를 반드시 순서대로 방문해야되는 줄 알앗슴
#   -> 1 - v1 - v2 - N, 1 - v2 - v1 - N 각각 구해서 그 중에서 최솟값 출력
#   -> start - end 사이 경로가 없으면 -1 출력하고 바로 프로그램 종료