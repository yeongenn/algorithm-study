# 2차 월말평가 대비
# BFS - queue
# 평가에서는 import 사용 불가
import sys
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

N, M = map(int, input().split())
maze = [list(map(int, str(input()))) for _ in range(N)]

# 시작점은 고정
visited = [[0] * M for _ in range(N)]   # 몇 번만에 도착하는지 마킹
q = [(0, 0)]      # 다음 방문 좌표 저장용
visited[0][0] = 1
dt = [[-1, 0], [1, 0], [0, -1], [0, 1]]     # 상하좌우
while q:
    x, y = q.pop(0)     # 현재 좌표
    for i, j in dt:
        nx, ny = x + i, y + j
        if 0 <= nx < N and 0 <= ny < M:
            if maze[nx][ny] != 0 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
else:
    print(visited[N - 1][M - 1])
            