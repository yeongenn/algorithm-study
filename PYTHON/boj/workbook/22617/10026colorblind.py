import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
# sys.setrecursionlimit(10 ** 6)    # recursion error 방지

def color_blind(y, x, color):
    image_color_blind[y][x] = 'Z'
    
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i, j in zip(dy, dx):
        ny, nx = y + i, x + j
        if 0 <= ny < N and 0 <= nx < N and image_color_blind[ny][nx] == color:
            color_blind(ny, nx, color)

def not_color_blind(y, x, color):
    image[y][x] = 'Z'   # 방문 처리
    
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i, j in zip(dy, dx):
        ny, nx = y + i, x + j
        if 0 <= ny < N and 0 <= nx < N and image[ny][nx] == color:  # 범위 내 + 동일 색이면
            not_color_blind(ny, nx, color)

N = int(input())
image = [list(list(input())) for _ in range(N)]
image_color_blind = [['A'] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if image[i][j] == 'B':
            image_color_blind[i][j] = image[i][j]
        else:
            image_color_blind[i][j] = 'R'   # R이나 G면 R로
# print(image)
# print(image_color_blind)

color_blind_cnt = 0
not_color_blin_cnt = 0  
for i in range(N):
    for j in range(N):
        # 색맹 아닌 경우
        if image[i][j] == 'Z': continue     # 이미 방문했으면 pass
        
        not_color_blind(i, j, image[i][j])
        not_color_blin_cnt += 1
        
        # 색맹인 경우
        if image_color_blind[i][j] == 'Z': continue
        
        color_blind(i, j, image_color_blind[i][j])
        color_blind_cnt += 1
        
print(not_color_blin_cnt, color_blind_cnt)

############################################### review ###############################################

# 색맹용 이미지 변환 + 함수도 따로 만들어서 -> ...? 중복 난발...??
#   -> 함수 하나로 하는 방법?
#       -> 색맹 아닌 경우 먼저 구하고 image를 색맹 버전으로 변경해서 같은 함수로 진행

# 3차원 배열로 색명 여부까지 받아서 그래프 만들면 메모리 초과난다고
