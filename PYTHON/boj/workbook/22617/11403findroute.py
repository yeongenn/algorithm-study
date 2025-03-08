import sys
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

N = int(input())

def find_route(node):     # BFS
    q = [node]
    visited = [0] * N
    while q:
        next = q.pop(0)
        for n in adj_list[next]:
            if visited[n] == 1: continue
            
            visited[n] = 1
            q.append(n)
            
    print(*visited)

adj = [list(map(int, input().split())) for _ in range(N)]   # 방향 그래프!
adj_list = [[] for _ in range(N)]   # 인접 리스트로 변환
for i in range(N):
    for j in range(N):
        if adj[i][j] == 1:
            adj_list[i].append(j)
# print(adj_list)

for i in range(N):
    find_route(i)   # 노드 하나씩 순회
    
# print(result)

####################################### review #######################################

""""
Floyd-Warshall

시간 복잡도 : O(N ^ 3)
이 문제의 경우 1 <= N <= 100 이라 시간 내 가능

이런 생각은 대체 어찌..하는건지....??..
"""
N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if adj[i][k] and adj[k][j]:
                adj[i][j] = 1
                
for r in adj:   # 출력
    for c in r:
        print(c, end=" ")
    print()
