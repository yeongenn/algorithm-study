import sys
# sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")
sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

def drive(sy, sx, commands):
    dt = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d = 0   # 상방향으로 시작
    cy, cx = sy, sx
    
    for i in range(C):
        if commands[i] == 'L':
            d = (d - 1) % 4
        elif commands[i] == 'R':
            d = (d + 1) % 4
        else:
            i, j = dt[d]
            ny, nx = cy + i, cx + j
            if 0 <= ny < N and 0 <= nx < N and field[ny][nx] != 'T':
                cy, cx = ny, nx         # 위치 이동
    
    if field[cy][cx] == 'Y':
        return 1
    return 0

T = int(input())
for t in range(T):
    N = int(input())
    field = [list(input()) for _ in range(N)]
    results = []
    
    sy, sx = -1, -1     # 시작점
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                sy, sx = i, j
        
    Q = int(input())
    for _ in range(Q):
        C, commands = input().split()
        C = int(C)
        commands = list(commands)
        
        results.append(drive(sy, sx, commands))
        
    print(f'#{t + 1}', *results)