import sys
# sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")
sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

def drive(field, K):
    dt = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상부터 시계방향

    visited = [[[[0] * (K + 1) for _ in range(4)] for _ in range(N)] for _ in range(N)]
    q = [(sy, sx, 0, 0, 0)]  # y, x, 방향, 벤 나무 수, 조작 횟수
    visited[sy][sx][0][0] = 0

    while q:
        y, x, d, cut, cnt = q.pop(0)
        if y == ey and x == ex:
            return cnt

        # 1. 전진
        ny, nx = y + dt[d][0], x + dt[d][1]
        if 0 <= ny < N and 0 <= nx < N:
            next = field[ny][nx]
            if next == 'G' or next == 'Y' and visited[ny][nx][d][cut] == 0:
                visited[ny][nx][d][cut] = cnt + 1
                q.append((ny, nx, d, cut, cnt + 1))
            elif next == 'T' and cut < K and visited[ny][nx][d][cut + 1] == 0:
                visited[ny][nx][d][cut + 1] = cnt + 1
                q.append((ny, nx, d, cut + 1, cnt + 1))

        # 2. 좌회전
        nd = (d - 1) % 4
        if visited[y][x][nd][cut] == 0:
            visited[y][x][nd][cut] = cnt + 1
            q.append((y, x, nd, cut, cnt + 1))

        # 3. 우회전
        nd = (d + 1) % 4
        if visited[y][x][nd][cut] == 0:
            visited[y][x][nd][cut] = cnt + 1
            q.append((y, x, nd, cut, cnt + 1))

    return -1

T = int(input())
for t in range(T):
    N, K = map(int, input().split())    # K : 나무를 벨 수 있는 최대 횟수
    field = [list(input()) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':      # 시작점
                sy, sx = i, j
            if field[i][j] == 'Y':      # 끝점
                ey, ex = i, j
    
    print(f'#{t + 1} {drive(field, K)}')