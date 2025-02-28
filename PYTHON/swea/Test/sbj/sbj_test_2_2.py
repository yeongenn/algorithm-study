T = int(input())

for t in range(T):
    N = int(input())    # RGB 괴물 수
    section = [list(map(int, input())) for _ in range(10)]
    # print(section)

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 0 : 괴물 없음, 1 : R, 2 : G, 3 : B, 4 : 벽
    # 괴물 광선 닿는 곳 표시
    for i in range(10):
        for j in range(10):
            if section[i][j] == 1 or section[i][j] == 2 or section[i][j] == 3:
                for n, m in zip(dx, dy):
                    for k in range(1, section[i][j] + 1):
                        nx, ny = i + (n * k), j + (m * k)
                        if 0 <= nx < 10 and 0 <= ny < 10:   # 유효 인덱스이면
                            if 1 <= section[nx][ny] <= 4:    # 다른 괴물 만나거나 벽 만나면 그 방향으로 중지
                                break
                            section[nx][ny] = 9    # 광선 닿는 곳 마킹

    possible = 0    # 갈 수 있는 곳 카운트
    for i in range(10):
        for j in range(10):
            if section[i][j] == 0:
                possible += 1
    print(f'#{t + 1} {possible}')