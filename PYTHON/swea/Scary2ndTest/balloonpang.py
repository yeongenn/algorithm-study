T = int(input())

for t in range(T):
    N = int(input())
    ballons = [list(map(int, input().split())) for _ in range(N)]

    max_s = 0
    min_s = N * (2 * N - 1)

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for x in range(N):
        for y in range(N):
            comp = 0

            comp += ballons[x][y]
            for i in range(4):
                for j in range(1, N):
                    nx = x + (dx[i] * j)
                    ny = y + (dy[i] * j)

                    # 범위 유효할 때만
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue

                    # 계산
                    comp += ballons[nx][ny]

            max_s = max(max_s, comp)
            min_s = min(min_s, comp)


    result = max_s - min_s
    print(f'#{t + 1} {result}')