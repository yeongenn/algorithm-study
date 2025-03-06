N, M, V = map(int, input().split())
# 인접 행렬 (0번은 버린다 - (N+1) * (N+1))
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1  # 양방향 그래프


def dfs(node):
    # 모든 노드를 확인
    for next_node in range(1, N + 1):
        if graph[node][next_node] == 0:  # 못가면 pass
            continue

        if visited[next_node]:  # 이미 방문했으면 pass
            continue

        print(next_node, end=" ")
        visited[next_node] = 1
        dfs(next_node)


def bfs(start):
    queue = [start]  # queue 에 들어가는 데이터의 의미
    # 후보군, 대기열
    visited = [0] * (N + 1)
    visited[start] = 1  # 시작점 초기화
    print(start, end=" ")

    while queue:
        now = queue.pop(0)
        # print(now, end=" ")

        for next_node in range(1, N + 1):
            if graph[now][next_node] == 0:
                continue

            if visited[next_node]:
                continue

            print(next_node, end=" ")
            visited[next_node] = 1
            queue.append(next_node)


visited = [0] * (N + 1)  # 싸이클을 막기위한 리스트
visited[V] = 1  # 시작점 초기화
print(V, end=" ")
dfs(V)
print()
bfs(V)
