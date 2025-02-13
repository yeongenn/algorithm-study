T = int(input())

# def escape(x, y):
#     global maze
#     if maze[x][y] == 2: return 1
#     pass

for t in range(T):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    # print(maze)

    # 출발, 도착
    start, end = [], []
    for i in range(N):
        if 3 in maze[i]:
            start = [i, maze[i].index(3)]
        if 2 in maze[i]:
            end = [i, maze[i].index(2)]

    # print(start, end)
    # escape(*start)

    x, y = start
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        for j in range(1, N):
            nx = x + (dx[i] * j)
            ny = y + (dy[i] * j)

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                if maze[nx][ny] == 0:
                    continue

    result = 0  # 도착할 수 있으면 1, 아니면 0
    print(f'#{t + 1} {result}')