from collections import defaultdict

T = int(input())

################ runtime error ################ -> 수정하기
# def search(graph, n, stack):
#     if n not in stack:
#         stack.append(n)
    
#     while 1 in graph[n]:
#         idx = graph[n].index(1)
#         result = search(graph, idx, stack)
#         if result == idx:
#             graph[n][idx] = 0   # 탐색 완료 후 값변경 - 마킹
#     else: return n
    

# for t in range(T):
#     N = int(input())
#     graph = [list(map(int, input().split())) for _ in range(N)]
    
#     stack = []  # 노드 관리
#     search(graph, 0, stack)
            
#     print(f'#{t + 1}', *stack)


################ runtime error ################
def search(node, nodes, stack, is_visited):
    if is_visited[node] is False:
        stack.append(node)
        is_visited[node] = True

    # while nodes[node] != []:
    #     s_node = nodes[node][0]
    #     e_node = search(s_node, nodes, stack, is_visited)
    #     if s_node == e_node:
    #         nodes[node].remove(s_node)
    # else:
    #     return node

    while nodes[node]:
        # 값 가져옴과 동시에 pop하면 if s_node == e_node: 이렇게 비교할 필요 X
        s_node = nodes[node].pop(0)     
        if not is_visited[s_node]: 
            search(s_node, nodes, stack, is_visited)

for t in range(T):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]


    nodes = defaultdict(list)
    stack = []
    is_visited = [False] * N    # 마킹용

    for i in range(N):
        for j in range(N):
            if graph[i][j]:
                nodes[i].append(j)

    search(0, nodes, stack, is_visited)

    print(f'#{t + 1}', *stack)