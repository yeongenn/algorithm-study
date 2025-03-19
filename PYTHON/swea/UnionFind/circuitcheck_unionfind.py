import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parent, x, y):
    global result
    x = find_parent(parents, x)
    y = find_parent(parents, y)
    
    if x < y:
        parent[y] = x
    elif x > y:
        parent[x] = y
    else:       # x == y면 싸이클
        result = 'WARNING'

for t in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    parents = [x for x in range(N)]
    result = 'STABLE'
    
    for i in range(N):
        for j in range(i, N):                           # ver1
            if i != j and graph[i][j] == 1:
                # graph[j][i] = 0                       # ver2
                union_parent(parents, i, j)             # 이때는 parents 배열 안 넘겨줘두댐
        
    print(f'#{t + 1} {result}')