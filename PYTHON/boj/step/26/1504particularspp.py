import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

from heapq import heappop, heappush

def dijkstra(start, end):
    pass

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))     # a 정점에서 b 정점까지 양방향 길, 그 거리가 c
    graph[b].append((a, c))
    
# print(graph)
v1, v2 = map(int, input().split())       # 반드시 거쳐야 하는 정점