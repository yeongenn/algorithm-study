import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]

def dfs(node):
    global visited
    if visited[node] == 1: return
    else: visited[node] = 1        # 방문 처리
    
    if len(edges[node]) == 0: return
    
    for i in range(len(edges[node])):
        dfs(edges[node][i])

for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)      # 방향이 없다 -> 양방향
# print(edges)

visited = [0] * (N + 1)
cnct_cnt = 0        # 몇 번만에 visited 배열이 다 1이 되는가
for j in range(1, N + 1):
    if visited[j] == 1: continue
    dfs(j)
    cnct_cnt += 1

print(cnct_cnt)

####################################### 찾았던 반례 #######################################

"""
5 4
2 1
1 5
4 3
5 4

1
"""
