import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

N, M = map(int, input().split())    # N : 정점 갯수, M : 간선 갯수
edges = [[] for _ in range(N + 1)]

def connected(i):     # 연결된 제일 마지막 노드 반환
    global visited
    pass

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)

visited = [0] * (N + 1)

cnct_cnt = 0
for i in range(1, N + 1):
    pass
print(cnct_cnt)