import sys
sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

T = int(input())
dt = [[(0, 0)], [(-1, 0), (1, 0), (0, -1), (0, 1)], [(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, 0), (0, 1)], [(1, 0), (0, 1)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)]]

def get_escape_area_range(r, c, l):
    hour = 0
    scope = 0
    q = [[r, c]]
    checked[r][c] = 1
    s, t = 1, 0
    while hour < l: 
        hour += 1                   
        for _ in range(s):
            y, x = q.pop(0)
            scope += 1
            
            for i, j in dt[tunnel[y][x]]:
                ny, nx = y + i, x + j
                if 0 <= ny < N and 0 <= nx < M and tunnel[ny][nx] != 0 and checked[ny][nx] == 0:
                    # i, j의 상하좌우 방향 여부와 ny, nx 맨홀 방향이 맞아야 한다
                    if i == -1 and j == 0:  # 상
                        if tunnel[ny][nx] == 3 or tunnel[ny][nx] == 4 or tunnel[ny][nx] == 7: continue
                    elif i == 1 and j == 0: # 하
                        if tunnel[ny][nx] == 3 or tunnel[ny][nx] == 5 or tunnel[ny][nx] == 6: continue
                    elif i == 0 and j == -1:    # 좌
                        if tunnel[ny][nx] == 2 or tunnel[ny][nx] == 6 or tunnel[ny][nx] == 7: continue
                    elif i == 0 and j == 1: # 우
                        if tunnel[ny][nx] == 2 or tunnel[ny][nx] == 4 or tunnel[ny][nx] == 5: continue
                        
                    q.append([ny, nx])
                    checked[ny][nx] = 1     # 마킹
                    t += 1
        
        s = t
        t = 0   # 리셋
    
    return scope

for t in range(T):
    N, M, R, C, L = map(int, input().split())   # N : 세로, M : 가로, R, C : 맨홀 위치, L : 탈출 후 경과 시간
    # print(N, M, R, C, L)
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    checked = [[0] * M for _ in range(N)]       # 마킹용

    result = get_escape_area_range(R, C, L)
    print(f'#{t + 1} {result}')