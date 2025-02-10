for i in range(1):
    tc = int(input())

    ladders = [list(map(int, input().split())) for _ in range(3)]
    check = [[False] * 3] * 3

    d = [[0, 1], [0, -1], [1, 0]]

    x = 0
    dir_h = 0

    for j in range(3):
        y = j
        # while ladders[x][y] != 2:
        if ladders[x][y] == 1:
            check[x][y] = True
            if y == 0:
                if ladders[x][y + 1] == 1:  # 오른쪽
                    y += 1
                else:
                    x += 1

            if 0 <= y - 1 < 3:
                if ladders[x][y + 1] == 1:  # 오른쪽
                    y += 1
                elif ladders[x][y - 1] == 1:  # 왼쪽
                    y -= 1
                else:
                    x += 1  # 기본 진행 방향

    result = 0

    print(f'{tc} {result}')
