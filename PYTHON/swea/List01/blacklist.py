# DAT 연습 문제
# 블랙 리스트
T = int(input())

for t in range(T):
    i, j = map(int, input().split())

    # apt = []
    apt = [list(map(int, input().split())) for _ in range(i)]

    m, n = map(int, input().split())
    given_black_list = []
    for row in range(m):
        row_list = map(int, input().split())
        given_black_list.extend(row_list)

    # print(given_black_list)

    black_list = [0] * 100001
    
    for black in given_black_list:
        black_list[black] = 1

    count_black = 0
    for h in range(i):
        for w in range(j):
            if black_list[apt[h][w]] == 1:
                  count_black += 1


    print(f'#{t + 1} {count_black} {i * j - count_black}')