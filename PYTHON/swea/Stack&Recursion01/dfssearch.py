T = int(input())

def search(graph, n, stack):
    if n not in stack:
        stack.append(n)
    
    while 1 in graph[n]:
        idx = graph[n].index(1)
        result = search(graph, idx, stack)
        if result == idx:
            graph[n][idx] = 0   # 탐색 완료 후 값변경 - 마킹
    else: return n
    

for t in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    stack = []  # 노드 관리
    search(graph, 0, stack)
            
    print(f'#{t + 1}', *stack)