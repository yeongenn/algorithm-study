import sys
import copy
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")
sys.stdin = open("C:\\SSAFY\\algo-python\\PYTHON\\boj\\input.txt", "r")

N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

# 기본 주사위: 위-뒤-오-왼-앞-바
dice = [0] * 6

# 동서북남
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

# 굴리는 방향별로
def roll_east():
    # 바-왼-위-오-바
    dice_copy = copy.deepcopy(dice)
    dice[3] = dice_copy[-1]
    dice[0] = dice_copy[3]
    dice[2] = dice_copy[0]
    dice[-1] = dice_copy[2]
    
def roll_west():
    # 바-오-위-왼-바
    dice_copy = copy.deepcopy(dice)
    dice[2] = dice_copy[-1]
    dice[0] = dice_copy[2]
    dice[3] = dice_copy[0]
    dice[-1] = dice_copy[3]
    
def roll_north():
    # 바-앞-위-뒤-바
    dice_copy = copy.deepcopy(dice)
    dice[4] = dice_copy[-1]
    dice[0] = dice_copy[4]
    dice[1] = dice_copy[0]
    dice[-1] = dice_copy[1]
    
def roll_south():
    # 바-뒤-위-앞-바
    dice_copy = copy.deepcopy(dice)
    dice[1] = dice_copy[-1]
    dice[0] = dice_copy[1]
    dice[4] = dice_copy[0]
    dice[-1] = dice_copy[4]
    
nx, ny = x, y
for order in orders:
    nx += dx[order - 1]
    ny += dy[order - 1]
    if nx < 0 or nx > (N - 1) or ny < 0 or ny > (M - 1):
        nx -= dx[order - 1]
        ny -= dy[order - 1]
        continue
    if order == 1:
        roll_east()
    elif order == 2:
        roll_west()
    elif order == 3:
        roll_north()
    else:
        roll_south()
    
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
        print(dice[0])
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0
        print(dice[0])
        

