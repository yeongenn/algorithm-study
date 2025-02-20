from collections import defaultdict
import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())

for t in range(T):
    N = int(input())
    adj = [list(map(int, input().split())) for _ in range(N)]
    is_visited = [False] * N

    print(f'#{t + 1}', end=" ")

    nodes = defaultdict(list)   # {0: [2, 3, 4], 2: [5], 3: [1], 5: [6]}
    for i in range(N):
        for j in range(N):
            if adj[i][j]:
                nodes[i].append(j)

    q = []
    s_node = 0
    q.append(s_node)  # 시작점
    is_visited[s_node] = 1    # enqueue와 동시에 visited 마킹 - 시작점 마킹

    while nodes[s_node]:
        if len(q) == 0:
            break

        temp = q.pop(0)

        # dequeue한 다음 visited에 마킹
        # if not is_visited[temp]:
        #     is_visited[temp] = True
        #     print(temp, end=" ")
        #     for i in nodes[temp]:
        #         if not is_visited[i]:
        #             q.append(i)

        # enqueue와 동시에 visited에 마킹
        print(temp, end=" ")
        for i in nodes[temp]:
            if not is_visited[i]:
                q.append(i)
                is_visited[i] = is_visited[temp] + 1
                # is_visited의 각 원소는 배열 인덱스를 번호로 삼는 정점들의 방문 순서가 된다

    print()
    print(is_visited)
    


"""
            DFS         BFS
동작 원리   Stack       Queue
구현 방법   recursive   queue, while
"""