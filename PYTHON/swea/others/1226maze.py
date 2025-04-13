import sys
# sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")
sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

def escape(sy, sx):
    q = [(sy, sx)]
    visited = [[0] * 16 for _ in range(16)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while q:
        y, x = q.pop(0)
        visited[y][x] = 1
        
        for i, j in zip(dy, dx):
            ny, nx = y + i, x + j
            if 0 <= ny < 16 and 0 <= nx < 16 and maze[ny][nx] != 1 and not visited[ny][nx]:
                if maze[ny][nx] == 3:
                    return 1
                q.append((ny, nx))

    return 0    # 여기까지 왔으면 탈출 불가

T = 10
for _ in range(T):
    t = int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]
    
    sy, sx = -1, -1
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                sy, sx = i, j
                break
    
    print(f'#{t} {escape(sy, sx)}')