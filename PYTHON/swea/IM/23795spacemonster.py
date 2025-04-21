import sys
sys.stdin = open("c://Users//SSAFY//Desktop//YH//algo-python//PYTHON//swea//input.txt", "r")
# sys.stdin = open("c://SSAFY//algo-python//PYTHON//swea//input.txt", "r")

def attack(my, mx):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    for i, j in zip(dy, dx):
        for n in range(1, N):
            ny, nx = my + (i * n), mx + (j * n)
            if 0 <= ny < N and 0 <= nx < N:
                if section[ny][nx] == 0:
                    section[ny][nx] = 2
                else:
                    break

T = int(input())
for t in range(T):
    N = int(input())
    section = [list(map(int, input().split())) for _ in range(N)]   # 0 : 빈칸, 1 : 벽, 2 : 괴물

    my, mx = 0, 0       # 괴물 좌표 구하기
    for i in range(N):
        for j in range(N):
            if section[i][j] == 2:
                my, mx = i, j
                break

    attack(my, mx)

    result = 0
    for i in range(N):
        for j in range(N):
            if section[i][j] == 0:
                result += 1

    print(f'#{t + 1} {result}')