import sys
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\swea\\input.txt", "r")

T = int(input())

def tsar_bomb(x, y):
    killed = 0
    
    killed += village[x][y]
    
    dx , dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i, j in zip(dx, dy):
        for p in range(1, P + 1):
            nx, ny = x + i * p, y + j * p
            if 0 <= nx < N and 0 <= ny < N:
                killed += village[nx][ny]
    return killed
            

for t in range(T):
    N, P = map(int, input().split())
    village = [list(map(int, input().split())) for _ in range(N)]
    max_killed = 0
    
    for r in range(N):
        for c in range(N):
            virus_killed = tsar_bomb(r, c)
            max_killed = max(max_killed, virus_killed)
    
    print(f'#{t + 1} {max_killed}')