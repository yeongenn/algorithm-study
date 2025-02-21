import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\YH\\algo-python\\PYTHON\\boj\\input.txt", "r")

def func(N, arr, sx, sy):
    cnt_0 = 0
    for i in range(sx, sx + N):
        for j in range(sy, sy + N):
            if arr[i][j] == '0':
                cnt_0 += 1
    if cnt_0 == N * N:
        print(0, end="")
        return
    elif cnt_0 == 0:
        print(1, end="")
        return
    else:
        print("(", end="")
        half = N // 2
        for r in range(0, N, half):
            for c in range(0, N, half):
                func(half, arr, sx + r, sy + c) # 현재 좌표에서 거리 계산해야
        print(")", end="")
    
N = int(input())

q_tree = [list(input()) for _ in range(N)]
# print(q_tree)

func(N, q_tree, 0, 0)