import sys
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

cnt_cleaned = 0
dt = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def clean(y, x, dr):
    global cnt_cleaned
    
    # 현재 칸 청소, 청소한 방은 -1
    if room[y][x] == 0:
        room[y][x] = 99
        cnt_cleaned += 1
        
    can_clean = False
    
    for i, j in dt:
        dr = (dr - 1) % 4
        ny, nx = y + dt[dr][0], x + dt[dr][1]
        if room[ny][nx] == 0:
            can_clean = True
            clean(ny, nx, dr)
            can_clean = False
            return
        
    if not can_clean:
        ny, nx = y - dt[dr][0], x - dt[dr][1]
        if room[ny][nx] != 1:
            clean(ny, nx, dr)
                
clean(r, c, d)
print(cnt_cleaned)