import sys
sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

import copy

T = int(input())

def break_brick(y, x, bricks):
    K = bricks[y][x]    # 깨트릴 칸 수
    bricks[y][x] = 0     # 깨트렸음~
        
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]   # 상하좌우
    for i, j in zip(dy, dx):
        for k in range(K):
            ny, nx = y + i * k, x + j * k
            if 0 <= ny < H and 0 <= nx < W and bricks[ny][nx] != 0:
                break_brick(ny, nx, bricks)
                
def renew_bricks(bricks):
    renewal = [[0] * W for _ in range(H)]
    for j in range(W):
        idx = H - 1
        for i in range(H - 1, -1, -1):  # 밑에서 부터
            if bricks[i][j]:
                renewal[idx][j] = bricks[i][j]
                idx -= 1    # 인덱스 조정
                
    return renewal

def count_bricks(bricks):
    temp_cnt = 0
    for i in range(H):
        for j in range(W):
            if bricks[i][j]:
                temp_cnt += 1
    return temp_cnt

def drop_bead(N, bricks):
    global min_bricks
    if N == 0:  # 구슬 다 떨어뜨렸으면
        cnt = count_bricks(bricks)
        min_bricks = min(min_bricks, cnt)
        return
    
    for j in range(W):
        copied_bricks = copy.deepcopy(bricks)   # 벽돌 상태 복사
        for i in range(H):
            if copied_bricks[i][j] != 0:
                break_brick(i, j, copied_bricks)
                break
            
        copied_bricks = renew_bricks(copied_bricks)     # 벽돌 칸 조정
        drop_bead(N - 1, copied_bricks)

for t in range(T):
    N, W, H = map(int, input().split())     # N : 구슬 수
    bricks = [list(map(int, input().split())) for _ in range(H)]
    min_bricks = W * H      # 최솟값 초기화
    
    drop_bead(N, bricks)
    
    print(f'#{t + 1} {min_bricks}')