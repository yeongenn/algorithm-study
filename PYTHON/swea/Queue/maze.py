# DFS ver.

T = 10

def search(x, y):
    global flag, visited
    if flag == 1:
        return
    
    if maze[x][y] == 3:
        flag = 1
        return

    if visited[x][y] == 0:
        visited[x][y] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i, j in zip(dx, dy):
        nx, ny = x + i, y + j
        if 0 <= nx < 16 and 0 <= ny < 16:
            if maze[nx][ny] != 1 and visited[nx][ny] != 1:
                search(nx, ny)

for t in range(T):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    # 시작점 찾기
    sx, sy = 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                sx, sy = i, j
                break

    flag = 0
    visited = [[0] * 16 for _ in range(16)]
    
    search(sx, sy)
    print(f'#{tc} {flag}')