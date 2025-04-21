import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//boj//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//boj//input.txt", "r")

def is_bingo():
    bingo_count = 0

    # 대각선
    diag_t_b, diag_b_t = 0, 0
    for i in range(5):
        for j in range(5):
            if i == j and bingo[i][j] == 99:
                diag_t_b += 1
            if i + j == 4 and bingo[i][j] == 99:
                diag_b_t += 1
    if diag_b_t == 5: bingo_count += 1
    if diag_t_b == 5: bingo_count += 1

    # 가로
    for i in range(5):
        row = 0
        for j in range(5):
            if bingo[i][j] == 99:
                row += 1
        if row == 5:
            bingo_count += 1
            
    # 세로
    for j in range(5):
        col = 0
        for i in range(5):
            if bingo[i][j] == 99:
                col += 1

        if col == 5:
            bingo_count += 1

    if bingo_count >= 3:
        return True
    else: return False

bingo = [list(map(int, input().split())) for _ in range(5)]
nums = [] 
for _ in range(5):
    nums.extend(list(map(int, input().split())))

for idx in range(25):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == nums[idx]:
                bingo[i][j] = 99
    if is_bingo():
        print(idx + 1)
        break