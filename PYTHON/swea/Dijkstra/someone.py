import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\swea\\input.txt", "r")
# sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\swea\\input.txt", "r")

from heapq import heappush, heappop

def dijkstra(r, c):
    pq = [(village[Y][X], Y, X)]
    dist = [[float('inf')] * N for _ in range(N)]
    dist[Y][X] = village[Y][X]

    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    while pq:
        w, a, b = heappop(pq)

        if dist[a][b] < w:
            continue

        for i, j in zip(dx, dy):
            na, nb = a + i, b + j
            if 0 <= na < N and 0 <= nb < N and village[na][nb] != -1:
                nw = w + village[na][nb]    # 거리 갱신
                
                if dist[na][nb] > nw:
                    dist[na][nb] = nw
                    heappush(pq, (nw, na, nb))

        if a == r and b == c:
            return dist[r][c]

T = int(input())
for t in range(T):
    Y, X = map(int, input().split())    # 시어머니 좌표 -> 시작점
    N = int(input())
    village = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for r in range(N):
        for c in range(N):
            if village[r][c] != -1:     # -1은 벽
                max_value = max(max_value, dijkstra(r, c))

    print(f'#{t + 1} {max_value}')