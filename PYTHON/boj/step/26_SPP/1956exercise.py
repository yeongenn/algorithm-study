import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
# sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

#################################### 다익스트라로 푸니까 메모리 초과 ####################################

# from heapq import heappop, heappush

# def exercise():
#     while pq:
#         w, start, end = heappop(pq)

#         if start == end:    # 출발점 == 도착점 -> 사이클, pq에서 뽑은 경로 w 출력
#             return w

#         if dist[start][end] < w:    # 이미 작은 경로이면 지나가기
#             continue

#         for next_e, next_w in graph[end]:
#             new_w = w + next_w
#             if dist[start][next_e] > new_w:
#                 dist[start][next_e] = new_w
#                 heappush(pq, [new_w, start, next_e])
    
#     return -1       # 여기까지 왔다 -> 운동 경로 없다

# # 두 노드 왕복하는 경우도 사이클에 포함
# V, E = map(int, input().split())
# graph = [[] for _ in range(V + 1)]
# dist = [[float('inf')] * (V + 1) for _ in range(V + 1)]
# pq = []

# for _ in range(E):
#     a, b, c = map(int, input().split())
#     graph[a].append([b, c])     # a -> b로 가는 거리 c인 도로
#     heappush(pq, [c, a, b])     # 경로 미리 저장

# print(exercise())

##################################### 플로이드 워셜 방법 #####################################
################################### 이마저도 pypy로 통과 #####################################

V, E = map(int, input().split())
graph = [[float('inf')] * (V + 1) for _ in range(V + 1)]    # 인접 행렬

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, V + 1):   #  인덱스 제발 주의ㅠㅠ
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            # i -> j / i -> k -> j 중 빠른 경로 찾기
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = float('inf')
# 그래프 순회하면서 최솟값 가져오기
# for i in range(1, V + 1):
#     for j in range(1, V + 1):
#         # 사이클인 경우를 체크해야하니까
#         # 출발지와 도착지가 같은 경우
#         # i에서 출발해서 i로 도착하는 경우
#         result = min(result, graph[i][j] + graph[j][i])

# 위 이중 for문 대신 이렇게도 가능
for i in range(1, V + 1):
    result = min(result, graph[i][i])

print(result) if result != float('inf') else print(-1)