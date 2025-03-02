import sys, math
sys.stdin = open("c:\\SSAFY\\algo-python\\PYTHON\\swea\\input.txt", "r")

T = int(input())

for t in range(T):
    N = int(input())
    ville_map = [list(map(int, input().split())) for _ in range(N)] # 0 : 빈 공간, 1 : 집 있음, 2 : 중계기 설치
    rp_x, rp_y = 0, 0
    houses = []
    
    R = 1   # 초기값
    
    # 집, 중계기 좌표
    for i in range(N):
        for j in range(N):
            if ville_map[i][j] == 0: continue
            elif ville_map[i][j] == 1:
                houses.append((i, j))
            else:
                rp_x, rp_y = i, j
                
    for hx, hy in houses:
        d = math.ceil(math.sqrt((hx - rp_x) ** 2 + (hy - rp_y) ** 2))   # 범위에 포함되야하니까 올림처리
        if d > R: R = d
        elif d <= R: continue

    print(f'#{t + 1} {R}')