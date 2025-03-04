T = int(input())

for t in range(T):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]  # 0 : 통로, 1 : 벽, 2 : 출발점, 3 : 도착점, 4 : 점프대

    # 출발점 좌표 얻기
    sx, sy = 0, 0
    ex, ey = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sx, sy = i, j
            elif maze[i][j] == 3:
                ex, ey = i, j
            else: continue

    to_visit = [(sx, sy)]   # 다음 경로
    visited = [[0] * N for _ in range(N)]
    visited[sx][sy] = 1     # 초기값
    is_arrived = False      # flag
    while to_visit:
        # 일단 점프대 없는 버전
        if is_arrived: break
        cx, cy = to_visit.pop(0)

        if maze[cx][cy] == 4:
            dx, dy = [-2, 2, 0, 0], [0, 0, -2, 2]   # 상하좌우
        else: dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]   # 상하좌우
        for i, j in zip(dx, dy):
            nx, ny = cx + i, cy + j
            if 0 <= nx < N and 0 <= ny < N:
                if maze[nx][ny] != 1 and visited[nx][ny] == 0:
                    to_visit.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1

                    if nx == ex and ny == ey:   # 도착했으면
                        is_arrived = True
                        break

    result = 0  # 도착점까지 갈 수 있으면 최단 경로 길이, 도착할 수 없으면 -1
    if is_arrived: result = visited[ex][ey]
    else: result = -1

    print(f'#{t + 1} {result}')