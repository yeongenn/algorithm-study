import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.setrecursionlimit(10 ** 6)    # recursion error 방지

M, N, K = map(int, input().split())     # 세로, 가로, 직사각형 갯수
grid = [[0] * N for _ in range(M)]      # 모눈 종이

def find_area(y, x):
    # print(y, x)
    area = 1
    
    if grid[y][x] == 99: return area
    
    grid[y][x] = 99     # 방문 마킹
    
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i, j in zip(dy, dx):
        ny, nx = y + i, x + j
        if 0 <= ny < M and 0 <= nx < N and grid[ny][nx] == 0:
            area += find_area(ny, nx)
            
    return area

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1

# print(grid)
area_cnt = 0
areas = []      # 영역 넓이
for i in range(M):
    for j in range(N):
        if grid[i][j] == 1 or grid[i][j] == 99: continue
        area_cnt += 1
        areas.append(find_area(i, j))
        
print(area_cnt)
print(*sorted(areas))