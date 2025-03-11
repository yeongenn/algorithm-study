import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

T = int(input())

def bfs(r, c):
    q = [[r, c]]
    checked[r][c] = 1
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while q:
        y, x = q.pop(0)
        
        for i, j in zip(dy, dx):
            ny, nx = y + i, x + j
            if 0 <= ny < N and 0 <= nx < M and cabbages[ny][nx] == 1 and checked[ny][nx] == 0:
                q.append([ny, nx])
                checked[ny][nx] = 1

for t in range(T):
    M, N, K = map(int, input().split())     # M : 가로, N : 세로, K : 배추 포기
    cabbages = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        y, x = map(int, input().split())
        cabbages[x][y] = 1
    # print(cabbages)
    
    checked = [[0] * M for _ in range(N)]   # 마킹
    count = 0   # 필요한 지렁이 수
    
    for i in range(N):
        for j in range(M):
            if cabbages[i][j] == 1 and checked[i][j] == 0:
                bfs(i, j)
                count += 1
                
    print(count)
    