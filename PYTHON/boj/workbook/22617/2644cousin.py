import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

N = int(input())
A, B = map(int, input().split())    # 촌수 계산해야 하는 사람
M = int(input())    # 간선 수
adj = [[] for _ in range(N + 1)]

def cousin(s):
    visited = [0] * (N + 1)
    q = [s]     # 시작점 push
    visited[s] = 1      # 방문 처리
    while q:
        k = q.pop(0)
        # print(k)
        
        for i in range(len(adj[k])):
            if visited[adj[k][i]] == 0:
                q.append(adj[k][i])
                visited[adj[k][i]] = visited[k] + 1
    return visited

for _ in range(M):
    x, y = map(int, input().split())
    adj[y].append(x)
    adj[x].append(y)
# print(adj)
    
result = cousin(A)   # 시작점

print(result[B] - 1)
