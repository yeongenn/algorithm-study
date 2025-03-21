import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    
    if x == y:
        return
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

N = int(input())    # 도시의 수
M = int(input())    # 여행 계획에 속한 도시의 수
graph = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))  # 여행 계획에 속한 도시들, 인덱스 주의
parents = [x for x in range(N)]

for i in range(N):
    for j in range(N):   # 대각선 기준 우상방
        if graph[i][j]:
            union(i, j)

connected = True
for k in range(M - 1):
    if find_set(plan[k] - 1) != find_set(plan[k + 1] - 1):
        connected = False

print('YES') if connected else print('NO')