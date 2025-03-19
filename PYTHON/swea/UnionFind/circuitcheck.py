import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

def check(parent, n):
    visited[n] = 1
    
    for j in range(N):
        if parent == j or n == j or graph[n][j] == 0:
            continue
        
        if visited[j]:
            return False
        
        is_cycle = check(n, j)
        if not is_cycle:
            return False
        
    return True

for t in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    # print(graph)
    visited = [0] * N
    result = 'STABLE'
    
    for i in range(N):      # N개 노드 순회
        if not visited[i]:
            if not check(-1, i):
                result = 'WARNING'            
    
    print(f'#{t + 1} {result}')