T = int(input())

def escape(x, y):
    global flag
    
    # 체크해야 할 모든 조건을 확인한 후 return 하는게 X
    # 말 그대로 함수 '종료' 조건 체크한 후에만 return 처리
    if flag == 1: return
    
    if not visited[x][y]:
        visited[x][y] = True
        
    if maze[x][y] == 3: 
        flag = 1
        
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N:   # 미로 범위 내에서만
            if (maze[nx][ny] != 1) and not visited[nx][ny]: # 벽이 아니고 아직 지난 적 없을 때만
                escape(nx, ny)
    

for t in range(T):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    flag = 0
    
    x, y = 0, 0    # 출발
    for i in range(N):
        if 2 in maze[i]:
            x, y = i, maze[i].index(2)
    
    escape(x, y)

    # 도착할 수 있으면 1, 아니면 0
    print(f'#{t + 1} {flag}')
