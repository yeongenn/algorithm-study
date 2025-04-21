import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

def pang(y, x):
    sum_score = stage[y][x]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i, j in zip(dy, dx):
        for n in range(1, N):
            ny, nx = y + i * n, x + j * n
            if 0 <= ny < N and 0 <= nx < N:
                sum_score += stage[ny][nx]
    return sum_score

T = int(input())
for t in range(T):
    N = int(input())
    stage = [list(map(int, input().split())) for _ in range(N)]
    
    max_value, min_value = 0, 20 * 20
    for i in range(N):
        for j in range(N):
            score = pang(i, j)
            max_value = max(max_value, score)
            min_value = min(min_value, score)

    print(f'#{t + 1} {max_value - min_value}')