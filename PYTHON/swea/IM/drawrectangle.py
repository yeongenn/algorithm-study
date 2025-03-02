import sys
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\swea\\input.txt", "r")

T = int(input())

def draw(x, y):
    global max_area, max_area_cnt
    
    # delta
    for r in range(0, N - x):
        for c in range(0, N - y):
            nx, ny = x + r, y + c
            
            if board[nx][ny] != board[x][y]:
                continue
            
            area = (nx - x + 1) * (ny - y + 1)
            if area < max_area:
                continue
            elif area == max_area:
                max_area_cnt += 1
            else:
                max_area = area     # 최대 넓이 갱신
                max_area_cnt = 1    # 갯수 갱신 

for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_area = 1    # 최대 넓이
    max_area_cnt = 0    # 최대 넓이와 같은 사각형 갯수
    
    for i in range(N):
        for j in range(N):
            draw(i, j)

    print(f'#{t + 1} {max_area_cnt}')